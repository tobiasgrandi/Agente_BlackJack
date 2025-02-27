from blackjack import BlackJack
from q_learning import Qlearning
from plot import Plotter
import numpy as np

env = BlackJack()
qlearning = Qlearning(alpha=0.05, gamma=0.85, epsilon=1)

episodes = 20000000
qlearning.train(env, num_episodes= episodes)


plot = Plotter(qlearning)
plot.plot_training_metrics()
plot.plot_tables()
print(f'Recompensa total: {sum(qlearning.rewards_history)}')
print(f'Recompensa promedio: {np.mean(qlearning.rewards_history)}')
print(f'Recompensa promedio ultimos 100.000: {np.mean(qlearning.rewards_history[-100000:])}')
print(f'Win rate: {qlearning.results["Win"]*100/episodes}%')
print(f'Win rate ultimos 100.000: {qlearning.wins_history[-100000:].count(1)*100/100000}%')

print(qlearning.results, '\n') 

simulations = 100000
simulate_wins, simulate_losses = qlearning.play(env, simulations)
print(f'Wins: {simulate_wins}, Losses: {simulate_losses}')
print(f'Win rate: {simulate_wins*100/simulations}%')

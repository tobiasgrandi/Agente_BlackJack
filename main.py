from blackjack import BlackJack
from q_learning import Qlearning
from plot import Plotter
import numpy as np

env = BlackJack()
qlearning = Qlearning(alpha=0.1, gamma=0.85, epsilon=1)

episodes = 10000000
qlearning.train(env, num_episodes= episodes)


plot = Plotter(qlearning)
plot.plot_rewards_var()
plot.plot_wins()
plot.plot_tables(0)
plot.plot_tables(1)
print(f'Recompensa total: {sum(qlearning.rewards_history)}')
print(f'Recompensa promedio: {np.mean(qlearning.rewards_history)}')
print(f'Win rate: {qlearning.results["Win"]*100/episodes}%')
print(f'Win rate últimos 500.000: {qlearning.wins_history[-500000:].count(1)*100/500000}%')

print(qlearning.results)

#qlearning = Qlearning(alpha=0.3, gamma=0.85, epsilon=1)
#episodes = 10000000
#Recompensa total: 27074054.299939953
#Recompensa promedio: 1.8272655290093163
#Win rate: 40.91394%

#qlearning = Qlearning(alpha=0.1, gamma=0.85, epsilon=1)
#
#episodes = 10000000
#Recompensa total: 26932144.599933073
#Recompensa promedio: 1.7492483377618544
#Win rate: 41.07147%

#qlearning = Qlearning(alpha=0.1, gamma=0.95, epsilon=1)
#
#episodes = 10000000
#
#Recompensa total: -15420459.399549738
#Recompensa promedio: -0.9545042717436033
#Win rate: 39.63744%
#{'Lose': 6036256, 'Win': 3963744}
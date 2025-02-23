from blackjack import BlackJack, Player
from q_learning import Qlearning
from plot import Plotter

env = BlackJack()
qlearning = Qlearning(alpha=0.3, gamma=0.85, epsilon=0.8)

episodes = 10000000
qlearning.train(env, num_episodes= episodes)

plot = Plotter(qlearning)
plot.plot_rewards()
plot.plot_var()
plot.plot_wins()
plot.plot_tables(0)
plot.plot_tables(1)


print(qlearning.results)
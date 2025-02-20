from blackjack import BlackJack, Player
from q_learning import Qlearning

env = BlackJack()
qlearning = Qlearning(alpha=0.5, gamma=0.7, epsilon=0.8)

qlearning.train(env)
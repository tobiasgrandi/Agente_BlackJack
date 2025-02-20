import numpy as np

class Qlearning():
    def __init__(self):
        self.qtable = np.zeros((18, 10, 2, 2)) #18 sumas diferentes del jugador, 
                                                #10 sumas distintas para el dealer (As siempre vale 11), 
                                                #has_ace
                                                #Q(pedir), Q(quedarse)
        self.alpha = 0 #Tasa de aprendizaje
        self.gamma = 0 #Tasa de descuento
        self.epsilon = 0 #Tasa de exploración
        self.reward = {"Lose": -1, #Perder
                       "Win": 1, #Ganar
                       "Under 21": 1,
                       'Over 21': -1} #Empatar


    def select_action(self, state): #Devuelve la acción a tomar por el jugador
        if np.random.rand() < self.epsilon: #Exploración
            return np.random.choice([0,1])
        return np.argmax(self.qtable[state['sum_player'], state['dealer'], ['has_ace']]) #Explotación
    
    

    def update_qtable(self, current_state, next_state, action):
        current_q = self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action]
        max_next_q = np.max(self.qtable[next_state['sum_player']-4, next_state['dealer']-2, next_state['has_ace']])
        reward = self.reward[current_state['player_state']]

        self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action] = current_q + self.alpha*(reward+self.gamma*max_next_q-current_q)

    def train(self, env, num_episodes=10000):

        for episode in range(num_episodes):
            env.reset()
            state = env.get_state()

            done = False

            while not done:
                player_action = self.select_action(state)
                env.step(player_action)
                next_state = env.get_state()
                self.update_qtable(state, next_state, player_action)
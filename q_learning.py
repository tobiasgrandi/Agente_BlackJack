import numpy as np

class Qlearning():
    def __init__(self):
        self.qtable = np.zeros((18, 10, 2, 2)) #18 sumas diferentes del jugador, 
                                                #10 sumas distintas para el dealer (As siempre vale 11), 
                                                #Q(pedir), Q(quedarse)
        self.alpha = 0 #Tasa de aprendizaje
        self.gamma = 0 #Tasa de descuento
        self.epsilon = 0 #Tasa de exploración
        self.reward = {"0": -1, #Perder
                       "1": 1, #Ganar
                       "2": -1} #Empatar


    def select_action(self, state): #Devuelve la acción a tomar por el jugador
        if np.random.rand() < self.epsilon: #Exploración
            return np.random.choice([0,1])
        return np.argmax(self.qtable[state['sum_player'], state['dealer'], ['has_ace']]) #Explotación
    
    

    def update_qtable(self, actual_state, new_state, action):
        pass

    def train(self, env, num_episodes=10000):

        for episode in range(num_episodes):
            env.reset()
            state = env.get_state()

            done = False

            while not done:
                player_action = self.select_action(state)
                
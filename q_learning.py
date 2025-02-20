import numpy as np

class Qlearning():
    def __init__(self, alpha, gamma, epsilon):
        self.qtable = np.zeros((18, 10, 2, 2)) #18 sumas diferentes del jugador, 
                                                #10 sumas distintas para el dealer (As siempre vale 11), 
                                                #has_ace
                                                #Q(pedir), Q(quedarse)
        self.alpha = alpha #Tasa de aprendizaje
        self.gamma = gamma #Tasa de descuento
        self.epsilon = epsilon #Tasa de exploración
        self.reward = {"Lose": -1, #Perder
                        "Win": 1, #Ganar
                        "Under 21": 1,
                        'Over 21': -1} #Empatar


    def select_action(self, state): #Devuelve la acción a tomar por el jugador
        if np.random.rand() < self.epsilon: #Exploración
            return np.random.choice([0,1])
        return np.argmax(self.qtable[state['sum_player']-4, state['dealer']-2, state['has_ace']]) #Explotación
    
    

    def update_qtable(self, current_state, next_state, action):
        current_q = self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action]
        max_next_q = np.max(self.qtable[next_state['sum_player']-4, next_state['dealer']-2, next_state['has_ace']])
        reward = self.reward[current_state['player_state']]

        self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action] = current_q + self.alpha*(reward+self.gamma*max_next_q-current_q)

    def train(self, env, num_episodes=100):

        results = {
            'Lose': 0,
            'Win': 0,
            'Over 21': 0
        }
        for episode in range(num_episodes):
            env.reset()

            done = False
            while not done:
                state = env.get_state()
                player_action = self.select_action(state)
                env.step(player_action)
                next_state = env.get_state()
                if next_state['player_state'] != 'Over 21': ##CHEQUEAR ESTA LÓGICA
                    self.update_qtable(state, next_state, player_action)
                done = env.done

            print(next_state)
            results[next_state['player_state']] += 1
        
            print(results)
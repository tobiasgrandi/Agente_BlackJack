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
        self.reward = {"Lose": -1,
                        "Win": 1,
                        'Over 21': -1}
        self.results = {
            'Lose': 0,
            'Win': 0,
            'Over 21': 0,
        }
        self.rewards_history = []
        self.wins_history = []


    def select_action(self, state): #Devuelve la acción a tomar por el jugador
        if np.random.rand() < self.epsilon: #Exploración
            return np.random.choice([0,1])
        return np.argmax(self.qtable[state['sum_player']-4, state['dealer']-2, state['has_ace']]) #Explotación
    
    
    def update_qtable(self, current_state, next_state, action, reward):
        current_q = self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action]
        max_next_q = np.max(self.qtable[next_state['sum_player']-4, next_state['dealer']-2, next_state['has_ace']])
        
        
        self.qtable[current_state['sum_player']-4, current_state['dealer']-2, current_state['has_ace'], action] = current_q + self.alpha*(reward+self.gamma*max_next_q-current_q)


    def reduce_exploration(self):
        self.epsilon = max(0.1, self.epsilon*0.7)

    def get_reward(self, player_state):
        return self.reward[player_state]


    def train(self, env, num_episodes=10000000):

        for episode in range(num_episodes):
            env.reset()

            done = False
            episode_reward = 0
            episode_history = []
            while not done:
                state = env.get_state()
                player_action = self.select_action(state)
                env.step(player_action)
                next_state = env.get_state()

                if next_state['player_state'] == 'Over 21':
                    next_state['sum_player'] = state['sum_player'] #Si se pasó, penalizar la última suma antes de que se pase
                
                episode_history.append((state, player_action, next_state))

                done = env.done

            self.reduce_exploration()

            for state, player_action, next_state in episode_history:
                result = env.player_state
                reward = self.get_reward(result)
                self.update_qtable(state, next_state, player_action, reward)
                self.rewards_history.append(reward)

            if next_state['player_state'] == 'Win':
                self.wins_history.append(1)
            else:
                self.wins_history.append(0)


            self.results[next_state['player_state']] += 1

            if episode % 100000 == 0:
                print(episode)
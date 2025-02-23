import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

class Plotter():

    def __init__(self, qlearning):
        self.qlearning = qlearning

    
    def plot_rewards(self):
        window = 1000
        # Recompensas promedio con media movil de tamaño window
        avg_rewards = pd.Series(self.qlearning.rewards_history).rolling(window).mean()

        # Gráfico
        plt.figure(figsize=(10,5))
        plt.plot(np.arange(len(avg_rewards)), avg_rewards, label="Recompensa Promedio")
        plt.xlabel("Episodios")
        plt.ylabel("Recompensa Promedio")
        plt.title("Evolución de la Recompensa Durante el Entrenamiento")
        plt.legend()
        plt.show()

    def plot_var(self):
        window = 1000
        var_rewards = pd.Series(self.qlearning.rewards_history).rolling(window).var()

        plt.figure(figsize=(10, 5))
        plt.plot(np.arange(len(var_rewards)), var_rewards, label='Varianza de la Recompensa', color='red')
        plt.xlabel('Bloques de episodios')
        plt.ylabel('Varianza')
        plt.title('Evolución de la Varianza de la Recompensa')
        plt.legend()
        plt.show()

    def plot_wins(self):
        window = 100000

        avg_wins = pd.Series(self.qlearning.wins_history).rolling(window).mean()

        plt.figure(figsize=(10,5))
        plt.plot(np.arange(len(avg_wins)), avg_wins, label="Victorias Promedio")
        plt.xlabel("Episodios")
        plt.ylabel("Victorias Promedio")
        plt.title("Evolución de las Victorias Durante el Entrenamiento")
        plt.legend()
        plt.show()

    def plot_tables(self, has_ace):
        qtable = self.qlearning.qtable

        fig, ax = plt.subplots(figsize=(7, 7))


        colors = [(0, "green"), (1, "red")]  # (valor, color)
        n_bins = 100  # Número de divisiones del mapa de colores
        cmap_name = "green_to_red"
        color_map = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)
        
        # Seleccionar las acciones más probables basadas en el valor de has_ace
        table = np.argmax(qtable[:, :, has_ace, :], axis=2)  # Seleccionar la acción para cada combinación jugador-dealer

        # Graficar la tabla
        cax = ax.matshow(table, cmap=color_map, aspect='auto')
        fig.colorbar(cax, ax=ax)
        
        # Títulos y etiquetas
        if has_ace == 0:
            ax.set_title("Acción cuando no hay As")
        else:
            ax.set_title("Acción cuando hay As")
        
        ax.set_xlabel("Suma carta del Dealer")
        ax.set_ylabel("Suma del Jugador")
        
        ax.set_xticks(np.arange(10))
        ax.set_xticklabels(np.arange(2, 12))  # Cartas del dealer (2 a 11)
        
        ax.set_yticks(np.arange(18))
        ax.set_yticklabels(np.arange(4, 22))  # Sumas del jugador (4 a 21)

        # Dibujar líneas horizontales y verticales para separar las celdas
        for i in range(1, 18):  # Líneas horizontales entre filas
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(1, 10):  # Líneas verticales entre columnas
            ax.axvline(j - 0.5, color='black', linewidth=1)

        plt.tight_layout()
        plt.show()
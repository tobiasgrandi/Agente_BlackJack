import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math
import numpy as np
import pandas as pd

class Plotter():

    def __init__(self, qlearning):
        self.qlearning = qlearning
        self.window = 100000


    def plot_rewards_var(self):
        rewards_history = pd.Series(self.qlearning.rewards_history)

        avg_rewards = rewards_history.rolling(self.window).mean()
        var_rewards = rewards_history.rolling(self.window).var()

        fig, ax1 = plt.subplots(figsize=(10, 5))

        # Eje Y de la recompensa promedio (azul)
        ax1.set_xlabel("Episodios")
        ax1.set_ylabel("Recompensa Promedio", color="blue")
        line1, = ax1.plot(np.arange(len(avg_rewards)), avg_rewards, label="Recompensa Promedio", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        # Eje Y de la varianza (rojo)
        ax2 = ax1.twinx()
        ax2.set_ylabel("Varianza de la Recompensa", color="red")
        line2, = ax2.plot(np.arange(len(var_rewards)), var_rewards, label="Varianza de la Recompensa", color="red")
        ax2.tick_params(axis="y", labelcolor="red")

        # Agregar leyenda combinada
        fig.legend(handles=[line1, line2], loc="upper left", bbox_to_anchor=(0.1, 0.9))

        fig.suptitle("Evolución de la Recompensa y su Varianza Durante el Entrenamiento")
        fig.tight_layout()
        plt.show()

    def plot_wins(self):

        avg_wins = pd.Series(self.qlearning.wins_history).rolling(self.window).mean()

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
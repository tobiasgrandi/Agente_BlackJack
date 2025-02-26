import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import math
import numpy as np
import pandas as pd

class Plotter():

    def __init__(self, qlearning):
        self.qlearning = qlearning
        self.window = 100000


    def plot_training_metrics(self):
        rewards_history = pd.Series(self.qlearning.rewards_history)
        wins_history = pd.Series(self.qlearning.wins_history)

        avg_rewards = rewards_history.rolling(self.window).mean()
        var_rewards = rewards_history.rolling(self.window).var()
        avg_wins = wins_history.rolling(self.window).mean()

        fig, axes = plt.subplots(1, 2, figsize=(15, 5))  # Dos filas, una columna

        # Gráfica de Recompensa y Varianza
        ax1 = axes[0]  
        ax1.set_xlabel("Episodios")
        ax1.set_ylabel("Recompensa Promedio", color="blue")
        line1, = ax1.plot(np.arange(len(avg_rewards)), avg_rewards, label="Recompensa Promedio", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        ax2 = ax1.twinx()  # Segundo eje Y para varianza
        ax2.set_ylabel("Varianza de la Recompensa", color="red")
        line2, = ax2.plot(np.arange(len(var_rewards)), var_rewards, label="Varianza de la Recompensa", color="red")
        ax2.tick_params(axis="y", labelcolor="red")

        #Gráfica de victorias promedio
        ax3 = axes[1]  
        line3, = ax3.plot(np.arange(len(avg_wins)), avg_wins, label="Victorias Promedio", color="green")
        ax3.set_xlabel("Episodios")
        ax3.set_ylabel("Victorias Promedio")


        axes[0].legend(handles=[line1, line2], loc="upper left", bbox_to_anchor=(0.1, 0.9))
        axes[1].legend(handles=[line3], loc="upper left")

        fig.suptitle("Evolución de la Recompensa, Varianza y Victorias Durante el Entrenamiento")
        fig.tight_layout()
        plt.show()

    def plot_tables(self):
        qtable = self.qlearning.qtable

        fig, axes = plt.subplots(1, 2, figsize=(14, 7))  # Dos subgráficos en una fila

        colors = [(0, "green"), (1, "red")]  # (valor, color)
        n_bins = 100  
        cmap_name = "green_to_red"
        color_map = mcolors.LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

        for i, has_ace in enumerate([0, 1]):  # Iterar sobre sin As (0) y con As (1)
            ax = axes[i]  # Seleccionar el subplot
            table = np.argmax(qtable[:, :, has_ace, :], axis=2)  

            cax = ax.matshow(table, cmap=color_map, aspect='auto')
            fig.colorbar(cax, ax=ax)

            title = "Acción cuando hay As" if has_ace else "Acción cuando no hay As"
            ax.set_title(title)

            ax.set_xlabel("Suma carta del Dealer")
            ax.set_ylabel("Suma del Jugador")

            ax.set_xticks(np.arange(10))
            ax.set_xticklabels(np.arange(2, 12))

            ax.set_yticks(np.arange(18))
            ax.set_yticklabels(np.arange(4, 22))

            # Líneas de separación
            for j in range(1, 18):
                ax.axhline(j - 0.5, color='black', linewidth=1)
            for k in range(1, 10):
                ax.axvline(k - 0.5, color='black', linewidth=1)

        plt.tight_layout()
        plt.show()
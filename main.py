import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def plot_generes(data):
    y = np.array(data['Genero'].values)
    plt.hist(y)
    plt.title("Generes")
    plt.show()


def plot_lack_of_food(data):
    occ = Counter(data['Ha sufrido de escasez de alimentos'].values).most_common()[:20]
    df = pd.DataFrame(occ, columns=['Model', 'Frequency'])
    df.plot(kind='bar', x='Model')
    plt.title("has food shortages")
    plt.show()


def plot_reason(data):
    occ = Counter(data['Razon de la escasez de alimentos'].values).most_common()
    df = pd.DataFrame(occ, columns=['Fuel type', 'Frequency'])
    df.plot(kind='bar', x='Fuel type')
    # df.drop('nan', inplace=True, axis=1)
    plt.title("Reasons")
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('table.csv')
    plot_generes(data)
    plot_lack_of_food(data)
    plot_reason(data)

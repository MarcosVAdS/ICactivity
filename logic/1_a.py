#First question for Computacional Inteligence class
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

#dados = pd.read_csv('./data/estudante_201606840030.txt', sep=" ", header=None)

data = ["A", "B", "C", "RESULT"]

df = pd.read_csv('./data/estudante_201606840030.txt',  sep=',', usecols=data)

print(df["A"])




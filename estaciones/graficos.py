import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,6))
sns.set_context("paper", font_scale=1.4)

def gen_heatmap(url):

    
    matrixA={}
    matrixA['7']= np.random.randn(30)
    matrixA['8']= np.random.randn(30)
    matrixA['9']= np.random.randn(30)
    matrixA['10']= np.random.randn(30)
    matrixA['11']= np.random.randn(30)
    matrixA['12']= np.random.randn(30)
    matrixA['13']= np.random.randn(30)
    matrixA['14']= np.random.randn(30)
    matrixA['15']= np.random.randn(30)
    matrixA['16']= np.random.randn(30)
    matrixA['17']= np.random.randn(30)
    matrixA['18']= np.random.randn(30)
    matrixA['19']= np.random.randn(30)
    matrixA['20']= np.random.randn(30)
    matrixA['21']= np.random.randn(30)
    matrixA['22']= np.random.randn(30)
    matrixA['23']= np.random.randn(30)
    matrixA['00']= np.random.randn(30)
    matrixA['1']= np.random.randn(30)
    matrixA['2']= np.random.randn(30)
    matrixA['3']= np.random.randn(30)
    matrixA['4']= np.random.randn(30)
    matrixA['5']= np.random.randn(30)
    matrixA['6']= np.random.randn(30)



    data = pd.DataFrame(matrixA)

    #crash_mx =  np.random.randn(10, 12)
    
    sns.heatmap(data, cmap="Reds")
    plt.savefig('static/graphic.png')

    return str(url) + 'static/graphic.png'

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

iris = sns.load_dataset('iris')

def processing(s: str):
    return s.lower().replace(' ', '_')


def dist(param: str):
    
    plot = sns.displot(iris, x= processing(param), hue=iris['species'])
    plot.set(xlabel=param)

    st.pyplot(plot.fig)
    
def scatter(x: str, y: str):
    
    plot = sns.scatterplot(data=iris, x=processing(x), y=processing(y), hue=iris['species'])
    plot.set(xlabel=x, ylabel=y)
    st.pyplot(plot.get_figure())
    
def corrmatrix():
    d = iris.drop(['species'], axis = 1)
    corr = d.corr()
    plot = sns.heatmap(corr, annot=True, fmt=".2f")
    st.pyplot(plot.get_figure())
    
    
# -*- coding: utf-8 -*-
"""C-103.csv

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g9qSKECcbJjgsnrz6D5yhSr5FtJBlLSv
"""

import pandas as pd
import plotly.express as px
from google.colab import files
data_to_load=files.upload()
df=pd.read_csv('data.csv')
fig=px.line(df,x='Country',
y='',
color='Country')
fig.show()
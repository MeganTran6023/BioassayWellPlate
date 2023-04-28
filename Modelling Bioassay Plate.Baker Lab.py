#!/usr/bin/env python
# coding: utf-8

# ## Excel Python Tutorial Link:
# 
# ## https://youtu.be/fKKtO1w77bg?t=269
# ## https://www.youtube.com/watch?v=HY7cf-CYs1o

# # Installing Python Packages

# In[1]:


pip install ipysheet


# # Imports
# 

# In[2]:


import ipysheet
from ipysheet import calculation
import ipywidgets
import pandas as pd
import numpy as np


# # Forming Excel Sheet
# 

# In[3]:


#create sheet
dataSheet = ipysheet.sheet()

#display sheet on screen
display(dataSheet)


# # Setting Length x Width of Chart

# In[7]:


dataSheet = ipysheet.sheet(rows=9, columns= 13)

display(dataSheet)


# # Labelling x and y axis
# 
# ### start labelling column from 1

# In[81]:


dataSheet = ipysheet.sheet(rows=9, columns= 13)

#Labelling top horizontal row with numbers 1-12

cellA = ipysheet.cell(row = 0, column=1, value = "", label_left="",background_color = "powderblue")
cellB = ipysheet.cell(row = 0, column=2, value = "", label_left="1",background_color = "powderblue")
cellC = ipysheet.cell(row = 0, column=3, value = "", label_left="2",background_color = "powderblue")
cellD = ipysheet.cell(row = 0, column=4, value = "", label_left="3",background_color = "powderblue")
cellE = ipysheet.cell(row = 0, column=5, value = "", label_left="4",background_color = "powderblue")
cellF = ipysheet.cell(row = 0, column=6, value = "", label_left="5",background_color = "powderblue")
cellG = ipysheet.cell(row = 0, column=7, value = "", label_left="6",background_color = "powderblue")
cellH = ipysheet.cell(row = 0, column=8, value = "", label_left="7",background_color = "powderblue")
cellI= ipysheet.cell(row = 0, column=9, value = "", label_left="8",background_color = "powderblue")
cellJ = ipysheet.cell(row = 0, column=10, value = "", label_left="9",background_color = "powderblue")
cellK = ipysheet.cell(row = 0, column=11, value = "", label_left="10",background_color = "powderblue")
cellL= ipysheet.cell(row = 0, column=12, value = "", label_left="11",background_color = "powderblue")
cellM= ipysheet.cell(row = 0, column=13, value = "", label_left="12",background_color = "powderblue")


#Coloring columns
columncolor1 = ipysheet.cell(row=1,column=0,background_color = "powderblue")
columncolor2 = ipysheet.cell(row=2,column=0,background_color = "powderblue")
columncolor3 = ipysheet.cell(row=3,column=0,background_color = "powderblue")
columncolor4 = ipysheet.cell(row=4,column=0,background_color = "powderblue")
columncolor5 = ipysheet.cell(row=5,column=0,background_color = "powderblue")
columncolor6 = ipysheet.cell(row=6,column=0,background_color = "powderblue")
columncolor7 = ipysheet.cell(row=7,column=0,background_color = "powderblue")
columncolor8 = ipysheet.cell(row=8,column=0,background_color = "powderblue")

#Labelling columns
column1 = ipysheet.cell(row=1,column=1,value = "",label_left="A")
column2 = ipysheet.cell(row=2,column=1,value = "",label_left="B")
column3 = ipysheet.cell(row=3,column=1,value = "",label_left="C")
column4 = ipysheet.cell(row=4,column=1,value = "",label_left="D")
column5 = ipysheet.cell(row=5,column=1,value = "",label_left="E")
column6 = ipysheet.cell(row=6,column=1,value = "",label_left="F")
column7 = ipysheet.cell(row=7,column=1,value = "",label_left="G")
column8 = ipysheet.cell(row=8,column=1,value = "",label_left="H")




display(dataSheet)


# # Open Reference Bioassay Plate

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# In[2]:


df = pd.read_csv("Estonian citizens abroad.csv",
                 header=0)
df.head()


# In[3]:


target = df["# of Estonian citizens"]
target_label = "# of Estonian citizens"

name = df["Name"]
name_label = "Name"

df["Name and number of citizens"] = name.map(str) + '\n' + target.map(str)
name_target = df["Name and number of citizens"]
name_target_label = "Name and number of citizens"


# In[4]:


# normalize distances

distance = df["Distance between Capital and Tallinn (km)"]


distance_norm = (distance-distance.min())/ (distance.max() - distance.min())

df["Distance normalized"] = distance_norm


# In[5]:


fig = go.Figure(go.Scattergeo(
    text = df[name_target_label],
        lat = df["Latitude (capital)"],
        lon = df["Longitude (capital)"],
        marker = dict(
        size = df[target_label]**0.36,
        color = df[target_label],
        colorscale = "plasma",
        colorbar_title= target_label
        )
))
fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, projection_type="natural earth",
    showland=True, landcolor="LightBlue"
)
fig.update_traces(customdata=df[name_target_label])
fig.update_traces(hovertemplate='%{customdata}<extra></extra>')

fig.show()


# In[6]:



fig = px.scatter(df, x="Distance normalized", y = target_label,
                 color = "Continent",
                 log_y = True,
                 hover_name = "Name",
                 hover_data = {"Distance normalized":False,
                               "Continent":False,
                               target_label:":.0f"},
                 labels = {target_label: "# of Estonian citizens",
                            "Distance normalized": "Distance between country capital and Tallinn (normalized)"},
                )
fig.show()


# In[7]:


# normalize GDP PPP per capita
GDP = df["GDP PPP per capita"]
GDP_norm = (GDP-GDP.min())/ (GDP.max() - GDP.min())

df["GDP PPP per capita normalized"] = GDP_norm
df.sort_values(by="GDP PPP per capita normalized", ascending = False)


# In[8]:


fig = px.scatter(df, 
                 x="GDP PPP per capita", y = target_label,
                 color = "Continent",
                 log_y = True,
                 hover_name = "Name",
                 hover_data = {"GDP PPP per capita":":.0f",
                               "Continent":False,
                               target_label:False
                              },
                 labels = {
                     target_label: "# of Estonian citizens",
                     "GDP PPP per capita": "GDP PPP per capita (INT USD, 2020)"
                 }
                )
fig.show()


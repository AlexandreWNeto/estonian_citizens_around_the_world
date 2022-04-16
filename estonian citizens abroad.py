#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np


# In[2]:


# reading data from .csv file
df = pd.read_csv("Estonian citizens abroad.csv",
                 header=0)

# examining first entries on the dataset
df.head()


# In[3]:


#naming the columns of the dataset

# number of estonians citizens (target column)
target = df["# of Estonian citizens"]
target_label = "# of Estonian citizens"

# country name

name = df["Name"]
name_label = "Name"

#distance between country capital and Tallinn

distance_label = "Distance between Capital and Tallinn (km)"
distance = df[distance_label]

# Creating a column with "name" and "number of citizens" concatenated in a string for visualisation purposes
df["Name and number of citizens"] = name.map(str) + '\n' + target.map(str)
name_target = df["Name and number of citizens"]
name_target_label = "Name and number of citizens"


# In[4]:


# Creating scatter plot on a world map projection for # of estonian citizens across the world

fig = go.Figure(go.Scattergeo(
    text = df[name_target_label],
        lat = df["Latitude (capital)"],
        lon = df["Longitude (capital)"],
        marker = dict(
            size = df[target_label]**0.36, # scaling size for better visualisation
            color = df[target_label]**0.36, # scaling color for better visualisation
            colorscale = "Viridis_r",
            colorbar_title = target_label,
            colorbar_tickvals = np.array([1,10,100,1000,10000,50000])**0.36, # scaling color scale
            colorbar_ticktext = np.array([1,10,100,1000,10000,50000])
            )
))

fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, projection_type="natural earth",
    showland=True, landcolor="LightBlue"
)

fig.update_traces(customdata=np.stack((df["Name"], df[target_label]), axis=-1))
fig.update_traces(hovertemplate='<b>%{customdata[0]}</b><br><br># of Estonian citizens: %{customdata[1]}<br><extra></extra>') 

fig.update_layout(title="Estonian citizens across the world")

fig.show()


# In[5]:


fig = px.scatter(df, x=distance_label, y = target_label,
                 color = "Continent", # dividing data into continents
                 log_y = True, # setting logarithmic axis for number of Estonian citizens for better visualisation
                 hover_name = "Name",
                 hover_data = {target_label:":.0f",
                               distance_label:":.0f",
                               "Continent":False
                               },
                 labels = {target_label: "# of Estonian citizens",
                            distance_label: "Distance (km)"},
                )

fig.update_layout(
    xaxis_title="Distance between country capital and Tallinn (km)",
    yaxis_title="# of Estonian citizens",
)

fig.update_traces(
    marker=dict(symbol="square")
)


fig.update_layout(title="Number of Estonian citizens vs Distance between country capital and Tallinn")

fig.show()


# In[6]:


fig = px.scatter(df, x="GDP PPP per capita", y = target_label,
                 color = "Continent", # dividing data into continents
                 log_y = True, # setting logarithmic axis for number of Estonian citizens for better visualisation
                 log_x = True, # setting logarithmic axis for GDP PPP per capita for better visualisation
                 hover_name = "Name",
                 hover_data = {"GDP PPP per capita":":.2f",
                               "Continent":False,
                               target_label:":.0f"
                              },
                 labels = {
                     target_label: "# of Estonian citizens",
                     "GDP PPP per capita": "GDP PPP per capita"
                 }
                )

fig.update_layout(
    xaxis_title="GDP PPP per capita (INT USD, 2020)",
    yaxis_title="# of Estonian citizens",
)

fig.update_traces(
    marker=dict(symbol="square")
)


fig.update_layout(title="Number of Estonian citizens vs Country GDP PPP")

fig.show()


# In[7]:


fig = px.scatter(df, y="GDP PPP per capita", x ="Distance between Capital and Tallinn (km)",
                 color = np.log(df[target_label]),
                 color_continuous_scale="Viridis",
                 opacity = 1,
                 
                 
                 size = (df[target_label])**0.6, # scaling the size of the scatter points
                 size_max = 35,
                 
                 hover_name = "Name",
                 hover_data = {target_label:True,
                               "GDP PPP per capita":":.0f",
                               "Continent":False,
                                "Distance between Capital and Tallinn (km)":":.0f",
                                        
                              },
                 labels = {
                     target_label: "# of Estonian citizens",
                     "GDP PPP per capita": "GDP PPP per capita (INT USD, 2020)",
                     "Distance between Capital and Tallinn (km)":"Distance (km)"
                          }
                )

fig.update_layout(coloraxis_colorbar=dict(len=0.75,
                  title='# Estonian<br>citizens', 
                  tickvals = np.log([1,10,100,1000,10000,50000]),
                  ticktext = [1,10,100,1000,10000,50000])) #scaling color axis 
                                                        

fig.update_layout(
    xaxis_title="Distance between Capital and Tallinn (km)",
    yaxis_title="GDP PPP per capita (INT USD, 2020)",
)

fig.update_traces(customdata=np.stack((df["Name"], df[target_label]), axis=-1))
fig.update_traces(hovertemplate='<b>%{customdata[0]}</b><br><br> # of Estonian citizens: %{customdata[1]}<br>\
Distance between capital and Tallinn (km) %{x:.0f}<br>\
GDP PPP (INT USD, 2020): %{y:.2f}') 


fig.update_layout(title="Number of Estonian citizens<br>Country GDP PPP vs Distance between country capital and Tallinn")

fig.show()


# In[8]:


# assessing number of Estonian citizens for countries in small countries (population <= 100k)

# filter countries with population <= 100k
df2 = df[df["Population (2020)"] <= 100000]

fig = px.bar(df2, x="Name", y = target_label,
                 color = "Sub-region", # dividing data into sub-regions
                 hover_name = "Name",
                 hover_data = {"Population (2020)":":.2f",
                               "Sub-region": False,
                               target_label: ":.0f",
                               "Name": False
                              },
                 labels = {
                     target_label: "# of Estonian citizens",
                     "Population (2020)": "Population (2020)"
                 }
                )

fig.update_layout(
    title="Number of Estonian citizens living in countries with a population <= 100k",
    xaxis_title=None,
    yaxis_title="# of Estonian citizens",
)


fig.show()


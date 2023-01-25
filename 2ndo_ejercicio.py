#!/usr/bin/env python
# coding: utf-8

# In[9]:


quarters = [
    ["Enero", "Febrero", "Marzo"], 
    ["Abril", "Mayo", "Junio"], 
    ["Julio", "Agosto", "Septiembre"], 
    ["Octubre", "Noviembre", "Deciembre"]
]

# El segundo mes de primer trimestre
print(quarters[0][1]) # Output: "Febrero"

# Los meses de primer quarto del año
print(quarters[0]) # Output: ["Enero", "Febrero", "Marzo"]

# Septiembre y Octubre
print([months for quarter in quarters[2:4] for months in quarter]) # Output: ["Septiembre", "Octubre"]


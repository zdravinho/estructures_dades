#!/usr/bin/env python
# coding: utf-8

# In[18]:


compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }

# Afegeix alguna fruita més
compra["Plàtans"] = {"Qty": 2, "€": 0.30}
compra["Taronges"] = {"Qty": 4, "€": 0.50}

# Quant han costat les peres en total?
cost_peres = compra["Peres"]["Qty"] * compra["Peres"]["€"]
print(cost_peres) # Output: 1.98

# Quantes fruites hem comprat en total?
total_qty = sum([fruita["Qty"] for fruita in compra.values()])
print(total_qty) # Output: 14

# Quina és la fruita més cara?
mes_cara = max(compra, key=lambda x: compra[x]["€"])
print(mes_cara) # Output: "Peres"


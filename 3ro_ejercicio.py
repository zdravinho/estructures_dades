#!/usr/bin/env python
# coding: utf-8

# In[11]:


numero = [4, 2, 9, 3, 7, 5, 3, 1, 8, 6]

# Quants números hi ha?
print(len(numero)) # Output: 10

# Quantes vegades apareix el número 3.
print(numero.count(3)) # Output: 2

# Quantes vegades apareixen els nombres 3 i 4?
print(numero.count(3) + numero.count(4)) # Output: 3

# Quin és el número més gran?
print(max(numero)) # Output: 9

# Quins són els 3 números més petits?
print(sorted(numero)[:3]) # Output: [1, 2, 3]

# Quin és el rang d’aquesta llista?
print(max(numero) - min(numero)) # Output: 8


# In[ ]:





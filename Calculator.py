#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title("Trapezium Calculator")
base_1 = int(st.number_input("base 1 is:"))
base_2 = int(st.number_input("base 2 is:"))
height = int(st.number_input("height is:"))
A = 1/2*(base_1+base_2)*height
st.write(A)


# In[ ]:





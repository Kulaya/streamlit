#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title("SIMPLE CALCULATOR")
st.text("Created by Aviti Kulaya")
app_mode = st.sidebar.selectbox('Select Page',['Age Calculator','Area of a trapezium','Perimeter of a trapezium','Degrees-Radians Converter','Radians-Degrees Converter'])
if app_mode=='Age Calculator':
    st.text("It is easier to know your years old using this calculator")
    Current_year = int(st.number_input("Enter your current year:"))
    Year_of_Birth = int(st.number_input("Enter your year of birth:"))
    Your_age = Current_year-Year_of_Birth
    st.write("Your age is:",Your_age)
if app_mode=='Area of a trapezium' :
    st.header("Area")
    st.text("Calculates Area of a Trapezium")
    base_1 = int(st.number_input("base 1 :"))
    base_2 = int(st.number_input("base 2 :"))
    height = int(st.number_input("height :"))
    Area_of_a_trapezium = 1/2*(base_1+base_2)*height
    st.write("Area of a trapezium is :",Area_of_a_trapezium)
if app_mode=='Perimeter of a trapezium' :
    st.subheader("Perimeter")
    st.text("Calculates Area of a Trapezium")
    base_3 = int(st.number_input("base 1 :"))
    base_4 = int(st.number_input("base 2 :"))
    side_5 = int(st.number_input("side 1 :"))
    side_6 = int(st.number_input("side 2 :"))
    Perimeter_of_a_trapezium = base_3+base_4+side_5+side_6
    st.write("Perimeter of a trapezium is :",Perimeter_of_a_trapezium)
from math import pi
if app_mode=='Degrees-Radians Converter':
    degrees = int(st.number_input("Enter angle in degrees"))
    radians = degrees*(pi/180)
    st.write("Angle in radians is : ",radians)
if app_mode=='Radians-Degrees Converter':
    radians = int(st.number_input("Enter angle in radians"))
    degrees = radians*(180/pi)
    st.write("Angle in degrees is : ",degrees)



# In[ ]:





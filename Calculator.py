#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title("SIMPLE CALCULATOR")
st.subheader("Created by Aviti Kulaya")
st.sidebar.subheader("Select what you want to calculate")
app_mode = st.sidebar.selectbox('Normal Calculations',['Addition','Subtraction','Multiplication','Division'])
st.header("Normal Calculations")
if app_mode=='Addition':
    a = int(st.number_input("Enter the first value :"))
    b = int(st.number_input("Enter the second value :"))
    A = a+b
    st.write("{}+{}= ",A)
if app_mode=='Subtraction':
    a = int(st.number_input("Enter the first value :"))
    b = int(st.number_input("Enter the second value :"))
    S = a-b
    st.write("{}-{}= ",S)
if app_mode=='Multiplication':
    a = int(st.number_input("Enter the first value :"))
    b = int(st.number_input("Enter the second value :"))
    M = a*b
    st.write("{}*{}= ",M)
if app_mode=='Division':
    a = int(st.number_input("Enter the first value :"))
    b = int(st.number_input("Enter the second value :"))
    D = a/b
    st.write("{}/{}= ",D)
mode_app = st.sidebar.selectbox('Conversion Calculations',['Convert Degrees-Radians','Convert Radians-Degrees'])
if mode_app=='Convert Degrees-Radians' :
    st.header("Conversion Calculations")
    degrees = int(st.number_input("Enter angle in degrees :"))
    radians = degrees*(3.141592653589793/180)
    st.write("Angle in radians is : ",radians)
if mode_app=='Convert Radians-Degrees' :
    radians = int(st.number_input("Enter angle in radians :"))
    degrees = radians*(180/3.141592653589793)
    st.write("Angle in degrees is : ",degrees)
aviti_app = st.sidebar.selectbox('Age Calculations',['Age Calculating'])
if aviti_app=='Age Calculating':
    st.header("Age Calculating")
    st.text("It is easier to know your years old using this calculator")
    Current_year = int(st.number_input("Enter your current year:"))
    Year_of_Birth = int(st.number_input("Enter your year of birth:"))
    Your_age = Current_year-Year_of_Birth
    st.write("Your age is:",Your_age)
apps_mode = st.sidebar.selectbox('Other Calculations',['Area of a trapezium','Perimeter of a trapezium','Volume of a cylinder','Surface Area of a cylinder'])
st.header("Other Calculations")
if apps_mode=='Area of a trapezium' :
    st.subheader("Area")
    st.text("Calculates Area of a Trapezium")
    base_1 = int(st.number_input("base 1 :"))
    base_2 = int(st.number_input("base 2 :"))
    height = int(st.number_input("height :"))
    Area_of_a_trapezium = 1/2*(base_1+base_2)*height
    st.write("Area of a trapezium is :",Area_of_a_trapezium)
if apps_mode=='Perimeter of a trapezium' :
    st.subheader("Perimeter")
    st.text("Calculates perimeter of a Trapezium")
    base_3 = int(st.number_input("base 1 :"))
    base_4 = int(st.number_input("base 2 :"))
    side_5 = int(st.number_input("side 1 :"))
    side_6 = int(st.number_input("side 2 :"))
    Perimeter_of_a_trapezium = base_3+base_4+side_5+side_6
    st.write("Perimeter of a trapezium is :",Perimeter_of_a_trapezium)
if apps_mode=='Volume of a cylinder' :
    from math import pi
    radius = int(st.number_input("Radius :"))
    height = int(st.number_input("height :"))
    V = pi*radius**2*height
    st.write("Volume of a cylinder is :",V)
if apps_mode=='Surface Area of a cylinder' :
    from math import pi
    radius = int(st.number_input("Radius :"))
    height = int(st.number_input("height :"))
    A = (2*pi*radius*height)+(2*pi*radius**2)
    st.write("Surface Area of a cylinder is :",A)



# In[ ]:





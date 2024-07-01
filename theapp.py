import streamlit as st
import pandas as pd
import random


def specific_protein(button):
    meals = pd.read_excel('meals.xlsx')
    meals_dinner = meals[meals['MealTime'].str.contains('Dinner')]
    filtered_meals = meals_dinner[meals_dinner['Protein'].str.contains(button)]
    max_index = len(filtered_meals)
    random_index = random.randint(0, max_index-1)
    random_meal = filtered_meals.iloc[random_index]
    return random_meal

def specific_protein_lunch(button):
    meals = pd.read_excel('meals.xlsx')
    meals_dinner = meals[meals['MealTime'].str.contains('Lunch')]
    filtered_meals = meals_dinner[meals_dinner['Protein'].str.contains(button)]
    max_index = len(filtered_meals)
    random_index = random.randint(0, max_index-1)
    random_meal = filtered_meals.iloc[random_index]
    return random_meal

def surprise_me():
    meals = pd.read_excel('meals.xlsx')
    meals_dinner = meals[meals['MealTime'].str.contains('Dinner')]
    max_index = len(meals)
    random_index = random.randint(0, max_index-1)
    random_meal = meals_dinner.iloc[random_index]
    return random_meal

st.set_page_config(page_title="Halla's Food Suggestor", page_icon=':dumpling:')
st.title('What Should I eat today?')
st.subheader('Dinner')
st.text("")
col1, col2, col3 = st.columns(3)
with col1:
    surprise_me_button = st.button('Surprise me! :shallow_pan_of_food:')
    salmon_button = st.button('Salmon :sushi:' )
    steak_button = st.button('Steak :cut_of_meat:')
    

with col2:
    beef_button = st.button('Beef :meat_on_bone:' )
    shrimp_button = st.button('Shrimp :fried_shrimp:' )

with col3:
    chicken_button = st.button('Chicken :poultry_leg:')
    kebda_button = st.button('Kebda :falafel:')

st.text("")
st.text("")

if surprise_me_button:
    st.text(surprise_me())
if salmon_button:
    st.text(specific_protein('Salmon'))

if beef_button:
    st.text(specific_protein('Beef'))

if chicken_button:
    st.text(specific_protein('Chicken'))

if shrimp_button:
    st.text(specific_protein('Shrimp'))

if steak_button:
    st.text(specific_protein('Steak'))

if kebda_button:
    st.text(specific_protein('Kebda'))


st.subheader('Lunch')
st.text("")


col4, col5, col6 = st.columns(3)
with col4:
    salmon_lunch_button = st.button('Salmon :fish_cake:' )

with col5:
    egg_button = st.button('Eggs :fried_egg:' )

with col6:
    tuna_button = st.button('Tuna :hot_pepper:')

if salmon_lunch_button:
    st.text(specific_protein_lunch('Salmon'))

if egg_button:
    st.text(specific_protein_lunch('Egg'))

if tuna_button:
    st.text(specific_protein_lunch('Tuna'))



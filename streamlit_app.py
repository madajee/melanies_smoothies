# Import python packages
import streamlit as st
import requests
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie
  """
)


name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your smoothie will be", name_on_order)
ingredients_list = ['Blueberries', 'Apples', 'Dragon Fruit', 'Elderberries', 'Jackfruit']

if ingredients_list: 
    st.write(ingredients_list)
    st.text(ingredients_list)

    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        st.write(ingredients_string)
        st.subheader(fruit chosen + 'Nutrition Information')
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)  
        #st.text(smoothiefroot_response.json())
        sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")




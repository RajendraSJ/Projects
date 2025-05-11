import streamlit as st
import random

st.title("🎸 Band Name Generator")

city_list = ["Neon", "Electric", "Shadow", "Mystic", "Crimson", "Silver"]
animal_list = ["Tigers", "Wolves", "Dragons", "Penguins", "Panthers", "Eagles"]

user_city = st.text_input("What is the name of your city?")
user_animal = st.text_input("What is your favorite animal?")

if st.button("Generate Band Names"):
    if user_city and user_animal:
        random_city = random.choice(city_list)
        random_animal = random.choice(animal_list)

        band_name_0 = f"{user_city} {user_animal}"
        band_name_1 = f"{user_city} {random_animal}"
        band_name_2 = f"{random_city} {user_animal}"
        band_name_3 = f"{random_city} {random_animal}"

        st.subheader("🎤 Your Band Name Ideas:")
        st.write(f"1. {band_name_0}")
        st.write(f"2. {band_name_1}")
        st.write(f"3. {band_name_2}")
        st.write(f"4. {band_name_3}")
    else:
        st.warning("Please enter both your city and favorite animal.")

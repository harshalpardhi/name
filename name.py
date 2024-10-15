import streamlit as st
import requests
import random

# Function to get a random animal from an API
def get_random_animal():
    response = requests.get("https://zoo-animal-api.herokuapp.com/animals/rand")
    if response.status_code == 200:
        animal_data = response.json()
        return animal_data['name']
    else:
        return "Unicorn"  # Fallback if the API call fails

# Function to generate funny nicknames
def generate_nickname(name, animal, color, gender):
    base_nickname = f"{color} {animal}"
    if gender == "Boy":
        funny_nicknames = [
            f"{base_nickname} Dude",
            f"{base_nickname} McBoys",
            f"{base_nickname}inator",
            f"{base_nickname} the Brave",
            f"{base_nickname}zilla"
        ]
    else:
        funny_nicknames = [
            f"{base_nickname} Princess",
            f"{base_nickname} McGirls",
            f"{base_nickname}ina",
            f"{base_nickname} the Fierce",
            f"{base_nickname} Blossom"
        ]
    return random.choice(funny_nicknames)

# Streamlit app
st.title("Funny Nickname Generator")

# Input fields
name = st.text_input("Enter your name:")
color = st.text_input("Enter your favorite color:")
gender = st.selectbox("Select for whom you want the name:", ["Boy", "Girl"])

# Button to generate nickname
if st.button("Generate Nickname"):
    if name and color:
        animal = get_random_animal()
        nickname = generate_nickname(name, animal, color, gender)
        st.success(f"Your funny nickname is: **{nickname}**")
    else:
        st.error("Please fill in all fields!")


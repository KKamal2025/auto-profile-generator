import streamlit as st
import requests
import random

def generate_name():
    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

st.title("تولید خودکار نام و عکس پروفایل")

email = st.text_input("آدرس جیمیل خود را وارد کنید:")

if email:
    full_name = generate_name()
    image_url = "https://thispersondoesnotexist.com/image"

    st.subheader("نام تولید شده:")
    st.write(full_name)

    st.subheader("عکس پروفایل:")
    st.image(image_url, caption="عکس تولید شده", use_column_width=True)

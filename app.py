import streamlit as st
import requests
import random
from PIL import Image
from io import BytesIO

def generate_name():
    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

st.title("تولید خودکار نام و عکس پروفایل")

email = st.text_input("آدرس جیمیل خود را وارد کنید:")

if email:
    full_name = generate_name()
    st.subheader("نام تولید شده:")
    st.write(full_name)

    st.subheader("عکس پروفایل:")

    try:
        response = requests.get("https://thispersondoesnotexist.com/image")
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="عکس تولید شده", use_container_width=True)
    except:
        st.error("خطا در بارگذاری عکس. دوباره تلاش کنید.")

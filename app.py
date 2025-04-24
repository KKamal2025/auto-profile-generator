import streamlit as st
import random

# تابع برای تولید اسم و فامیل تصادفی آمریکایی
def generate_name():
    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# عنوان اپلیکیشن
st.title("تولید خودکار نام و عکس پروفایل")

# فیلد برای وارد کردن جیمیل
email = st.text_input("آدرس جیمیل خود را وارد کنید:")

# وقتی جیمیل وارد شد، عملیات انجام بشه
if email:
    # تولید اسم و فامیل تصادفی
    full_name = generate_name()

    # انتخاب تصادفی جنسیت و شماره عکس برای آدرس عکس
    gender = random.choice(["men", "women"])
    img_number = random.randint(1, 99)
    image_url = f"https://randomuser.me/api/portraits/{gender}/{img_number}.jpg"

    # نمایش نام تولید شده
    st.subheader("نام تولید شده:")
    st.write(full_name)

    # نمایش عکس پروفایل
    st.subheader("عکس پروفایل:")
    st.image(image_url, caption="عکس تولید شده", use_container_width=True)

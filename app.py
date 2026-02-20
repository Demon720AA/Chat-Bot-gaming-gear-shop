import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gaming Gear Bot (CSV)", page_icon="🎮")

# ฟังก์ชันสำหรับโหลดข้อมูลจาก CSV
@st.cache_data # ใช้ cache เพื่อไม่ให้โหลดไฟล์ใหม่ทุกครั้งที่พิมพ์แชท
def load_data():
    df = pd.read_csv('gaming_gear_qa.csv')
    return df

# โหลดข้อมูล
try:
    df_qa = load_data()
except FileNotFoundError:
    st.error("ไม่พบไฟล์ gaming_gear_qa.csv กรุณาตรวจสอบชื่อไฟล์")
    st.stop()

st.title("🎮 Gaming Gear Assistant")
st.info("บอทตัวนี้ดึงข้อมูลคำถาม-ตอบมาจากไฟล์ CSV")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("สอบถามเรื่องสินค้าหรือบริการ..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Logic การค้นหาคำตอบจาก DataFrame
    user_query = prompt.lower()
    response = "ขออภัยครับ ผมไม่พบข้อมูลที่คุณต้องการ ลองสอบถามเรื่อง 'เมาส์', 'การส่งของ' หรือ 'โปรโมชั่น' นะครับ"

    # วนลูปเช็คจากข้อมูลใน CSV
    for index, row in df_qa.iterrows():
        keywords = str(row['keywords']).split() # แยกคำหลักออกจากกัน
        if any(word in user_query for word in keywords):
            response = row['answer']
            break

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
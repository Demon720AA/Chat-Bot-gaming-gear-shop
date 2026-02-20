import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Gaming Gear Bot", page_icon="🎮")

# ข้อมูลสินค้าจำลอง (ในอนาคตดึงจาก Database ได้)
inventory = {
    "mouse": "เรามี Logitech G Pro X Superlight (3,990.-) และ Razer DeathAdder V3 (4,590.-) ครับ",
    "keyboard": "แนะนำ Keychron V1 (3,290.-) หรือ Corsair K70 RGB (5,190.-) ครับ",
    "monitor": "ตอนนี้มี Zowie XL2546K 240Hz (19,900.-) สินค้าขายดีเลยครับ",
    "shipping": "ส่งฟรีทั่วไทยเมื่อซื้อครบ 2,000 บาทครับ ปกติใช้เวลา 1-2 วัน"
}

# ส่วนแสดงผลหน้าเว็บ
st.title("🎮 Gaming Gear Store Assistant")
st.subheader("ยินดีต้อนรับ! สอบถามข้อมูลสินค้าหรือการจัดส่งได้เลยครับ")

# สร้าง Session State เพื่อเก็บประวัติการคุย
if "messages" not in st.session_state:
    st.session_state.messages = []

# แสดงข้อความเก่า
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ส่วนรับ Input จากผู้ใช้
if prompt := st.chat_input("พิมพ์คำถามที่นี่..."):
    # แสดงข้อความของผู้ใช้
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Logic การตอบคำถามแบบง่าย (Keyword Matching)
    user_query = prompt.lower()
    response = "ขออภัยครับ ผมไม่เข้าใจคำถาม ลองถามเกี่ยวกับ 'เมาส์', 'คีย์บอร์ด' หรือ 'การส่งของ' ดูไหมครับ?"

    if "เมาส์" in user_query or "mouse" in user_query:
        response = inventory["mouse"]
    elif "คีย์บอร์ด" in user_query or "keyboard" in user_query:
        response = inventory["keyboard"]
    elif "จอ" in user_query or "monitor" in user_query:
        response = inventory["monitor"]
    elif "ส่ง" in user_query or "shipping" in user_query:
        response = inventory["shipping"]

    # แสดงคำตอบของ Bot
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
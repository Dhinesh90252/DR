import streamlit as st

# Page config
st.set_page_config(page_title="Private Message ❤️", layout="centered")

# Custom styles
st.markdown("""
    <style>
    body { background-color: #fff0f5; }
    .stApp {
        background-image: linear-gradient(to bottom, #fff0f5, #ffe6f0);
        font-family: 'Georgia', serif;
        color: #800000;
    }
    h2 {
        text-align: center;
        color: #FF1493;
    }
    </style>
""", unsafe_allow_html=True)

# --- Password Protection ---
PASSWORD = "Rofi2212"  # You can change this to your custom secret

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("### 🔐 Enter the secret password to view the message")
    pw = st.text_input("Password", type="password")
    if st.button("Submit"):
        if pw == PASSWORD:
            st.session_state.auth = True
            st.success("Welcome to my heart 💖")
        else:
            st.error("Close... but I only let the special ones in 💋")
    st.stop()

# --- Romantic Content ---
st.markdown("## To Someone Very Special ❤️")

with st.expander("💌 Click to Read My Heart 💌"):
    st.markdown("""
    **உயிரே.....💓,**

    Yeahh, ur correct we completed our 6 months in our journey..... ❤️❤️❤️❤️❤️❤️
    In this 6 months we came across many situations with endless amount of love....💋💋💋 
    It all started in a simple random Hi at 31st December 2024 at around 7pm 💓
    You don't know one thing On that day just overcome some depression I texted you but now it becomes my lifetime happiness❤️❤️❤️
    You became the important part of my life I hope everytime ur with me...... 😘
    You only gave me a space to share anything without any shame.... 
    I think in the world ur the only one understood me that who i am.... 
    No one can replace it more than u 😘😘😘
    Everyday falling for u more and more and going soooo deeper 💋
    The fight we or I made is only of love and not for anyother thing 
    Bcz i not want to losee u in that only the fights are arising hope u understand
    Nowadays ur the only one u made me laugh, dream and giving hope to big dreams 💓💓💓
    I know ur loving mee more than what im thinking but ur not expressing it outside am i ryt...?
     U only making me to overcome my introverness and giving space to express all my emotions such as happy, sad, cry etc.... 💓
     U making me happier day by day, When I am with u in any way like voice call or video literally i feel i am the happiest person in the world 
     that i cant expess in words..... 😘😘😘😘😘😘😘
     And a simple "mm" msg from u also making me to overcome from sadness sometimes thats the power of my girl😘💋
     And thanks for coming into my life and making my life brighter and meaningful
     And finally orey oru chinna aasa thaa may be u call it as Peraasai intha 6 month anniversary 60 year anniversary ahh convert aaganum ❤️❤️❤️❤️
     Happy Half year Anniversary uyireeeee ❤️
     Need u until my last breath with infinite amount love and want to spend the whole life with u...💓
     Love u my....................🫂🫀🌎❤️
                                    
                                         **I love you ** 💖
                                         
     
     என்றும் உனக்காக
        உன்.... ❤️

      
      
    """)

st.image("ChatGPT Image Mar 31, 2025, 03_11_37 PM.png", caption="A Moment That I Cherish 💞", use_column_width=True)

st.markdown("""
<p style='color:#C71585; font-size:16px; text-align: center;'>
Hope to capture this one in real with My Poocha kuttyyyy......💖
</p>
""", unsafe_allow_html=True)

audio_file = open("msg.mp3", "rb")
st.audio(audio_file.read(), format="audio/mp3")

st.success("I'll love you, forever and always. 💕")

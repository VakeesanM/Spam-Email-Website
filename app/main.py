import streamlit as st
import sklearn 
import joblib

model = joblib.load("app/Spam-detection.pkl")

def spam_detection(email:str):
    result = model.predict([email])[0]
    if result == 0:
        "#### This is a :green[Real Email]!"
    else:
        "#### This is a :red[Spam Email]! Block the sender and ignore it!"


st.markdown("<h1 style='text-align: center;'>Email Spam Detector</h1>",unsafe_allow_html=True)
with st.form("Spam_form"):
    email = st.text_area("## Please Copy Paste your Email Here:", height="content")

    if st.form_submit_button("Detect Spam"):
        if (email != ""):
            spam_detection(email=email)
        else:
            "#### You didn't input an Email!"




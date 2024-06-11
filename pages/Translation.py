import streamlit as st
from openai import OpenAI

st.sidebar.header("ALAstora Parameters :")
model_temp = st.sidebar.slider("Temp", step=0.01, min_value=0.0,
                               max_value=2.0,
                               value=0.2)
max_token = st.sidebar.slider("Max Token", step=100, min_value=200,
                              max_value=4000,
                              value=512)
model_top = st.sidebar.slider("Top P", step=0.01, min_value=0.0,
                              max_value=1.0,
                              value=1.0)
frqncy_penalty = st.sidebar.slider("Frequency Penalty", step=0.1, min_value=0.0,
                              max_value=2.0,
                              value=0.0)
prsnc_penalty = st.sidebar.slider("Presence Penalty", step=0.1, min_value=0.0,
                              max_value=2.0,
                              value=0.6)

def get_translate(lang1,lang2,word):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": f"You will be provided with a sentence in {lang1}, and your task is to translate it into {lang2}."
            },
            {
            "role": "user",
            "content": f"{word}"
            }
        ],
        temperature=model_temp,
        max_tokens= max_token,
        top_p=model_top,
        frequency_penalty=frqncy_penalty,
        presence_penalty=prsnc_penalty,
    )
    return response.choices[0].message.content


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.title("ALAstora WebSite")
st.subheader("Translate natural language text")
with st.form("my_form", clear_on_submit=False, border=True):
    lang1 = st.selectbox('from language?',('Arabic', 'English', 'French', 'German', 'Spanish',))
    lang2 = st.selectbox('to language?',('English', 'Arabic', 'French', 'German', 'Spanish',))
    word = st.text_input("Write the sentence here : أكتب الجملة هنا")
    st.form_submit_button(label="Send", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    response = get_translate(lang1,lang2,word)
    st.text_area("Translation : نتيجة الترجمة الخاصة بك",value=f"{response}")
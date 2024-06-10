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

def get_answer(ask,tables):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": f"Given the following SQL tables, your job is to write queries given a user’s request.\n {tables};"
            },
            {
            "role": "user",
            "content": f"{ask}"
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
st.subheader("Convert natural language into SQL queries")
with st.form("my_form", clear_on_submit=False, border=True):
    tables = st.text_input("Paste your table creation commands here : قم بلصق اوامر إنشاء الجداول الخاصه بك هنا")
    ask = st.text_input("Describe here the relationship you want : أوصف هنا أمر العلاقة التي تريدها")
    st.form_submit_button(label="Send", help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
    response = get_answer(ask,tables)
    st.text_area("Code edit : نتيجة البحث الخاصة بك",value=f"{response}")
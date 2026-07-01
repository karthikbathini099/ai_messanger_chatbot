from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import streamlit as st


llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

st.title("1st ai chat bot:🤖")
query=st.chat_input("ask anything :")
if query:
    res=llm.invoke(query)
    st.chat_message("ai").write(res.content)
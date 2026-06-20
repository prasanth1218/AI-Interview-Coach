import os
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.report_prompt import report_prompt

load_dotenv()

groq_api_key = (
    os.getenv("GROQ_API_KEY")
    or st.secrets["GROQ_API_KEY"]
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    api_key=groq_api_key
)

report_chain = (
    report_prompt
    | llm
)
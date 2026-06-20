import os
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from prompts.evaluator_prompt import evaluator_prompt
from utils.parser import parser

load_dotenv()

groq_api_key = (
    os.getenv("GROQ_API_KEY")
    or st.secrets.get("GROQ_API_KEY")
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    api_key=groq_api_key
)

evaluation_chain = (
    evaluator_prompt
    | llm
    | parser
)
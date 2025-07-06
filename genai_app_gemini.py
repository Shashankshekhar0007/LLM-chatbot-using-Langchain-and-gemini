import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from  langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm= ChatGoogleGenerativeAI(
  model="gemini-1.5-flash",
  temperature=0,
  max_tokens=None,
  timeout=None,
  max_retries=2
)

prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are an AI assistant."),
    ("human","Question: {question}")
  ]
)

st.title("LangChain Chatbot")
input_text = st.text_input("Enter your question")

outputp=StrOutputParser()

chain=prompt|llm|outputp

if input_text:
  st.write(chain.invoke({"question": input_text}))
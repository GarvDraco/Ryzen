import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

st.title("Ryzen")
st.write("Chat with this simple AI assistant")

api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if api_key:
    model = ChatGroq(
        model_name="llama2-70b-4096",
        groq_api_key=api_key,
        temperature=1,
    )
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=model,
        memory=memory,
        verbose=False,
    )

# Get user input
if 'GROQ_API_KEY' in os.environ:
    user_input = st.chat_input("Type your message here...")
    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Thinking..."):
            response = conversation.predict(input=user_input)
        
        with st.chat_message("assistant"):
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.info("Please enter your Groq API key in the sidebar to start chatting!")
    st.write("Don't have a key? Sign up at https://console.groq.com to get one for free.")

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.subheader("About this Chatbot")
st.sidebar.write("""
    This is a simple Chatbot made by Garv using:
    - Streamlit for the web interface 
    - Langchain for managing the conversation
    - ChatGroq for accessing AI language models
    
    To use it, simply enter your Groq API key and start chatting!
""")

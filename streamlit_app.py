import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 chabotSL App')
st.set_page_config(
    page_title="My Custom Theme",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define custom theme
custom_theme = {
    "primaryColor": "#7F00FF",
    "backgroundColor": "blue",
    "secondaryBackgroundColor": "#EBEBEB",
    "textColor": "#333333",
    "font": "sans serif"
}

# Set Streamlit theme with custom theme
st.set_theme(custom_theme)

# Add elements to Streamlit app
st.title("My Custom Theme Example")
st.write("This is an example of a Streamlit app with a custom theme.")

#=============================
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

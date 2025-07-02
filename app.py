import streamlit as st
import streamlit.components.v1 as components

# Inject custom CSS to hide Streamlit's default UI elements
st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    .css-1d391kg {
        padding-top: 0rem;
        padding-right: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
    }
    .stApp {
        margin: auto;
    }
    header {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Read the HTML file content
with open("Ice_breaker_Data_Detectives_Case_Files.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Embed the HTML content in the Streamlit app
components.html(html_content, height=1000, scrolling=True)


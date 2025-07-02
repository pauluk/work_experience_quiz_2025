import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file content
with open("Ice_breaker_Data_Detectives_Case_Files.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Embed the HTML content in the Streamlit app
components.html(html_content, height=1000, scrolling=True)

st.write("This is your HTML content embedded in a Streamlit app.")

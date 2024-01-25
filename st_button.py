import streamlit as st
st.header("Streamlit Button")

if st.button("say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

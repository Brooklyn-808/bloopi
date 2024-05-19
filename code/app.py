import streamlit as st

    

    

def contact():
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")
    st.write("- Email: example@example.com")
    st.write("- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/)")
    st.write("- GitHub: [Your GitHub Profile](https://github.com/)")

st.sidebar.write("Navigation")
st.sidebar.page_link("app.py", label="Homepage")
st.sidebar.page_link("pages/about.py", label="About Me")
st.sidebar.page_link("pages/contact.py", label="Contact")
st.title("Welcome to My Portfolio!")
st.write("This is the home page of my portfolio website.")
st.write("Feel free to browse around and learn more about me.")


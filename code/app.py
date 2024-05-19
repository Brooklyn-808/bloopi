import streamlit as st

def home():
    st.title("Welcome to My Portfolio!")
    st.write("This is the home page of my portfolio website.")
    st.write("Feel free to browse around and learn more about me.")

def about():
    st.title("About Me")
    st.write("I am a passionate developer who loves creating awesome projects.")
    st.write("In my free time, I enjoy learning new technologies and building cool stuff.")

def contact():
    st.title("Contact Me")
    st.write("Feel free to reach out to me through the following channels:")
    st.write("- Email: example@example.com")
    st.write("- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/)")
    st.write("- GitHub: [Your GitHub Profile](https://github.com/)")

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

    if selection == "Home":
        home()
    elif selection == "About":
        about()
    elif selection == "Contact":
        contact()

if __name__ == "__main__":
    main()

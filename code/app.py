import streamlit as st
import openai

# Fetching the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

def generate_text(prompt, max_tokens=50, temperature=0.7):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=max_tokens,
      temperature=temperature,
    )
    return response.choices[0].text.strip()

def main():
    st.title("Generative AI Text Generation")

    prompt = st.text_area("Enter a prompt:", "Once upon a time")

    max_tokens = st.slider("Max Tokens (length of generated text)", min_value=20, max_value=200, value=50, step=10)
    temperature = st.slider("Temperature (creativity of the AI)", min_value=0.1, max_value=1.0, value=0.7, step=0.1)

    if st.button("Generate"):
        with st.spinner("Generating..."):
            generated_text = generate_text(prompt, max_tokens=max_tokens, temperature=temperature)
            st.text_area("Generated Text:", generated_text, height=300)

if __name__ == "__main__":
    main()

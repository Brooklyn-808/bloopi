import streamlit as st
import gpt_2_simple as gpt2

# Download the GPT-2 model (this only needs to be done once)
gpt2.download_gpt2(model_name="124M")

# Function to generate text using GPT-2
def generate_text(prompt):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    generated_text = gpt2.generate(sess, prefix=prompt, return_as_list=True)[0]
    return generated_text

def main():
    st.title("Generative AI Text Generation")

    prompt = st.text_area("Enter a prompt:", "Once upon a time")

    if st.button("Generate"):
        with st.spinner("Generating..."):
            generated_text = generate_text(prompt)
            st.text_area("Generated Text:", generated_text, height=300)

if __name__ == "__main__":
    main()

import streamlit as st
import google.generativeai as genai

# Configure Gemini AI API key
GOOGLE_API_KEY = "AIzaSyABcgB6_ekXpU1FffEt9ANh2fLEMWRbLu8"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

st.title("💻 Gemini AI Code Generator")

st.write("""
Enter a prompt describing the code you want to generate, and Gemini AI will create the code for you.
""")

prompt = st.text_area("Enter your code generation prompt here:", height=150)

if st.button("Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a prompt to generate code.")
    else:
        with st.spinner("Generating code with Gemini AI..."):
            try:
                # We can give a clear instruction to generate code from the prompt
                # Optionally you can add system instructions or temperature etc.
                response = model.generate_content(
                    f"Write code for the following request:\n\"\"\"\n{prompt}\n\"\"\"\n"
                )
                st.subheader("🧑‍💻 Generated Code")
                st.code(response.text, language="python")  # show code block with syntax highlight
            except Exception as e:
                st.error(f"Gemini API error: {e}")

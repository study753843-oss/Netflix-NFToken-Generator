import streamlit as st
import subprocess

st.title("Netflix NFToken Generator")
st.write("Apni cookie niche paste karein aur Generate par click karein.")

cookie_input = st.text_area("Cookie yahan paste karein:")

if st.button("Generate Token"):
    if cookie_input:
        with open("input.txt", "w") as f:
            f.write(cookie_input)
        
        # Script run karna
        result = subprocess.run(["python", "nf-token-generator.py"], capture_output=True, text=True)
        st.code(result.stdout)
    else:
        st.error("Cookie field khali hai!")
      

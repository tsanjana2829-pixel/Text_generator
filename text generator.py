
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖"
)

st.title("🤖 AI Text Generator")
st.write("✨ Enter a sentence and let AI complete it!")

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="LiquidAI/LFM2.5-2.6B"
    )

generator = load_model()

prompt = st.text_area(
    "✍️ Enter your text:",
    placeholder="Artificial Intelligence is..."
)

if st.button("✨ Generate Text"):
    if prompt:
        with st.spinner("🤖 Generating..."):
            result = generator(
                prompt,
                max_new_tokens=50,
                num_return_sequences=1
            )

        st.subheader("📝 Generated Text")
        st.write(result[0]["generated_text"])
    else:
        st.warning("⚠️ Please enter some text first!")
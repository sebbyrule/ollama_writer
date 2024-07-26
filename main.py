import streamlit as st
from langchain_ollama import OllamaLLM
import time

st.set_page_config(page_title="Ollama Article Writer", layout="wide")
st.title('Ollama Article Writer')

# Available models
MODELS = ["llama3.1", "mistral", "llama2-uncensored", "zephyr"]

def generate_article(prompt, model_name, max_tokens):
    """
    Generates an article using the given prompt and model.
    """
    try:
        llm = OllamaLLM(model=model_name, num_ctx=max_tokens)
        with st.spinner('Generating article...'):
            response = llm.invoke(prompt)
        return response
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def save_article(filename, content, format='txt'):
    """
    Saves an article to a file.
    """
    try:
        with open(f"./articles/{filename}.{format}", "w") as f:
            f.write(content)
        st.success(f"Article saved to {filename}.{format}")
    except Exception as e:
        st.error(f"An error occurred while saving: {str(e)}")

# Initialize session state
if 'articles' not in st.session_state:
    st.session_state.articles = []

# Sidebar for configuration
st.sidebar.header("Configuration")
selected_model = st.sidebar.selectbox("Choose a model", MODELS)
max_tokens = st.sidebar.slider("Max Tokens", 100, 15000, 500)

# Main form for article generation
with st.form("article_form"):
    prompt = st.text_area("Enter your prompt")
    submitted = st.form_submit_button("Generate Article")
    if submitted and prompt:
        article = generate_article(prompt, selected_model, max_tokens)
        if article:
            st.session_state.articles.append(article)

# Display generated articles
if st.session_state.articles:
    st.header("Generated Articles")
    for i, article in enumerate(st.session_state.articles):
        with st.expander(f"Article {i+1}"):
            st.markdown(article)
            st.write(f"Word count: {len(article.split())}")
            
            # Edit functionality
            edited_article = st.text_area("Edit article", value=article, key=f"edit_{i}", height=300)
            if st.button("Update", key=f"update_{i}"):
                st.session_state.articles[i] = edited_article
                st.success("Article updated!")
            
            # Download functionality
            col1, col2 = st.columns(2)
            filename = col1.text_input("Filename", key=f"filename_{i}")
            format = col2.selectbox("Format", ['txt', 'md'], key=f"format_{i}")
            if st.button("Download", key=f"download_{i}"):
                if filename:
                    save_article(filename, edited_article, format)
                else:
                    st.warning("Please enter a filename.")

# Clear all button
if st.session_state.articles and st.button("Clear All Articles"):
    st.session_state.articles = []
    st.success("All articles cleared!")

if __name__ == "__main__":
    pass
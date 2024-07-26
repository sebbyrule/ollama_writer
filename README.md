# Ollama Article Writer

Ollama Article Writer is a Streamlit-based web application that leverages the power of Ollama's language models to generate articles based on user prompts. This tool allows users to easily create, edit, and download AI-generated content.

## Features

- Generate articles using various Ollama models
- Edit generated articles within the app
- Download articles in different formats (txt, md)
- Configure generation parameters (model selection, max tokens)
- Keep a history of generated articles in the current session
- Display word count for each article
- Clear all generated articles with a single click

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Ollama installed and running on your system
- Streamlit
- LangChain

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/sebbyrule/ollama-writer.git
   ```

2. Navigate to the project directory:
   ```
   cd ollama-writer
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure Ollama is running on your system.

2. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Use the sidebar to select your desired Ollama model and set the maximum token length.

5. Enter your prompt in the text area and click "Generate Article".

6. View, edit, and download your generated articles as needed.

## Configuration

You can modify the available models by editing the `MODELS` list in the script:

```python
MODELS = ["llama2", "mistral", "llama2-uncensored", "zephyr"]
```

Add or remove models based on what you have available in your Ollama installation.

## Contributing

Contributions to the Ollama Article Writer are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the language models
- [Streamlit](https://streamlit.io/) for the web app framework
- [LangChain](https://www.langchain.com/) for the LLM integration

## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.
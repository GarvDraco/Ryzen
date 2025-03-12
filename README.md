# Ryzen Chatbot

This is a simple AI assistant chatbot built using Streamlit, Langchain, and ChatGroq.

## Features

- **Streamlit**: Provides a web interface for the chatbot.
- **Langchain**: Manages the conversation flow.
- **ChatGroq**: Accesses AI language models for generating responses.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <your-github-repo-url>
   cd <your-repo-name>
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\.venv\Scripts\Activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run chatbot.py
   ```

## Usage

- Enter your Groq API key in the sidebar to start chatting with the AI assistant.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Groq AI Chatbot

A simple command-line AI chatbot built using the Groq API and Python.

## Features

* Accepts user input continuously
* Generates AI-powered responses using Groq
* Secure API key management using `.env`
* Exits gracefully when the user types `exit`

## Project Structure

GROQ_CHATBOT/

├── app.py

├── .env

├── .gitignore

├── requirements.txt

└── venv/

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd GROQ_CHATBOT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a .env file

```env
GROQ_API_KEY=your_api_key_here
```

### 6. Run the chatbot

```bash
python app.py
```

## Example

```text
AI Chatbot Started!
Type 'exit' to quit.

You: What is AI?

Bot: Artificial Intelligence (AI) is...

You: exit

Bot: Goodbye!
```

## Technologies Used
* Python
* Groq API
* python-dotenv

## Author
Suganda Karaguppi

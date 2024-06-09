# AI Promt Codebase Generation

This Python script utilizes the Gemini AI API to generate codebase for user interfaces (UIs) and packages them into a zip file. The generated codebase includes files for a React frontend, a Node.js backend, and MongoDB storage, all integrated to create a functional application.

## Requirements
- Python 3.x
- `google.generativeai` library
- Gemini AI API key (obtained from the Gemini AI website)

## Setup
1. Install the required dependencies using pip install -r requirements.txt:
2. Obtain an API key from the Gemini AI website and set it as an environment variable named `API_KEY` in a `.env` file.

## Usage
1. Run the Python script `main.py`.
2. Input the prompt when prompted by the script. This prompt should describe the requirements for the codebase generation, such as the desired technologies (React, Node.js, MongoDB), features, and any specific instructions.
3. The script will generate the codebase based on the provided prompt and package it into a zip file named `application.zip` and also file in folder generate_app.


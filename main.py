import os
import zipfile
from dotenv import load_dotenv
import google.generativeai as genai
import re

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found. Make sure it is set in the .env file")

genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 10285,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

# User prompt
prompt = input("Enter your prompt: ")
response = chat_session.send_message(prompt)

print(response.text)

# Function to extract file extension from prompt
def extract_file_extension(prompt):
    match = re.search(r'\b(\w+)\s*file\b', prompt.lower())
    if match:
        return f".{match.group(1)}"
    return ".txt"  # Default extension if none found

file_extension = extract_file_extension(prompt)
file_name = "app" + file_extension
file_content = response.text.strip()

def save_file(content, file_name, base_dir="generated_app"):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Created file: {file_path} with content:\n{content}")

def create_zip_from_files(base_dir="generated_app", zip_file_name="application.zip"):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, _, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Adding {file_path} to zip")
                zipf.write(file_path, os.path.relpath(file_path, base_dir))
    print(f"Created zip file: {zip_file_name}")

save_file(file_content, file_name)

print(f"Files in {os.listdir('generated_app')}")

create_zip_from_files()

print("Application generated and zipped successfully!")

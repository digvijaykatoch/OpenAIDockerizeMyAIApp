from flask import Flask, request, render_template
from flask_cors import CORS
import openai
import os
import re

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# Set up OpenAI API key and model
openai.api_key = "YOUR_API_KEY"
model_engine = "davinci"

# Define endpoint for training the OpenAI model on the specified text data
@app.route('/train', methods=['POST'])
def train():
    folder_path = request.json['folder_path']

    # Get all text files in the specified folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    # Combine all text files into a single string
    text = ""
    for file in text_files:
        with open(os.path.join(folder_path, file), 'r') as f:
            text += f.read()

    # Clean up the text by removing extra whitespace and special characters
    text = re.sub('\s+', ' ', text)
    text = re.sub('[^a-zA-Z0-9 \n\.]', '', text)

    # Train the OpenAI model on the cleaned text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Return the model response as JSON
    return {
        'response': response.choices[0].text
    }

# Define endpoint for running the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    question = request.json['question']

    # Persist the question
    with open('question_log.txt', 'a') as f:
        f.write(question + '\n')

    # Generate a response from the OpenAI model
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return the model response as JSON
    return {
        'response': response.choices[0].text
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

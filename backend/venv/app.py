
import re
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import requests
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_log_file(log_file_path):
    log_entries = []
    current_log = ""

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line:  # Skip empty lines
                    if is_timestamp_line(line):
                        if current_log:
                            log_entries.append(current_log)
                        current_log = line
                    else:
                        current_log += " " + line

            # Append the last log entry
            if current_log:
                log_entries.append(current_log)
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return log_entries

def is_timestamp_line(line):
    timestamp_patterns = [
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
        r"\d{10,13}",
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
        r"\[\d+\.\d+\]",
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
        r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
        r"\d{13}",
        r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
    ]
    return any(re.match(pattern, line) for pattern in timestamp_patterns)

def preprocess_logs(logs):
    print("Preprocessing logs...")
    parsed_logs = []
    for log in logs:
        timestamp, message = extract_timestamp_and_message(log)
        if timestamp and message:
            parsed_logs.append({'timestamp': timestamp, 'message': message})
            print(f"{timestamp}\n{message}")
    return pd.DataFrame(parsed_logs)

def extract_timestamp_and_message(log):
    for pattern in [
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
        r"\d{10,13}",
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
        r"\[\d+\.\d+\]",
        r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
        r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
        r"\d{13}",
        r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
    ]:
        match = re.match(pattern, log)
        if match:
            timestamp = match.group()
            message = log[len(timestamp):].strip()
            return timestamp, message
    return None, None

def load_error_keywords(file_path):
    error_keywords = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                keyword = line.strip()
                if keyword:
                    error_keywords.append(keyword)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading error keywords: {e}")
    return error_keywords

def check_for_errors(message, error_keywords):
    # Check if any error keywords are present in the message (case-insensitive)
    for keyword in error_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
            return True
    return False

@app.route('/api/analyze', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    uploaded_file = request.files['file']
    prompt = request.form.get('prompt')  # Get the prompt from the request
    error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
    if uploaded_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if uploaded_file and allowed_file(uploaded_file.filename):
        # Save the uploaded file to a specific location
        upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
        uploaded_file.save(upload_file_path)

        # Open and process the saved file
        logs = parse_log_file(upload_file_path)
        print(logs)
        parsed_logs = preprocess_logs(logs)
        print(parsed_logs)
        # parsed_logs.to_csv('parsed_log.csv')
        error_keywords = load_error_keywords(error_keywords_file_path)
        errors = []
        for index, row in parsed_logs.iterrows():
            message = row['message']
            if check_for_errors(message, error_keywords):
                errors.append({'timestamp': row['timestamp'], 'message': message})
        # Create a DataFrame from the list of errors
        error_df = pd.DataFrame(errors)
        print(error_df)
        timestamps, messages, response_texts = [], [], []
        for index, row in error_df.iterrows():
            response_texts.append(send_query_to_api(row['timestamp'], row['message'], prompt))
            timestamps.append(row['timestamp'])
            messages.append(row['message'])
        # Return the separate arrays as response
        return jsonify({'timestamps': timestamps, 'messages': messages, 'response_texts': response_texts}), 200
    else:
        return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

def send_query_to_api(timestamp, message, prompt):
    print(prompt)
    response_text = ''
    try:
        response = requests.post('################################################################################',
                                 json={
                                     'prompt': f"""{{
                                         'systemPrompt': 'You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the errors and other interesting aspects of the logs, and explain them so a new user can understand what they mean. If there are any steps they can do to resolve them, list the steps in your answer.',
                                         'user': 'hi',
                                         'Assistant': 'Hello, I am an error monitor in a log file',
                                         'user_query': '{prompt} {timestamp} {message}'
                                     }}""",
                                     "temperature": 0.75,
                                     "topP": 0.9,
                                     "maxTokens": 600
                                 },
                                 stream=True)

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                response_text += chunk.decode('utf-8')

    except Exception as e:
        print(f"An error occurred while sending query to API: {e}")

    return response_text

if __name__ == '__main__':
    app.run(debug=True)

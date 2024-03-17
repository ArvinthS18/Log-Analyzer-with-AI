# .\venv\Scripts\Activate
# Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/data')
# def get_data():
#   # Simulate some data)
#   try:
#     data = {'message': 'Hello from Flask12!'}
#     return jsonify(data)
#   except Exception as e:  # Catch potential exceptions for robust error handling
#     return jsonify({'error': str(e)}), 500  # Return error message and status code 500 (Internal Server Error)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import csv
# import json
# import re

# app = Flask(__name__)
# CORS(app)

# ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def is_valid_csv(file_content):
#     try:
#         csv.reader(file_content.decode().splitlines())
#         return True
#     except Exception as e:
#         return False

# def is_valid_json(file_content):
#     try:
#         json.loads(file_content.decode())
#         return True
#     except Exception as e:
#         return False

# def is_valid_xml(file_content):
#     # Check if it looks like XML (simplified check)
#     return '<' in file_content.decode() and '>' in file_content.decode()

# def extract_logs_from_text(file_content):
#     logs = []
#     lines = file_content.decode().splitlines()

#     # Assume the first line contains headers
#     headers = lines[0].split()

#     for line in lines[1:]:
#         # Split the line based on whitespace or any other delimiter
#         values = re.split(r'\s+', line.strip())

#         # Create a dictionary to store the log entry
#         log_entry = {}
        
#         # Check if the number of values matches the number of headers
#         if len(values) == len(headers):
#             for i in range(len(headers)):
#                 log_entry[headers[i]] = values[i]
#         else:
#             # If the number of values doesn't match, create a single 'Message' field
#             log_entry['Message'] = ' '.join(values)

#         logs.append(log_entry)

#     return logs

# def analyze_file(file_content, filename):
#     logs = []

#     # Check if it's a valid CSV, JSON, or XML based on file extension
#     file_extension = filename.rsplit('.', 1)[1].lower()
#     if file_extension == 'csv' and is_valid_csv(file_content):
#         csv_data = csv.DictReader(file_content.decode().splitlines())
#         logs = [row for row in csv_data]
#     elif file_extension == 'json' and is_valid_json(file_content):
#         logs = json.loads(file_content.decode())
#     elif file_extension == 'xml' and is_valid_xml(file_content):
#         # Placeholder for XML parsing logic (not implemented here)
#         pass
#     else:
#         # Assume it's plain text and try to extract logs
#         logs = extract_logs_from_text(file_content)

#     return logs

# @app.route('/api/analyze', methods=['POST'])
# def analyze_file_endpoint():
#     if request.method == 'POST':
#         try:
#             uploaded_file = request.files.get('file')
#             if uploaded_file and allowed_file(uploaded_file.filename):
#                 file_content = uploaded_file.read()
#                 logs = analyze_file(file_content, uploaded_file.filename)
#                 return jsonify({'logs': logs})
#             else:
#                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500
#     else:
#         return jsonify({'error': 'Method not allowed'}), 405

# if __name__ == '__main__':
#     app.run(debug=True)
# import requests
# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/api/analyze', methods=['POST'])
# def analyze_file_endpoint():
#     if request.method == 'POST':
#         try:
#             uploaded_file = request.files.get('file')
            
#             if uploaded_file and allowed_file(uploaded_file.filename):
#                 file_content = uploaded_file.read()
#                 print(file_content)
#                 # Send logs to Logstash
#                 response = requests.post(LOGSTASH_URL, data=file_content)
                
#                 if response.status_code == 200:
#                     print("HI")
#                     return jsonify({'message': 'Logs sent to Logstash successfully'})
#                 else:
#                     return jsonify({'error': 'Failed to send logs to Logstash'}), 500
#             else:
#                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500
#     else:
#         return jsonify({'error': 'Method not allowed'}), 405

# if __name__ == '__main__':
#     app.run(debug=True)
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running
ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"  # Elasticsearch URL with credentials
INDEX_NAME = "weare"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/analyze', methods=['POST'])
def analyze_file_endpoint():
    if request.method == 'POST':
        try:
            uploaded_file = request.files.get('file')
            
            if uploaded_file and allowed_file(uploaded_file.filename):
                file_content = uploaded_file.read()
                # Send logs to Logstash
                response = requests.post(LOGSTASH_URL, data=file_content)
                
                if response.status_code == 200:
                    print("Logs sent to Logstash successfully")
                    # Fetch analyzed data from Elasticsearch
                    es = Elasticsearch([ELASTICSEARCH_URL])  # Initialize Elasticsearch client with credentials
                    query = {"query": {"match_all": {}}}  # Match all documents in the index
                    result = es.search(index=INDEX_NAME, body=query)
                    analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
                    # Print the analyzed data in the terminal
                    print("Analyzed data:")
                    for data in analyzed_data:
                        print(data)
                    return jsonify({'message': 'Logs sent to Logstash successfully', 'analyzed_data': analyzed_data})
                else:
                    return jsonify({'error': 'Failed to send logs to Logstash'}), 500
            else:
                return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)

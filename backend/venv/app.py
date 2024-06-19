# # # # # # # .\venv\Scripts\Activate
# # # # # # # Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# # # # # # # from flask import Flask, jsonify

# # # # # # # app = Flask(__name__)

# # # # # # # @app.route('/api/data')
# # # # # # # def get_data():
# # # # # # #   # Simulate some data)
# # # # # # #   try:
# # # # # # #     data = {'message': 'Hello from Flask12!'}
# # # # # # #     return jsonify(data)
# # # # # # #   except Exception as e:  # Catch potential exceptions for robust error handling
# # # # # # # # # # # # # #     return jsonify({'error': str(e)}), 500  # Return error message and status code 500 (Internal Server Error)
# # # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # # # import csv
# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # import re

# # # # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # # # def is_valid_csv(file_content):
# # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # #         csv.reader(file_content.decode().splitlines())
# # # # # # # # # # # # # #         return True
# # # # # # # # # # # # # #     except Exception as e:
# # # # # # # # # # # # # #         return False

# # # # # # # # # # # # # # def is_valid_json(file_content):
# # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # #         json.loads(file_content.decode())
# # # # # # # # # # # # # #         return True
# # # # # # # # # # # # # #     except Exception as e:
# # # # # # # # # # # # # #         return False

# # # # # # # # # # # # # # def is_valid_xml(file_content):
# # # # # # # # # # # # # #     # Check if it looks like XML (simplified check)
# # # # # # # # # # # # # #     return '<' in file_content.decode() and '>' in file_content.decode()

# # # # # # # # # # # # # # def extract_logs_from_text(file_content):
# # # # # # # # # # # # # #     logs = []
# # # # # # # # # # # # # #     lines = file_content.decode().splitlines()

# # # # # # # # # # # # # #     # Assume the first line contains headers
# # # # # # # # # # # # # #     headers = lines[0].split()

# # # # # # # # # # # # # #     for line in lines[1:]:
# # # # # # # # # # # # # #         # Split the line based on whitespace or any other delimiter
# # # # # # # # # # # # # #         values = re.split(r'\s+', line.strip())

# # # # # # # # # # # # # #         # Create a dictionary to store the log entry
# # # # # # # # # # # # # #         log_entry = {}
        
# # # # # # # # # # # # # #         # Check if the number of values matches the number of headers
# # # # # # # # # # # # # #         if len(values) == len(headers):
# # # # # # # # # # # # # #             for i in range(len(headers)):
# # # # # # # # # # # # # #                 log_entry[headers[i]] = values[i]
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             # If the number of values doesn't match, create a single 'Message' field
# # # # # # # # # # # # # #             log_entry['Message'] = ' '.join(values)

# # # # # # # # # # # # # #         logs.append(log_entry)

# # # # # # # # # # # # # #     return logs

# # # # # # # # # # # # # # def analyze_file(file_content, filename):
# # # # # # # # # # # # # #     logs = []

# # # # # # # # # # # # # #     # Check if it's a valid CSV, JSON, or XML based on file extension
# # # # # # # # # # # # # #     file_extension = filename.rsplit('.', 1)[1].lower()
# # # # # # # # # # # # # #     if file_extension == 'csv' and is_valid_csv(file_content):
# # # # # # # # # # # # # #         csv_data = csv.DictReader(file_content.decode().splitlines())
# # # # # # # # # # # # # #         logs = [row for row in csv_data]
# # # # # # # # # # # # # #     elif file_extension == 'json' and is_valid_json(file_content):
# # # # # # # # # # # # # #         logs = json.loads(file_content.decode())
# # # # # # # # # # # # # #     elif file_extension == 'xml' and is_valid_xml(file_content):
# # # # # # # # # # # # # #         # Placeholder for XML parsing logic (not implemented here)
# # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         # Assume it's plain text and try to extract logs
# # # # # # # # # # # # # #         logs = extract_logs_from_text(file_content)

# # # # # # # # # # # # # #     return logs

# # # # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # # # def analyze_file_endpoint():
# # # # # # # # # # # # # #     if request.method == 'POST':
# # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # #             uploaded_file = request.files.get('file')
# # # # # # # # # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # # # #                 file_content = uploaded_file.read()
# # # # # # # # # # # # # #                 logs = analyze_file(file_content, uploaded_file.filename)
# # # # # # # # # # # # # #                 return jsonify({'logs': logs})
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # # # # import requests
# # # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # # from flask_cors import CORS

# # # # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running

# # # # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # # # def analyze_file_endpoint():
# # # # # # # # # # # # # #     if request.method == 'POST':
# # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # # # # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # # # #                 file_content = uploaded_file.read()
# # # # # # # # # # # # # #                 print(file_content)
# # # # # # # # # # # # # #                 # Send logs to Logstash
# # # # # # # # # # # # # #                 response = requests.post(LOGSTASH_URL, data=file_content)
                
# # # # # # # # # # # # # #                 if response.status_code == 200:
# # # # # # # # # # # # # #                     print("HI")
# # # # # # # # # # # # # #                     return jsonify({'message': 'Logs sent to Logstash successfully'})
# # # # # # # # # # # # # #                 else:
# # # # # # # # # # # # # #                     return jsonify({'error': 'Failed to send logs to Logstash'}), 500
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # # # # import requests
# # # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # # # from elasticsearch import Elasticsearch

# # # # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running
# # # # # # # # # # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"  # Elasticsearch URL with credentials
# # # # # # # # # # # # # # INDEX_NAME = "hi123"

# # # # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # # # def analyze_file_endpoint():
# # # # # # # # # # # # # #     if request.method == 'POST':
# # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # # # # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # # # #                 file_content = uploaded_file.read()
# # # # # # # # # # # # # #                 # Send logs to Logstash
# # # # # # # # # # # # # #                 response = requests.post(LOGSTASH_URL, data=file_content)
                
# # # # # # # # # # # # # #                 if response.status_code == 200:
# # # # # # # # # # # # # #                     print("Logs sent to Logstash successfully")
# # # # # # # # # # # # # #                     # Fetch analyzed data from Elasticsearch
# # # # # # # # # # # # # #                     es = Elasticsearch([ELASTICSEARCH_URL])  # Initialize Elasticsearch client with credentials
# # # # # # # # # # # # # #                     query = {"query": {"match_all": {}}}  # Match all documents in the index
# # # # # # # # # # # # # #                     result = es.search(index=INDEX_NAME, body=query)
# # # # # # # # # # # # # #                     analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # # # # # # # # # #                     # Print the analyzed data in the terminal
# # # # # # # # # # # # # #                     print("Analyzed data:")
# # # # # # # # # # # # # #                     for data in analyzed_data:
# # # # # # # # # # # # # #                         print(data)
# # # # # # # # # # # # # #                     return jsonify({'message': 'Logs sent to Logstash successfully', 'analyzed_data': analyzed_data})
# # # # # # # # # # # # # #                 else:
# # # # # # # # # # # # # #                     return jsonify({'error': 'Failed to send logs to Logstash'}), 500
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # # # # import requests
# # # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # # # from elasticsearch import Elasticsearch

# # # # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running
# # # # # # # # # # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"  # Elasticsearch URL with credentials
# # # # # # # # # # # # # # INDEX_NAME = "hi123"

# # # # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # # # def get_analyzed_data_from_elasticsearch():
# # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # #         es = Elasticsearch([ELASTICSEARCH_URL])
# # # # # # # # # # # # # #         query = {"query": {"match_all": {}}}
# # # # # # # # # # # # # #         result = es.search(index=INDEX_NAME, body=query)
# # # # # # # # # # # # # #         analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # # # # # # # # # #         return analyzed_data
# # # # # # # # # # # # # #     except Exception as e:
# # # # # # # # # # # # # #         print(f"Error fetching data from Elasticsearch: {str(e)}")
# # # # # # # # # # # # # #         return None

# # # # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # # # def analyze_file_endpoint():
# # # # # # # # # # # # # #     if request.method == 'POST':
# # # # # # # # # # # # # #         try:
# # # # # # # # # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # # # # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # # # #                 files = {'file': uploaded_file}
# # # # # # # # # # # # # #                 response = requests.post(LOGSTASH_URL, files=files)
                
# # # # # # # # # # # # # #                 if response.status_code == 200:
# # # # # # # # # # # # # #                     print("File sent to Logstash successfully")
# # # # # # # # # # # # # #                     analyzed_data = get_analyzed_data_from_elasticsearch()
# # # # # # # # # # # # # #                     if analyzed_data:
# # # # # # # # # # # # # #                         return jsonify({'message': 'File sent to Logstash successfully', 'analyzed_data': analyzed_data})
# # # # # # # # # # # # # #                     else:
# # # # # # # # # # # # # #                         return jsonify({'error': 'Failed to fetch analyzed data from Elasticsearch'}), 500
# # # # # # # # # # # # # #                 else:
# # # # # # # # # # # # # #                     return jsonify({'error': 'Failed to send file to Logstash'}), 500
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # # # # # # # # #         except Exception as e:
# # # # # # # # # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # # # import requests
# # # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # # from elasticsearch import Elasticsearch

# # # # # # # # # # # # # app = Flask(__name__)

# # # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # # LOGSTASH_URL = "http://localhost:5044"
# # # # # # # # # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"
# # # # # # # # # # # # # INDEX_NAME = "hi123"

# # # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # # def send_to_logstash(file):
# # # # # # # # # # # # #     try:
# # # # # # # # # # # # #         files = {'file': file}
# # # # # # # # # # # # #         response = requests.post(LOGSTASH_URL, files=files)
# # # # # # # # # # # # #         return response.status_code == 200
# # # # # # # # # # # # #     except Exception as e:
# # # # # # # # # # # # #         print(f"Error sending file to Logstash: {str(e)}")
# # # # # # # # # # # # #         return False

# # # # # # # # # # # # # def get_analyzed_data_from_elasticsearch():
# # # # # # # # # # # # #     try:
# # # # # # # # # # # # #         es = Elasticsearch([ELASTICSEARCH_URL])
# # # # # # # # # # # # #         query = {"query": {"match_all": {}}}
# # # # # # # # # # # # #         result = es.search(index=INDEX_NAME, body=query)
# # # # # # # # # # # # #         analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # # # # # # # # #         return analyzed_data
# # # # # # # # # # # # #     except Exception as e:
# # # # # # # # # # # # #         print(f"Error fetching data from Elasticsearch: {str(e)}")
# # # # # # # # # # # # #         return None

# # # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # # def upload_file():
# # # # # # # # # # # # #     if 'file' not in request.files:
# # # # # # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # # #         if send_to_logstash(uploaded_file):
# # # # # # # # # # # # #             analyzed_data = get_analyzed_data_from_elasticsearch()
# # # # # # # # # # # # #             if analyzed_data:
# # # # # # # # # # # # #                 return jsonify({'message': 'File uploaded and analyzed successfully', 'analyzed_data': analyzed_data}), 200
# # # # # # # # # # # # #             else:
# # # # # # # # # # # # #                 return jsonify({'error': 'Failed to fetch analyzed data from Elasticsearch'}), 500
# # # # # # # # # # # # #         else:
# # # # # # # # # # # # #             return jsonify({'error': 'Failed to send file to Logstash'}), 500
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # # import ollama
# # # # # # # # # # # # import datetime
# # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # # CORS(app)

# # # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # # def preprocess_logs(logs):
# # # # # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # # # # #     parsed_logs = []
# # # # # # # # # # # #     for log in logs:
# # # # # # # # # # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # # # # # # # # # #         message = log[20:].strip()
# # # # # # # # # # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # # # # def analyze_log_message(log_message):
# # # # # # # # # # # #     print("Analyzing log message:", log_message)
# # # # # # # # # # # #     analysis = ollama.chat(
# # # # # # # # # # # #         model="mistral",
# # # # # # # # # # # #         messages=[{"role": "user", "content": log_message}]
# # # # # # # # # # # #     )["message"]["content"]
# # # # # # # # # # # #     return analysis

# # # # # # # # # # # # def monitor_errors_and_warnings(logs):
# # # # # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # # # # #         analysis = analyze_log_message(row['message'] + " Please analyze this log message for errors.")
# # # # # # # # # # # #         print(f"Analysis for log message '{row['message']}':\n{analysis}\n")

# # # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # # def upload_file():
# # # # # # # # # # # #     if 'file' not in request.files:
# # # # # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # # #         # Read the file as text and preprocess logs
# # # # # # # # # # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # # # # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # # # # # #         monitor_errors_and_warnings(parsed_logs)
# # # # # # # # # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # # import ollama
# # # # # # # # # # # import datetime
# # # # # # # # # # # import pandas as pd
# # # # # # # # # # # import requests

# # # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # # CORS(app)

# # # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # # # # # # # # # def allowed_file(filename):
# # # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # # def preprocess_logs(logs):
# # # # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # # # #     parsed_logs = []
# # # # # # # # # # #     for log in logs:
# # # # # # # # # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # # # # # # # # #         message = log[20:].strip()
# # # # # # # # # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # # # def analyze_log_message(log_message):
# # # # # # # # # # #     print("Analyzing log message:", log_message)
# # # # # # # # # # #     analysis = ollama.chat(
# # # # # # # # # # #         model="mistral",
# # # # # # # # # # #         messages=[{"role": "user", "content": log_message}]
# # # # # # # # # # #     )["message"]["content"]
# # # # # # # # # # #     return analysis

# # # # # # # # # # # def monitor_errors_and_warnings(logs):
# # # # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # # # #         analysis = analyze_log_message(row['message'] + " Please analyze this log message for errors.")
# # # # # # # # # # #         print(f"Analysis for log message '{row['message']}':\n{analysis}\n")
        
# # # # # # # # # # #         # Prepare data to be sent to Logstash
# # # # # # # # # # #         log_data = {
# # # # # # # # # # #             'timestamp': str(row['timestamp']),
# # # # # # # # # # #             'message': row['message'],
# # # # # # # # # # #             'analysis': analysis
# # # # # # # # # # #         }
        
# # # # # # # # # # #         # Send data to Logstash
# # # # # # # # # # #         try:
# # # # # # # # # # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # # #                 print("Data sent to Logstash successfully")
# # # # # # # # # # #             else:
# # # # # # # # # # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # # # # # # # # # #         except Exception as e:
# # # # # # # # # # #             print(f"Error occurred while sending data to Logstash: {str(e)}")

# # # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # # def upload_file():
# # # # # # # # # # #     if 'file' not in request.files:
# # # # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # # #         # Read the file as text and preprocess logs
# # # # # # # # # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # # # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # # # # #         monitor_errors_and_warnings(parsed_logs)
# # # # # # # # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # # # # # # # #     else:
# # # # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # #     app.run(debug=True)
# # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # import ollama
# # # # # # # # # # import datetime
# # # # # # # # # # import pandas as pd
# # # # # # # # # # import requests
# # # # # # # # # # import pandas as pd
# # # # # # # # # # from sklearn.model_selection import train_test_split
# # # # # # # # # # from sklearn.feature_extraction.text import CountVectorizer
# # # # # # # # # # from sklearn.naive_bayes import MultinomialNB
# # # # # # # # # # from sklearn.metrics import accuracy_score

# # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # CORS(app)
# # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # # # # # # # # def allowed_file(filename):
# # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # def preprocess_logs(logs):
# # # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # # #     parsed_logs = []
# # # # # # # # # #     for log in logs:
# # # # # # # # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # # # # # # # #         message = log[20:].strip()
# # # # # # # # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # # def analyze_log_message(timestamp, log_message):
# # # # # # # # # #     print("Analyzing log message:", timestamp, log_message)
# # # # # # # # # #     analysis = ollama.chat(
# # # # # # # # # #         model="mistral",
# # # # # # # # # #         messages=[{"role": "user", "timestamp": str(timestamp), "content": log_message}]
# # # # # # # # # #     )["message"]["content"]
# # # # # # # # # #     return analysis

# # # # # # # # # # def monitor_errors_and_warnings(logs):
# # # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # # #         timestamp = str(row['timestamp'])
# # # # # # # # # #         message = row['message']
# # # # # # # # # #         analysis = analyze_log_message(timestamp, message + " Please analyze this log message for errors.")
# # # # # # # # # #         print(f"Analysis for log message '{message}':\n{analysis}\n")
# # # # # # # # # #         log_data = {
# # # # # # # # # #             'timestamp': timestamp,
# # # # # # # # # #             'message': message,
# # # # # # # # # #             'analysis': analysis
# # # # # # # # # #         }
# # # # # # # # # #         try:
# # # # # # # # # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # #                 print("Data sent to Logstash successfully")
# # # # # # # # # #             else:
# # # # # # # # # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # # # # # # # # #         except Exception as e:
# # # # # # # # # #             print(f"Error occurred while sending data to Logstash: {str(e)}")


# # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # def upload_file():
# # # # # # # # # #     if 'file' not in request.files:
# # # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # # # #         print("Logs preprocessed:")
# # # # # # # # # #         print(parsed_logs)
# # # # # # # # # #         monitor_errors_and_warnings(parsed_logs)
# # # # # # # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # # # # # # #     else:
# # # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # #     app.run(debug=True)

# # # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # # from flask_cors import CORS
# # # # # # # # # # import ollama
# # # # # # # # # # import datetime
# # # # # # # # # # import pandas as pd
# # # # # # # # # # import requests
# # # # # # # # # # import pandas as pd
# # # # # # # # # # from sklearn.model_selection import train_test_split
# # # # # # # # # # from sklearn.feature_extraction.text import CountVectorizer
# # # # # # # # # # from sklearn.naive_bayes import MultinomialNB
# # # # # # # # # # from sklearn.metrics import accuracy_score

# # # # # # # # # # app = Flask(__name__)
# # # # # # # # # # CORS(app)
# # # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # # # # # # # # def allowed_file(filename):
# # # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # # def preprocess_logs(logs):
# # # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # # #     parsed_logs = []
# # # # # # # # # #     for log in logs:
# # # # # # # # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # # # # # # # #         message = log[20:].strip()
# # # # # # # # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # # #         print(parsed_logs)
# # # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # # def analyze_log_message(timestamp, log_message):
# # # # # # # # # #     print("Analyzing log message:", timestamp, log_message)
# # # # # # # # # #     analysis = ollama.chat(
# # # # # # # # # #         model="mistral",
# # # # # # # # # #         messages=[{"role": "user", "timestamp": str(timestamp), "content": log_message}]
# # # # # # # # # #     )["message"]["content"]
# # # # # # # # # #     return analysis

# # # # # # # # # # def monitor_errors_and_warnings(logs, prompt):
# # # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # # #         timestamp = str(row['timestamp'])
# # # # # # # # # #         message = row['message']
# # # # # # # # # #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# # # # # # # # # #         print(f"Analysis for log message '{message}':\n{analysis}\n")
# # # # # # # # # #         log_data = {
# # # # # # # # # #             'timestamp': timestamp,
# # # # # # # # # #             'message': message,
# # # # # # # # # #             'analysis': analysis
# # # # # # # # # #         }
# # # # # # # # # #         try:
# # # # # # # # # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # #                 print("Data sent to Logstash successfully")
# # # # # # # # # #             else:
# # # # # # # # # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # # # # # # # # #         except Exception as e:
# # # # # # # # # #             print(f"Error occurred while sending data to Logstash: {str(e)}")


# # # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # # def upload_file():
# # # # # # # # # #     if 'file' not in request.files:
# # # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request

# # # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # # # #         print("Logs preprocessed:")
# # # # # # # # # #         print(parsed_logs)
# # # # # # # # # #         monitor_errors_and_warnings(parsed_logs, prompt)  # Pass the prompt to the function
# # # # # # # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # # # # # # #     else:
# # # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # #     app.run(debug=True)
# # # # # # # # # import re
# # # # # # # # # import os
# # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # from flask_cors import CORS
# # # # # # # # # import ollama
# # # # # # # # # import datetime
# # # # # # # # # import pandas as pd
# # # # # # # # # import requests
# # # # # # # # # from werkzeug.utils import secure_filename

# # # # # # # # # app = Flask(__name__)
# # # # # # # # # CORS(app)
# # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'
# # # # # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # # # # def allowed_file(filename):
# # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # def parse_log_file(log_file_path):
# # # # # # # # #     log_entries = []
# # # # # # # # #     current_log = ""

# # # # # # # # #     try:
# # # # # # # # #         with open(log_file_path, 'r') as file:
# # # # # # # # #             for line in file:
# # # # # # # # #                 line = line.strip()

# # # # # # # # #                 if line:  # Skip empty lines
# # # # # # # # #                     if is_timestamp_line(line):
# # # # # # # # #                         if current_log:
# # # # # # # # #                             log_entries.append(current_log)
# # # # # # # # #                         current_log = line
# # # # # # # # #                     else:
# # # # # # # # #                         current_log += " " + line

# # # # # # # # #             # Append the last log entry
# # # # # # # # #             if current_log:
# # # # # # # # #                 log_entries.append(current_log)
# # # # # # # # #     except FileNotFoundError:
# # # # # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"An error occurred: {e}")

# # # # # # # # #     return log_entries

# # # # # # # # # def is_timestamp_line(line):
# # # # # # # # #     timestamp_patterns = [
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # # #         r"\d{10,13}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # # #         r"\d{13}",
# # # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # # #     ]
# # # # # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # # # # def preprocess_logs(logs):
# # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # #     parsed_logs = []
# # # # # # # # #     for log in logs:
# # # # # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # # # # #         if timestamp and message:
# # # # # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # #             print(f"{timestamp}\n{message}")
# # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # def extract_timestamp_and_message(log):
# # # # # # # # #     for pattern in [
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # # #         r"\d{10,13}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # # #         r"\d{13}",
# # # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # # #     ]:
# # # # # # # # #         match = re.match(pattern, log)
# # # # # # # # #         if match:
# # # # # # # # #             timestamp = match.group()
# # # # # # # # #             message = log[len(timestamp):].strip()
# # # # # # # # #             return timestamp, message
# # # # # # # # #     return None, None
# # # # # # # # # def load_error_keywords(file_path):
# # # # # # # # #     error_keywords = []
# # # # # # # # #     try:
# # # # # # # # #         with open(file_path, 'r') as file:
# # # # # # # # #             for line in file:
# # # # # # # # #                 keyword = line.strip()
# # # # # # # # #                 if keyword:
# # # # # # # # #                     error_keywords.append(keyword)
# # # # # # # # #     except FileNotFoundError:
# # # # # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # # # # #     return error_keywords

# # # # # # # # # def check_for_errors(message, error_keywords):
# # # # # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # # # # #     for keyword in error_keywords:
# # # # # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # # # # #             return True
# # # # # # # # #     return False

# # # # # # # # # def analyze_log_message(timestamp, log_message):
# # # # # # # # #     print("Analyzing log message:", timestamp, log_message)
# # # # # # # # #     combined_message = f"{timestamp}: {log_message}"
# # # # # # # # #     analysis = ollama.chat(
# # # # # # # # #         model="error-monitor",
# # # # # # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # # # # # #     )["message"]["content"]
# # # # # # # # #     return analysis

# # # # # # # # # def monitor_errors_and_warnings(logs, prompt):
# # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # #         timestamp = str(row['timestamp'])
# # # # # # # # #         message = row['message']
# # # # # # # # #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# # # # # # # # #         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
# # # # # # # # #         log_data = {
# # # # # # # # #             'timestamp': timestamp,
# # # # # # # # #             'message': message,
# # # # # # # # #             'analysis': analysis
# # # # # # # # #         }
# # # # # # # # #         try:
# # # # # # # # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # # # # # # # #             if response.status_code == 200:
# # # # # # # # #                 print("Data sent to Logstash successfully")
# # # # # # # # #             else:
# # # # # # # # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # # # # # # # #         except Exception as e:
# # # # # # # # #             print(f"Error occurred while sending data to Logstash: {str(e)}")

# # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # def upload_file():
# # # # # # # # #     if 'file' not in request.files:
# # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # #         # Save the uploaded file to a specific location
# # # # # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # # # # #         uploaded_file.save(upload_file_path)

# # # # # # # # #         # Open and process the saved file
# # # # # # # # #         logs = parse_log_file(upload_file_path)
# # # # # # # # #         print(logs)
# # # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # # #         print(parsed_logs)
# # # # # # # # #         # parsed_logs.to_csv('parsed_log.csv')
# # # # # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # # # # #         errors = []
# # # # # # # # #         for index, row in parsed_logs.iterrows():
# # # # # # # # #             message = row['message']
# # # # # # # # #             if check_for_errors(message, error_keywords):
# # # # # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message})

# # # # # # # # #     # Create a DataFrame from the list of errors
# # # # # # # # #         error_df = pd.DataFrame(errors)

# # # # # # # # #     # Print the DataFrame containing errors
# # # # # # # # #         print("Errors detected:")
# # # # # # # # #         print(error_df)
# # # # # # # # #         monitor_errors_and_warnings(error_df, prompt)  # Pass the prompt to the function
        
# # # # # # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # # # # # #     else:
# # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     app.run(debug=True)


# # # # # # # # # import re
# # # # # # # # # import os
# # # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # # from flask_cors import CORS
# # # # # # # # # import ollama
# # # # # # # # # import datetime
# # # # # # # # # import pandas as pd
# # # # # # # # # import requests
# # # # # # # # # from werkzeug.utils import secure_filename

# # # # # # # # # app = Flask(__name__)
# # # # # # # # # CORS(app)
# # # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'
# # # # # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # # # # def allowed_file(filename):
# # # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # # def parse_log_file(log_file_path):
# # # # # # # # #     log_entries = []
# # # # # # # # #     current_log = ""

# # # # # # # # #     try:
# # # # # # # # #         with open(log_file_path, 'r') as file:
# # # # # # # # #             for line in file:
# # # # # # # # #                 line = line.strip()

# # # # # # # # #                 if line:  # Skip empty lines
# # # # # # # # #                     if is_timestamp_line(line):
# # # # # # # # #                         if current_log:
# # # # # # # # #                             log_entries.append(current_log)
# # # # # # # # #                         current_log = line
# # # # # # # # #                     else:
# # # # # # # # #                         current_log += " " + line

# # # # # # # # #             # Append the last log entry
# # # # # # # # #             if current_log:
# # # # # # # # #                 log_entries.append(current_log)
# # # # # # # # #     except FileNotFoundError:
# # # # # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"An error occurred: {e}")

# # # # # # # # #     return log_entries

# # # # # # # # # def is_timestamp_line(line):
# # # # # # # # #     timestamp_patterns = [
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # # #         r"\d{10,13}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # # #         r"\d{13}",
# # # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # # #     ]
# # # # # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # # # # def preprocess_logs(logs):
# # # # # # # # #     print("Preprocessing logs...")
# # # # # # # # #     parsed_logs = []
# # # # # # # # #     for log in logs:
# # # # # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # # # # #         if timestamp and message:
# # # # # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # # #             print(f"{timestamp}\n{message}")
# # # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # # def extract_timestamp_and_message(log):
# # # # # # # # #     for pattern in [
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # # #         r"\d{10,13}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # # #         r"\d{13}",
# # # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # # #     ]:
# # # # # # # # #         match = re.match(pattern, log)
# # # # # # # # #         if match:
# # # # # # # # #             timestamp = match.group()
# # # # # # # # #             message = log[len(timestamp):].strip()
# # # # # # # # #             return timestamp, message
# # # # # # # # #     return None, None

# # # # # # # # # def load_error_keywords(file_path):
# # # # # # # # #     error_keywords = []
# # # # # # # # #     try:
# # # # # # # # #         with open(file_path, 'r') as file:
# # # # # # # # #             for line in file:
# # # # # # # # #                 keyword = line.strip()
# # # # # # # # #                 if keyword:
# # # # # # # # #                     error_keywords.append(keyword)
# # # # # # # # #     except FileNotFoundError:
# # # # # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # # # # #     except Exception as e:
# # # # # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # # # # #     return error_keywords

# # # # # # # # # def check_for_errors(message, error_keywords):
# # # # # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # # # # #     for keyword in error_keywords:
# # # # # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # # # # #             return True
# # # # # # # # #     return False

# # # # # # # # # def analyze_log_message(timestamp, log_message):
# # # # # # # # #     print("Analyzing log message:", timestamp, log_message)
# # # # # # # # #     combined_message = f"{timestamp}: {log_message}"
# # # # # # # # #     analysis = ollama.chat(
# # # # # # # # #         model="error-monitor",
# # # # # # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # # # # # #     )["message"]["content"]
# # # # # # # # #     return analysis

# # # # # # # # # def monitor_errors_and_warnings(logs, prompt):
# # # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # # #     analysis_results = []
# # # # # # # # #     for index, row in logs.iterrows():
# # # # # # # # #         timestamp = str(row['timestamp'])
# # # # # # # # #         message = row['message']
# # # # # # # # #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# # # # # # # # #         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
# # # # # # # # #         analysis_results.append(analysis)
# # # # # # # # #         print(analysis_results)

# # # # # # # # #     # Concatenate all analysis results into a single string
# # # # # # # # #     analysis_data = "\n".join(analysis_results)
# # # # # # # # #     return analysis_data

# # # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # # def upload_file():
# # # # # # # # #     if 'file' not in request.files:
# # # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # # #     uploaded_file = request.files['file']
# # # # # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# # # # # # # # #     if uploaded_file.filename == '':
# # # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # # #         # Save the uploaded file to a specific location
# # # # # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # # # # #         uploaded_file.save(upload_file_path)

# # # # # # # # #         # Open and process the saved file
# # # # # # # # #         logs = parse_log_file(upload_file_path)
# # # # # # # # #         parsed_logs = preprocess_logs(logs)

# # # # # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # # # # #         errors = []
# # # # # # # # #         for index, row in parsed_logs.iterrows():
# # # # # # # # #             message = row['message']
# # # # # # # # #             if check_for_errors(message, error_keywords):
# # # # # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message})

# # # # # # # # #         # Create a DataFrame from the list of errors
# # # # # # # # #         error_df = pd.DataFrame(errors)
# # # # # # # # #         print(error_df)

# # # # # # # # #         # Monitor errors and warnings and get analysis data
# # # # # # # # #         analysis_data = monitor_errors_and_warnings(error_df, prompt)  

# # # # # # # # #         # Return analysis data as response
# # # # # # # # #         return jsonify({'analysis_data': analysis_data}), 200
# # # # # # # # #     else:
# # # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # # # # if __name__ == '__main__':
# # # # # # # # #     app.run(debug=True) 

# # # # # # # # import re
# # # # # # # # import os
# # # # # # # # from flask import Flask, request, jsonify
# # # # # # # # from flask_cors import CORS
# # # # # # # # import ollama
# # # # # # # # import datetime
# # # # # # # # import pandas as pd
# # # # # # # # import requests
# # # # # # # # from werkzeug.utils import secure_filename

# # # # # # # # app = Flask(__name__)
# # # # # # # # CORS(app)
# # # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'
# # # # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # # # def allowed_file(filename):
# # # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # # def parse_log_file(log_file_path):
# # # # # # # #     log_entries = []
# # # # # # # #     current_log = ""

# # # # # # # #     try:
# # # # # # # #         with open(log_file_path, 'r') as file:
# # # # # # # #             for line in file:
# # # # # # # #                 line = line.strip()

# # # # # # # #                 if line:  # Skip empty lines
# # # # # # # #                     if is_timestamp_line(line):
# # # # # # # #                         if current_log:
# # # # # # # #                             log_entries.append(current_log)
# # # # # # # #                         current_log = line
# # # # # # # #                     else:
# # # # # # # #                         current_log += " " + line

# # # # # # # #             # Append the last log entry
# # # # # # # #             if current_log:
# # # # # # # #                 log_entries.append(current_log)
# # # # # # # #     except FileNotFoundError:
# # # # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # # # #     except Exception as e:
# # # # # # # #         print(f"An error occurred: {e}")

# # # # # # # #     return log_entries

# # # # # # # # def is_timestamp_line(line):
# # # # # # # #     timestamp_patterns = [
# # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # #         r"\d{10,13}",
# # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # #         r"\d{13}",
# # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # #     ]
# # # # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # # # def preprocess_logs(logs):
# # # # # # # #     print("Preprocessing logs...")
# # # # # # # #     parsed_logs = []
# # # # # # # #     for log in logs:
# # # # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # # # #         if timestamp and message:
# # # # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # # #             print(f"{timestamp}\n{message}")
# # # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # # def extract_timestamp_and_message(log):
# # # # # # # #     for pattern in [
# # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # # #         r"\d{10,13}",
# # # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # # #         r"\[\d+\.\d+\]",
# # # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # # #         r"\d{13}",
# # # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # # #     ]:
# # # # # # # #         match = re.match(pattern, log)
# # # # # # # #         if match:
# # # # # # # #             timestamp = match.group()
# # # # # # # #             message = log[len(timestamp):].strip()
# # # # # # # #             return timestamp, message
# # # # # # # #     return None, None

# # # # # # # # def load_error_keywords(file_path):
# # # # # # # #     error_keywords = []
# # # # # # # #     try:
# # # # # # # #         with open(file_path, 'r') as file:
# # # # # # # #             for line in file:
# # # # # # # #                 keyword = line.strip()
# # # # # # # #                 if keyword:
# # # # # # # #                     error_keywords.append(keyword)
# # # # # # # #     except FileNotFoundError:
# # # # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # # # #     except Exception as e:
# # # # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # # # #     return error_keywords

# # # # # # # # def check_for_errors(message, error_keywords):
# # # # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # # # #     for keyword in error_keywords:
# # # # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # # # #             return True
# # # # # # # #     return False

# # # # # # # # def analyze_log_message(timestamp, log_message):
# # # # # # # #     print("Analyzing log message:", timestamp, log_message)
# # # # # # # #     combined_message = f"{timestamp}: {log_message}"
# # # # # # # #     analysis = ollama.chat(
# # # # # # # #         model="error-monitor",
# # # # # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # # # # #     )["message"]["content"]
# # # # # # # #     return analysis

# # # # # # # # def monitor_errors_and_warnings(logs, prompt):
# # # # # # # #     print("Monitoring errors and warnings...")
# # # # # # # #     timestamps = []
# # # # # # # #     messages = []
# # # # # # # #     analysis_results = []
# # # # # # # #     for index, row in logs.iterrows():
# # # # # # # #         timestamp = str(row['timestamp'])
# # # # # # # #         message = row['message']
# # # # # # # #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# # # # # # # #         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
# # # # # # # #         timestamps.append(timestamp)
# # # # # # # #         messages.append(message)
# # # # # # # #         analysis_results.append(analysis)

# # # # # # # #     return timestamps, messages, analysis_results

# # # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # # def upload_file():
# # # # # # # #     if 'file' not in request.files:
# # # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # # #     uploaded_file = request.files['file']
# # # # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# # # # # # # #     if uploaded_file.filename == '':
# # # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # # #         # Save the uploaded file to a specific location
# # # # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # # # #         uploaded_file.save(upload_file_path)

# # # # # # # #         # Open and process the saved file
# # # # # # # #         logs = parse_log_file(upload_file_path)
# # # # # # # #         print(logs)
# # # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # # #         print(parsed_logs)
# # # # # # # #         # parsed_logs.to_csv('parsed_log.csv')
# # # # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # # # #         errors = []
# # # # # # # #         for index, row in parsed_logs.iterrows():
# # # # # # # #             message = row['message']
# # # # # # # #             if check_for_errors(message, error_keywords):
# # # # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message})
# # # # # # # #         # Create a DataFrame from the list of errors
# # # # # # # #         error_df = pd.DataFrame(errors)
# # # # # # # #         print(error_df)
# # # # # # # #         timestamps, messages,analysis_results  = monitor_errors_and_warnings(error_df, prompt)

# # # # # # # #         # Return the separate arrays as response
# # # # # # # #         return jsonify({'timestamps': timestamps, 'messages': messages, 'analysis_results': analysis_results}), 200
# # # # # # # #     else:
# # # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # # # if __name__ == '__main__':
# # # # # # # #     app.run(debug=True)









# # # # # # # import re
# # # # # # # import os
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS
# # # # # # # import pandas as pd
# # # # # # # import requests
# # # # # # # from werkzeug.utils import secure_filename

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)
# # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # # def allowed_file(filename):
# # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # def parse_log_file(log_file_path):
# # # # # # #     log_entries = []
# # # # # # #     current_log = ""

# # # # # # #     try:
# # # # # # #         with open(log_file_path, 'r') as file:
# # # # # # #             for line in file:
# # # # # # #                 line = line.strip()

# # # # # # #                 if line:  # Skip empty lines
# # # # # # #                     if is_timestamp_line(line):
# # # # # # #                         if current_log:
# # # # # # #                             log_entries.append(current_log)
# # # # # # #                         current_log = line
# # # # # # #                     else:
# # # # # # #                         current_log += " " + line

# # # # # # #             # Append the last log entry
# # # # # # #             if current_log:
# # # # # # #                 log_entries.append(current_log)
# # # # # # #     except FileNotFoundError:
# # # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # # #     except Exception as e:
# # # # # # #         print(f"An error occurred: {e}")

# # # # # # #     return log_entries

# # # # # # # def is_timestamp_line(line):
# # # # # # #     timestamp_patterns = [
# # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # #         r"\d{10,13}",
# # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # #         r"\[\d+\.\d+\]",
# # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # #         r"\d{13}",
# # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # #     ]
# # # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # # def preprocess_logs(logs):
# # # # # # #     print("Preprocessing logs...")
# # # # # # #     parsed_logs = []
# # # # # # #     for log in logs:
# # # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # # #         if timestamp and message:
# # # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # # #             print(f"{timestamp}\n{message}")
# # # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # # def extract_timestamp_and_message(log):
# # # # # # #     for pattern in [
# # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # # #         r"\d{10,13}",
# # # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # # #         r"\[\d+\.\d+\]",
# # # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # # #         r"\d{13}",
# # # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # # #     ]:
# # # # # # #         match = re.match(pattern, log)
# # # # # # #         if match:
# # # # # # #             timestamp = match.group()
# # # # # # #             message = log[len(timestamp):].strip()
# # # # # # #             return timestamp, message
# # # # # # #     return None, None

# # # # # # # def load_error_keywords(file_path):
# # # # # # #     error_keywords = []
# # # # # # #     try:
# # # # # # #         with open(file_path, 'r') as file:
# # # # # # #             for line in file:
# # # # # # #                 keyword = line.strip()
# # # # # # #                 if keyword:
# # # # # # #                     error_keywords.append(keyword)
# # # # # # #     except FileNotFoundError:
# # # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # # #     except Exception as e:
# # # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # # #     return error_keywords

# # # # # # # def check_for_errors(message, error_keywords):
# # # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # # #     for keyword in error_keywords:
# # # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # # #             return True
# # # # # # #     return False

# # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # def upload_file():
# # # # # # #     if 'file' not in request.files:
# # # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # # #     uploaded_file = request.files['file']
# # # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# # # # # # #     if uploaded_file.filename == '':
# # # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # #         # Save the uploaded file to a specific location
# # # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # # #         uploaded_file.save(upload_file_path)

# # # # # # #         # Open and process the saved file
# # # # # # #         logs = parse_log_file(upload_file_path)
# # # # # # #         print(logs)
# # # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # # #         print(parsed_logs)
# # # # # # #         # parsed_logs.to_csv('parsed_log.csv')
# # # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # # #         errors = []
# # # # # # #         for index, row in parsed_logs.iterrows():
# # # # # # #             message = row['message']
# # # # # # #             if check_for_errors(message, error_keywords):
# # # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message})
# # # # # # #         # Create a DataFrame from the list of errors
# # # # # # #         error_df = pd.DataFrame(errors)
# # # # # # #         print(error_df)
# # # # # # #         timestamps, messages, response_texts = [], [], []
# # # # # # #         for index, row in error_df.iterrows():
# # # # # # #             response_texts.append(send_query_to_api(row['timestamp'], row['message'], prompt))
# # # # # # #             timestamps.append(row['timestamp'])
# # # # # # #             messages.append(row['message'])
# # # # # # #         # Return the separate arrays as response
# # # # # # #         return jsonify({'timestamps': timestamps, 'messages': messages, 'response_texts': response_texts}), 200
# # # # # # #     else:
# # # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # # def send_query_to_api(timestamp, message, prompt):
# # # # # # #     print(prompt)
# # # # # # #     response_text = ''
# # # # # # #     try:
# # # # # # #         response = requests.post('https://fumes-api.onrender.com/llama3',
# # # # # # #                                  json={
# # # # # # #                                      'prompt': f"""{{
# # # # # # #                                          'systemPrompt': 'You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the errors and other interesting aspects of the logs, and explain them so a new user can understand what they mean. If there are any steps they can do to resolve them, list the steps in your answer.',
# # # # # # #                                          'user': 'hi',
# # # # # # #                                          'Assistant': 'Hello, I am an error monitor in a log file',
# # # # # # #                                          'user_query': '{prompt} {timestamp} {message}'
# # # # # # #                                      }}""",
# # # # # # #                                      "temperature": 0.75,
# # # # # # #                                      "topP": 0.9,
# # # # # # #                                      "maxTokens": 600
# # # # # # #                                  },
# # # # # # #                                  stream=True)

# # # # # # #         for chunk in response.iter_content(chunk_size=1024):
# # # # # # #             if chunk:
# # # # # # #                 response_text += chunk.decode('utf-8')

# # # # # # #     except Exception as e:
# # # # # # #         print(f"An error occurred while sending query to API: {e}")

# # # # # # #     return response_text

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True)



# # # # # # import re
# # # # # # import os
# # # # # # from flask import Flask, request, jsonify
# # # # # # from flask_cors import CORS
# # # # # # import pandas as pd
# # # # # # import requests
# # # # # # from werkzeug.utils import secure_filename
# # # # # # from collections import Counter
# # # # # # import matplotlib.pyplot as plt
# # # # # # from collections import defaultdict
# # # # # # from gradio_client import Client
# # # # # # import ollama
# # # # # # from collections import defaultdict
# # # # # # import json

# # # # # # app = Flask(__name__)
# # # # # # CORS(app)
# # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # def allowed_file(filename):
# # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # def parse_log_file(log_file_path):
# # # # # #     log_entries = []
# # # # # #     current_log = ""

# # # # # #     try:
# # # # # #         with open(log_file_path, 'r') as file:
# # # # # #             for line in file:
# # # # # #                 line = line.strip()

# # # # # #                 if line:  # Skip empty lines
# # # # # #                     if is_timestamp_line(line):
# # # # # #                         if current_log:
# # # # # #                             log_entries.append(current_log)
# # # # # #                         current_log = line
# # # # # #                     else:
# # # # # #                         current_log += " " + line

# # # # # #             # Append the last log entry
# # # # # #             if current_log:
# # # # # #                 log_entries.append(current_log)
# # # # # #     except FileNotFoundError:
# # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # #     except Exception as e:
# # # # # #         print(f"An error occurred: {e}")

# # # # # #     return log_entries

# # # # # # def is_timestamp_line(line):
# # # # # #     timestamp_patterns = [
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # #         r"\d{10,13}",
# # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\[\d+\.\d+\]",
# # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # #         r"\d{13}",
# # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # #     ]
# # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # def preprocess_logs(logs):
# # # # # #     print("Preprocessing logs...")
# # # # # #     parsed_logs = []
# # # # # #     for log in logs:
# # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # #         if timestamp and message:
# # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # #             print(f"{timestamp}\n{message}")
# # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # def extract_timestamp_and_message(log):
# # # # # #     for pattern in [
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # #         r"\d{10,13}",
# # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\[\d+\.\d+\]",
# # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # #         r"\d{13}",
# # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # #     ]:
# # # # # #         match = re.match(pattern, log)
# # # # # #         if match:
# # # # # #             timestamp = match.group()
# # # # # #             message = log[len(timestamp):].strip()
# # # # # #             return timestamp, message
# # # # # #     return None, None


# # # # # # def load_error_keywords(file_path):
# # # # # #     error_keywords = {}
# # # # # #     try:
# # # # # #         with open(file_path, 'r') as file:
# # # # # #             for line in file:
# # # # # #                 keyword = line.strip()
# # # # # #                 if keyword:
# # # # # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # # # # #     except FileNotFoundError:
# # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # #     except Exception as e:
# # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # #     return error_keywords

# # # # # # def check_for_errors(message, error_keywords):
# # # # # #     errors_found = []
# # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # #     for keyword in error_keywords:
# # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # #             errors_found.append(keyword)
# # # # # #             error_keywords[keyword] += 1  # Increment the count for the found keyword
# # # # # #     return errors_found

# # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # def upload_file():
# # # # # #     if 'file' not in request.files:
# # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # #     uploaded_file = request.files['file']
# # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\err.txt'
# # # # # #     if uploaded_file.filename == '':
# # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # #         # Save the uploaded file to a specific location
# # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # #         uploaded_file.save(upload_file_path)

# # # # # #         # Open and process the saved file
# # # # # #         logs = parse_log_file(upload_file_path)
# # # # # #         if not logs:
# # # # # #             print("No log entries found in the file.")
# # # # # #             return
# # # # # #         print(logs)
# # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # #         print(parsed_logs)
# # # # # #         parsed_logs.to_csv('parsed_log.csv')
# # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # #         if not error_keywords:
# # # # # #             print("No error keywords found.")
# # # # # #             return
# # # # # #         errors = []
# # # # # #         # Filter errors and add them to the list along with timestamps
# # # # # #         for index, row in parsed_logs.iterrows():
# # # # # #             message = row['message']
# # # # # #             error_keywords_found = check_for_errors(message, error_keywords)
# # # # # #             if error_keywords_found:
# # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
        
# # # # # #         # Create a DataFrame from the list of errors
# # # # # #         print("errors detected")
# # # # # #         error_df = pd.DataFrame(errors)
# # # # # #         error_counts = []
# # # # # #         print(error_df)
        
# # # # # #         print("Error counts:")
# # # # # #         for keyword, count in error_keywords.items():
# # # # # #             if count > 0:
# # # # # #                 error_counts.append((keyword, count))
# # # # # #                 print(f"{keyword}: {count}")

# # # # # #         print("Error counts list:", error_counts)
       
# # # # # #         timestamps, messages, response_texts = [], [], []
# # # # # #         response_texts1=[]
# # # # # #         for index, row in error_df.iterrows():
# # # # # #             response_texts.append(send_query_to_api(row['timestamp'], row['message'], prompt))
# # # # # #             response_texts1.append(send_query_to_api1(row['timestamp'], row['message'],prompt))
# # # # # #             # print(response_texts)
# # # # # #             timestamps.append(row['timestamp'])
# # # # # #             messages.append(row['message'])
            
# # # # # #         # Return the separate arrays as response
# # # # # #         error_phrases = []

# # # # # #         # for error in response_texts1:
# # # # # #         #     match = re.search(r'!(.*?)\s*\n\s*\n', error)
# # # # # #         #     if match:
# # # # # #         #         error_phrase = match.group(1).strip()
# # # # # #         #         error_phrases.append(error_phrase)
# # # # # #         #     else:
# # # # # #         #         error_phrases.append("Unknown")

# # # # # #         # print(error_phrases)

# # # # # #         detected_errors = [error.split("! ")[-1] for error in response_texts1]
# # # # # #         print(detected_errors)


# # # # # #         error_counts = Counter(detected_errors)

# # # # # #         print("Error Counts:")
# # # # # #         # for error, count in error_counts.items():
# # # # # #         #     print(f"{error}: {count}")
# # # # # #         # Convert error phrases and counts to lists
# # # # # #         error_list = list(error_counts.keys())
# # # # # #         count_list = list(error_counts.values())


# # # # # #         print("Error List:", error_list)
# # # # # #         print("Count List:", count_list)
# # # # # #         data = {'error_list': error_list, 'count_list': count_list}
# # # # # #         result_dict = defaultdict(list)

# # # # # #         # Iterate over each element in a, b, timestamp, and log_message and group them accordingly
# # # # # #         for key, value, ts, msg in zip(error_list, response_texts, timestamps, messages):
# # # # # #             result_dict[key].append({"value": value, "timestamp": ts, "log_message": msg})

# # # # # #         # Extract the results for each unique key in a
# # # # # #         results = [{"key": key, "values": values} for key, values in result_dict.items()]

# # # # # #         # Convert results to JSON format
# # # # # #         results_json = json.dumps(results)

# # # # # #         print(results_json)
# # # # # #         print(timestamps)
# # # # # #         print(messages)
# # # # # #         print(response_texts)
# # # # # #         print(error_list)
# # # # # #         print(count_list)
# # # # # #         timestamps1=['2024-04-04 10:30:05', '2024-04-04 10:35:20']
# # # # # #         messages1=['ERROR: Database connection failed', 'ERROR: Server overload detected']
# # # # # #         count_list1=[1, 1]
# # # # # #         error_list1=['Database Connection Failed', 'Server overload detected']
# # # # # #         response_texts2 = [
# # # # # #     'assistant\n\nWhat a great log line!\n\nError: Database connection failed\n\n**What does this error mean?**\n\nThis error indicates that the software application was unable to establish a connection to the database. This is a critical error, as the application relies heavily on the database to store and retrieve data.\n\n**Why is this error important?**\n\nThis error is important because it can cause the application to malfunction or even crash. Without a database connection, the application won\'t be able to perform its intended functions, which can lead to data inconsistencies, lost data, or even security vulnerabilities.\n\n**What can be done to resolve this error?**\n\nTo resolve this error, the following steps can be taken:\n\n1. **Check the database server status**: Ensure that the database server is up and running, and that it\'s not experiencing any issues.\n2. **Verify database credentials**: Double-check that the database username and password are correct, and that the application has the necessary permissions to connect to the database.\n3. **Check network connectivity**: Ensure that the application has network connectivity to the database server, and that there are no firewall or network configuration issues preventing the connection.\n4. **Check database configuration**: Verify that the database configuration is correct, and that the database is configured to accept connections from the application.\n5. **Restart the application**: If none of the above steps resolve the issue, try restarting the application to see if the error is temporary.\n\n**Additional troubleshooting steps**\n\nIf the above steps don\'t resolve the issue, further troubleshooting may be necessary. This could include:\n\n* Checking the database logs for any errors or issues\n* Verifying that the database is configured to allow connections from the application\'s IP address\n* Checking the application\'s configuration files for any typos or incorrect settings\n* Contacting the database administrator or a system administrator for further assistance\n\nBy following these steps, you should be able to resolve the "Database connection failed" error and get the application up and running smoothly again.',
    
# # # # # #     'assistant\n\nA new log line to analyze!\n\n**Error:** 2024-04-04 10:35:20 ERROR: Server overload detected\n\n**Summary:** This error indicates that the server hosting the software application has become overwhelmed with too many requests, causing a slowdown or even crashes. This can happen when there is a sudden surge in user activity, a misconfiguration, or insufficient resources (e.g., memory, CPU, or network bandwidth).\n\n**What this means for the user:** If you\'re experiencing this error, it means that the server is struggling to handle the current workload, which may result in:\n\n* Slow response times or timeouts\n* Inability to access certain features or functions\n* Frequent crashes or errors\n* Poor overall performance\n\n**Steps to resolve:**\n\n1. **Check server resource utilization**: Monitor the server\'s CPU, memory, and network usage to identify potential bottlenecks. This can help you determine if the issue is related to a specific component or resource.\n2. **Optimize server configuration**: Review the server\'s configuration to ensure it\'s properly tuned for the expected workload. This may involve adjusting settings, such as increasing memory allocation, adjusting CPU priorities, or configuring caching mechanisms.\n3. **Scale the server (if possible)**: If the server is underprovisioned, consider upgrading or adding resources to handle the increased demand.\n4. **Implement load balancing or clustering**: If the server is handling a large number of requests, consider implementing load balancing or clustering to distribute the load across multiple servers.\n5. **Review application code and performance**: Analyze the application\'s code and performance to identify areas that may be contributing to the server overload. Optimize the code, reduce unnecessary computations, and consider caching frequently accessed data.\n6. **Monitor server logs**: Keep a close eye on server logs to detect any patterns or trends that may indicate the root cause of the overload.\n\nBy following these steps, you should be able to identify and address the underlying cause of the server overload, ensuring a smoother and more reliable experience for your users.'
# # # # # # ]
# # # # # #         log_data = [
# # # # # #     {
# # # # # #         "key": "Database Connection Failed",
# # # # # #         "values": [
# # # # # #             {
# # # # # #                 "value": "assistant\n\nAnother log line to analyze!\n\nHere's the error message:\n\n`2024-04-04 10:30:05 ERROR: Database connection failed`\n\nLet's break it down:\n\n* `ERROR`: This is the severity of the log message. It indicates that something went wrong.\n* `Database connection failed`: This is the specific error message. It's telling us that the software application was unable to connect to the database.\n\nWhat does this mean? In simple terms, the software application is unable to communicate with the database it needs to store or retrieve data. This could be due to various reasons such as:\n\n* The database is not running or is not reachable.\n* The database connection settings (e.g., username, password, hostname) are incorrect.\n* The network connection between the software application and the database is not stable or is down.\n\nSteps to resolve this error:\n\n1. **Check the database status**: Ensure the database is running and accessible. You can do this by checking the database's logs, status pages, or by running a simple query to verify its connectivity.\n2. **Verify database connection settings**: Double-check the database connection settings in the software application's configuration files or settings. Ensure that the username, password, hostname, and port are correct and match the database's configuration.\n3. **Check network connectivity**: Verify that the network connection between the software application and the database is stable and working correctly. You can try pinging the database's hostname or IP address to ensure connectivity.\n4. **Consult the software application's documentation**: If you're still having trouble, refer to the software application's documentation or support resources for specific guidance on resolving database connection issues.\n\nBy following these steps, you should be able to identify and resolve the issue preventing the software application from connecting to the database.",
# # # # # #                 "timestamp": "2024-04-04 10:30:05",
# # # # # #                 "log_message": "ERROR: Database connection failed"
# # # # # #             }
# # # # # #         ]
# # # # # #     },
# # # # # #     {
# # # # # #         "key": "Server overload detected",
# # # # # #         "values": [
# # # # # #             {
# # # # # #                 "value": "assistant\n\nLog Line: 2024-04-04 10:35:20 ERROR: Server overload detected\n\nError: Server Overload Detected\n\nDescription: This error indicates that the server is experiencing a high level of traffic or activity, which is causing it to slow down or become unresponsive. This can occur when there are too many users accessing the server simultaneously, or when there are resource-intensive processes running on the server.\n\nImplications:\n\n* The server may become slow or unresponsive, leading to a poor user experience.\n* Data may not be processed or stored correctly, resulting in errors or inconsistencies.\n* The server may even crash or become unavailable, causing downtime and potential data loss.\n\nSteps to Resolve:\n\n1. **Check Server Load**: Use tools like top, vmstat, or sysctl to monitor the server's load. Identify the processes or services consuming the most resources and take steps to optimize or reduce their usage.\n2. **Scale Up the Server**: If the server is underpowered, consider upgrading the hardware or adding more resources (e.g., increasing RAM, CPU, or disk space).\n3. **Optimize Server Configuration**: Review the server's configuration to ensure it is optimized for the current workload. Adjust settings like memory allocation, CPU affinity, and disk I/O priorities as needed.\n4. **Implement Load Balancing**: Consider implementing load balancing techniques, such as round-robin DNS or a load balancer appliance, to distribute traffic across multiple servers.\n5. **Monitor and Analyze Server Logs**: Regularly review server logs to identify trends and patterns that may indicate potential issues before they become critical.\n6. **Upgrade Server Software**: Ensure the server's operating system and software are up-to-date, as newer versions often include performance optimizations and bug fixes.\n\nBy taking these steps, you can help prevent or mitigate server overload and ensure a smoother user experience.",
# # # # # #                 "timestamp": "2024-04-04 10:35:20",
# # # # # #                 "log_message": "ERROR: Server overload detected"
# # # # # #             }
# # # # # #         ]
# # # # # #     }
# # # # # # ]

# # # # # #         # return jsonify({'timestamps': timestamps, 'messages': messages, 'response_texts': response_texts,'data':data}), 200
# # # # # #         # return jsonify({'timestamps': timestamps1,'messages': messages1,'response_texts': response_texts2,'error_list': error_list1,'count_list': count_list1,'results_json':log_data}), 200
# # # # # #         return jsonify({'timestamps': timestamps,'messages': messages,'response_texts': response_texts,'error_list': error_list,'count_list': count_list,'results_json':results_json}), 200
# # # # # #     else:
# # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
    


# # # # # # #llama3 api 70b
# # # # # # def send_query_to_api(timestamp, message, prompt):
# # # # # #     # # print(prompt)
# # # # # #     # response_text = ''
# # # # # #     # try:
# # # # # #     #     response = requests.post('https://fumes-api.onrender.com/llama3',
# # # # # #     #                              json={
# # # # # #     #                                  'prompt': f"""{{
# # # # # #     #                                      'systemPrompt': 'You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the errors and other interesting aspects of the logs, and explain them so a new user can understand what they mean. If there are any steps they can do to resolve them, list the steps in your answer.',
# # # # # #     #                                      'user': 'hi',
# # # # # #     #                                      'Assistant': 'Hello, I am an error monitor in a log file',
# # # # # #     #                                      'user_query': '{prompt} {timestamp} {message}'
# # # # # #     #                                  }}""",
# # # # # #     #                                  "temperature": 0.75,
# # # # # #     #                                  "topP": 0.9,
# # # # # #     #                                  "maxTokens": 600
# # # # # #     #                              },
# # # # # #     #                              stream=True)

# # # # # #     #     for chunk in response.iter_content(chunk_size=1024):
# # # # # #     #         if chunk:
# # # # # #     #             response_text += chunk.decode('utf-8')
                

# # # # # #     # except Exception as e:
# # # # # #     #     print(f"An error occurred while sending query to API: {e}")
# # # # # #     # print(response_text)
# # # # # #     # return response_text
# # # # # #     message2="You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the errors and other interesting aspects of the logs, and explain them so a new user can understand what they mean. If there are any steps they can do to resolve them, list the steps in your answer."

# # # # # #     messageq = f"{message2} Monitor this log line: {timestamp} {message} {prompt}"
# # # # # #     # Initialize the Gradio client
# # # # # #     client = Client("ysharma/Chat_with_Meta_llama3_8b")

# # # # # #     # Make a prediction request with the constructed message
# # # # # #     result = client.predict(
# # # # # #         message=messageq,
# # # # # #         request=0.95,
# # # # # #         param_3=512,
# # # # # #         api_name="/chat"
# # # # # #     )
# # # # # #     return result
# # # # # #     # print("Analyzing log message:", timestamp, message)
# # # # # #     # combined_message = f"{timestamp}: {message} {prompt}"
# # # # # #     # result = ollama.chat(
# # # # # #     #     model="error-monitor",
# # # # # #     #     messages=[{"role": "user", "content": combined_message}]
# # # # # #     # )["message"]["content"]
# # # # # #     # print(result)
# # # # # #     # return result
# # # # # # #     content = f"{timestamp} {message} {prompt}"
# # # # # # #     prompt = f"""{{
# # # # # # #     "prompt": [
# # # # # # #         {{
# # # # # # #             "role": "system",
# # # # # # #             "content": "{message2}"
# # # # # # #         }},
# # # # # # #         {{
# # # # # # #             "role": "user",
# # # # # # #             "content": "{timestamp} {message}{prompt}"
# # # # # # #         }}
# # # # # # #     ],
# # # # # # #     "temperature": 0.75,
# # # # # # #     "topP": 0.9,
# # # # # # #     "maxTokens": 600
# # # # # # # }}"""

# # # # # # # # Make the POST request
# # # # # # #     response = requests.post('https://apix-30ox.onrender.com/llama3',
# # # # # # #         json=json.loads(prompt)).text

# # # # # # #     # Split the response to extract content
# # # # # # #     sections = response.split('data: ')
# # # # # # #     result = ''

# # # # # # #     # Extract content from sections
# # # # # # #     for section in sections:
# # # # # # #         if section.strip(): 
# # # # # # #             try:
# # # # # # #                 cleaned_section = section.strip()
# # # # # # #                 section_json = json.loads(cleaned_section)
# # # # # # #                 for choice in section_json.get('choices', []):
# # # # # # #                     content = choice.get('delta', {}).get('content', '')
# # # # # # #                     result += content
# # # # # # #             except json.JSONDecodeError:
# # # # # # #                 continue

# # # # # # #     # Print the final content
# # # # # # #     print(result)
# # # # # # #     return result





# # # # # # def send_query_to_api1(timestamp, message,prompt):
# # # # # #     # print(prompt)
# # # # # #     # response_text1 = ''
# # # # # #     # try:
# # # # # #     #     response1 = requests.post('https://fumes-api.onrender.com/llama3',
# # # # # #     #                      json={
# # # # # #     #                          'prompt': f"""{{
# # # # # #     #                              'systemPrompt': 'You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the error type and give the error type in ! this symbol. For example Example output like ! Database Connection Failed  and ! Server overload detected',
# # # # # #     #                              'user': 'hi',
# # # # # #     #                              'Assistant': 'Hello, I am an error monitor in a log file',
# # # # # #     #                              'user_query':  '{timestamp} {message}'
# # # # # #     #                          }}""",
# # # # # #     #                          "temperature": 0.75,
# # # # # #     #                          "topP": 0.9,
# # # # # #     #                          "maxTokens": 600
# # # # # #     #                      },
# # # # # #     #                      stream=True)

# # # # # #     #     for chunk in response1.iter_content(chunk_size=1024):
# # # # # #     #         if chunk:
# # # # # #     #             response_text1 += chunk.decode('utf-8')
                

# # # # # #     # except Exception as e:
# # # # # #     #     print(f"An error occurred while sending query to API: {e}")
# # # # # #     # print(response_text1)
# # # # # #     # return response_text1

# # # # # #     message1 = "You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the error type and give the error type in ! this symbol. For example Example output like ! Database Connection Failed and ! Server overload detected."
# # # # # #     message = f"{message1} Monitor this log line: {timestamp}{message}"
# # # # # #     # Make a prediction request with the constructed message
# # # # # #     client1 = Client("ysharma/Chat_with_Meta_llama3_8b")
# # # # # #     response_text1 = client1.predict(
# # # # # #         message=message,
# # # # # #         request=0.95,
# # # # # #         param_3=512,
# # # # # #         api_name="/chat"
# # # # # #     )

# # # # # #     print(response_text1)
# # # # # #     return response_text1
# # # # # #     # print("Analyzing log message:", timestamp, message)
# # # # # #     # combined_message = f"{timestamp}: {message}"
# # # # # #     # response_text1 = ollama.chat(
# # # # # #     #     model="mymodel",
# # # # # #     #     messages=[{"role": "user", "content": combined_message}]
# # # # # #     # )["message"]["content"]
# # # # # #     # print(response_text1)
# # # # # #     # return response_text1
# # # # # #     # Define variables
# # # # # #     # a = "hi"
# # # # # #     # b = "who is the sachin"

# # # # # #     # # Concatenate the strings
# # # # # #     # content = f"{timestamp} {message}"

# # # # # #     # # Make the POST request
# # # # # #     # response = requests.post('https://apix-30ox.onrender.com/llama3',
# # # # # #     #     json={
# # # # # #     #         'prompt': [{"role":"You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the error type and give the error type in ! this symbol. For example Example output like ! Database Connection Failed  and ! Server overload detected","content":"Be a helpful Error monitoring assistant in a log file"},{"role":"user","content": content}],
# # # # # #     #         "temperature": 0.75,
# # # # # #     #         "topP": 0.9,
# # # # # #     #         "maxTokens": 600
# # # # # #     #     }).text

# # # # # #     # # Split the response to extract content
# # # # # #     # sections = response.split('data: ')
# # # # # #     # response_text1 = ''

# # # # # #     # # Extract content from sections
# # # # # #     # for section in sections:
# # # # # #     #     if section.strip(): 
# # # # # #     #         try:
# # # # # #     #             cleaned_section = section.strip()
# # # # # #     #             section_json = json.loads(cleaned_section)
# # # # # #     #             for choice in section_json.get('choices', []):
# # # # # #     #                 content = choice.get('delta', {}).get('content', '')
# # # # # #     #                 response_text1 += content
# # # # # #     #         except json.JSONDecodeError:
# # # # # #     #             continue

# # # # # #     # # Print the final content
# # # # # #     # print("ji",response_text1)
# # # # # #     # return(response_text1)
# # # # # # #     prompt = f"""{{
# # # # # # #     "prompt": [
# # # # # # #         {{
# # # # # # #             "role": "system",
# # # # # # #             "content": "You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the error type and give the error type in ! this symbol. For example Example output like ! Database Connection Failed and ! Server overload detected"
# # # # # # #         }},
# # # # # # #         {{
# # # # # # #             "role": "user",
# # # # # # #             "content": "{timestamp} {message}"
# # # # # # #         }}
# # # # # # #     ],
# # # # # # #     "temperature": 0.75,
# # # # # # #     "topP": 0.9,
# # # # # # #     "maxTokens": 600
# # # # # # # }}"""

# # # # # # # # Make the POST request
# # # # # # #     response = requests.post('https://apix-30ox.onrender.com/llama3',
# # # # # # #         json=json.loads(prompt)).text

# # # # # # #     # Split the response to extract content
# # # # # # #     sections = response.split('data: ')
# # # # # # #     response_text1 = ''

# # # # # # #     # Extract content from sections
# # # # # # #     for section in sections:
# # # # # # #         if section.strip(): 
# # # # # # #             try:
# # # # # # #                 cleaned_section = section.strip()
# # # # # # #                 section_json = json.loads(cleaned_section)
# # # # # # #                 for choice in section_json.get('choices', []):
# # # # # # #                     content = choice.get('delta', {}).get('content', '')
# # # # # # #                     response_text1 += content
# # # # # # #             except json.JSONDecodeError:
# # # # # # #                 continue

# # # # # # #     # Print the final content
# # # # # # #     print(response_text1)
# # # # # # #     return response_text1


# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True)



# # # # # # import re
# # # # # # import os
# # # # # # from flask import Flask, request, jsonify
# # # # # # from flask_cors import CORS
# # # # # # import pandas as pd
# # # # # # import requests
# # # # # # from werkzeug.utils import secure_filename
# # # # # # from collections import Counter
# # # # # # import matplotlib.pyplot as plt
# # # # # # from collections import defaultdict
# # # # # # from gradio_client import Client
# # # # # # import ollama
# # # # # # from collections import defaultdict
# # # # # # import json

# # # # # # app = Flask(__name__)
# # # # # # CORS(app)
# # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # def allowed_file(filename):
# # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # def parse_log_file(log_file_path):
# # # # # #     log_entries = []
# # # # # #     current_log = ""

# # # # # #     try:
# # # # # #         with open(log_file_path, 'r') as file:
# # # # # #             for line in file:
# # # # # #                 line = line.strip()

# # # # # #                 if line:  # Skip empty lines
# # # # # #                     if is_timestamp_line(line):
# # # # # #                         if current_log:
# # # # # #                             log_entries.append(current_log)
# # # # # #                         current_log = line
# # # # # #                     else:
# # # # # #                         current_log += " " + line

# # # # # #             # Append the last log entry
# # # # # #             if current_log:
# # # # # #                 log_entries.append(current_log)
# # # # # #     except FileNotFoundError:
# # # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # # #     except Exception as e:
# # # # # #         print(f"An error occurred: {e}")

# # # # # #     return log_entries

# # # # # # def is_timestamp_line(line):
# # # # # #     timestamp_patterns = [
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # #         r"\d{10,13}",
# # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\[\d+\.\d+\]",
# # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # #         r"\d{13}",
# # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # #     ]
# # # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # # def preprocess_logs(logs):
# # # # # #     print("Preprocessing logs...")
# # # # # #     parsed_logs = []
# # # # # #     for log in logs:
# # # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # # #         if timestamp and message:
# # # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # # #             print(f"{timestamp}\n{message}")
# # # # # #     return pd.DataFrame(parsed_logs)

# # # # # # def extract_timestamp_and_message(log):
# # # # # #     for pattern in [
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # # #         r"\d{10,13}",
# # # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\[\d+\.\d+\]",
# # # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # # #         r"\d{13}",
# # # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # # #     ]:
# # # # # #         match = re.match(pattern, log)
# # # # # #         if match:
# # # # # #             timestamp = match.group()
# # # # # #             message = log[len(timestamp):].strip()
# # # # # #             return timestamp, message
# # # # # #     return None, None


# # # # # # def load_error_keywords(file_path):
# # # # # #     error_keywords = {}
# # # # # #     try:
# # # # # #         with open(file_path, 'r') as file:
# # # # # #             for line in file:
# # # # # #                 keyword = line.strip()
# # # # # #                 if keyword:
# # # # # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # # # # #     except FileNotFoundError:
# # # # # #         print(f"Error: File '{file_path}' not found.")
# # # # # #     except Exception as e:
# # # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # # #     return error_keywords

# # # # # # def check_for_errors(message, error_keywords):
# # # # # #     errors_found = []
# # # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # # #     for keyword in error_keywords:
# # # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # # #             errors_found.append(keyword)
# # # # # #             error_keywords[keyword] += 1  # Increment the count for the found keyword
# # # # # #     return errors_found

# # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # def upload_file():
# # # # # #     if 'file' not in request.files:
# # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # #     uploaded_file = request.files['file']
# # # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\err.txt'
# # # # # #     if uploaded_file.filename == '':
# # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # #         # Save the uploaded file to a specific location
# # # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # # #         uploaded_file.save(upload_file_path)

# # # # # #         # Open and process the saved file
# # # # # #         logs = parse_log_file(upload_file_path)
# # # # # #         if not logs:
# # # # # #             print("No log entries found in the file.")
# # # # # #             return
# # # # # #         print(logs)
# # # # # #         parsed_logs = preprocess_logs(logs)
# # # # # #         print(parsed_logs)
# # # # # #         parsed_logs.to_csv('parsed_log.csv')
# # # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # # #         if not error_keywords:
# # # # # #             print("No error keywords found.")
# # # # # #             return
# # # # # #         errors = []
# # # # # #         # Filter errors and add them to the list along with timestamps
# # # # # #         for index, row in parsed_logs.iterrows():
# # # # # #             message = row['message']
# # # # # #             error_keywords_found = check_for_errors(message, error_keywords)
# # # # # #             if error_keywords_found:
# # # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
        
# # # # # #         # Create a DataFrame from the list of errors
# # # # # #         print("errors detected")
# # # # # #         error_df = pd.DataFrame(errors)
# # # # # #         error_counts = []
# # # # # #         print(error_df)
        
# # # # # #         print("Error counts:")
# # # # # #         for keyword, count in error_keywords.items():
# # # # # #             if count > 0:
# # # # # #                 error_counts.append((keyword, count))
# # # # # #                 print(f"{keyword}: {count}")

# # # # # #         print("Error counts list:", error_counts)
       
# # # # # #         timestamps, messages, response_texts = [], [], []
# # # # # #         response_texts1=[]
# # # # # #         for index, row in error_df.iterrows():
# # # # # #             response_texts.append(send_query_to_api(row['timestamp'], row['message'], prompt))
# # # # # #             response_texts1.append(send_query_to_api1(row['timestamp'], row['message'],prompt))
# # # # # #             # print(response_texts)
# # # # # #             timestamps.append(row['timestamp'])
# # # # # #             messages.append(row['message'])
            
# # # # # #         detected_errors = [error.split("! ")[-1] for error in response_texts1]
# # # # # #         print(detected_errors)


# # # # # #         error_counts = Counter(detected_errors)

# # # # # #         print("Error Counts:")
# # # # # #         error_list = list(error_counts.keys())
# # # # # #         count_list = list(error_counts.values())


# # # # # #         print("Error List:", error_list)
# # # # # #         print("Count List:", count_list)
# # # # # #         data = {'error_list': error_list, 'count_list': count_list}
# # # # # #         result_dict = defaultdict(list)

# # # # # #         # Iterate over each element in a, b, timestamp, and log_message and group them accordingly
# # # # # #         for key, value, ts, msg in zip(error_list, response_texts, timestamps, messages):
# # # # # #             result_dict[key].append({"value": value, "timestamp": ts, "log_message": msg})

# # # # # #         # Extract the results for each unique key in a
# # # # # #         results = [{"key": key, "values": values} for key, values in result_dict.items()]

# # # # # #         # Convert results to JSON format
# # # # # #         results_json = json.dumps(results)

# # # # # #         print(results_json)
# # # # # #         print(timestamps)
# # # # # #         print(messages)
# # # # # #         print(response_texts)
# # # # # #         print(error_list)
# # # # # #         print(count_list)
# # # # # #         return jsonify({'timestamps': timestamps,'messages': messages,'response_texts': response_texts,'error_list': error_list,'count_list': count_list,'results_json':results_json}), 200
# # # # # #     else:
# # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
    


# # # # # # #llama3 api 70b
# # # # # # def send_query_to_api(timestamp, message, prompt):
# # # # # #     message2="You are an error monitor in a log file. You will receive a set of lines from a log file for some software application, find the errors and other interesting aspects of the logs, and explain them so a new user can understand what they mean. If there are any steps they can do to resolve them, list the steps in your answer."
# # # # # #     print("Analyzing log message:", timestamp, message)
# # # # # #     combined_message = f"{timestamp}: {message} {prompt}"
# # # # # #     result = ollama.chat(
# # # # # #         model="error-monitor",
# # # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # # #     )["message"]["content"]
# # # # # #     print(result)
# # # # # #     return result

# # # # # # def send_query_to_api1(timestamp, message,prompt):
# # # # # #     print("Analyzing log message:", timestamp, message)
# # # # # #     combined_message = f"{timestamp}: {message}"
# # # # # #     response_text1 = ollama.chat(
# # # # # #         model="mymodel",
# # # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # # #     )["message"]["content"]
# # # # # #     print(response_text1)
# # # # # #     return response_text1

# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True)


# # # # # import re
# # # # # import os
# # # # # import threading
# # # # # import time
# # # # # import json
# # # # # from flask import Flask, request, jsonify
# # # # # from flask_cors import CORS
# # # # # import pandas as pd
# # # # # from werkzeug.utils import secure_filename
# # # # # from collections import Counter, defaultdict
# # # # # import ollama
# # # # # import google.generativeai as genai

# # # # # app = Flask(__name__)
# # # # # CORS(app)
# # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # # Shared lists and lock
# # # # # p = []
# # # # # analyzed_messages = []
# # # # # timestamps = []
# # # # # messages = []
# # # # # lock = threading.Lock()

# # # # # def allowed_file(filename):
# # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # def parse_log_file(log_file_path):
# # # # #     log_entries = []
# # # # #     current_log = ""

# # # # #     try:
# # # # #         with open(log_file_path, 'r') as file:
# # # # #             for line in file:
# # # # #                 line = line.strip()

# # # # #                 if line:  # Skip empty lines
# # # # #                     if is_timestamp_line(line):
# # # # #                         if current_log:
# # # # #                             log_entries.append(current_log)
# # # # #                         current_log = line
# # # # #                     else:
# # # # #                         current_log += " " + line

# # # # #             # Append the last log entry
# # # # #             if current_log:
# # # # #                 log_entries.append(current_log)
# # # # #     except FileNotFoundError:
# # # # #         print(f"Error: File '{log_file_path}' not found.")
# # # # #     except Exception as e:
# # # # #         print(f"An error occurred: {e}")

# # # # #     return log_entries

# # # # # def is_timestamp_line(line):
# # # # #     timestamp_patterns = [
# # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # #         r"\d{10,13}",
# # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # #         r"\[\d+\.\d+\]",
# # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # #         r"\d{13}",
# # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # #     ]
# # # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # # def preprocess_logs(logs):
# # # # #     print("Preprocessing logs...")
# # # # #     parsed_logs = []
# # # # #     for log in logs:
# # # # #         timestamp, message = extract_timestamp_and_message(log)
# # # # #         if timestamp and message:
# # # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # #             print(f"{timestamp}\n{message}")
# # # # #     return pd.DataFrame(parsed_logs)

# # # # # def extract_timestamp_and_message(log):
# # # # #     for pattern in [
# # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # # #         r"\d{10,13}",
# # # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # # #         r"\[\d+\.\d+\]",
# # # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # # #         r"\d{13}",
# # # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # # #     ]:
# # # # #         match = re.match(pattern, log)
# # # # #         if match:
# # # # #             timestamp = match.group()
# # # # #             message = log[len(timestamp):].strip()
# # # # #             return timestamp, message
# # # # #     return None, None

# # # # # def load_error_keywords(file_path):
# # # # #     error_keywords = {}
# # # # #     try:
# # # # #         with open(file_path, 'r') as file:
# # # # #             for line in file:
# # # # #                 keyword = line.strip()
# # # # #                 if keyword:
# # # # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # # # #     except FileNotFoundError:
# # # # #         print(f"Error: File '{file_path}' not found.")
# # # # #     except Exception as e:
# # # # #         print(f"An error occurred while loading error keywords: {e}")
# # # # #     return error_keywords

# # # # # def check_for_errors(message, error_keywords):
# # # # #     errors_found = []
# # # # #     # Check if any error keywords are present in the message (case-insensitive)
# # # # #     for keyword in error_keywords:
# # # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # # #             errors_found.append(keyword)
# # # # #             error_keywords[keyword] += 1  # Increment the count for the found keyword
# # # # #     return errors_found

# # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # def upload_file():
# # # # #     if 'file' not in request.files:
# # # # #         return jsonify({'error': 'No file part'}), 400

# # # # #     uploaded_file = request.files['file']
# # # # #     prompt = request.form.get('prompt')  # Get the prompt from the request
# # # # #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\err.txt'
# # # # #     if uploaded_file.filename == '':
# # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # #         # Save the uploaded file to a specific location
# # # # #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# # # # #         uploaded_file.save(upload_file_path)

# # # # #         # Open and process the saved file
# # # # #         logs = parse_log_file(upload_file_path)
# # # # #         if not logs:
# # # # #             print("No log entries found in the file.")
# # # # #             return jsonify({'error': 'No log entries found in the file'}), 400

# # # # #         parsed_logs = preprocess_logs(logs)
# # # # #         error_keywords = load_error_keywords(error_keywords_file_path)
# # # # #         if not error_keywords:
# # # # #             print("No error keywords found.")
# # # # #             return jsonify({'error': 'No error keywords found'}), 400

# # # # #         errors = []
# # # # #         for index, row in parsed_logs.iterrows():
# # # # #             message = row['message']
# # # # #             error_keywords_found = check_for_errors(message, error_keywords)
# # # # #             if error_keywords_found:
# # # # #                 errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
        
# # # # #         error_df = pd.DataFrame(errors)
# # # # #         print(error_df)
# # # # #         threading.Thread(target=process_data, args=(error_df, prompt)).start()
# # # # #         threading.Thread(target=update_error_counts).start()

# # # # #         return jsonify({'message': 'File uploaded and processing started'}), 200
# # # # #     else:
# # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # def analyze_and_add_to_list(timestamp, message):
# # # # #     combined_message = f"{timestamp}: {message}"
# # # # #     response_text = ollama.chat(
# # # # #         model="mymodel",
# # # # #         messages=[{"role": "user", "content": combined_message}]
# # # # #     )["message"]["content"]

# # # # #     pattern = r'!\s*(.*)'
# # # # #     result1 = re.search(pattern, response_text)
# # # # #     if result1:  
# # # # #         extracted_text = result1.group(1)
    
# # # # #     with lock:
# # # # #         p.append(extracted_text)

# # # # # def process_data(df, prompt):
# # # # #     for index, row in df.iterrows():
# # # # #         timestamp = row['timestamp']
# # # # #         message = row['message']
# # # # #         analyze_and_add_to_list(timestamp, message)
        
# # # # #         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
# # # # #         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# # # # #         generation_config = {
# # # # #           "temperature": 1,
# # # # #           "top_p": 0.95,
# # # # #           "top_k": 64,
# # # # #           "max_output_tokens": 8192,
# # # # #           "response_mime_type": "text/plain",
# # # # #         }
# # # # #         safety_settings = [
# # # # #           {
# # # # #             "category": "HARM_CATEGORY_HARASSMENT",
# # # # #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # # # #           },
# # # # #           {
# # # # #             "category": "HARM_CATEGORY_HATE_SPEECH",
# # # # #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # # # #           },
# # # # #           {
# # # # #             "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# # # # #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # # # #           },
# # # # #           {
# # # # #             "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# # # # #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # # # #           },
# # # # #         ]
# # # # #         model = genai.GenerativeModel(
# # # # #           model_name="gemini-1.5-flash-latest",
# # # # #           safety_settings=safety_settings,
# # # # #           generation_config=generation_config,
# # # # #         )
# # # # #         chat_session = model.start_chat(history=[])
# # # # #         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
# # # # #         analyzed_message = response.text
        
# # # # #         with lock:
# # # # #             timestamps.append(timestamp)
# # # # #             messages.append(message)
# # # # #             analyzed_messages.append(analyzed_message)
        
# # # # #         time.sleep(2)

# # # # # def update_error_counts():
# # # # #     while True:
# # # # #         try:
# # # # #             with lock:
# # # # #                 error_counts = Counter(p)
# # # # #             with open('error_counts.json', 'w') as f:
# # # # #                 json.dump(error_counts, f)
# # # # #         except Exception as e:
# # # # #             print(f"Error updating error counts: {e}")
# # # # #         time.sleep(5)


# # # # # @app.route('/get_data', methods=['GET'])
# # # # # def get_data():
# # # # #     with lock:
# # # # #         print(p)
# # # # #         return jsonify(p)

# # # # # @app.route('/get_analyzed_messages', methods=['GET'])
# # # # # def get_analyzed_messages():
# # # # #     with lock:
# # # # #         print(analyzed_messages)
# # # # #         return jsonify(analyzed_messages)

# # # # # @app.route('/get_timestamps', methods=['GET'])
# # # # # def get_timestamps():
# # # # #     with lock:
# # # # #         print(timestamps)
# # # # #         return jsonify(timestamps)

# # # # # @app.route('/get_messages', methods=['GET'])
# # # # # def get_messages():
# # # # #     with lock:
# # # # #         print(messages)
# # # # #         return jsonify(messages)

# # # # # @app.route('/get_error_counts', methods=['GET'])
# # # # # def get_error_counts():
# # # # #     try:
# # # # #         with open('error_counts.json', 'r') as f:
# # # # #             error_counts = json.load(f)
# # # # #         return jsonify(error_counts)
# # # # #     except FileNotFoundError:
# # # # #         # Handle case where error_counts.json does not exist
# # # # #         return jsonify({})
# # # # #     except Exception as e:
# # # # #         # Handle other exceptions gracefully
# # # # #         return jsonify({'error': str(e)})


# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True)

# # # # import os
# # # # import re
# # # # import threading
# # # # import time
# # # # import pandas as pd
# # # # from flask import Flask, jsonify
# # # # from flask_cors import CORS

# # # # app = Flask(__name__)
# # # # CORS(app)

# # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\logs'
# # # # ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'  # Path to your error keywords file
# # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # # # Shared lists and lock
# # # # timestamps = []
# # # # messages = []
# # # # errors = []
# # # # lock = threading.Lock()

# # # # # Set to track processed files
# # # # processed_files = set()
# # # # processed_files_lock = threading.Lock()

# # # # # To track if a processing thread is running
# # # # processing_thread = None
# # # # thread_lock = threading.Lock()

# # # # ALLOWED_EXTENSIONS = {'txt', 'log'}

# # # # def allowed_file(filename):
# # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # def parse_log_file(log_file_path):
# # # #     log_entries = []
# # # #     current_log = ""

# # # #     try:
# # # #         with open(log_file_path, 'r') as file:
# # # #             for line in file:
# # # #                 line = line.strip()

# # # #                 if line:  # Skip empty lines
# # # #                     if is_timestamp_line(line):
# # # #                         if current_log:
# # # #                             log_entries.append(current_log)
# # # #                         current_log = line
# # # #                     else:
# # # #                         current_log += " " + line

# # # #             # Append the last log entry
# # # #             if current_log:
# # # #                 log_entries.append(current_log)
# # # #     except FileNotFoundError:
# # # #         print(f"Error: File '{log_file_path}' not found.")
# # # #     except Exception as e:
# # # #         print(f"An error occurred: {e}")

# # # #     return log_entries

# # # # def is_timestamp_line(line):
# # # #     timestamp_patterns = [
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # #         r"\d{10,13}",
# # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # #         r"\[\d+\.\d+\]",
# # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # #         r"\d{13}",
# # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # #     ]
# # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # def preprocess_logs(logs):
# # # #     parsed_logs = []
# # # #     for log in logs:
# # # #         timestamp, message = extract_timestamp_and_message(log)
# # # #         if timestamp and message:
# # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # #     return pd.DataFrame(parsed_logs)

# # # # def extract_timestamp_and_message(log):
# # # #     for pattern in [
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # #         r"\d{10,13}",
# # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # #         r"\[\d+\.\d+\]",
# # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # #         r"\d{13}",
# # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # #     ]:
# # # #         match = re.match(pattern, log)
# # # #         if match:
# # # #             timestamp = match.group()
# # # #             message = log[len(timestamp):].strip()
# # # #             return timestamp, message
# # # #     return None, None

# # # # def analyze_and_add_to_list(timestamp, message, error_keywords):
# # # #     with lock:
# # # #         timestamps.append(timestamp)
# # # #         messages.append(message)
# # # #         error_keywords_found = check_for_errors(message, error_keywords)
# # # #         if error_keywords_found:
# # # #             errors.append({'timestamp': timestamp, 'message': message, 'errors_found': error_keywords_found})

# # # # def check_for_errors(message, error_keywords):
# # # #     errors_found = []
# # # #     for keyword in error_keywords:
# # # #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # #             errors_found.append(keyword)
# # # #             error_keywords[keyword] += 1
# # # #     return errors_found

# # # # def load_error_keywords(file_path):
# # # #     error_keywords = {}
# # # #     try:
# # # #         with open(file_path, 'r') as file:
# # # #             for line in file:
# # # #                 keyword = line.strip()
# # # #                 if keyword:
# # # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # # #     except FileNotFoundError:
# # # #         print(f"Error: File '{file_path}' not found.")
# # # #     except Exception as e:
# # # #         print(f"An error occurred while loading error keywords: {e}")
# # # #     return error_keywords

# # # # def process_log_file(file_path, error_keywords):
# # # #     logs = parse_log_file(file_path)
# # # #     if not logs:
# # # #         print("No log entries found in the file.")
# # # #         return

# # # #     parsed_logs = preprocess_logs(logs)
# # # #     for index, row in parsed_logs.iterrows():
# # # #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# # # #     print(f"File processing done: {file_path}")

# # # # def process_log_files():
# # # #     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
# # # #     if not error_keywords:
# # # #         print("No error keywords found.")
# # # #         return

# # # #     while True:
# # # #         files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
# # # #         for file_name in files:
# # # #             file_path = os.path.join(UPLOAD_FOLDER, file_name)
# # # #             with processed_files_lock:
# # # #                 if file_path not in processed_files:
# # # #                     process_log_file(file_path, error_keywords)
# # # #                     processed_files.add(file_path)
# # # #         time.sleep(5)  # Add a sleep to prevent constant polling

# # # # @app.route('/process_logs', methods=['GET'])
# # # # def start_processing():
# # # #     global processing_thread
# # # #     with thread_lock:
# # # #         if processing_thread is None or not processing_thread.is_alive():
# # # #             processing_thread = threading.Thread(target=process_log_files)
# # # #             processing_thread.daemon = True  # Make the thread a daemon
# # # #             processing_thread.start()
# # # #             return jsonify({'message': 'File processing started'}), 200
# # # #         else:
# # # #             return jsonify({'message': 'File processing is already running'}), 200

# # # # @app.route('/get_timestamps', methods=['GET'])
# # # # def get_timestamps():
# # # #     with lock:
# # # #         return jsonify(timestamps)

# # # # @app.route('/get_messages', methods=['GET'])
# # # # def get_messages():
# # # #     with lock:
# # # #         return jsonify(messages)

# # # # @app.route('/get_errors', methods=['GET'])
# # # # def get_errors():
# # # #     with lock:
# # # #         return jsonify(errors)

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)



# # # # import os
# # # # import re
# # # # import threading
# # # # import time
# # # # import pandas as pd
# # # # from flask import Flask, jsonify
# # # # from flask_cors import CORS
# # # # import joblib



# # # # app = Flask(__name__)
# # # # CORS(app)

# # # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
# # # # ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'  # Path to your error keywords file
# # # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # # # Shared lists and lock
# # # # timestamps = []
# # # # messages = []
# # # # errors = []
# # # # lock = threading.Lock()

# # # # # Set to track processed files
# # # # processed_files = set()
# # # # processed_files_lock = threading.Lock()

# # # # # To track if a processing thread is running
# # # # processing_thread = None
# # # # thread_lock = threading.Lock()

# # # # ALLOWED_EXTENSIONS = {'txt', 'log'}

# # # # def allowed_file(filename):
# # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # def parse_log_file(log_file_path):
# # # #     log_entries = []
# # # #     current_log = ""

# # # #     try:
# # # #         with open(log_file_path, 'r') as file:
# # # #             for line in file:
# # # #                 line = line.strip()

# # # #                 if line:  # Skip empty lines
# # # #                     if is_timestamp_line(line):
# # # #                         if current_log:
# # # #                             log_entries.append(current_log)
# # # #                         current_log = line
# # # #                     else:
# # # #                         current_log += " " + line

# # # #             # Append the last log entry
# # # #             if current_log:
# # # #                 log_entries.append(current_log)
# # # #     except FileNotFoundError:
# # # #         print(f"Error: File '{log_file_path}' not found.")
# # # #     except Exception as e:
# # # #         print(f"An error occurred: {e}")

# # # #     return log_entries

# # # # def is_timestamp_line(line):
# # # #     timestamp_patterns = [
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # #         r"\d{10,13}",
# # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # #         r"\[\d+\.\d+\]",
# # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # #         r"\d{13}",
# # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # #     ]
# # # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # # def preprocess_logs(logs):
# # # #     parsed_logs = []
# # # #     for log in logs:
# # # #         timestamp, message = extract_timestamp_and_message(log)
# # # #         if timestamp and message:
# # # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # #     return pd.DataFrame(parsed_logs)

# # # # def extract_timestamp_and_message(log):
# # # #     for pattern in [
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # # #         r"\d{10,13}",
# # # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # # #         r"\[\d+\.\d+\]",
# # # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # # #         r"\d{13}",
# # # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # # #     ]:
# # # #         match = re.match(pattern, log)
# # # #         if match:
# # # #             timestamp = match.group()
# # # #             message = log[len(timestamp):].strip()
# # # #             return timestamp, message
# # # #     return None, None

# # # # def analyze_and_add_to_list(timestamp, message, error_keywords):
# # # #     with lock:
# # # #         timestamps.append(timestamp)
# # # #         messages.append(message)
# # # #         error_keywords_found = check_for_errors(message, error_keywords)
# # # #         if error_keywords_found:
# # # #             errors.append({'timestamp': timestamp, 'message': message, 'errors_found': error_keywords_found})

# # # # def check_for_errors(message, error_keywords):
# # # #     # errors_found = []
# # # #     # for keyword in error_keywords:
# # # #     #     if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# # # #     #         errors_found.append(keyword)
# # # #     #         error_keywords[keyword] += 1
# # # #     # return errors_found
# # # #     errors_found = []
# # # #     for keyword in error_keywords:
# # # #         # Check for the keyword in the message
# # # #         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
# # # #             errors_found.append(keyword)
# # # #             error_keywords[keyword] += 1
# # # #     return errors_found

# # # # def load_error_keywords(file_path):
# # # #     error_keywords = {}
# # # #     try:
# # # #         with open(file_path, 'r') as file:
# # # #             for line in file:
# # # #                 keyword = line.strip()
# # # #                 if keyword:
# # # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # # #     except FileNotFoundError:
# # # #         print(f"Error: File '{file_path}' not found.")
# # # #     except Exception as e:
# # # #         print(f"An error occurred while loading error keywords: {e}")
# # # #     return error_keywords

# # # # def process_log_file(file_path, error_keywords):
# # # #     logs = parse_log_file(file_path)
# # # #     if not logs:
# # # #         print("No log entries found in the file.")
# # # #         return

# # # #     log_df = preprocess_logs(logs)  # Name the DataFrame
# # # #     errors_df = pd.DataFrame()  # Create an empty DataFrame for errors

# # # #     for index, row in log_df.iterrows():
# # # #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# # # #     # Convert errors list to DataFrame if there are errors
# # # #     # if errors:
# # # #     #     errors_df = pd.DataFrame(errors)
# # # #     # print(errors_df)
# # # #     # Convert errors list to DataFrame if there are errors
# # # #     if errors:
# # # #         errors_df = pd.DataFrame(errors)
# # # #         # Extract messages from errors_df
# # # #         messages_to_predict = errors_df['message'].tolist()
# # # #         # Load the trained model
# # # #         model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# # # #         model = joblib.load(model_path)
# # # #         # Predict error type for each message
# # # #         predicted_error_types = model.predict(messages_to_predict)
# # # #         # Add predicted error types to the DataFrame
# # # #         errors_df['predicted_error_type'] = predicted_error_types
# # # #     # # Save DataFrames to CSV
# # # #     # log_csv_file_path = file_path + '_logs.csv'
# # # #     errors_csv_file_path = file_path + '_errors.csv'
# # # #     # log_df.to_csv(log_csv_file_path, index=False)
# # # #     if not errors_df.empty:
# # # #         errors_df.to_csv(errors_csv_file_path, index=False)
    
# # # #     print(f"File processing done and saved to {file_path}")

# # # # def process_log_files():
# # # #     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
# # # #     if not error_keywords:
# # # #         print("No error keywords found.")
# # # #         return

# # # #     while True:
# # # #         files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
# # # #         for file_name in files:
# # # #             file_path = os.path.join(UPLOAD_FOLDER, file_name)
# # # #             with processed_files_lock:
# # # #                 if file_path not in processed_files:
# # # #                     process_log_file(file_path, error_keywords)
# # # #                     processed_files.add(file_path)
# # # #         time.sleep(5)  # Add a sleep to prevent constant polling
# # # #     print("All files have been processed.")

# # # # @app.route('/process_logs', methods=['GET'])
# # # # def start_processing():
# # # #     global processing_thread
# # # #     with thread_lock:
# # # #         if processing_thread is None or not processing_thread.is_alive():
# # # #             processing_thread = threading.Thread(target=process_log_files)
# # # #             processing_thread.daemon = True  # Make the thread a daemon
# # # #             processing_thread.start()
# # # #             return jsonify({'message': 'File processing started'}), 200
# # # #         else:
# # # #             return jsonify({'message': 'File processing is already running'}), 200

# # # # @app.route('/get_timestamps', methods=['GET'])
# # # # def get_timestamps():
# # # #     with lock:
# # # #         return jsonify(timestamps)

# # # # @app.route('/get_messages', methods=['GET'])
# # # # def get_messages():
# # # #     with lock:
# # # #         return jsonify(messages)

# # # # @app.route('/get_errors', methods=['GET'])
# # # # def get_errors():
# # # #     with lock:
# # # #         return jsonify(errors)

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)




# # # import os
# # # import re
# # # import threading
# # # import time
# # # import pandas as pd
# # # from flask import Flask, jsonify
# # # from flask_cors import CORS
# # # import joblib
# # # from collections import Counter

# # # app = Flask(__name__)
# # # CORS(app)

# # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
# # # ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'  # Path to your error keywords file
# # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # # Shared lists and lock
# # # timestamps = []
# # # messages = []
# # # errors = []
# # # lock = threading.Lock()

# # # # Set to track processed files
# # # processed_files = set()
# # # processed_files_lock = threading.Lock()

# # # # To track if a processing thread is running
# # # processing_thread = None
# # # thread_lock = threading.Lock()

# # # ALLOWED_EXTENSIONS = {'txt', 'log'}

# # # def allowed_file(filename):
# # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # def parse_log_file(log_file_path):
# # #     log_entries = []
# # #     current_log = ""

# # #     try:
# # #         with open(log_file_path, 'r') as file:
# # #             for line in file:
# # #                 line = line.strip()

# # #                 if line:  # Skip empty lines
# # #                     if is_timestamp_line(line):
# # #                         if current_log:
# # #                             log_entries.append(current_log)
# # #                         current_log = line
# # #                     else:
# # #                         current_log += " " + line

# # #             # Append the last log entry
# # #             if current_log:
# # #                 log_entries.append(current_log)
# # #     except FileNotFoundError:
# # #         print(f"Error: File '{log_file_path}' not found.")
# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")

# # #     return log_entries

# # # def is_timestamp_line(line):
# # #     timestamp_patterns = [
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # #         r"\d{10,13}",
# # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # #         r"\[\d+\.\d+\]",
# # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # #         r"\d{13}",
# # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # #     ]
# # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # def preprocess_logs(logs):
# # #     parsed_logs = []
# # #     for log in logs:
# # #         timestamp, message = extract_timestamp_and_message(log)
# # #         if timestamp and message:
# # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # #     return pd.DataFrame(parsed_logs)

# # # def extract_timestamp_and_message(log):
# # #     for pattern in [
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # #         r"\d{10,13}",
# # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # #         r"\[\d+\.\d+\]",
# # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # #         r"\d{13}",
# # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # #     ]:
# # #         match = re.match(pattern, log)
# # #         if match:
# # #             timestamp = match.group()
# # #             message = log[len(timestamp):].strip()
# # #             return timestamp, message
# # #     return None, None

# # # def analyze_and_add_to_list(timestamp, message, error_keywords):
# # #     with lock:
# # #         timestamps.append(timestamp)
# # #         messages.append(message)
# # #         error_keywords_found = check_for_errors(message, error_keywords)
# # #         if error_keywords_found:
# # #             errors.append({'timestamp': timestamp, 'message': message, 'errors_found': error_keywords_found})

# # # def check_for_errors(message, error_keywords):
# # #     errors_found = []
# # #     for keyword in error_keywords:
# # #         # Check for the keyword in the message
# # #         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
# # #             errors_found.append(keyword)
# # #             error_keywords[keyword] += 1
# # #     return errors_found

# # # def load_error_keywords(file_path):
# # #     error_keywords = {}
# # #     try:
# # #         with open(file_path, 'r') as file:
# # #             for line in file:
# # #                 keyword = line.strip()
# # #                 if keyword:
# # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # #     except FileNotFoundError:
# # #         print(f"Error: File '{file_path}' not found.")
# # #     except Exception as e:
# # #         print(f"An error occurred while loading error keywords: {e}")
# # #     return error_keywords

# # # def process_log_file(file_path, error_keywords):
# # #     logs = parse_log_file(file_path)
# # #     if not logs:
# # #         print("No log entries found in the file.")
# # #         return

# # #     log_df = preprocess_logs(logs)  # Name the DataFrame
# # #     errors_df = pd.DataFrame()  # Create an empty DataFrame for errors

# # #     for index, row in log_df.iterrows():
# # #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# # #     predicted_error_types_list = []  # Initialize the list to store predicted error types

# # #     if errors:
# # #         errors_df = pd.DataFrame(errors)
# # #         # Extract messages from errors_df
# # #         messages_to_predict = errors_df['message'].tolist()
# # #         # Load the trained model
# # #         model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# # #         model = joblib.load(model_path)
# # #         # Predict error type for each message
# # #         predicted_error_types = model.predict(messages_to_predict)
# # #         # Add predicted error types to the DataFrame
# # #         errors_df['predicted_error_type'] = predicted_error_types

# # #         # Store the predicted error types in the list
# # #         predicted_error_types_list.extend(predicted_error_types)
# # #     # print(predicted_error_types_list)
# # #     if not errors_df.empty:
# # #         errors_with_timestamps = errors_df[['timestamp', 'predicted_error_type']]
# # #         errors_with_timestamps_df = pd.DataFrame(errors_with_timestamps)
# # #         print(errors_with_timestamps)

# # #     # Use Counter to count occurrences of each error type
# # #     error_counts = Counter(predicted_error_types)

# # #     # Print the counts
# # #     for error_type, count in error_counts.items():
# # #         print(f"{error_type}: {count}")
# # #     errors_csv_file_path = file_path + '_errors.csv'
# # #     if not errors_df.empty:
# # #         errors_df.to_csv(errors_csv_file_path, index=False)
    
# # #     print(f"File processing done and saved to {file_path}")

# # #     return predicted_error_types_list  # Return the list of predicted error types

# # # def process_log_files():
# # #     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
# # #     if not error_keywords:
# # #         print("No error keywords found.")
# # #         return

# # #     while True:
# # #         files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
# # #         for file_name in files:
# # #             file_path = os.path.join(UPLOAD_FOLDER, file_name)
# # #             with processed_files_lock:
# # #                 if file_path not in processed_files:
# # #                     process_log_file(file_path, error_keywords)
# # #                     processed_files.add(file_path)
# # #         time.sleep(5)  # Add a sleep to prevent constant polling
# # #     print("All files have been processed.")

# # # @app.route('/process_logs', methods=['GET'])
# # # def start_processing():
# # #     global processing_thread
# # #     with thread_lock:
# # #         if processing_thread is None or not processing_thread.is_alive():
# # #             processing_thread = threading.Thread(target=process_log_files)
# # #             processing_thread.daemon = True  # Make the thread a daemon
# # #             processing_thread.start()
# # #             return jsonify({'message': 'File processing started'}), 200
# # #         else:
# # #             return jsonify({'message': 'File processing is already running'}), 200

# # # @app.route('/get_timestamps', methods=['GET'])
# # # def get_timestamps():
# # #     with lock:
# # #         return jsonify(timestamps)

# # # @app.route('/get_messages', methods=['GET'])
# # # def get_messages():
# # #     with lock:
# # #         return jsonify(messages)
# # # @app.route('/get_errors', methods=['GET'])
# # # def get_errors():
# # #     with lock:
# # #         return jsonify(errors)
# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # # import os
# # # import re
# # # import threading
# # # import time
# # # import pandas as pd
# # # from flask import Flask, jsonify
# # # from flask_cors import CORS
# # # import joblib
# # # from collections import Counter
# # # import google.generativeai as genai

# # # # from google.cloud import genai  # Make sure to import genai if you have the package installed

# # # app = Flask(__name__)
# # # CORS(app)

# # # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
# # # ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'  # Path to your error keywords file
# # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # # Shared lists and lock
# # # timestamps = []
# # # messages = []
# # # errors = []
# # # lock = threading.Lock()

# # # # Set to track processed files
# # # processed_files = set()
# # # processed_files_lock = threading.Lock()

# # # # To track if a processing thread is running
# # # processing_thread = None
# # # thread_lock = threading.Lock()

# # # ALLOWED_EXTENSIONS = {'txt', 'log'}

# # # def allowed_file(filename):
# # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # def parse_log_file(log_file_path):
# # #     log_entries = []
# # #     current_log = ""

# # #     try:
# # #         with open(log_file_path, 'r') as file:
# # #             for line in file:
# # #                 line = line.strip()

# # #                 if line:  # Skip empty lines
# # #                     if is_timestamp_line(line):
# # #                         if current_log:
# # #                             log_entries.append(current_log)
# # #                         current_log = line
# # #                     else:
# # #                         current_log += " " + line

# # #             # Append the last log entry
# # #             if current_log:
# # #                 log_entries.append(current_log)
# # #     except FileNotFoundError:
# # #         print(f"Error: File '{log_file_path}' not found.")
# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")

# # #     return log_entries

# # # def is_timestamp_line(line):
# # #     timestamp_patterns = [
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # #         r"\d{10,13}",
# # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # #         r"\[\d+\.\d+\]",
# # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # #         r"\d{13}",
# # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # #     ]
# # #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # # def preprocess_logs(logs):
# # #     parsed_logs = []
# # #     for log in logs:
# # #         timestamp, message = extract_timestamp_and_message(log)
# # #         if timestamp and message:
# # #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# # #     return pd.DataFrame(parsed_logs)

# # # def extract_timestamp_and_message(log):
# # #     for pattern in [
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# # #         r"\d{10,13}",
# # #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# # #         r"\[\d+\.\d+\]",
# # #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# # #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# # #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# # #         r"\d{13}",
# # #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# # #     ]:
# # #         match = re.match(pattern, log)
# # #         if match:
# # #             timestamp = match.group()
# # #             message = log[len(timestamp):].strip()
# # #             return timestamp, message
# # #     return None, None

# # # def analyze_and_add_to_list(timestamp, message, error_keywords):
# # #     with lock:
# # #         timestamps.append(timestamp)
# # #         messages.append(message)
# # #         error_keywords_found = check_for_errors(message, error_keywords)
# # #         if error_keywords_found:
# # #             errors.append({'timestamp': timestamp, 'message': message, 'errors_found': error_keywords_found})

# # # def check_for_errors(message, error_keywords):
# # #     errors_found = []
# # #     for keyword in error_keywords:
# # #         # Check for the keyword in the message
# # #         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
# # #             errors_found.append(keyword)
# # #             error_keywords[keyword] += 1
# # #     return errors_found

# # # def load_error_keywords(file_path):
# # #     error_keywords = {}
# # #     try:
# # #         with open(file_path, 'r') as file:
# # #             for line in file:
# # #                 keyword = line.strip()
# # #                 if keyword:
# # #                     error_keywords[keyword] = 0  # Initialize the count to zero
# # #     except FileNotFoundError:
# # #         print(f"Error: File '{file_path}' not found.")
# # #     except Exception as e:
# # #         print(f"An error occurred while loading error keywords: {e}")
# # #     return error_keywords

# # # # def process_log_file(file_path, error_keywords):
# # # #     logs = parse_log_file(file_path)
# # # #     if not logs:
# # # #         print("No log entries found in the file.")
# # # #         return

# # # #     log_df = preprocess_logs(logs)  # Name the DataFrame
# # # #     errors_df = pd.DataFrame()  # Create an empty DataFrame for errors

# # # #     for index, row in log_df.iterrows():
# # # #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# # # #     predicted_error_types_list = []  # Initialize the list to store predicted error types

# # # #     if errors:
# # # #         errors_df = pd.DataFrame(errors)
# # # #         # Extract messages from errors_df
# # # #         messages_to_predict = errors_df['message'].tolist()
# # # #         # Load the trained model
# # # #         model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# # # #         model = joblib.load(model_path)
# # # #         # Predict error type for each message
# # # #         predicted_error_types = model.predict(messages_to_predict)
# # # #         # Add predicted error types to the DataFrame
# # # #         errors_df['predicted_error_type'] = predicted_error_types

# # # #         # Store the predicted error types in the list
# # # #         predicted_error_types_list.extend(predicted_error_types)

# # # #     if not errors_df.empty:
# # # #         errors_with_timestamps = errors_df[['timestamp', 'predicted_error_type']]
# # # #         errors_with_timestamps_df = pd.DataFrame(errors_with_timestamps)
# # # #         print(errors_with_timestamps)
# # # #     print(errors_df)
# # # #     # Use Counter to count occurrences of each error type
# # # #     error_counts = Counter(predicted_error_types)

# # # #     # Print the counts
# # # #     for error_type, count in error_counts.items():
# # # #         print(f"{error_type}: {count}")

# # # #     errors_csv_file_path = file_path + '_errors.csv'
# # # #     if not errors_df.empty:
# # # #         errors_df.to_csv(errors_csv_file_path, index=False)
    
# # # #     print(f"File processing done and saved to {file_path}")

# # # #     # Process each message using genai API
# # # #     # process_data(errors_df)

# # # #     return predicted_error_types_list  # Return the list of predicted error types

# # # def process_log_file(file_path, error_keywords):
# # #     global errors  # Declare errors as global to reset it

# # #     # Reset the errors list for each file processing
# # #     errors = []

# # #     logs = parse_log_file(file_path)
# # #     if not logs:
# # #         print("No log entries found in the file.")
# # #         return

# # #     log_df = preprocess_logs(logs)  # Name the DataFrame

# # #     for index, row in log_df.iterrows():
# # #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# # #     # Initialize a new DataFrame for errors for this specific file
# # #     errors_df = pd.DataFrame()

# # #     predicted_error_types_list = []  # Initialize the list to store predicted error types

# # #     if errors:
# # #         errors_df = pd.DataFrame(errors)
# # #         # Extract messages from errors_df
# # #         messages_to_predict = errors_df['message'].tolist()
# # #         # Load the trained model
# # #         model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# # #         model = joblib.load(model_path)
# # #         # Predict error type for each message
# # #         predicted_error_types = model.predict(messages_to_predict)
# # #         # Add predicted error types to the DataFrame
# # #         errors_df['predicted_error_type'] = predicted_error_types

# # #         # Store the predicted error types in the list
# # #         predicted_error_types_list.extend(predicted_error_types)

# # #     if not errors_df.empty:
# # #         errors_with_timestamps = errors_df[['timestamp', 'predicted_error_type']]
# # #         errors_with_timestamps_df = pd.DataFrame(errors_with_timestamps)
# # #         print(errors_with_timestamps)
    
   
    
# # #     # process_data(errors_df)
# # #     # Use Counter to count occurrences of each error type
# # #     error_counts = Counter(predicted_error_types)

# # #     # Print the counts
# # #     for error_type, count in error_counts.items():
# # #         print(f"{error_type}: {count}")

# # #     errors_csv_file_path = file_path + '_errors.csv'
# # #     if not errors_df.empty:
# # #         errors_df.to_csv(errors_csv_file_path, index=False)
# # #     print("Test",errors_df)
# # #     print(f"File processing done and saved to {file_path}")

# # #     return predicted_error_types_list  # Return the list of predicted error types

# # # def process_data(errors_df):
# # #     for index, row in errors_df.iterrows():
# # #         timestamp = row['timestamp']
# # #         message = row['message']
# # #         predicted_error_type=row['predicted_error_type']
# # #         print( predicted_error_type)
# # #         print(message)
# # #         # Initialize genai if needed
# # #         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
# # #         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# # #         generation_config = {
# # #             "temperature": 1,
# # #             "top_p": 0.95,
# # #             "top_k": 64,
# # #             "max_output_tokens": 8192,
# # #             "response_mime_type": "text/plain",
# # #         }
# # #         safety_settings = [
# # #             {
# # #                 "category": "HARM_CATEGORY_HARASSMENT",
# # #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # #             },
# # #             {
# # #                 "category": "HARM_CATEGORY_HATE_SPEECH",
# # #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # #             },
# # #             {
# # #                 "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# # #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # #             },
# # #             {
# # #                 "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# # #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# # #             },
# # #         ]
# # #         model = genai.GenerativeModel(
# # #             model_name="gemini-1.5-flash-latest",
# # #             safety_settings=safety_settings,
# # #             generation_config=generation_config,
# # #         )
# # #         chat_session = model.start_chat(history=[])
# # #         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
# # #         analyzed_message = response.text
        
# # #         with lock:
# # #             timestamps.append(timestamp)
# # #             messages.append(message)
# # #             print(f"Analyzed Message: {analyzed_message}")
        
# # #         time.sleep(2)

# # # def process_log_files():
# # #     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
# # #     if not error_keywords:
# # #         print("No error keywords found.")
# # #         return

# # #     while True:
# # #         files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
# # #         for file_name in files:
# # #             file_path = os.path.join(UPLOAD_FOLDER, file_name)
# # #             with processed_files_lock:
# # #                 if file_path not in processed_files:
# # #                     process_log_file(file_path, error_keywords)
# # #                     processed_files.add(file_path)
# # #         time.sleep(5)  # Add a sleep to prevent constant polling
# # #     print("All files have been processed.")

# # # @app.route('/process_logs', methods=['GET'])
# # # def start_processing():
# # #     global processing_thread
# # #     with thread_lock:
# # #         if processing_thread is None or not processing_thread.is_alive():
# # #             processing_thread = threading.Thread(target=process_log_files)
# # #             processing_thread.daemon = True  # Make the thread a daemon
# # #             processing_thread.start()
# # #             return jsonify({'message': 'File processing started'}), 200
# # #         else:
# # #             return jsonify({'message': 'File processing is already running'}), 200

# # # @app.route('/get_timestamps', methods=['GET'])
# # # def get_timestamps():
# # #     with lock:
# # #         return jsonify(timestamps)

# # # @app.route('/get_messages', methods=['GET'])
# # # def get_messages():
# # #     with lock:
# # #         return jsonify(messages)

# # # @app.route('/get_errors', methods=['GET'])
# # # def get_errors():
# # #     with lock:
# # #         return jsonify(errors)

# # # if __name__ == '__main__':
# # #     app.run(debug=True)

# # import os
# # import re
# # import threading
# # import time
# # import pandas as pd
# # from flask import Flask, jsonify
# # from flask_cors import CORS
# # import joblib
# # from collections import Counter
# # import google.generativeai as genai

# # # from google.cloud import genai  # Make sure to import genai if you have the package installed

# # app = Flask(__name__)
# # CORS(app)

# # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
# # ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'  # Path to your error keywords file
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # # Shared lists and lock
# # timestamps = []
# # messages = []
# # errors = []
# # lock = threading.Lock()

# # # Set to track processed files
# # processed_files = set()
# # processed_files_lock = threading.Lock()

# # # To track if a processing thread is running
# # processing_thread = None
# # thread_lock = threading.Lock()

# # ALLOWED_EXTENSIONS = {'txt', 'log'}

# # def allowed_file(filename):
# #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # def parse_log_file(log_file_path):
# #     log_entries = []
# #     current_log = ""

# #     try:
# #         with open(log_file_path, 'r') as file:
# #             for line in file:
# #                 line = line.strip()

# #                 if line:  # Skip empty lines
# #                     if is_timestamp_line(line):
# #                         if current_log:
# #                             log_entries.append(current_log)
# #                         current_log = line
# #                     else:
# #                         current_log += " " + line

# #             # Append the last log entry
# #             if current_log:
# #                 log_entries.append(current_log)
# #     except FileNotFoundError:
# #         print(f"Error: File '{log_file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# #     return log_entries

# # def is_timestamp_line(line):
# #     timestamp_patterns = [
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# #         r"\d{10,13}",
# #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# #         r"\[\d+\.\d+\]",
# #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# #         r"\d{13}",
# #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# #     ]
# #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # def preprocess_logs(logs):
# #     parsed_logs = []
# #     for log in logs:
# #         timestamp, message = extract_timestamp_and_message(log)
# #         if timestamp and message:
# #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# #     return pd.DataFrame(parsed_logs)

# # def extract_timestamp_and_message(log):
# #     for pattern in [
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# #         r"\d{10,13}",
# #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# #         r"\[\d+\.\d+\]",
# #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# #         r"\d{13}",
# #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# #     ]:
# #         match = re.match(pattern, log)
# #         if match:
# #             timestamp = match.group()
# #             message = log[len(timestamp):].strip()
# #             return timestamp, message
# #     return None, None

# # def analyze_and_add_to_list(timestamp, message, error_keywords):
# #     with lock:
# #         timestamps.append(timestamp)
# #         messages.append(message)
# #         error_keywords_found = check_for_errors(message, error_keywords)
# #         if error_keywords_found:
# #             errors.append({'timestamp': timestamp, 'message': message, 'errors_found': error_keywords_found})

# # def check_for_errors(message, error_keywords):
# #     errors_found = []
# #     for keyword in error_keywords:
# #         # Check for the keyword in the message
# #         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
# #             errors_found.append(keyword)
# #             error_keywords[keyword] += 1
# #     return errors_found

# # def load_error_keywords(file_path):
# #     error_keywords = {}
# #     try:
# #         with open(file_path, 'r') as file:
# #             for line in file:
# #                 keyword = line.strip()
# #                 if keyword:
# #                     error_keywords[keyword] = 0  # Initialize the count to zero
# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred while loading error keywords: {e}")
# #     return error_keywords

# # def process_log_file(file_path, error_keywords):
# #     global errors  # Declare errors as global to reset it

# #     # Reset the errors list for each file processing
# #     errors = []

# #     logs = parse_log_file(file_path)
# #     if not logs:
# #         print("No log entries found in the file.")
# #         return

# #     log_df = preprocess_logs(logs)  # Name the DataFrame

# #     for index, row in log_df.iterrows():
# #         analyze_and_add_to_list(row['timestamp'], row['message'], error_keywords)

# #     # Initialize a new DataFrame for errors for this specific file
# #     errors_df = pd.DataFrame()

# #     predicted_error_types_list = []  # Initialize the list to store predicted error types

# #     if errors:
# #         errors_df = pd.DataFrame(errors)
# #         # Extract messages from errors_df
# #         messages_to_predict = errors_df['message'].tolist()
# #         # Load the trained model
# #         model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# #         model = joblib.load(model_path)
# #         # Predict error type for each message
# #         predicted_error_types = model.predict(messages_to_predict)
# #         # Add predicted error types to the DataFrame
# #         errors_df['predicted_error_type'] = predicted_error_types

# #         # Store the predicted error types in the list
# #         predicted_error_types_list.extend(predicted_error_types)

# #     if not errors_df.empty:
# #         errors_with_timestamps = errors_df[['timestamp', 'predicted_error_type']]
# #         errors_with_timestamps_df = pd.DataFrame(errors_with_timestamps)
# #         print(errors_with_timestamps)

# #     process_data(errors_df)
# #     # Use Counter to count occurrences of each error type
# #     error_counts = Counter(predicted_error_types)

# #     # Print the counts
# #     for error_type, count in error_counts.items():
# #         print(f"{error_type}: {count}")

# #     errors_csv_file_path = file_path + '_errors.csv'
# #     if not errors_df.empty:
# #         errors_df.to_csv(errors_csv_file_path, index=False)
# #     print("Test",errors_df)
# #     print(f"File processing done and saved to {file_path}")

# #     return predicted_error_types_list  # Return the list of predicted error types

# # def process_data(errors_df):
# #     for index, row in errors_df.iterrows():
# #         timestamp = row['timestamp']
# #         message = row['message']
# #         predicted_error_type=row['predicted_error_type']
# #         print( predicted_error_type)
# #         print(message)
# #         # Initialize genai if needed
# #         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
# #         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# #         generation_config = {
# #             "temperature": 1,
# #             "top_p": 0.95,
# #             "top_k": 64,
# #             "max_output_tokens": 8192,
# #             "response_mime_type": "text/plain",
# #         }
# #         safety_settings = [
# #             {
# #                 "category": "HARM_CATEGORY_HARASSMENT",
# #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #             },
# #             {
# #                 "category": "HARM_CATEGORY_HATE_SPEECH",
# #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #             },
# #             {
# #                 "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #             },
# #             {
# #                 "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# #                 "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #             },
# #         ]
# #         model = genai.GenerativeModel(
# #             model_name="gemini-1.5-flash-latest",
# #             safety_settings=safety_settings,
# #             generation_config=generation_config,
# #         )
# #         chat_session = model.start_chat(history=[])
# #         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
# #         analyzed_message = response.text
        
# #         with lock:
# #             timestamps.append(timestamp)
# #             messages.append(message)
# #             print(f"Analyzed Message: {analyzed_message}")
        
# #         time.sleep(2)

# # def process_log_files():
# #     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
# #     if not error_keywords:
# #         print("No error keywords found.")
# #         return

# #     while True:
# #         files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
# #         for file_name in files:
# #             file_path = os.path.join(UPLOAD_FOLDER, file_name)
# #             with processed_files_lock:
# #                 if file_path not in processed_files:
# #                     process_log_file(file_path, error_keywords)
# #                     processed_files.add(file_path)
# #         time.sleep(5)  # Add a sleep to prevent constant polling
# #     print("All files have been processed.")

# # @app.route('/process_logs', methods=['GET'])
# # def start_processing():
# #     global processing_thread
# #     with thread_lock:
# #         if processing_thread is None or not processing_thread.is_alive():
# #             processing_thread = threading.Thread(target=process_log_files)
# #             processing_thread.daemon = True  # Make the thread a daemon
# #             processing_thread.start()
# #             return jsonify({'message': 'File processing started'}), 200
# #         else:
# #             return jsonify({'message': 'File processing is already running'}), 200

# # @app.route('/get_timestamps', methods=['GET'])
# # def get_timestamps():
# #     with lock:
# #         return jsonify(timestamps)

# # @app.route('/get_messages', methods=['GET'])
# # def get_messages():
# #     with lock:
# #         return jsonify(messages)

# # @app.route('/get_errors', methods=['GET'])
# # def get_errors():
# #     with lock:
# #         return jsonify(errors)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# # import re
# # import os
# # import threading
# # import time
# # import json
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import pandas as pd
# # from werkzeug.utils import secure_filename
# # from collections import Counter, defaultdict
# # import google.generativeai as genai
# # import joblib

# # app = Flask(__name__)
# # CORS(app)
# # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # # Shared lists and lock
# # p = []
# # analyzed_messages = []
# # timestamps = []
# # messages = []
# # lock = threading.Lock()

# # def allowed_file(filename):
# #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # def parse_log_file(log_file_path):
# #     log_entries = []
# #     current_log = ""

# #     try:
# #         with open(log_file_path, 'r') as file:
# #             for line in file:
# #                 line = line.strip()

# #                 if line:  # Skip empty lines
# #                     if is_timestamp_line(line):
# #                         if current_log:
# #                             log_entries.append(current_log)
# #                         current_log = line
# #                     else:
# #                         current_log += " " + line

# #             # Append the last log entry
# #             if current_log:
# #                 log_entries.append(current_log)
# #     except FileNotFoundError:
# #         print(f"Error: File '{log_file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# #     return log_entries

# # def is_timestamp_line(line):
# #     timestamp_patterns = [
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# #         r"\d{10,13}",
# #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# #         r"\[\d+\.\d+\]",
# #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# #         r"\d{13}",
# #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# #     ]
# #     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# # def preprocess_logs(logs):
# #     print("Preprocessing logs...")
# #     parsed_logs = []
# #     for log in logs:
# #         timestamp, message = extract_timestamp_and_message(log)
# #         if timestamp and message:
# #             parsed_logs.append({'timestamp': timestamp, 'message': message})
# #             print(f"{timestamp}\n{message}")
# #     return pd.DataFrame(parsed_logs)

# # def extract_timestamp_and_message(log):
# #     for pattern in [
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
# #         r"\d{10,13}",
# #         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
# #         r"\[\d+\.\d+\]",
# #         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
# #         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
# #         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
# #         r"\d{13}",
# #         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
# #     ]:
# #         match = re.match(pattern, log)
# #         if match:
# #             timestamp = match.group()
# #             message = log[len(timestamp):].strip()
# #             return timestamp, message
# #     return None, None

# # def load_error_keywords(file_path):
# #     error_keywords = {}
# #     try:
# #         with open(file_path, 'r') as file:
# #             for line in file:
# #                 keyword = line.strip()
# #                 if keyword:
# #                     error_keywords[keyword] = 0  # Initialize the count to zero
# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred while loading error keywords: {e}")
# #     return error_keywords
# # def check_for_errors(message, error_keywords):
# #     errors_found = []
# #     for keyword in error_keywords:
# #         # Check for the keyword in the message
# #         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
# #             errors_found.append(keyword)
# #             error_keywords[keyword] += 1
# #     return errors_found

# # @app.route('/api/analyze', methods=['POST'])
# # def upload_file():
# #     if 'file' not in request.files:
# #         return jsonify({'error': 'No file part'}), 400

# #     uploaded_file = request.files['file']
# #     prompt = request.form.get('prompt')  # Get the prompt from the request
# #     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# #     if uploaded_file.filename == '':
# #         return jsonify({'error': 'No selected file'}), 400

# #     if uploaded_file and allowed_file(uploaded_file.filename):
# #         # Save the uploaded file to a specific location
# #         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
# #         uploaded_file.save(upload_file_path)

# #         # Open and process the saved file
# #         logs = parse_log_file(upload_file_path)
# #         if not logs:
# #             print("No log entries found in the file.")
# #             return jsonify({'error': 'No log entries found in the file'}), 400

# #         parsed_logs = preprocess_logs(logs)
# #         error_keywords = load_error_keywords(error_keywords_file_path)
# #         if not error_keywords:
# #             print("No error keywords found.")
# #             return jsonify({'error': 'No error keywords found'}), 400

# #         errors = []
# #         for index, row in parsed_logs.iterrows():
# #             message = row['message']
# #             error_keywords_found = check_for_errors(message, error_keywords)
# #             if error_keywords_found:
# #                 errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
        
# #         error_df = pd.DataFrame(errors)
# #         print(error_df)
# #         threading.Thread(target=process_data, args=(error_df, prompt)).start()
# #         threading.Thread(target=update_error_counts).start()

# #         return jsonify({'message': 'File uploaded and processing started'}), 200
# #     else:
# #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # def analyze_and_add_to_list(timestamp, message):
# #     model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
# #     model = joblib.load(model_path)
# #     combined_message = f"{timestamp}: {message}"
# #     # Assuming your model expects a list of messages for prediction
# #     messages_to_predict = [combined_message]
    
# #     # Predict error type for the message
# #     predicted_error_types = model.predict(messages_to_predict)
# #     response_text = predicted_error_types[0]
# #     print(response_text)
# #     with lock:
# #         p.append(response_text)

# # def process_data(df, prompt):
# #     for index, row in df.iterrows():
# #         timestamp = row['timestamp']
# #         message = row['message']
# #         analyze_and_add_to_list(timestamp, message)
        
# #         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
# #         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# #         generation_config = {
# #           "temperature": 1,
# #           "top_p": 0.95,
# #           "top_k": 64,
# #           "max_output_tokens": 8192,
# #           "response_mime_type": "text/plain",
# #         }
# #         safety_settings = [
# #           {
# #             "category": "HARM_CATEGORY_HARASSMENT",
# #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #           },
# #           {
# #             "category": "HARM_CATEGORY_HATE_SPEECH",
# #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #           },
# #           {
# #             "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #           },
# #           {
# #             "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# #             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #           },
# #         ]
# #         model = genai.GenerativeModel(
# #           model_name="gemini-1.5-flash-latest",
# #           safety_settings=safety_settings,
# #           generation_config=generation_config,
# #         )
# #         chat_session = model.start_chat(history=[])
# #         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
# #         analyzed_message = response.text
        
# #         with lock:
# #             timestamps.append(timestamp)
# #             messages.append(message)
# #             analyzed_messages.append(analyzed_message)
        
# #         time.sleep(2)

# # def update_error_counts():
# #     while True:
# #         try:
# #             with lock:
# #                 error_counts = Counter(p)
# #             with open('error_counts.json', 'w') as f:
# #                 json.dump(error_counts, f)
# #         except Exception as e:
# #             print(f"Error updating error counts: {e}")
# #         time.sleep(5)


# # @app.route('/get_data', methods=['GET'])
# # def get_data():
# #     with lock:
# #         print(p)
# #         return jsonify(p)

# # @app.route('/get_analyzed_messages', methods=['GET'])
# # def get_analyzed_messages():
# #     with lock:
# #         return jsonify(analyzed_messages)

# # @app.route('/get_timestamps', methods=['GET'])
# # def get_timestamps():
# #     with lock:
# #         return jsonify(timestamps)

# # @app.route('/get_messages', methods=['GET'])
# # def get_messages():
# #     with lock:
# #         return jsonify(messages)

# # @app.route('/get_error_counts', methods=['GET'])
# # def get_error_counts():
# #     try:
# #         with open('error_counts.json', 'r') as f:
# #             error_counts = json.load(f)
# #         return jsonify(error_counts)
# #     except FileNotFoundError:
# #         # Handle case where error_counts.json does not exist
# #         return jsonify({})
# #     except Exception as e:
# #         # Handle other exceptions gracefully
# #         return jsonify({'error': str(e)})
    
# # if __name__ == '__main__':
# #     app.run(debug=True)



# import re
# import os
# import threading
# import time
# import json
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from werkzeug.utils import secure_filename
# from collections import Counter
# import google.generativeai as genai
# import joblib

# app = Flask(__name__)
# CORS(app)
# ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# SAMPLE_LOGS_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'  # Change this to your log files folder
# ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Shared lists and lock
# p = []
# analyzed_messages = []
# timestamps = []
# messages = []
# lock = threading.Lock()

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def parse_log_file(log_file_path):
#     log_entries = []
#     current_log = ""

#     try:
#         with open(log_file_path, 'r') as file:
#             for line in file:
#                 line = line.strip()

#                 if line:  # Skip empty lines
#                     if is_timestamp_line(line):
#                         if current_log:
#                             log_entries.append(current_log)
#                         current_log = line
#                     else:
#                         current_log += " " + line

#             # Append the last log entry
#             if current_log:
#                 log_entries.append(current_log)
#     except FileNotFoundError:
#         print(f"Error: File '{log_file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     return log_entries

# def is_timestamp_line(line):
#     timestamp_patterns = [
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
#         r"\d{10,13}",
#         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
#         r"\[\d+\.\d+\]",
#         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
#         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
#         r"\d{13}",
#         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
#     ]
#     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# def preprocess_logs(logs):
#     print("Preprocessing logs...")
#     parsed_logs = []
#     for log in logs:
#         timestamp, message = extract_timestamp_and_message(log)
#         if timestamp and message:
#             parsed_logs.append({'timestamp': timestamp, 'message': message})
#             print(f"{timestamp}\n{message}")
#     return pd.DataFrame(parsed_logs)

# def extract_timestamp_and_message(log):
#     for pattern in [
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
#         r"\d{10,13}",
#         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
#         r"\[\d+\.\d+\]",
#         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
#         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
#         r"\d{13}",
#         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
#     ]:
#         match = re.match(pattern, log)
#         if match:
#             timestamp = match.group()
#             message = log[len(timestamp):].strip()
#             return timestamp, message
#     return None, None

# def load_error_keywords(file_path):
#     error_keywords = {}
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 keyword = line.strip()
#                 if keyword:
#                     error_keywords[keyword] = 0  # Initialize the count to zero
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred while loading error keywords: {e}")
#     return error_keywords

# def check_for_errors(message, error_keywords):
#     errors_found = []
#     for keyword in error_keywords:
#         # Check for the keyword in the message
#         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
#             errors_found.append(keyword)
#             error_keywords[keyword] += 1
#     return errors_found

# def process_files_in_folder():
#     processed_files = set()
#     print("Starting file processing...")  # Debug print
#     while True:
#         # List all files in the sample_logs folder
#         files = os.listdir(SAMPLE_LOGS_FOLDER)
#         print(f"Files in directory: {files}")  # Debug print

#         for file in files:
#             if file not in processed_files:
#                 file_path = os.path.join(SAMPLE_LOGS_FOLDER, file)
#                 print(f"Processing file: {file_path}")  # Debug print

#                 logs = parse_log_file(file_path)
#                 if not logs:
#                     print("No log entries found in the file.")  # Debug print
#                     continue

#                 parsed_logs = preprocess_logs(logs)
#                 error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
#                 if not error_keywords:
#                     print("No error keywords found.")  # Debug print
#                     continue

#                 errors = []
#                 for index, row in parsed_logs.iterrows():
#                     message = row['message']
#                     error_keywords_found = check_for_errors(message, error_keywords)
#                     if error_keywords_found:
#                         errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
                
#                 error_df = pd.DataFrame(errors)
#                 print(f"Errors found: {error_df}")  # Debug print
#                 threading.Thread(target=process_data, args=(error_df, None)).start()
#                 threading.Thread(target=update_error_counts).start()
#                 processed_files.add(file)
#         print("Sleeping for 10 seconds...")  # Debug print
#         time.sleep(10)

# def analyze_and_add_to_list(timestamp, message):
#     model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
#     model = joblib.load(model_path)
#     combined_message = f"{timestamp}: {message}"
#     # Assuming your model expects a list of messages for prediction
#     messages_to_predict = [combined_message]
    
#     # Predict error type for the message
#     predicted_error_types = model.predict(messages_to_predict)
#     response_text = predicted_error_types[0]
#     print(response_text)
#     with lock:
#         p.append(response_text)

# def process_data(df, prompt):
#     for index, row in df.iterrows():
#         timestamp = row['timestamp']
#         message = row['message']
#         analyze_and_add_to_list(timestamp, message)
        
#         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
#         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
#         generation_config = {
#           "temperature": 1,
#           "top_p": 0.95,
#           "top_k": 64,
#           "max_output_tokens": 8192,
#           "response_mime_type": "text/plain",
#         }
#         safety_settings = [
#           {
#             "category": "HARM_CATEGORY_HARASSMENT",
#             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#           },
#           {
#             "category": "HARM_CATEGORY_HATE_SPEECH",
#             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#           },
#           {
#             "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#           },
#           {
#             "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#             "threshold": "BLOCK_MEDIUM_AND_ABOVE",
#           },
#         ]
#         model = genai.GenerativeModel(
#           model_name="gemini-1.5-flash-latest",
#           safety_settings=safety_settings,
#           generation_config=generation_config,
#         )
#         chat_session = model.start_chat(history=[])
#         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
#         analyzed_message = response.text
        
#         with lock:
#             timestamps.append(timestamp)
#             messages.append(message)
#             analyzed_messages.append(analyzed_message)
        
#         time.sleep(2)

# def update_error_counts():
#     global p
#     error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
#     error_counts = Counter()
#     for keyword in error_keywords:
#         error_counts[keyword] = error_keywords[keyword]
#     with lock:
#         p = dict(error_counts)
#     # Simulate some processing delay
#     time.sleep(2)

# @app.route('/start_processing', methods=['GET'])
# def start_processing():
#     threading.Thread(target=process_files_in_folder).start()
#     return jsonify({'status': 'Processing started'}), 200

# @app.route('/upload_log', methods=['POST'])
# def upload_log():
#     if 'logfile' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
#     file = request.files['logfile']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected for uploading'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#         return jsonify({'success': f'File {filename} uploaded successfully'}), 200
#     else:
#         return jsonify({'error': 'Allowed file types are csv, json, xml, txt, log'}), 400

# @app.route('/get_analyzed_messages', methods=['GET'])
# def get_analyzed_messages():
#     global analyzed_messages
#     with lock:
#         analyzed_messages_copy = analyzed_messages.copy()
#     return jsonify(analyzed_messages_copy), 200

# @app.route('/get_error_counts', methods=['GET'])
# def get_error_counts():
#     global p
#     with lock:
#         error_counts_copy = p.copy()
#     return jsonify(error_counts_copy), 200

# if __name__ == '__main__':
#     # Comment out the automatic thread start for manual testing
#     # threading.Thread(target=process_files_in_folder).start()
#     app.run(debug=True)


# import re
# import os
# import threading
# import time
# import json
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from werkzeug.utils import secure_filename
# from collections import Counter
# import google.generativeai as genai
# import joblib

# app = Flask(__name__)
# CORS(app)
# ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'
# SAMPLE_LOGS_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
# ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Shared lists and lock
# p=[]
# analyzed_messages = []
# timestamps = []
# messages = []
# error_counts = Counter()
# lock = threading.Lock()

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def parse_log_file(log_file_path):
#     log_entries = []
#     current_log = ""
#     try:
#         with open(log_file_path, 'r') as file:
#             for line in file:
#                 line = line.strip()
#                 if line:
#                     if is_timestamp_line(line):
#                         if current_log:
#                             log_entries.append(current_log)
#                         current_log = line
#                     else:
#                         current_log += " " + line
#             if current_log:
#                 log_entries.append(current_log)
#     except FileNotFoundError:
#         print(f"Error: File '{log_file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return log_entries

# def is_timestamp_line(line):
#     timestamp_patterns = [
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
#         r"\d{10,13}",
#         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
#         r"\[\d+\.\d+\]",
#         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
#         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
#         r"\d{13}",
#         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
#     ]
#     return any(re.match(pattern, line) for pattern in timestamp_patterns)

# def preprocess_logs(logs):
#     print("Preprocessing logs...")
#     parsed_logs = []
#     for log in logs:
#         timestamp, message = extract_timestamp_and_message(log)
#         if timestamp and message:
#             parsed_logs.append({'timestamp': timestamp, 'message': message})
#             print(f"{timestamp}\n{message}")
#     return pd.DataFrame(parsed_logs)

# def extract_timestamp_and_message(log):
#     for pattern in [
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z",
#         r"\d{10,13}",
#         r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
#         r"\[\d+\.\d+\]",
#         r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}\]",
#         r"[A-Za-z]{3} \d{1,2} \d{2}:\d{2}:\d{2}",
#         r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{2}:\d{2}",
#         r"\d{13}",
#         r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
#     ]:
#         match = re.match(pattern, log)
#         if match:
#             timestamp = match.group()
#             message = log[len(timestamp):].strip()
#             return timestamp, message
#     return None, None

# def load_error_keywords(file_path):
#     error_keywords = {}
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 keyword = line.strip()
#                 if keyword:
#                     error_keywords[keyword] = 0
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred while loading error keywords: {e}")
#     return error_keywords

# def check_for_errors(message, error_keywords):
#     errors_found = []
#     for keyword in error_keywords:
#         if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
#             errors_found.append(keyword)
#             error_keywords[keyword] += 1
#     return errors_found

# def process_files_in_folder():
#     processed_files = set()
#     print("Starting file processing...")
#     while True:
#         files = os.listdir(SAMPLE_LOGS_FOLDER)
#         print(f"Files in directory: {files}")
#         for file in files:
#             if file not in processed_files:
#                 file_path = os.path.join(SAMPLE_LOGS_FOLDER, file)
#                 print(f"Processing file: {file_path}")
#                 logs = parse_log_file(file_path)
#                 if not logs:
#                     print("No log entries found in the file.")
#                     continue

#                 parsed_logs = preprocess_logs(logs)
#                 error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
#                 if not error_keywords:
#                     print("No error keywords found.")
#                     continue

#                 errors = []
#                 for index, row in parsed_logs.iterrows():
#                     message = row['message']
#                     error_keywords_found = check_for_errors(message, error_keywords)
#                     if error_keywords_found:
#                         errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
                
#                 error_df = pd.DataFrame(errors)
#                 print(f"Errors found: {error_df}")
#                 process_data(error_df)
#                 update_error_counts(error_keywords)
#                 processed_files.add(file)
#         print("Sleeping for 10 seconds...")
#         time.sleep(10)

# def analyze_and_add_to_list(timestamp, message):
#     model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
#     model = joblib.load(model_path)
#     combined_message = f"{timestamp}: {message}"
#     messages_to_predict = [combined_message]
#     predicted_error_types = model.predict(messages_to_predict)
#     response_text = predicted_error_types[0]
#     print(response_text)
#     with lock:
#         p.append(response_text)

# def process_data(df):
#     for index, row in df.iterrows():
#         timestamp = row['timestamp']
#         message = row['message']
#         analyze_and_add_to_list(timestamp, message)
        
#         os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
#         genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
#         generation_config = {
#             "temperature": 1,
#             "top_p": 0.95,
#             "top_k": 64,
#             "max_output_tokens": 8192,
#             "response_mime_type": "text/plain",
#         }
#         safety_settings = [
#             {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#             {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
#         ]
#         model = genai.GenerativeModel(
#             model_name="gemini-1.5-flash-latest",
#             safety_settings=safety_settings,
#             generation_config=generation_config,
#         )
#         chat_session = model.start_chat(history=[])
#         response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
#         analyzed_message = response.text
        
#         with lock:
#             timestamps.append(timestamp)
#             messages.append(message)
#             analyzed_messages.append(analyzed_message)
#             print(f"Analyzed Message: {analyzed_message}")
        
#         time.sleep(2)

# def update_error_counts(error_keywords):
#     with lock:
#         global error_counts
#         error_counts.update(error_keywords)

# @app.route('/start_processing', methods=['GET'])
# def start_processing():
#     threading.Thread(target=process_files_in_folder).start()
#     return jsonify({'status': 'Processing started'}), 200

# @app.route('/upload_log', methods=['POST'])
# def upload_log():
#     if 'logfile' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
#     file = request.files['logfile']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected for uploading'}), 400
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#         return jsonify({'success': f'File {filename} uploaded successfully'}), 200
#     else:
#         return jsonify({'error': 'Allowed file types are csv, json, xml, txt, log'}), 400

# @app.route('/get_analyzed_messages', methods=['GET'])
# def get_analyzed_messages():
#     with lock:
#         analyzed_messages_copy = analyzed_messages.copy()
#     return jsonify(analyzed_messages_copy), 200



# @app.route('/get_error_counts', methods=['GET'])
# def get_error_counts():
#     with lock:
#         error_counts_copy = dict(error_counts)
#     return jsonify(error_counts_copy), 200

# if __name__ == '__main__':
#     app.run(debug=True)


import re
import os
import threading
import time
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from werkzeug.utils import secure_filename
from collections import Counter
import google.generativeai as genai
import joblib

app = Flask(__name__)
CORS(app)
ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'
SAMPLE_LOGS_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\sample logs'
ERROR_KEYWORDS_FILE_PATH = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Shared lists and lock
p = []
analyzed_messages = []
timestamps = []
messages = []
error_counts = Counter()
lock = threading.Lock()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_log_file(log_file_path):
    log_entries = []
    current_log = ""
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    if is_timestamp_line(line):
                        if current_log:
                            log_entries.append(current_log)
                        current_log = line
                    else:
                        current_log += " " + line
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
    error_keywords = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                keyword = line.strip()
                if keyword:
                    error_keywords[keyword] = 0
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading error keywords: {e}")
    return error_keywords

def check_for_errors(message, error_keywords):
    errors_found = []
    for keyword in error_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b|\B' + re.escape(keyword), message, re.IGNORECASE):
            errors_found.append(keyword)
            error_keywords[keyword] += 1
    return errors_found

def process_files_in_folder():
    processed_files = set()
    print("Starting file processing...")
    while True:
        files = os.listdir(SAMPLE_LOGS_FOLDER)
        print(f"Files in directory: {files}")
        for file in files:
            if file not in processed_files:
                file_path = os.path.join(SAMPLE_LOGS_FOLDER, file)
                print(f"Processing file: {file_path}")
                logs = parse_log_file(file_path)
                if not logs:
                    print("No log entries found in the file.")
                    continue

                parsed_logs = preprocess_logs(logs)
                error_keywords = load_error_keywords(ERROR_KEYWORDS_FILE_PATH)
                if not error_keywords:
                    print("No error keywords found.")
                    continue

                errors = []
                for index, row in parsed_logs.iterrows():
                    message = row['message']
                    error_keywords_found = check_for_errors(message, error_keywords)
                    if error_keywords_found:
                        errors.append({'timestamp': row['timestamp'], 'message': message, 'errors_found': error_keywords_found})
                
                error_df = pd.DataFrame(errors)
                print(f"Errors found: {error_df}")
                process_data(error_df)
                update_error_counts(error_keywords)
                processed_files.add(file)
        print("Sleeping for 10 seconds...")
        time.sleep(10)

def analyze_and_add_to_list(timestamp, message):
    model_path = r'C:\Users\Aravindan\test1\backend\venv\model\error_classification_model.pkl'
    model = joblib.load(model_path)
    combined_message = f"{timestamp}: {message}"
    messages_to_predict = [combined_message]
    predicted_error_types = model.predict(messages_to_predict)
    response_text = predicted_error_types[0]
    print(response_text)
    with lock:
        p.append(response_text)

def process_data(df):
    for index, row in df.iterrows():
        timestamp = row['timestamp']
        message = row['message']
        analyze_and_add_to_list(timestamp, message)
        
        os.environ["GOOGLE_API_KEY"] = "AIzaSyDfn-oQG2LysAOQHL49yqXpq8p3zCiiuHE"
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
            safety_settings=safety_settings,
            generation_config=generation_config,
        )
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(f"You are a log Analyzer {timestamp} {message} analyze this log message")
        analyzed_message = response.text
        
        with lock:
            timestamps.append(timestamp)
            messages.append(message)
            analyzed_messages.append(analyzed_message)
            print(f"Analyzed Message: {analyzed_message}")
        
        time.sleep(2)

def update_error_counts(error_keywords):
    with lock:
        global error_counts
        error_counts.update(error_keywords)

@app.route('/start_processing', methods=['GET'])
def start_processing():
    threading.Thread(target=process_files_in_folder).start()
    return jsonify({'status': 'Processing started'}), 200

@app.route('/upload_log', methods=['POST'])
def upload_log():
    if 'logfile' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['logfile']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'success': f'File {filename} uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Allowed file types are csv, json, xml, txt, log'}), 400

@app.route('/get_analyzed_messages', methods=['GET'])
def get_analyzed_messages():
    with lock:
        analyzed_messages_copy = analyzed_messages.copy()
    return jsonify(analyzed_messages_copy), 200

@app.route('/get_timestamps', methods=['GET'])
def get_timestamps():
    with lock:
        analyzed_messages_copy2 = timestamps.copy()
    return jsonify(analyzed_messages_copy2), 200

@app.route('/get_messages', methods=['GET'])
def get_messages():
    with lock:
        analyzed_messages_copy3 = messages.copy()
    return jsonify(analyzed_messages_copy3), 200

@app.route('/get_p', methods=['GET'])
def get_p():
    with lock:
        analyzed_messages_copy1 = p.copy()
    return jsonify(analyzed_messages_copy1), 200

@app.route('/get_error_counts', methods=['GET'])
def get_error_counts():
    with lock:
        error_counts_copy = dict(error_counts)
    return jsonify(error_counts_copy), 200

@app.route('/get_live_error_counts', methods=['GET'])
def get_live_error_counts():
    with lock:
        error_group_counts = dict(Counter(p))
    return jsonify(error_group_counts), 200

if __name__ == '__main__':
    app.run(debug=True)

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
# # # # # # #     return jsonify({'error': str(e)}), 500  # Return error message and status code 500 (Internal Server Error)
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS
# # # # # # # import csv
# # # # # # # import json
# # # # # # # import re

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)

# # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # def allowed_file(filename):
# # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # def is_valid_csv(file_content):
# # # # # # #     try:
# # # # # # #         csv.reader(file_content.decode().splitlines())
# # # # # # #         return True
# # # # # # #     except Exception as e:
# # # # # # #         return False

# # # # # # # def is_valid_json(file_content):
# # # # # # #     try:
# # # # # # #         json.loads(file_content.decode())
# # # # # # #         return True
# # # # # # #     except Exception as e:
# # # # # # #         return False

# # # # # # # def is_valid_xml(file_content):
# # # # # # #     # Check if it looks like XML (simplified check)
# # # # # # #     return '<' in file_content.decode() and '>' in file_content.decode()

# # # # # # # def extract_logs_from_text(file_content):
# # # # # # #     logs = []
# # # # # # #     lines = file_content.decode().splitlines()

# # # # # # #     # Assume the first line contains headers
# # # # # # #     headers = lines[0].split()

# # # # # # #     for line in lines[1:]:
# # # # # # #         # Split the line based on whitespace or any other delimiter
# # # # # # #         values = re.split(r'\s+', line.strip())

# # # # # # #         # Create a dictionary to store the log entry
# # # # # # #         log_entry = {}
        
# # # # # # #         # Check if the number of values matches the number of headers
# # # # # # #         if len(values) == len(headers):
# # # # # # #             for i in range(len(headers)):
# # # # # # #                 log_entry[headers[i]] = values[i]
# # # # # # #         else:
# # # # # # #             # If the number of values doesn't match, create a single 'Message' field
# # # # # # #             log_entry['Message'] = ' '.join(values)

# # # # # # #         logs.append(log_entry)

# # # # # # #     return logs

# # # # # # # def analyze_file(file_content, filename):
# # # # # # #     logs = []

# # # # # # #     # Check if it's a valid CSV, JSON, or XML based on file extension
# # # # # # #     file_extension = filename.rsplit('.', 1)[1].lower()
# # # # # # #     if file_extension == 'csv' and is_valid_csv(file_content):
# # # # # # #         csv_data = csv.DictReader(file_content.decode().splitlines())
# # # # # # #         logs = [row for row in csv_data]
# # # # # # #     elif file_extension == 'json' and is_valid_json(file_content):
# # # # # # #         logs = json.loads(file_content.decode())
# # # # # # #     elif file_extension == 'xml' and is_valid_xml(file_content):
# # # # # # #         # Placeholder for XML parsing logic (not implemented here)
# # # # # # #         pass
# # # # # # #     else:
# # # # # # #         # Assume it's plain text and try to extract logs
# # # # # # #         logs = extract_logs_from_text(file_content)

# # # # # # #     return logs

# # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # def analyze_file_endpoint():
# # # # # # #     if request.method == 'POST':
# # # # # # #         try:
# # # # # # #             uploaded_file = request.files.get('file')
# # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # #                 file_content = uploaded_file.read()
# # # # # # #                 logs = analyze_file(file_content, uploaded_file.filename)
# # # # # # #                 return jsonify({'logs': logs})
# # # # # # #             else:
# # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # #         except Exception as e:
# # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # #     else:
# # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True)
# # # # # # # import requests
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)

# # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running

# # # # # # # def allowed_file(filename):
# # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # def analyze_file_endpoint():
# # # # # # #     if request.method == 'POST':
# # # # # # #         try:
# # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # #                 file_content = uploaded_file.read()
# # # # # # #                 print(file_content)
# # # # # # #                 # Send logs to Logstash
# # # # # # #                 response = requests.post(LOGSTASH_URL, data=file_content)
                
# # # # # # #                 if response.status_code == 200:
# # # # # # #                     print("HI")
# # # # # # #                     return jsonify({'message': 'Logs sent to Logstash successfully'})
# # # # # # #                 else:
# # # # # # #                     return jsonify({'error': 'Failed to send logs to Logstash'}), 500
# # # # # # #             else:
# # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # #         except Exception as e:
# # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # #     else:
# # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True)
# # # # # # # import requests
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS
# # # # # # # from elasticsearch import Elasticsearch

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)

# # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running
# # # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"  # Elasticsearch URL with credentials
# # # # # # # INDEX_NAME = "hi123"

# # # # # # # def allowed_file(filename):
# # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # def analyze_file_endpoint():
# # # # # # #     if request.method == 'POST':
# # # # # # #         try:
# # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # #                 file_content = uploaded_file.read()
# # # # # # #                 # Send logs to Logstash
# # # # # # #                 response = requests.post(LOGSTASH_URL, data=file_content)
                
# # # # # # #                 if response.status_code == 200:
# # # # # # #                     print("Logs sent to Logstash successfully")
# # # # # # #                     # Fetch analyzed data from Elasticsearch
# # # # # # #                     es = Elasticsearch([ELASTICSEARCH_URL])  # Initialize Elasticsearch client with credentials
# # # # # # #                     query = {"query": {"match_all": {}}}  # Match all documents in the index
# # # # # # #                     result = es.search(index=INDEX_NAME, body=query)
# # # # # # #                     analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # # #                     # Print the analyzed data in the terminal
# # # # # # #                     print("Analyzed data:")
# # # # # # #                     for data in analyzed_data:
# # # # # # #                         print(data)
# # # # # # #                     return jsonify({'message': 'Logs sent to Logstash successfully', 'analyzed_data': analyzed_data})
# # # # # # #                 else:
# # # # # # #                     return jsonify({'error': 'Failed to send logs to Logstash'}), 500
# # # # # # #             else:
# # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # #         except Exception as e:
# # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # #     else:
# # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True)
# # # # # # # import requests
# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS
# # # # # # # from elasticsearch import Elasticsearch

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)

# # # # # # # LOGSTASH_URL = "http://localhost:5044"  # URL where Logstash is running
# # # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"  # Elasticsearch URL with credentials
# # # # # # # INDEX_NAME = "hi123"

# # # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # # def allowed_file(filename):
# # # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # # def get_analyzed_data_from_elasticsearch():
# # # # # # #     try:
# # # # # # #         es = Elasticsearch([ELASTICSEARCH_URL])
# # # # # # #         query = {"query": {"match_all": {}}}
# # # # # # #         result = es.search(index=INDEX_NAME, body=query)
# # # # # # #         analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # # #         return analyzed_data
# # # # # # #     except Exception as e:
# # # # # # #         print(f"Error fetching data from Elasticsearch: {str(e)}")
# # # # # # #         return None

# # # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # # def analyze_file_endpoint():
# # # # # # #     if request.method == 'POST':
# # # # # # #         try:
# # # # # # #             uploaded_file = request.files.get('file')
            
# # # # # # #             if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # # #                 files = {'file': uploaded_file}
# # # # # # #                 response = requests.post(LOGSTASH_URL, files=files)
                
# # # # # # #                 if response.status_code == 200:
# # # # # # #                     print("File sent to Logstash successfully")
# # # # # # #                     analyzed_data = get_analyzed_data_from_elasticsearch()
# # # # # # #                     if analyzed_data:
# # # # # # #                         return jsonify({'message': 'File sent to Logstash successfully', 'analyzed_data': analyzed_data})
# # # # # # #                     else:
# # # # # # #                         return jsonify({'error': 'Failed to fetch analyzed data from Elasticsearch'}), 500
# # # # # # #                 else:
# # # # # # #                     return jsonify({'error': 'Failed to send file to Logstash'}), 500
# # # # # # #             else:
# # # # # # #                 return jsonify({'error': 'Invalid file type or no file uploaded'}), 400
# # # # # # #         except Exception as e:
# # # # # # #             return jsonify({'error': str(e)}), 500
# # # # # # #     else:
# # # # # # #         return jsonify({'error': 'Method not allowed'}), 405

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True)
# # # # # # import requests
# # # # # # from flask import Flask, request, jsonify
# # # # # # from flask_cors import CORS
# # # # # # from elasticsearch import Elasticsearch

# # # # # # app = Flask(__name__)

# # # # # # CORS(app)

# # # # # # LOGSTASH_URL = "http://localhost:5044"
# # # # # # ELASTICSEARCH_URL = "http://elastic:nP497vW-j4btnbgJVjDW@localhost:9200"
# # # # # # INDEX_NAME = "hi123"

# # # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # # def allowed_file(filename):
# # # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # # def send_to_logstash(file):
# # # # # #     try:
# # # # # #         files = {'file': file}
# # # # # #         response = requests.post(LOGSTASH_URL, files=files)
# # # # # #         return response.status_code == 200
# # # # # #     except Exception as e:
# # # # # #         print(f"Error sending file to Logstash: {str(e)}")
# # # # # #         return False

# # # # # # def get_analyzed_data_from_elasticsearch():
# # # # # #     try:
# # # # # #         es = Elasticsearch([ELASTICSEARCH_URL])
# # # # # #         query = {"query": {"match_all": {}}}
# # # # # #         result = es.search(index=INDEX_NAME, body=query)
# # # # # #         analyzed_data = [hit["_source"] for hit in result["hits"]["hits"]]
# # # # # #         return analyzed_data
# # # # # #     except Exception as e:
# # # # # #         print(f"Error fetching data from Elasticsearch: {str(e)}")
# # # # # #         return None

# # # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # # def upload_file():
# # # # # #     if 'file' not in request.files:
# # # # # #         return jsonify({'error': 'No file part'}), 400

# # # # # #     uploaded_file = request.files['file']
# # # # # #     if uploaded_file.filename == '':
# # # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # # #         if send_to_logstash(uploaded_file):
# # # # # #             analyzed_data = get_analyzed_data_from_elasticsearch()
# # # # # #             if analyzed_data:
# # # # # #                 return jsonify({'message': 'File uploaded and analyzed successfully', 'analyzed_data': analyzed_data}), 200
# # # # # #             else:
# # # # # #                 return jsonify({'error': 'Failed to fetch analyzed data from Elasticsearch'}), 500
# # # # # #         else:
# # # # # #             return jsonify({'error': 'Failed to send file to Logstash'}), 500
# # # # # #     else:
# # # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True)
# # # # # from flask import Flask, request, jsonify
# # # # # from flask_cors import CORS
# # # # # import ollama
# # # # # import datetime
# # # # # import pandas as pd

# # # # # app = Flask(__name__)
# # # # # CORS(app)

# # # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}

# # # # # def allowed_file(filename):
# # # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # # def preprocess_logs(logs):
# # # # #     print("Preprocessing logs...")
# # # # #     parsed_logs = []
# # # # #     for log in logs:
# # # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # # #         message = log[20:].strip()
# # # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # # #     return pd.DataFrame(parsed_logs)

# # # # # def analyze_log_message(log_message):
# # # # #     print("Analyzing log message:", log_message)
# # # # #     analysis = ollama.chat(
# # # # #         model="mistral",
# # # # #         messages=[{"role": "user", "content": log_message}]
# # # # #     )["message"]["content"]
# # # # #     return analysis

# # # # # def monitor_errors_and_warnings(logs):
# # # # #     print("Monitoring errors and warnings...")
# # # # #     for index, row in logs.iterrows():
# # # # #         analysis = analyze_log_message(row['message'] + " Please analyze this log message for errors.")
# # # # #         print(f"Analysis for log message '{row['message']}':\n{analysis}\n")

# # # # # @app.route('/api/analyze', methods=['POST'])
# # # # # def upload_file():
# # # # #     if 'file' not in request.files:
# # # # #         return jsonify({'error': 'No file part'}), 400

# # # # #     uploaded_file = request.files['file']
# # # # #     if uploaded_file.filename == '':
# # # # #         return jsonify({'error': 'No selected file'}), 400

# # # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # # #         # Read the file as text and preprocess logs
# # # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # # #         parsed_logs = preprocess_logs(logs)
# # # # #         monitor_errors_and_warnings(parsed_logs)
# # # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # # #     else:
# # # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True)
# # # # from flask import Flask, request, jsonify
# # # # from flask_cors import CORS
# # # # import ollama
# # # # import datetime
# # # # import pandas as pd
# # # # import requests

# # # # app = Flask(__name__)
# # # # CORS(app)

# # # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # # def allowed_file(filename):
# # # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # # def preprocess_logs(logs):
# # # #     print("Preprocessing logs...")
# # # #     parsed_logs = []
# # # #     for log in logs:
# # # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # # #         message = log[20:].strip()
# # # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # # #     return pd.DataFrame(parsed_logs)

# # # # def analyze_log_message(log_message):
# # # #     print("Analyzing log message:", log_message)
# # # #     analysis = ollama.chat(
# # # #         model="mistral",
# # # #         messages=[{"role": "user", "content": log_message}]
# # # #     )["message"]["content"]
# # # #     return analysis

# # # # def monitor_errors_and_warnings(logs):
# # # #     print("Monitoring errors and warnings...")
# # # #     for index, row in logs.iterrows():
# # # #         analysis = analyze_log_message(row['message'] + " Please analyze this log message for errors.")
# # # #         print(f"Analysis for log message '{row['message']}':\n{analysis}\n")
        
# # # #         # Prepare data to be sent to Logstash
# # # #         log_data = {
# # # #             'timestamp': str(row['timestamp']),
# # # #             'message': row['message'],
# # # #             'analysis': analysis
# # # #         }
        
# # # #         # Send data to Logstash
# # # #         try:
# # # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # # #             if response.status_code == 200:
# # # #                 print("Data sent to Logstash successfully")
# # # #             else:
# # # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # # #         except Exception as e:
# # # #             print(f"Error occurred while sending data to Logstash: {str(e)}")

# # # # @app.route('/api/analyze', methods=['POST'])
# # # # def upload_file():
# # # #     if 'file' not in request.files:
# # # #         return jsonify({'error': 'No file part'}), 400

# # # #     uploaded_file = request.files['file']
# # # #     if uploaded_file.filename == '':
# # # #         return jsonify({'error': 'No selected file'}), 400

# # # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # # #         # Read the file as text and preprocess logs
# # # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # # #         parsed_logs = preprocess_logs(logs)
# # # #         monitor_errors_and_warnings(parsed_logs)
# # # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # # #     else:
# # # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)
# # # from flask import Flask, request, jsonify
# # # from flask_cors import CORS
# # # import ollama
# # # import datetime
# # # import pandas as pd
# # # import requests
# # # import pandas as pd
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.feature_extraction.text import CountVectorizer
# # # from sklearn.naive_bayes import MultinomialNB
# # # from sklearn.metrics import accuracy_score

# # # app = Flask(__name__)
# # # CORS(app)
# # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # def allowed_file(filename):
# # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # def preprocess_logs(logs):
# # #     print("Preprocessing logs...")
# # #     parsed_logs = []
# # #     for log in logs:
# # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # #         message = log[20:].strip()
# # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # #     return pd.DataFrame(parsed_logs)

# # # def analyze_log_message(timestamp, log_message):
# # #     print("Analyzing log message:", timestamp, log_message)
# # #     analysis = ollama.chat(
# # #         model="mistral",
# # #         messages=[{"role": "user", "timestamp": str(timestamp), "content": log_message}]
# # #     )["message"]["content"]
# # #     return analysis

# # # def monitor_errors_and_warnings(logs):
# # #     print("Monitoring errors and warnings...")
# # #     for index, row in logs.iterrows():
# # #         timestamp = str(row['timestamp'])
# # #         message = row['message']
# # #         analysis = analyze_log_message(timestamp, message + " Please analyze this log message for errors.")
# # #         print(f"Analysis for log message '{message}':\n{analysis}\n")
# # #         log_data = {
# # #             'timestamp': timestamp,
# # #             'message': message,
# # #             'analysis': analysis
# # #         }
# # #         try:
# # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # #             if response.status_code == 200:
# # #                 print("Data sent to Logstash successfully")
# # #             else:
# # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # #         except Exception as e:
# # #             print(f"Error occurred while sending data to Logstash: {str(e)}")


# # # @app.route('/api/analyze', methods=['POST'])
# # # def upload_file():
# # #     if 'file' not in request.files:
# # #         return jsonify({'error': 'No file part'}), 400

# # #     uploaded_file = request.files['file']
# # #     if uploaded_file.filename == '':
# # #         return jsonify({'error': 'No selected file'}), 400

# # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # #         parsed_logs = preprocess_logs(logs)
# # #         print("Logs preprocessed:")
# # #         print(parsed_logs)
# # #         monitor_errors_and_warnings(parsed_logs)
# # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # #     else:
# # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # if __name__ == '__main__':
# # #     app.run(debug=True)

# # # from flask import Flask, request, jsonify
# # # from flask_cors import CORS
# # # import ollama
# # # import datetime
# # # import pandas as pd
# # # import requests
# # # import pandas as pd
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.feature_extraction.text import CountVectorizer
# # # from sklearn.naive_bayes import MultinomialNB
# # # from sklearn.metrics import accuracy_score

# # # app = Flask(__name__)
# # # CORS(app)
# # # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # # LOGSTASH_ENDPOINT = 'http://localhost:5044'

# # # def allowed_file(filename):
# # #     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # # def preprocess_logs(logs):
# # #     print("Preprocessing logs...")
# # #     parsed_logs = []
# # #     for log in logs:
# # #         timestamp = datetime.datetime.strptime(log[:19], '%Y-%m-%d %H:%M:%S')
# # #         message = log[20:].strip()
# # #         parsed_logs.append({'timestamp': timestamp, 'message': message})
# # #         print(parsed_logs)
# # #     return pd.DataFrame(parsed_logs)

# # # def analyze_log_message(timestamp, log_message):
# # #     print("Analyzing log message:", timestamp, log_message)
# # #     analysis = ollama.chat(
# # #         model="mistral",
# # #         messages=[{"role": "user", "timestamp": str(timestamp), "content": log_message}]
# # #     )["message"]["content"]
# # #     return analysis

# # # def monitor_errors_and_warnings(logs, prompt):
# # #     print("Monitoring errors and warnings...")
# # #     for index, row in logs.iterrows():
# # #         timestamp = str(row['timestamp'])
# # #         message = row['message']
# # #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# # #         print(f"Analysis for log message '{message}':\n{analysis}\n")
# # #         log_data = {
# # #             'timestamp': timestamp,
# # #             'message': message,
# # #             'analysis': analysis
# # #         }
# # #         try:
# # #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# # #             if response.status_code == 200:
# # #                 print("Data sent to Logstash successfully")
# # #             else:
# # #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# # #         except Exception as e:
# # #             print(f"Error occurred while sending data to Logstash: {str(e)}")


# # # @app.route('/api/analyze', methods=['POST'])
# # # def upload_file():
# # #     if 'file' not in request.files:
# # #         return jsonify({'error': 'No file part'}), 400

# # #     uploaded_file = request.files['file']
# # #     prompt = request.form.get('prompt')  # Get the prompt from the request

# # #     if uploaded_file.filename == '':
# # #         return jsonify({'error': 'No selected file'}), 400

# # #     if uploaded_file and allowed_file(uploaded_file.filename):
# # #         logs = uploaded_file.stream.read().decode("utf-8").splitlines()
# # #         parsed_logs = preprocess_logs(logs)
# # #         print("Logs preprocessed:")
# # #         print(parsed_logs)
# # #         monitor_errors_and_warnings(parsed_logs, prompt)  # Pass the prompt to the function
# # #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# # #     else:
# # #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400


# # # if __name__ == '__main__':
# # #     app.run(debug=True)
# # import re
# # import os
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import ollama
# # import datetime
# # import pandas as pd
# # import requests
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # CORS(app)
# # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # LOGSTASH_ENDPOINT = 'http://localhost:5044'
# # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
# #     error_keywords = []
# #     try:
# #         with open(file_path, 'r') as file:
# #             for line in file:
# #                 keyword = line.strip()
# #                 if keyword:
# #                     error_keywords.append(keyword)
# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred while loading error keywords: {e}")
# #     return error_keywords

# # def check_for_errors(message, error_keywords):
# #     # Check if any error keywords are present in the message (case-insensitive)
# #     for keyword in error_keywords:
# #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# #             return True
# #     return False

# # def analyze_log_message(timestamp, log_message):
# #     print("Analyzing log message:", timestamp, log_message)
# #     combined_message = f"{timestamp}: {log_message}"
# #     analysis = ollama.chat(
# #         model="error-monitor",
# #         messages=[{"role": "user", "content": combined_message}]
# #     )["message"]["content"]
# #     return analysis

# # def monitor_errors_and_warnings(logs, prompt):
# #     print("Monitoring errors and warnings...")
# #     for index, row in logs.iterrows():
# #         timestamp = str(row['timestamp'])
# #         message = row['message']
# #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# #         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
# #         log_data = {
# #             'timestamp': timestamp,
# #             'message': message,
# #             'analysis': analysis
# #         }
# #         try:
# #             response = requests.post(LOGSTASH_ENDPOINT, json=log_data)
# #             if response.status_code == 200:
# #                 print("Data sent to Logstash successfully")
# #             else:
# #                 print(f"Failed to send data to Logstash. Status code: {response.status_code}")
# #         except Exception as e:
# #             print(f"Error occurred while sending data to Logstash: {str(e)}")

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
# #         print(logs)
# #         parsed_logs = preprocess_logs(logs)
# #         print(parsed_logs)
# #         # parsed_logs.to_csv('parsed_log.csv')
# #         error_keywords = load_error_keywords(error_keywords_file_path)
# #         errors = []
# #         for index, row in parsed_logs.iterrows():
# #             message = row['message']
# #             if check_for_errors(message, error_keywords):
# #                 errors.append({'timestamp': row['timestamp'], 'message': message})

# #     # Create a DataFrame from the list of errors
# #         error_df = pd.DataFrame(errors)

# #     # Print the DataFrame containing errors
# #         print("Errors detected:")
# #         print(error_df)
# #         monitor_errors_and_warnings(error_df, prompt)  # Pass the prompt to the function
        
# #         return jsonify({'message': 'File uploaded and analyzed successfully'}), 200
# #     else:
# #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # if __name__ == '__main__':
# #     app.run(debug=True)


# # import re
# # import os
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import ollama
# # import datetime
# # import pandas as pd
# # import requests
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # CORS(app)
# # ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# # LOGSTASH_ENDPOINT = 'http://localhost:5044'
# # UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
# #     error_keywords = []
# #     try:
# #         with open(file_path, 'r') as file:
# #             for line in file:
# #                 keyword = line.strip()
# #                 if keyword:
# #                     error_keywords.append(keyword)
# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")
# #     except Exception as e:
# #         print(f"An error occurred while loading error keywords: {e}")
# #     return error_keywords

# # def check_for_errors(message, error_keywords):
# #     # Check if any error keywords are present in the message (case-insensitive)
# #     for keyword in error_keywords:
# #         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
# #             return True
# #     return False

# # def analyze_log_message(timestamp, log_message):
# #     print("Analyzing log message:", timestamp, log_message)
# #     combined_message = f"{timestamp}: {log_message}"
# #     analysis = ollama.chat(
# #         model="error-monitor",
# #         messages=[{"role": "user", "content": combined_message}]
# #     )["message"]["content"]
# #     return analysis

# # def monitor_errors_and_warnings(logs, prompt):
# #     print("Monitoring errors and warnings...")
# #     analysis_results = []
# #     for index, row in logs.iterrows():
# #         timestamp = str(row['timestamp'])
# #         message = row['message']
# #         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
# #         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
# #         analysis_results.append(analysis)
# #         print(analysis_results)

# #     # Concatenate all analysis results into a single string
# #     analysis_data = "\n".join(analysis_results)
# #     return analysis_data

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
# #         parsed_logs = preprocess_logs(logs)

# #         error_keywords = load_error_keywords(error_keywords_file_path)
# #         errors = []
# #         for index, row in parsed_logs.iterrows():
# #             message = row['message']
# #             if check_for_errors(message, error_keywords):
# #                 errors.append({'timestamp': row['timestamp'], 'message': message})

# #         # Create a DataFrame from the list of errors
# #         error_df = pd.DataFrame(errors)
# #         print(error_df)

# #         # Monitor errors and warnings and get analysis data
# #         analysis_data = monitor_errors_and_warnings(error_df, prompt)  

# #         # Return analysis data as response
# #         return jsonify({'analysis_data': analysis_data}), 200
# #     else:
# #         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# # if __name__ == '__main__':
# #     app.run(debug=True) 

# import re
# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import ollama
# import datetime
# import pandas as pd
# import requests
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# CORS(app)
# ALLOWED_EXTENSIONS = {'csv', 'json', 'xml', 'txt', 'log'}
# LOGSTASH_ENDPOINT = 'http://localhost:5044'
# UPLOAD_FOLDER = r'C:\Users\Aravindan\test1\backend\venv\upload'  # Change this to your desired upload folder
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
#     error_keywords = []
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 keyword = line.strip()
#                 if keyword:
#                     error_keywords.append(keyword)
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred while loading error keywords: {e}")
#     return error_keywords

# def check_for_errors(message, error_keywords):
#     # Check if any error keywords are present in the message (case-insensitive)
#     for keyword in error_keywords:
#         if re.search(r'\b' + re.escape(keyword) + r'\b', message, re.IGNORECASE):
#             return True
#     return False

# def analyze_log_message(timestamp, log_message):
#     print("Analyzing log message:", timestamp, log_message)
#     combined_message = f"{timestamp}: {log_message}"
#     analysis = ollama.chat(
#         model="error-monitor",
#         messages=[{"role": "user", "content": combined_message}]
#     )["message"]["content"]
#     return analysis

# def monitor_errors_and_warnings(logs, prompt):
#     print("Monitoring errors and warnings...")
#     timestamps = []
#     messages = []
#     analysis_results = []
#     for index, row in logs.iterrows():
#         timestamp = str(row['timestamp'])
#         message = row['message']
#         analysis = analyze_log_message(timestamp, message + " " + prompt)  # Include the prompt
#         print(f"Analysis for log message ' {timestamp}{message}':\n{analysis}\n")
#         timestamps.append(timestamp)
#         messages.append(message)
#         analysis_results.append(analysis)

#     return timestamps, messages, analysis_results

# @app.route('/api/analyze', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     uploaded_file = request.files['file']
#     prompt = request.form.get('prompt')  # Get the prompt from the request
#     error_keywords_file_path = r'C:\Users\Aravindan\test1\backend\venv\error_keywords.txt'
#     if uploaded_file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if uploaded_file and allowed_file(uploaded_file.filename):
#         # Save the uploaded file to a specific location
#         upload_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename))
#         uploaded_file.save(upload_file_path)

#         # Open and process the saved file
#         logs = parse_log_file(upload_file_path)
#         print(logs)
#         parsed_logs = preprocess_logs(logs)
#         print(parsed_logs)
#         # parsed_logs.to_csv('parsed_log.csv')
#         error_keywords = load_error_keywords(error_keywords_file_path)
#         errors = []
#         for index, row in parsed_logs.iterrows():
#             message = row['message']
#             if check_for_errors(message, error_keywords):
#                 errors.append({'timestamp': row['timestamp'], 'message': message})
#         # Create a DataFrame from the list of errors
#         error_df = pd.DataFrame(errors)
#         print(error_df)
#         timestamps, messages,analysis_results  = monitor_errors_and_warnings(error_df, prompt)

#         # Return the separate arrays as response
#         return jsonify({'timestamps': timestamps, 'messages': messages, 'analysis_results': analysis_results}), 200
#     else:
#         return jsonify({'error': 'Invalid file type or no file uploaded'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
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
        response = requests.post('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
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

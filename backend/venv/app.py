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
from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

def find_header(csv_file):
    # Read the first line of the CSV file to identify the header
    header = csv_file.readline().decode().strip().split(',')
    return header

def is_valid_csv(file_path):
    try:
        pd.read_csv(file_path)
        return True
    except Exception as e:
        return False

@app.route('/api/analyze', methods=['POST'])
def analyze_file():
    if request.method == 'POST':
        try:
            # Get uploaded file
            uploaded_file = request.files.get('file')
            if uploaded_file:
                # Check if it's a valid CSV file
                if not is_valid_csv(uploaded_file):
                    return jsonify({'error': 'Invalid CSV file format'}), 400
                
                # Read the uploaded file using pandas
                uploaded_file.seek(0)  # Reset file pointer to read again from the beginning
                header = find_header(uploaded_file)
                uploaded_file.seek(0)  # Reset file pointer again
                df = pd.read_csv(uploaded_file)

                # Convert DataFrame to a list of dictionaries (suitable for JSON)
                data = df.to_dict(orient='records')
                
                # Construct JSON response dynamically based on header and data
                response_data = {'header': header, 'data': data}
                print(response_data)
                return jsonify(response_data)
            else:
                return jsonify({'error': 'No file uploaded'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Return specific error message
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
# # # # # # # import streamlit as st
# # # # # # # import requests
# # # # # # # import pandas as pd
# # # # # # # import altair as alt
# # # # # # # import json

# # # # # # # # Define the Flask API endpoint
# # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # @st.cache_data(show_spinner=False)
# # # # # # # def get_analysis_results(file, prompt):
# # # # # # #     # Send file and prompt to Flask API
# # # # # # #     files = {'file': file}
# # # # # # #     data = {'prompt': prompt}
# # # # # # #     response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # #     if response.status_code == 200:
# # # # # # #         return response.json()
# # # # # # #     else:
# # # # # # #         return None

# # # # # # # def main():
# # # # # # #     st.title("Log Analyzer")

# # # # # # #     # Sidebar for file upload and prompt input
# # # # # # #     st.sidebar.header("Input")
# # # # # # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # # # # # #     # Analyze Button
# # # # # # #     analyze_button = st.sidebar.button("Analyze")

# # # # # # #     # Display analysis results in the main content area
# # # # # # #     if analyze_button:
# # # # # # #         if uploaded_file is not None:
# # # # # # #             analysis_result = get_analysis_results(uploaded_file, prompt)
# # # # # # #             if analysis_result:
# # # # # # #                 display_analysis_results(analysis_result)
# # # # # # #             else:
# # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # def display_analysis_results(analysis_result):
# # # # # # #     # Extract error list and count list
# # # # # # #     error_list = analysis_result.get('error_list', [])
# # # # # # #     count_list = analysis_result.get('count_list', [])
# # # # # # #     timestamps_list = analysis_result.get('timestamps', [])
# # # # # # #     log_messages_list = analysis_result.get('messages', [])
# # # # # # #     log_data = analysis_result.get('results_json', [])
# # # # # # #     print(log_data)

# # # # # # #     # Create a DataFrame for Altair
# # # # # # #     df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list, 'Timestamp': timestamps_list, 'Log Message': log_messages_list})
# # # # # # #     print(df)
# # # # # # #     if error_list and count_list:
# # # # # # #         st.subheader("Error Counts")
# # # # # # #         # Create Altair chart with tooltips
# # # # # # #         chart = alt.Chart(df).mark_bar().encode(
# # # # # # #             x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # # # #             y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # # # #             color=alt.Color('Error Type', scale=alt.Scale(scheme='category10'), legend=None),
# # # # # # #             tooltip=['Error Type', 'Error Count']
# # # # # # #         ).properties(
# # # # # # #             width=600,
# # # # # # #             height=400
# # # # # # #         )
# # # # # # #         st.altair_chart(chart, use_container_width=True)

# # # # # # #         # Convert JSON string to Python object
# # # # # # #         data = json.loads(log_data)
# # # # # # #         print(data)

# # # # # # #         # Main Streamlit app
# # # # # # #         st.title('JSON Data Visualization')

# # # # # # #         # Iterate over each dictionary in the data
# # # # # # #         # for entry in data:
# # # # # # #         #     key = entry['key']
# # # # # # #         #     values = entry['values']
            
# # # # # # #         #     st.subheader(f'Data for key: {key}')
            
# # # # # # #         #     # Display each value
# # # # # # #         #     for value_data in values:
# # # # # # #         #         value = value_data['value']
# # # # # # #         #         timestamp = value_data['timestamp']
# # # # # # #         #         log_message = value_data['log_message']
                
# # # # # # #         #         st.write(f"Value: {value}, Timestamp: {timestamp}, Log Message: {log_message}")
# # # # # # #         # Iterate over each dictionary in the data
# # # # # # #         for entry in data:
# # # # # # #             key = entry['key']
# # # # # # #             values = entry['values']
            
# # # # # # #             # Display key in a box
# # # # # # #             expander_key = st.expander(f'Data for key: {key}', expanded=False)
            
# # # # # # #             # Check if the expander is expanded (arrow icon clicked)
# # # # # # #             if expander_key.expanded:
# # # # # # #                 # Display details
# # # # # # #                 with expander_key:
# # # # # # #                     # Display each value
# # # # # # #                     for value_data in values:
# # # # # # #                         value = value_data['value']
# # # # # # #                         timestamp = value_data['timestamp']
# # # # # # #                         log_message = value_data['log_message']
                        
# # # # # # #                         # Style the output
# # # # # # #                         st.markdown(f"<p style='color:red;'>Timestamp: {timestamp}</p>", unsafe_allow_html=True)
# # # # # # #                         st.markdown(f"<p style='color:green;'>Log Message: {log_message}</p>", unsafe_allow_html=True)
# # # # # # #                         st.write(f"Value: {value}")


# # # # # # # if __name__ == "__main__":
# # # # # # #     main()








# # # # # # # import streamlit as st
# # # # # # # import requests
# # # # # # # import pandas as pd
# # # # # # # import altair as alt
# # # # # # # import json

# # # # # # # # Define the Flask API endpoint
# # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # @st.cache_data(show_spinner=False)
# # # # # # # def get_analysis_results(file, prompt):
# # # # # # #     # Send file and prompt to Flask API
# # # # # # #     files = {'file': file}
# # # # # # #     data = {'prompt': prompt}
# # # # # # #     response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # #     if response.status_code == 200:
# # # # # # #         return response.json()
# # # # # # #     else:
# # # # # # #         return None

# # # # # # # def main():
# # # # # # #     st.title("Log Analyzer")

# # # # # # #     # Sidebar for file upload and prompt input
# # # # # # #     st.sidebar.header("Input")
# # # # # # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # # # # # #     # Analyze Button
# # # # # # #     analyze_button = st.sidebar.button("Analyze")

# # # # # # #     # Display analysis results in the main content area
# # # # # # #     if analyze_button:
# # # # # # #         if uploaded_file is not None:
# # # # # # #             analysis_result = get_analysis_results(uploaded_file, prompt)
# # # # # # #             if analysis_result:
# # # # # # #                 display_analysis_results(analysis_result)
# # # # # # #             else:
# # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # def display_analysis_results(analysis_result):
# # # # # # #     # Extract error list and count list
# # # # # # #     error_list = analysis_result.get('error_list', [])
# # # # # # #     count_list = analysis_result.get('count_list', [])
# # # # # # #     timestamps_list = analysis_result.get('timestamps', [])
# # # # # # #     log_messages_list = analysis_result.get('messages', [])
# # # # # # #     log_data = analysis_result.get('results_json', [])
# # # # # # #     print(log_data)

# # # # # # #     # Create a DataFrame for Altair
# # # # # # #     df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list, 'Timestamp': timestamps_list, 'Log Message': log_messages_list})
# # # # # # #     print(df)
# # # # # # #     if error_list and count_list:
# # # # # # #         st.subheader("Error Counts")
# # # # # # #         # Create Altair chart with tooltips
# # # # # # #         chart = alt.Chart(df).mark_bar().encode(
# # # # # # #             x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # # # #             y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # # # #             color=alt.Color('Error Type', scale=alt.Scale(scheme='category10'), legend=None),
# # # # # # #             tooltip=['Error Type', 'Error Count']
# # # # # # #         ).properties(
# # # # # # #             width=600,
# # # # # # #             height=400
# # # # # # #         )
# # # # # # #         st.altair_chart(chart, use_container_width=True)

# # # # # # #         # Convert JSON string to Python object
# # # # # # #         data = json.loads(log_data)
# # # # # # #         print(data)

# # # # # # #         # Main Streamlit app
# # # # # # #         st.title('Assistant....')

# # # # # # #         for entry in data:
# # # # # # #             key = entry['key']
# # # # # # #             values = entry['values']
            
# # # # # # #             # Display key in a box
# # # # # # #             expander_key = st.expander(f'Error: {key}', expanded=False)
            
# # # # # # #             # Check if the expander is expanded (arrow icon clicked)
# # # # # # #             if expander_key.expanded:
# # # # # # #                 # Display details
# # # # # # #                 with expander_key:
# # # # # # #                     # Display each value
# # # # # # #                     for value_data in values:
# # # # # # #                         value = value_data['value']
# # # # # # #                         timestamp = value_data['timestamp']
# # # # # # #                         log_message = value_data['log_message']
                        
# # # # # # #                         # Style the output
# # # # # # #                         st.markdown(f"<p style='color:red;'>Timestamp: {timestamp}</p>", unsafe_allow_html=True)
# # # # # # #                         st.markdown(f"<p style='color:green;'>Log Message: {log_message}</p>", unsafe_allow_html=True)
# # # # # # #                         st.write(f"Value: {value}")


# # # # # # # if __name__ == "__main__":
# # # # # # #     main()



# # # # # # import streamlit as st
# # # # # # import requests
# # # # # # import time
# # # # # # import pandas as pd
# # # # # # from collections import Counter
# # # # # # import altair as alt

# # # # # # # Define the Flask server URLs
# # # # # # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # # # # # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # # # # # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # # # # # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # # # # # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # # # # # Predefined list of colors
# # # # # # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # # # # # st.title('Live Streaming Log Analyzer')

# # # # # # def fetch_data():
# # # # # #     response_data = requests.get(FLASK_DATA_URL)
# # # # # #     response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# # # # # #     response_messages = requests.get(FLASK_MESSAGE_URL)
# # # # # #     response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# # # # # #     response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
    
# # # # # #     if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# # # # # #         response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# # # # # #         response_error_counts.status_code == 200):
        
# # # # # #         data = response_data.json()
# # # # # #         timestamps = response_timestamps.json()
# # # # # #         messages = response_messages.json()
# # # # # #         analyzed_messages = response_analyzed_messages.json()
# # # # # #         error_counts = response_error_counts.json()
        
# # # # # #         return data, timestamps, messages, analyzed_messages, error_counts
# # # # # #     else:
# # # # # #         return None, None, None, None, None

# # # # # # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# # # # # #     # Extract error types and counts from the data
# # # # # #     error_types = list(error_counts.keys())
# # # # # #     error_values = list(error_counts.values())
    
# # # # # #     # Display current data with occurrences
# # # # # #     formatted_data = "\n".join(f"{i+1}. {item}: {error_counts[item]}" for i, item in enumerate(error_types))
# # # # # #     st.text(f"Current data:\n{formatted_data}")
    
# # # # # #     # Create a DataFrame from the error counts
# # # # # #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# # # # # #     # Assign colors to each error type
# # # # # #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# # # # # #     df['Color'] = df['Error Type'].map(color_mapping)
    
# # # # # #     # Create Altair chart with tooltips
# # # # # #     chart = alt.Chart(df).mark_bar().encode(
# # # # # #         x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # # #         y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # # #         color=alt.Color('Color', scale=None),  # Disable color scale
# # # # # #         tooltip=['Error Type', 'Error Count']
# # # # # #     ).properties(
# # # # # #         width=600,
# # # # # #         height=400
# # # # # #     )
    
# # # # # #     st.altair_chart(chart, use_container_width=True)
    
# # # # # #     # Display timestamps, messages, and analyzed messages
# # # # # #     combined_info = []
# # # # # #     for i in range(len(timestamps)):
# # # # # #         combined_info.append(f"**{i+1}. Error Assistant.........**")
# # # # # #         combined_info.append(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>")
# # # # # #         combined_info.append(f"<span style='color:red;'>**Message:** {messages[i]}</span>")
# # # # # #         combined_info.append(f"**Analyzed Message:** {analyzed_messages[i]}")
    
# # # # # #     st.markdown("<br><br>".join(combined_info), unsafe_allow_html=True)

# # # # # # st.sidebar.title("Log File Upload and Analysis")
# # # # # # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # # # # # analyze_button = st.sidebar.button("Analyze")

# # # # # # if analyze_button:
# # # # # #     if uploaded_file is not None and prompt:
# # # # # #         files = {'file': uploaded_file}
# # # # # #         data = {'prompt': prompt}
# # # # # #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# # # # # #         if response.status_code == 200:
# # # # # #             st.sidebar.success("File uploaded and analysis started.")
# # # # # #         else:
# # # # # #             st.sidebar.error("Error analyzing file. Please try again.")
# # # # # #     else:
# # # # # #         st.sidebar.error("Please upload a file and enter a prompt.")

# # # # # # while True:
# # # # # #     try:
# # # # # #         data, timestamps, messages, analyzed_messages, error_counts = fetch_data()
        
# # # # # #         if data is not None:
# # # # # #             display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# # # # # #         else:
# # # # # #             st.text("Error fetching data. Please check the server.")
# # # # # #     except Exception as e:
# # # # # #         st.text(f"Exception: {str(e)}")
    
# # # # # #     time.sleep(5)  # Fetch new data every 5 seconds

















# # # # # # #----------------------------------------------------------------------------------

# # # # # # # # # # import streamlit as st

# # # # # # # # # # # Mock data
# # # # # # # # # # log_data = [
# # # # # # # # # #     {
# # # # # # # # # #         'key': 'Database Connection Failed',
# # # # # # # # # #         'values': [
# # # # # # # # # #             {
# # # # # # # # # #                 'log_message': 'ERROR: Database connection failed',
# # # # # # # # # #                 'timestamp': '2024-04-04 10:30:05',
# # # # # # # # # #                 'value': "assistant\n\nAnother log line to analyze!\n\nHere's the error message:\n\n`2024-04-04 10:30:05 ERROR: Database connection failed`\n\nLet's break it down:\n\n* `ERROR`: This is the severity of the log message. It indicates that something went wrong.\n* `Database connection failed`: This is the specific error message. It's telling us that the software application was unable to connect to the database.\n\nWhat does this mean? In simple terms, the software application is unable to communicate with the database it needs to store or retrieve data. This could be due to various reasons such as:\n\n* The database is not running or is not reachable.\n* The database connection settings (e.g., username, password, hostname) are incorrect.\n* The network connection between the software application and the database is not stable or is down.\n\nSteps to resolve this error:\n\n1. **Check the database status**: Ensure the database is running and accessible. You can do this by checking the database's logs, status pages, or by running a simple query to verify its connectivity.\n2. **Verify database connection settings**: Double-check the database connection settings in the software application's configuration files or settings. Ensure that the username, password, hostname, and port are correct and match the database's configuration.\n3. **Check network connectivity**: Verify that the network connection between the software application and the database is stable and working correctly. You can try pinging the database's hostname or IP address to ensure connectivity.\n4. **Consult the software application's documentation**: If you're still having trouble, refer to the software application's documentation or support resources for specific guidance on resolving database connection issues.\n\nBy following these steps, you should be able to identify and resolve the issue preventing the software application from connecting to the database."
# # # # # # # # # #             }
# # # # # # # # # #         ]
# # # # # # # # # #     },
# # # # # # # # # #     {
# # # # # # # # # #         'key': 'Server overload detected',
# # # # # # # # # #         'values': [
# # # # # # # # # #             {
# # # # # # # # # #                 'log_message': 'ERROR: Server overload detected',
# # # # # # # # # #                 'timestamp': '2024-04-04 10:35:20',
# # # # # # # # # #                 'value': "assistant\n\nLog Line: 2024-04-04 10:35:20 ERROR: Server overload detected\n\nError: Server Overload Detected\n\nDescription: This error indicates that the server is experiencing a high level of traffic or activity, which is causing it to slow down or become unresponsive. This can occur when there are too many users accessing the server simultaneously, or when there are resource-intensive processes running on the server.\n\nImplications:\n\n* The server may become slow or unresponsive, leading to a poor user experience.\n* Data may not be processed or stored correctly, resulting in errors or inconsistencies.\n* The server may even crash or become unavailable, causing downtime and potential data loss.\n\nSteps to Resolve:\n\n1. **Check Server Load**: Use tools like top, vmstat, or sysctl to monitor the server's load. Identify the processes or services consuming the most resources and take steps to optimize or reduce their usage.\n2. **Scale Up the Server**: If the server is underpowered, consider upgrading the hardware or adding more resources (e.g., increasing RAM, CPU, or disk space).\n3. **Optimize Server Configuration**: Review the server's configuration to ensure it is optimized for the current workload. Adjust settings like memory allocation, CPU affinity, and disk I/O priorities as needed.\n4. **Implement Load Balancing**: Consider implementing load balancing techniques, such as round-robin DNS or a load balancer appliance, to distribute traffic across multiple servers.\n5. **Monitor and Analyze Server Logs**: Regularly review server logs to identify trends and patterns that may indicate potential issues before they become critical.\n6. **Upgrade Server Software**: Ensure the server's operating system and software are up-to-date, as newer versions often include performance optimizations and bug fixes.\n\nBy taking these steps, you can help prevent or mitigate server overload and ensure a smoother user experience."
# # # # # # # # # #             }
# # # # # # # # # #         ]
# # # # # # # # # #     }
# # # # # # # # # # ]

# # # # # # # # # # # Streamlit app
# # # # # # # # # # st.title('Error Log Analyzer')

# # # # # # # # # # # Iterate through each key-value pair and create dropdowns
# # # # # # # # # # for data in log_data:
# # # # # # # # # #     with st.expander(data['key'], expanded=False):
# # # # # # # # # #         for value in data['values']:
# # # # # # # # # #             st.subheader('Log Values:')
# # # # # # # # # #             st.write('Timestamp:', value['timestamp'])
# # # # # # # # # #             st.write('Log Message:', value['log_message'])
# # # # # # # # # #             st.write('Value:', value['value'])


# # # # # # # # import streamlit as st

# # # # # # # # # Mock JSON data
# # # # # # # # data = [
# # # # # # # #     {
# # # # # # # #         'key': 'Key 1',
# # # # # # # #         'values': [
# # # # # # # #             {'value': 10, 'timestamp': '2024-05-15 08:00:00', 'log_message': 'Value updated'},
# # # # # # # #             {'value': 15, 'timestamp': '2024-05-15 09:00:00', 'log_message': 'Value updated again'}
# # # # # # # #         ]
# # # # # # # #     },
# # # # # # # #     {
# # # # # # # #         'key': 'Key 2',
# # # # # # # #         'values': [
# # # # # # # #             {'value': 20, 'timestamp': '2024-05-15 10:00:00', 'log_message': 'Another value'}
# # # # # # # #         ]
# # # # # # # #     }
# # # # # # # # ]

# # # # # # # # # Main layout
# # # # # # # # st.title('JSON Data Visualization')

# # # # # # # # # Iterate over each dictionary in the data
# # # # # # # # for entry in data:
# # # # # # # #     key = entry['key']
# # # # # # # #     values = entry['values']
    
# # # # # # # #     # Display key in a box
# # # # # # # #     expander_key = st.expander(f'Data for key: {key}', expanded=False)
    
# # # # # # # #     # Check if the expander is expanded (arrow icon clicked)
# # # # # # # #     if expander_key.expanded:
# # # # # # # #         # Display details
# # # # # # # #         with expander_key:
# # # # # # # #             # Display each value
# # # # # # # #             for value_data in values:
# # # # # # # #                 value = value_data['value']
# # # # # # # #                 timestamp = value_data['timestamp']
# # # # # # # #                 log_message = value_data['log_message']
                
# # # # # # # #                 # Show timestamp and log message
# # # # # # # #                 st.write(f"Value: {value}, Timestamp: {timestamp}, Log Message: {log_message}")
# # # # # # # import streamlit as st

# # # # # # # # Mock JSON data
# # # # # # # data = [
# # # # # # #     {
# # # # # # #         'key': 'Key 1',
# # # # # # #         'values': [
# # # # # # #             {'value': 10, 'timestamp': '2024-05-15 08:00:00', 'log_message': 'Value updated'},
# # # # # # #             {'value': 15, 'timestamp': '2024-05-15 09:00:00', 'log_message': 'Value updated again'}
# # # # # # #         ]
# # # # # # #     },
# # # # # # #     {
# # # # # # #         'key': 'Key 2',
# # # # # # #         'values': [
# # # # # # #             {'value': 20, 'timestamp': '2024-05-15 10:00:00', 'log_message': 'Another value'}
# # # # # # #         ]
# # # # # # #     }
# # # # # # # ]

# # # # # # # # Main layout
# # # # # # # st.title('JSON Data Visualization')

# # # # # # # # Iterate over each dictionary in the data
# # # # # # # for entry in data:
# # # # # # #     key = entry['key']
# # # # # # #     values = entry['values']
    
# # # # # # #     # Display key in a box
# # # # # # #     expander_key = st.expander(f'Data for key: {key}', expanded=False)
    
# # # # # # #     # Check if the expander is expanded (arrow icon clicked)
# # # # # # #     if expander_key.expanded:
# # # # # # #         # Display details
# # # # # # #         with expander_key:
# # # # # # #             # Display each value
# # # # # # #             for value_data in values:
# # # # # # #                 value = value_data['value']
# # # # # # #                 timestamp = value_data['timestamp']
# # # # # # #                 log_message = value_data['log_message']
                
# # # # # # #                 # Style the output
# # # # # # #                 st.markdown(f"<p style='color:red;'>Timestamp: {timestamp}</p>", unsafe_allow_html=True)
# # # # # # #                 st.markdown(f"<p style='color:green;'>Log Message: {log_message}</p>", unsafe_allow_html=True)
# # # # # # #                 st.write(f"Value: {value}")
























































































# # # # # # #----------------------------------------------------------------------------------

# # # # # # # # # # import streamlit as st

# # # # # # # # # # # Mock data
# # # # # # # # # # log_data = [
# # # # # # # # # #     {
# # # # # # # # # #         'key': 'Database Connection Failed',
# # # # # # # # # #         'values': [
# # # # # # # # # #             {
# # # # # # # # # #                 'log_message': 'ERROR: Database connection failed',
# # # # # # # # # #                 'timestamp': '2024-04-04 10:30:05',
# # # # # # # # # #                 'value': "assistant\n\nAnother log line to analyze!\n\nHere's the error message:\n\n`2024-04-04 10:30:05 ERROR: Database connection failed`\n\nLet's break it down:\n\n* `ERROR`: This is the severity of the log message. It indicates that something went wrong.\n* `Database connection failed`: This is the specific error message. It's telling us that the software application was unable to connect to the database.\n\nWhat does this mean? In simple terms, the software application is unable to communicate with the database it needs to store or retrieve data. This could be due to various reasons such as:\n\n* The database is not running or is not reachable.\n* The database connection settings (e.g., username, password, hostname) are incorrect.\n* The network connection between the software application and the database is not stable or is down.\n\nSteps to resolve this error:\n\n1. **Check the database status**: Ensure the database is running and accessible. You can do this by checking the database's logs, status pages, or by running a simple query to verify its connectivity.\n2. **Verify database connection settings**: Double-check the database connection settings in the software application's configuration files or settings. Ensure that the username, password, hostname, and port are correct and match the database's configuration.\n3. **Check network connectivity**: Verify that the network connection between the software application and the database is stable and working correctly. You can try pinging the database's hostname or IP address to ensure connectivity.\n4. **Consult the software application's documentation**: If you're still having trouble, refer to the software application's documentation or support resources for specific guidance on resolving database connection issues.\n\nBy following these steps, you should be able to identify and resolve the issue preventing the software application from connecting to the database."
# # # # # # # # # #             }
# # # # # # # # # #         ]
# # # # # # # # # #     },
# # # # # # # # # #     {
# # # # # # # # # #         'key': 'Server overload detected',
# # # # # # # # # #         'values': [
# # # # # # # # # #             {
# # # # # # # # # #                 'log_message': 'ERROR: Server overload detected',
# # # # # # # # # #                 'timestamp': '2024-04-04 10:35:20',
# # # # # # # # # #                 'value': "assistant\n\nLog Line: 2024-04-04 10:35:20 ERROR: Server overload detected\n\nError: Server Overload Detected\n\nDescription: This error indicates that the server is experiencing a high level of traffic or activity, which is causing it to slow down or become unresponsive. This can occur when there are too many users accessing the server simultaneously, or when there are resource-intensive processes running on the server.\n\nImplications:\n\n* The server may become slow or unresponsive, leading to a poor user experience.\n* Data may not be processed or stored correctly, resulting in errors or inconsistencies.\n* The server may even crash or become unavailable, causing downtime and potential data loss.\n\nSteps to Resolve:\n\n1. **Check Server Load**: Use tools like top, vmstat, or sysctl to monitor the server's load. Identify the processes or services consuming the most resources and take steps to optimize or reduce their usage.\n2. **Scale Up the Server**: If the server is underpowered, consider upgrading the hardware or adding more resources (e.g., increasing RAM, CPU, or disk space).\n3. **Optimize Server Configuration**: Review the server's configuration to ensure it is optimized for the current workload. Adjust settings like memory allocation, CPU affinity, and disk I/O priorities as needed.\n4. **Implement Load Balancing**: Consider implementing load balancing techniques, such as round-robin DNS or a load balancer appliance, to distribute traffic across multiple servers.\n5. **Monitor and Analyze Server Logs**: Regularly review server logs to identify trends and patterns that may indicate potential issues before they become critical.\n6. **Upgrade Server Software**: Ensure the server's operating system and software are up-to-date, as newer versions often include performance optimizations and bug fixes.\n\nBy taking these steps, you can help prevent or mitigate server overload and ensure a smoother user experience."
# # # # # # # # # #             }
# # # # # # # # # #         ]
# # # # # # # # # #     }
# # # # # # # # # # ]

# # # # # # # # # # # Streamlit app
# # # # # # # # # # st.title('Error Log Analyzer')

# # # # # # # # # # # Iterate through each key-value pair and create dropdowns
# # # # # # # # # # for data in log_data:
# # # # # # # # # #     with st.expander(data['key'], expanded=False):
# # # # # # # # # #         for value in data['values']:
# # # # # # # # # #             st.subheader('Log Values:')
# # # # # # # # # #             st.write('Timestamp:', value['timestamp'])
# # # # # # # # # #             st.write('Log Message:', value['log_message'])
# # # # # # # # # #             st.write('Value:', value['value'])


# # # # # # # # import streamlit as st

# # # # # # # # # Mock JSON data
# # # # # # # # data = [
# # # # # # # #     {
# # # # # # # #         'key': 'Key 1',
# # # # # # # #         'values': [
# # # # # # # #             {'value': 10, 'timestamp': '2024-05-15 08:00:00', 'log_message': 'Value updated'},
# # # # # # # #             {'value': 15, 'timestamp': '2024-05-15 09:00:00', 'log_message': 'Value updated again'}
# # # # # # # #         ]
# # # # # # # #     },
# # # # # # # #     {
# # # # # # # #         'key': 'Key 2',
# # # # # # # #         'values': [
# # # # # # # #             {'value': 20, 'timestamp': '2024-05-15 10:00:00', 'log_message': 'Another value'}
# # # # # # # #         ]
# # # # # # # #     }
# # # # # # # # ]

# # # # # # # # # Main layout
# # # # # # # # st.title('JSON Data Visualization')

# # # # # # # # # Iterate over each dictionary in the data
# # # # # # # # for entry in data:
# # # # # # # #     key = entry['key']
# # # # # # # #     values = entry['values']
    
# # # # # # # #     # Display key in a box
# # # # # # # #     expander_key = st.expander(f'Data for key: {key}', expanded=False)
    
# # # # # # # #     # Check if the expander is expanded (arrow icon clicked)
# # # # # # # #     if expander_key.expanded:
# # # # # # # #         # Display details
# # # # # # # #         with expander_key:
# # # # # # # #             # Display each value
# # # # # # # #             for value_data in values:
# # # # # # # #                 value = value_data['value']
# # # # # # # #                 timestamp = value_data['timestamp']
# # # # # # # #                 log_message = value_data['log_message']
                
# # # # # # # #                 # Show timestamp and log message
# # # # # # # #                 st.write(f"Value: {value}, Timestamp: {timestamp}, Log Message: {log_message}")
# # # # # # # import streamlit as st

# # # # # # # # Mock JSON data
# # # # # # # data = [
# # # # # # #     {
# # # # # # #         'key': 'Key 1',
# # # # # # #         'values': [
# # # # # # #             {'value': 10, 'timestamp': '2024-05-15 08:00:00', 'log_message': 'Value updated'},
# # # # # # #             {'value': 15, 'timestamp': '2024-05-15 09:00:00', 'log_message': 'Value updated again'}
# # # # # # #         ]
# # # # # # #     },
# # # # # # #     {
# # # # # # #         'key': 'Key 2',
# # # # # # #         'values': [
# # # # # # #             {'value': 20, 'timestamp': '2024-05-15 10:00:00', 'log_message': 'Another value'}
# # # # # # #         ]
# # # # # # #     }
# # # # # # # ]

# # # # # # # # Main layout
# # # # # # # st.title('JSON Data Visualization')

# # # # # # # # Iterate over each dictionary in the data
# # # # # # # for entry in data:
# # # # # # #     key = entry['key']
# # # # # # #     values = entry['values']
    
# # # # # # #     # Display key in a box
# # # # # # #     expander_key = st.expander(f'Data for key: {key}', expanded=False)
    
# # # # # # #     # Check if the expander is expanded (arrow icon clicked)
# # # # # # #     if expander_key.expanded:
# # # # # # #         # Display details
# # # # # # #         with expander_key:
# # # # # # #             # Display each value
# # # # # # #             for value_data in values:
# # # # # # #                 value = value_data['value']
# # # # # # #                 timestamp = value_data['timestamp']
# # # # # # #                 log_message = value_data['log_message']
                
# # # # # # #                 # Style the output
# # # # # # #                 st.markdown(f"<p style='color:red;'>Timestamp: {timestamp}</p>", unsafe_allow_html=True)
# # # # # # #                 st.markdown(f"<p style='color:green;'>Log Message: {log_message}</p>", unsafe_allow_html=True)
# # # # # # #                 st.write(f"Value: {value}")


# # # # # import streamlit as st
# # # # # import requests
# # # # # import time
# # # # # import pandas as pd
# # # # # from collections import Counter
# # # # # import altair as alt

# # # # # # Define the Flask server URLs
# # # # # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # # # # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # # # # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # # # # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # # # # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # # # # Predefined list of colors
# # # # # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # # # # st.title('Live Streaming Log Analyzer')

# # # # # chart_placeholder = st.empty()

# # # # # def fetch_data():
# # # # #     response_data = requests.get(FLASK_DATA_URL)
# # # # #     response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# # # # #     response_messages = requests.get(FLASK_MESSAGE_URL)
# # # # #     response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# # # # #     response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
    
# # # # #     if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# # # # #         response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# # # # #         response_error_counts.status_code == 200):
        
# # # # #         data = response_data.json()
# # # # #         timestamps = response_timestamps.json()
# # # # #         messages = response_messages.json()
# # # # #         analyzed_messages = response_analyzed_messages.json()
# # # # #         error_counts = response_error_counts.json()
        
# # # # #         return data, timestamps, messages, analyzed_messages, error_counts
# # # # #     else:
# # # # #         return None, None, None, None, None

# # # # # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# # # # #     # Extract error types and counts from the data
# # # # #     error_types = list(error_counts.keys())
# # # # #     error_values = list(error_counts.values())
    
# # # # #     # Create a DataFrame from the error counts
# # # # #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# # # # #     # Assign colors to each error type
# # # # #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# # # # #     df['Color'] = df['Error Type'].map(color_mapping)
    
# # # # #     # Create Altair chart with tooltips
# # # # #     chart = alt.Chart(df).mark_bar().encode(
# # # # #         x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # #         y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # #         color=alt.Color('Color', scale=None),  # Disable color scale
# # # # #         tooltip=['Error Type', 'Error Count']
# # # # #     ).properties(
# # # # #         width=600,
# # # # #         height=400
# # # # #     )
    
# # # # #     chart_placeholder.altair_chart(chart, use_container_width=True)

# # # # # st.sidebar.title("Log File Upload and Analysis")
# # # # # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # # # # analyze_button = st.sidebar.button("Analyze")

# # # # # if analyze_button:
# # # # #     if uploaded_file is not None and prompt:
# # # # #         files = {'file': uploaded_file}
# # # # #         data = {'prompt': prompt}
# # # # #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# # # # #         if response.status_code == 200:
# # # # #             st.sidebar.success("File uploaded and analysis started.")
# # # # #         else:
# # # # #             st.sidebar.error("Error analyzing file. Please try again.")
# # # # #     else:
# # # # #         st.sidebar.error("Please upload a file and enter a prompt.")

# # # # # while True:
# # # # #     try:
# # # # #         data, timestamps, messages, analyzed_messages, error_counts = fetch_data()
        
# # # # #         if data is not None:
# # # # #             display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# # # # #         else:
# # # # #             st.text("Error fetching data. Please check the server.")
# # # # #     except Exception as e:
# # # # #         st.text(f"Exception: {str(e)}")
    
# # # # #     time.sleep(5)  # Fetch new data every 5 seconds



# # # # # import streamlit as st
# # # # # import requests
# # # # # import time
# # # # # import pandas as pd
# # # # # from collections import Counter
# # # # # import altair as alt

# # # # # # Define the Flask server URLs
# # # # # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # # # # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # # # # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # # # # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # # # # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # # # # Predefined list of colors
# # # # # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # # # # st.title('Live Streaming Log Analyzer')

# # # # # chart_placeholder = st.empty()
# # # # # info_placeholder = st.empty()

# # # # # def fetch_data():
# # # # #     try:
# # # # #         response_data = requests.get(FLASK_DATA_URL)
# # # # #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# # # # #         response_messages = requests.get(FLASK_MESSAGE_URL)
# # # # #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# # # # #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# # # # #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# # # # #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# # # # #             response_error_counts.status_code == 200):
            
# # # # #             data = response_data.json()
# # # # #             timestamps = response_timestamps.json()
# # # # #             messages = response_messages.json()
# # # # #             analyzed_messages = response_analyzed_messages.json()
# # # # #             error_counts = response_error_counts.json()
            
# # # # #             return data, timestamps, messages, analyzed_messages, error_counts
# # # # #         else:
# # # # #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# # # # #             return None, None, None, None, None
# # # # #     except Exception as e:
# # # # #         st.error(f"Exception occurred while fetching data: {str(e)}")
# # # # #         return None, None, None, None, None

# # # # # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# # # # #     # Extract error types and counts from the data
# # # # #     error_types = list(error_counts.keys())
# # # # #     error_values = list(error_counts.values())
    
# # # # #     # Create a DataFrame from the error counts
# # # # #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# # # # #     # Assign colors to each error type
# # # # #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# # # # #     df['Color'] = df['Error Type'].map(color_mapping)
    
# # # # #     # Create Altair chart with tooltips
# # # # #     chart = alt.Chart(df).mark_bar().encode(
# # # # #         x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # #         y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # #         color=alt.Color('Color', scale=None),  # Disable color scale
# # # # #         tooltip=['Error Type', 'Error Count']
# # # # #     ).properties(
# # # # #         width=600,
# # # # #         height=400
# # # # #     )
    
# # # # #     chart_placeholder.altair_chart(chart, use_container_width=True)
    
# # # # #     # Display timestamps, messages, and analyzed messages
# # # # #     combined_info = []
# # # # #     for i in range(len(timestamps)):
# # # # #         combined_info.append(f"**{i+1}. Error Assistant.........**")
# # # # #         combined_info.append(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>")
# # # # #         combined_info.append(f"<span style='color:red;'>**Message:** {messages[i]}</span>")
# # # # #         combined_info.append(f"**Analyzed Message:** {analyzed_messages[i]}")
    
# # # # #     info_placeholder.markdown("<br><br>".join(combined_info), unsafe_allow_html=True)

# # # # # st.sidebar.title("Log File Upload and Analysis")
# # # # # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # # # # analyze_button = st.sidebar.button("Analyze")

# # # # # if analyze_button:
# # # # #     if uploaded_file is not None and prompt:
# # # # #         files = {'file': uploaded_file}
# # # # #         data = {'prompt': prompt}
# # # # #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# # # # #         if response.status_code == 200:
# # # # #             st.sidebar.success("File uploaded and analysis started.")
# # # # #         else:
# # # # #             st.sidebar.error("Error analyzing file. Please try again.")
# # # # #     else:
# # # # #         st.sidebar.error("Please upload a file and enter a prompt.")

# # # # # while True:
# # # # #     data, timestamps, messages, analyzed_messages, error_counts = fetch_data()
    
# # # # #     if data is not None:
# # # # #         display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# # # # #     else:
# # # # #         st.text("Error fetching data. Please check the server.")
    
# # # # #     time.sleep(5)  # Fetch new data every 5 seconds

# # # # import streamlit as st
# # # # import requests
# # # # import time
# # # # import pandas as pd
# # # # from collections import Counter
# # # # import altair as alt

# # # # # Define the Flask server URLs
# # # # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # # # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # # # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # # # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # # # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # # # Predefined list of colors
# # # # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # # # st.title('Live Streaming Log Analyzer')

# # # # chart_placeholder = st.empty()
# # # # info_placeholder = st.empty()

# # # # def fetch_data():
# # # #     try:
# # # #         response_data = requests.get(FLASK_DATA_URL)
# # # #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# # # #         response_messages = requests.get(FLASK_MESSAGE_URL)
# # # #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# # # #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# # # #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# # # #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# # # #             response_error_counts.status_code == 200):
            
# # # #             data = response_data.json()
# # # #             timestamps = response_timestamps.json()
# # # #             messages = response_messages.json()
# # # #             analyzed_messages = response_analyzed_messages.json()
# # # #             error_counts = response_error_counts.json()
            
# # # #             return data, timestamps, messages, analyzed_messages, error_counts
# # # #         else:
# # # #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# # # #             return None, None, None, None, None
# # # #     except Exception as e:
# # # #         st.error(f"Exception occurred while fetching data: {str(e)}")
# # # #         return None, None, None, None, None

# # # # def display_analysis_results(data, error_counts, timestamps, messages, analyzed_messages):
# # # #     # Extract error types and counts from the data
# # # #     error_types = list(error_counts.keys())
# # # #     error_values = list(error_counts.values())
    
# # # #     # Create a DataFrame from the error counts
# # # #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# # # #     # Assign colors to each error type
# # # #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# # # #     df['Color'] = df['Error Type'].map(color_mapping)
    
# # # #     # Create Altair chart with tooltips
# # # #     chart = alt.Chart(df).mark_bar().encode(
# # # #         x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # #         y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # #         color=alt.Color('Color', scale=None),  # Disable color scale
# # # #         tooltip=['Error Type', 'Error Count']
# # # #     ).properties(
# # # #         width=600,
# # # #         height=400
# # # #     )
    
# # # #     chart_placeholder.altair_chart(chart, use_container_width=True)
    
# # # #     # Display headers from the data
# # # #     for i, entry in enumerate(data):
# # # #         with st.expander(f"Entry {i+1}"):
# # # #             st.write(entry)

# # # #     # Display timestamps, messages, and analyzed messages
# # # #     for i in range(len(timestamps)):
# # # #         with st.expander(f"Detailed Entry {i+1}"):
# # # #             st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# # # #             st.markdown(f"<span style='color:red;'>**Message:** {messages[i]}</span>", unsafe_allow_html=True)
# # # #             st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}")

# # # # st.sidebar.title("Log File Upload and Analysis")
# # # # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # # # analyze_button = st.sidebar.button("Analyze")

# # # # if analyze_button:
# # # #     if uploaded_file is not None and prompt:
# # # #         analysis_triggered = True
# # # #         files = {'file': uploaded_file}
# # # #         data = {'prompt': prompt}
# # # #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# # # #         if response.status_code == 200:
# # # #             st.sidebar.success("File uploaded and analysis started.")
# # # #             while True:
# # # #                 data, timestamps, messages, analyzed_messages, error_counts = fetch_data()

# # # #                 if data is not None:
# # # #                     display_analysis_results(data, error_counts, timestamps, messages, analyzed_messages)
# # # #                 else:
# # # #                     st.text("Error fetching data. Please check the server.")

# # # #                 time.sleep(5)  # Fetch new data every 5 seconds
# # # #         else:
# # # #             st.sidebar.error("Error analyzing file. Please try again.")
# # # #     else:
# # # #         st.sidebar.error("Please upload a file and enter a prompt.")


# # # # import streamlit as st
# # # # import requests
# # # # import time
# # # # import pandas as pd
# # # # from collections import Counter
# # # # import altair as alt

# # # # # Define the Flask server URLs
# # # # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # # # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # # # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # # # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # # # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # # # Predefined list of colors
# # # # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # # # st.title('Live Streaming Log Analyzer')

# # # # chart_placeholder = st.empty()
# # # # info_placeholder = st.empty()

# # # # def fetch_data():
# # # #     try:
# # # #         response_data = requests.get(FLASK_DATA_URL)
# # # #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# # # #         response_messages = requests.get(FLASK_MESSAGE_URL)
# # # #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# # # #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# # # #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# # # #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# # # #             response_error_counts.status_code == 200):
            
# # # #             data = response_data.json()
# # # #             timestamps = response_timestamps.json()
# # # #             messages = response_messages.json()
# # # #             analyzed_messages = response_analyzed_messages.json()
# # # #             error_counts = response_error_counts.json()
            
# # # #             return data, timestamps, messages, analyzed_messages, error_counts
# # # #         else:
# # # #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# # # #             return None, None, None, None, None
# # # #     except Exception as e:
# # # #         st.error(f"Exception occurred while fetching data: {str(e)}")
# # # #         return None, None, None, None, None

# # # # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# # # #     # Extract error types and counts from the data
# # # #     error_types = list(error_counts.keys())
# # # #     error_values = list(error_counts.values())
    
# # # #     # Create a DataFrame from the error counts
# # # #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# # # #     # Assign colors to each error type
# # # #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# # # #     df['Color'] = df['Error Type'].map(color_mapping)
    
# # # #     # Create Altair chart with tooltips
# # # #     chart = alt.Chart(df).mark_bar().encode(
# # # #         # x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # #         # y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # #         x=alt.X('Error Count', axis=alt.Axis(title='Error Count')),
# # # #         y=alt.Y('Error Type', axis=alt.Axis(title='Error Type')),
# # # #         color=alt.Color('Color', scale=None),  # Disable color scale
# # # #         tooltip=['Error Type', 'Error Count']
# # # #     ).properties(
# # # #         width=600,
# # # #         height=400
# # # #     )
    
# # # #     chart_placeholder.altair_chart(chart, use_container_width=True)
    
# # # #     # # Display timestamps, messages, and analyzed messages
# # # #     # combined_info = []
# # # #     # for i in range(len(timestamps)):
# # # #     #     combined_info.append(f"**{i+1}.<span style='color:green;'>**Error:** {data[i]}</span>**")
# # # #     #     combined_info.append(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>")
# # # #     #     combined_info.append(f"<span style='color:red;'>**Message:** {messages[i]}</span>")
# # # #     #     combined_info.append(f"**Analyzed Message:** {analyzed_messages[i]}")
    
# # # #     # info_placeholder.markdown("<br><br>".join(combined_info), unsafe_allow_html=True)
# # # #     # Display data[i] and use expander for details
# # # #     # for i in range(len(timestamps)):
# # # #     #     st.markdown(f"**{i+1}.** {data[i]}")
# # # #     #     with st.expander("Details"):
# # # #     #         st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"<span style='color:red;'>**Message:** {messages[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# # # #         # Display data[i] and use expander for details
# # # #     # combined_info = []
# # # #     # for i in range(len(timestamps)):
# # # #     #     combined_info.append(f"**{i+1}.** {data[i]}")
# # # #     #     with st.expander("Details"):
# # # #     #         st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"<span style='color:red;'>**Message:** {messages[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
    
# # # #     # info_placeholder.markdown("<br><br>".join(combined_info), unsafe_allow_html=True)
# # # #      # Display messages with expanders for details
# # # #     # info_placeholder.empty()  # Clear previous content
# # # #     # for i in range(len(messages)):
# # # #     #     with st.expander(f"**Message:** {messages[i]}", expanded=False):
# # # #     #         st.markdown(f"<span style='color:green;'>**Error:** {data[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# # # #     #         st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# # # #         # Display messages with expanders for details
# # # #     if 'displayed' not in st.session_state:
# # # #         st.session_state.displayed = set()

# # # #     info_placeholder.empty()  # Clear previous content
# # # #     for i in range(len(messages)):
# # # #         if messages[i] not in st.session_state.displayed:
# # # #             with st.expander(f"**Message:** {messages[i]}", expanded=False):
# # # #                 st.markdown(f"<span style='color:green;'>**Error:** {data[i]}</span>", unsafe_allow_html=True)
# # # #                 st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# # # #                 st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# # # #             st.session_state.displayed.add(messages[i])

# # # # st.sidebar.title("Log File Upload and Analysis")
# # # # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # # # analyze_button = st.sidebar.button("Analyze")

# # # # if analyze_button:
# # # #     if uploaded_file is not None and prompt:
# # # #         analysis_triggered = True
# # # #         files = {'file': uploaded_file}
# # # #         data = {'prompt': prompt}
# # # #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# # # #         if response.status_code == 200:
# # # #             st.sidebar.success("File uploaded and analysis started.")
# # # #             while True:
# # # #                 data, timestamps, messages, analyzed_messages, error_counts = fetch_data()

# # # #                 if data is not None:
# # # #                     display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# # # #                 else:
# # # #                     st.text("Error fetching data. Please check the server.")

# # # #                 time.sleep(5)  # Fetch new data every 5 seconds
# # # #         else:
# # # #             st.sidebar.error("Error analyzing file. Please try again.")
# # # #     else:
# # # #         st.sidebar.error("Please upload a file and enter a prompt.")




# # import streamlit as st
# # import requests
# # import time
# # import pandas as pd
# # from collections import Counter
# # import altair as alt

# # # Define the Flask server URLs
# # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # Predefined list of colors
# # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # st.title('Log Details')

# # chart_placeholder = st.empty()
# # info_placeholder = st.empty()

# # def fetch_data():
# #     try:
# #         response_data = requests.get(FLASK_DATA_URL)
# #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# #         response_messages = requests.get(FLASK_MESSAGE_URL)
# #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# #             response_error_counts.status_code == 200):
            
# #             data = response_data.json()
# #             timestamps = response_timestamps.json()
# #             messages = response_messages.json()
# #             analyzed_messages = response_analyzed_messages.json()
# #             error_counts = response_error_counts.json()
            
# #             return data, timestamps, messages, analyzed_messages, error_counts
# #         else:
# #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# #             return None, None, None, None, None
# #     except Exception as e:
# #         st.error(f"Exception occurred while fetching data: {str(e)}")
# #         return None, None, None, None, None

# # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# #     # Extract error types and counts from the data
# #     error_types = list(error_counts.keys())
# #     error_values = list(error_counts.values())
    
# #     # Create a DataFrame from the error counts
# #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# #     # Assign colors to each error type
# #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# #     df['Color'] = df['Error Type'].map(color_mapping)
    
# #     # Create Altair chart with tooltips
# #     chart = alt.Chart(df).mark_bar().encode(
# #         # x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# #         # y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# #         x=alt.X('Error Count', axis=alt.Axis(title='Error Count')),
# #         y=alt.Y('Error Type', axis=alt.Axis(title='Error Type')),
# #         color=alt.Color('Color', scale=None),  # Disable color scale
# #         tooltip=['Error Type', 'Error Count']
# #     ).properties(
# #         width=600,
# #         height=400
# #     )
# #     # chart = alt.Chart(df).mark_bar().encode(
# #     #     x=alt.X('Error Count', axis=alt.Axis(title='Error Count'), scale=alt.Scale(domain=[1, max(error_values)])),
# #     #     y=alt.Y('Error Type', axis=alt.Axis()),
# #     #     color=alt.Color('Color', scale=None),  # Disable color scale
# #     #     tooltip=['Error Type', 'Error Count']
# #     # ).properties(
# #     #     width=600,
# #     #     height=400
# #     # )


    



    
# #     chart_placeholder.altair_chart(chart, use_container_width=True)
# #     if 'displayed' not in st.session_state:
# #         st.session_state.displayed = set()

# #     info_placeholder.empty()  # Clear previous content
# #     for i in range(len(messages)):
# #         if messages[i] not in st.session_state.displayed:
# #             with st.expander(f"**Message:** {messages[i]}", expanded=False):
# #                 st.markdown(f"<span style='color:green;'>**Error:** {data[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# #             st.session_state.displayed.add(messages[i])

# # st.sidebar.title("Log File Upload and Analysis")
# # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # analyze_button = st.sidebar.button("Analyze")

# # if analyze_button:
# #     if uploaded_file is not None and prompt:
# #         analysis_triggered = True
# #         files = {'file': uploaded_file}
# #         data = {'prompt': prompt}
# #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# #         if response.status_code == 200:
# #             st.sidebar.success("File uploaded and analysis started.")
# #             while True:
# #                 data, timestamps, messages, analyzed_messages, error_counts = fetch_data()

# #                 if data is not None:
# #                     display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# #                 else:
# #                     st.text("Error fetching data. Please check the server.")

# #                 time.sleep(5)  # Fetch new data every 5 seconds
# #         else:
# #             st.sidebar.error("Error analyzing file. Please try again.")
# #     else:
# #         st.sidebar.error("Please upload a file and enter a prompt.")



# # import streamlit as st
# # import requests
# # import time
# # import pandas as pd
# # import altair as alt

# # # Define the Flask server URLs
# # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # Predefined list of colors
# # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # st.title('Error Update')

# # chart_placeholder = st.empty()
# # info_placeholder = st.empty()

# # def fetch_data():
# #     try:
# #         response_data = requests.get(FLASK_DATA_URL)
# #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# #         response_messages = requests.get(FLASK_MESSAGE_URL)
# #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# #             response_error_counts.status_code == 200):
            
# #             data = response_data.json()
# #             timestamps = response_timestamps.json()
# #             messages = response_messages.json()
# #             analyzed_messages = response_analyzed_messages.json()
# #             error_counts = response_error_counts.json()
            
# #             return data, timestamps, messages, analyzed_messages, error_counts
# #         else:
# #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# #             return None, None, None, None, None
# #     except Exception as e:
# #         st.error(f"Exception occurred while fetching data: {str(e)}")
# #         return None, None, None, None, None

# # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# #     # Extract error types and counts from the data
# #     error_types = list(error_counts.keys())
# #     error_values = list(error_counts.values())
    
# #     # Create a DataFrame from the error counts
# #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# #     # Assign colors to each error type
# #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# #     df['Color'] = df['Error Type'].map(color_mapping)
    
# #     # Create Altair chart with tooltips
# #     chart = alt.Chart(df).mark_bar().encode(
# #         x=alt.X('Error Count', axis=alt.Axis(title='Error Count'), scale=alt.Scale(domain=[1, 7])),
# #         y=alt.Y('Error Type', axis=alt.Axis()),
# #         color=alt.Color('Color', scale=None),  # Disable color scale
# #         tooltip=['Error Type', 'Error Count']
# #     ).properties(
# #         width=600,
# #         height=400
# #     )
    
# #     chart_placeholder.altair_chart(chart, use_container_width=True)
# #     if 'displayed' not in st.session_state:
# #         st.session_state.displayed = set()

# #     info_placeholder.empty()  # Clear previous content
# #     for i in range(len(messages)):
# #         if messages[i] not in st.session_state.displayed:
# #             with st.expander(f"**Message:** {messages[i]}", expanded=False):
# #                 st.markdown(f"<span style='color:green;'>**Error:** {data[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# #             st.session_state.displayed.add(messages[i])

# # st.sidebar.title("Log File Upload and Analysis")
# # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # analyze_button = st.sidebar.button("Analyze")

# # if analyze_button:
# #     if uploaded_file is not None and prompt:
# #         analysis_triggered = True
# #         files = {'file': uploaded_file}
# #         data = {'prompt': prompt}
# #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# #         if response.status_code == 200:
# #             st.sidebar.success("File uploaded and analysis started.")
# #             while True:
# #                 data, timestamps, messages, analyzed_messages, error_counts = fetch_data()

# #                 if data is not None:
# #                     display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# #                 else:
# #                     st.text("Error fetching data. Please check the server.")

# #                 time.sleep(5)  # Fetch new data every 5 seconds
# #         else:
# #             st.sidebar.error("Error analyzing file. Please try again.")
# #     else:
# #         st.sidebar.error("Please upload a file and enter a prompt.")


# # import streamlit as st
# # import requests
# # import time
# # import pandas as pd
# # import altair as alt

# # # Define the Flask server URLs
# # FLASK_DATA_URL = "http://127.0.0.1:5000/get_data"
# # FLASK_TIMESTAMP_URL = "http://127.0.0.1:5000/get_timestamps"
# # FLASK_MESSAGE_URL = "http://127.0.0.1:5000/get_messages"
# # FLASK_ANALYZED_MESSAGE_URL = "http://127.0.0.1:5000/get_analyzed_messages"
# # FLASK_ERROR_COUNTS_URL = "http://127.0.0.1:5000/get_error_counts"

# # # Predefined list of colors
# # colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# # st.title('Error Update')

# # chart_placeholder = st.empty()
# # info_placeholder = st.empty()

# # def fetch_data():
# #     try:
# #         response_data = requests.get(FLASK_DATA_URL)
# #         response_timestamps = requests.get(FLASK_TIMESTAMP_URL)
# #         response_messages = requests.get(FLASK_MESSAGE_URL)
# #         response_analyzed_messages = requests.get(FLASK_ANALYZED_MESSAGE_URL)
# #         response_error_counts = requests.get(FLASK_ERROR_COUNTS_URL)
        
# #         if (response_data.status_code == 200 and response_timestamps.status_code == 200 and 
# #             response_messages.status_code == 200 and response_analyzed_messages.status_code == 200 and 
# #             response_error_counts.status_code == 200):
            
# #             data = response_data.json()
# #             timestamps = response_timestamps.json()
# #             messages = response_messages.json()
# #             analyzed_messages = response_analyzed_messages.json()
# #             error_counts = response_error_counts.json()
            
# #             return data, timestamps, messages, analyzed_messages, error_counts
# #         else:
# #             st.error(f"Error fetching data. Status codes: {response_data.status_code}, {response_timestamps.status_code}, {response_messages.status_code}, {response_analyzed_messages.status_code}, {response_error_counts.status_code}")
# #             return None, None, None, None, None
# #     except Exception as e:
# #         st.error(f"Exception occurred while fetching data: {str(e)}")
# #         return None, None, None, None, None

# # def display_analysis_results(error_counts, timestamps, messages, analyzed_messages):
# #     # Extract error types and counts from the data
# #     error_types = list(error_counts.keys())
# #     error_values = list(error_counts.values())
    
# #     # Create a DataFrame from the error counts
# #     df = pd.DataFrame({'Error Type': error_types, 'Error Count': error_values})
    
# #     # Assign colors to each error type
# #     color_mapping = {error_type: colors[i % len(colors)] for i, error_type in enumerate(error_types)}
# #     df['Color'] = df['Error Type'].map(color_mapping)
    
# #     # Create Altair chart with tooltips
# #     chart = alt.Chart(df).mark_bar().encode(
# #         x=alt.X('Error Count', axis=alt.Axis(title='Error Count', tickMinStep=1), scale=alt.Scale(domain=[1, 7])),
# #         y=alt.Y('Error Type', axis=alt.Axis()),
# #         color=alt.Color('Color', scale=None),  # Disable color scale
# #         tooltip=['Error Type', 'Error Count']
# #     ).properties(
# #         width=600,
# #         height=400
# #     )
    
# #     chart_placeholder.altair_chart(chart, use_container_width=True)
# #     if 'displayed' not in st.session_state:
# #         st.session_state.displayed = set()

# #     info_placeholder.empty()  # Clear previous content
# #     for i in range(len(messages)):
# #         if messages[i] not in st.session_state.displayed:
# #             with st.expander(f"**Message:** {messages[i]}", expanded=False):
# #                 st.markdown(f"<span style='color:green;'>**Error:** {data[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"<span style='color:green;'>**Timestamp:** {timestamps[i]}</span>", unsafe_allow_html=True)
# #                 st.markdown(f"**Analyzed Message:** {analyzed_messages[i]}", unsafe_allow_html=True)
# #             st.session_state.displayed.add(messages[i])

# # st.sidebar.title("Log File Upload and Analysis")
# # uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # prompt = st.sidebar.text_input("Enter prompt for analysis")
# # analyze_button = st.sidebar.button("Analyze")

# # if analyze_button:
# #     if uploaded_file is not None and prompt:
# #         analysis_triggered = True
# #         files = {'file': uploaded_file}
# #         data = {'prompt': prompt}
# #         response = requests.post("http://127.0.0.1:5000/api/analyze", files=files, data=data)
# #         if response.status_code == 200:
# #             st.sidebar.success("File uploaded and analysis started.")
# #             while True:
# #                 data, timestamps, messages, analyzed_messages, error_counts = fetch_data()

# #                 if data is not None:
# #                     display_analysis_results(error_counts, timestamps, messages, analyzed_messages)
# #                 else:
# #                     st.text("Error fetching data. Please check the server.")

# #                 time.sleep(5)  # Fetch new data every 5 seconds
# #         else:
# #             st.sidebar.error("Error analyzing file. Please try again.")
# #     else:
# #         st.sidebar.error("Please upload a file and enter a prompt.")





# # import streamlit as st
# # import requests
# # import time

# # # URL of your Flask server
# # base_url = "http://127.0.0.1:5000"

# # st.title("Log Analyzer Dashboard")

# # # Function to fetch data from a given endpoint
# # def fetch_data(endpoint):
# #     response = requests.get(f"{base_url}{endpoint}")
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         st.error(f"Error fetching data from {endpoint}: {response.status_code}")
# #         return []

# # # Tabs for different data points
# # tab1, tab2, tab3, tab4, tab5 = st.tabs(["Live Error Counts", "P Values", "Messages", "Timestamps", "Analyzed Messages"])

# # with tab1:
# #     st.header("Live Error Counts")
# #     live_error_counts_placeholder = st.empty()

# # with tab2:
# #     st.header("P Values")
# #     p_values_placeholder = st.empty()

# # with tab3:
# #     st.header("Messages")
# #     messages_placeholder = st.empty()

# # with tab4:
# #     st.header("Timestamps")
# #     timestamps_placeholder = st.empty()

# # with tab5:
# #     st.header("Analyzed Messages")
# #     analyzed_messages_placeholder = st.empty()

# # # Function to update data in the UI
# # def update_data():
# #     with st.spinner("Updating data..."):
# #         live_error_counts = fetch_data('/get_live_error_counts')
# #         p_values = fetch_data('/get_p')
# #         messages = fetch_data('/get_messages')
# #         timestamps = fetch_data('/get_timestamps')
# #         analyzed_messages = fetch_data('/get_analyzed_messages')

# #         live_error_counts_placeholder.json(live_error_counts)
# #         p_values_placeholder.json(p_values)
# #         messages_placeholder.json(messages)
# #         timestamps_placeholder.json(timestamps)
# #         analyzed_messages_placeholder.json(analyzed_messages)

# # # Auto-refresh every 10 seconds
# # refresh_interval = 10

# # while True:
# #     update_data()
# #     time.sleep(refresh_interval)




# import streamlit as st
# import requests
# import time
# import plotly.express as px
# import pandas as pd  # Import pandas

# # URL of your Flask server
# base_url = "http://127.0.0.1:5000"

# st.title("Log Analyzer Dashboard")

# # Function to fetch data from a given endpoint
# def fetch_data(endpoint):
#     response = requests.get(f"{base_url}{endpoint}")
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"Error fetching data from {endpoint}: {response.status_code}")
#         return {}

# # Tabs for different data points
# tab1, tab2, tab3, tab4, tab5 = st.tabs(["Live Error Counts", "P Values", "Messages", "Timestamps", "Analyzed Messages"])

# with tab1:
#     st.header("Live Error Counts")
#     live_error_counts_placeholder = st.empty()

# with tab2:
#     st.header("P Values")
#     p_values_placeholder = st.empty()

# with tab3:
#     st.header("Messages")
#     messages_placeholder = st.empty()

# with tab4:
#     st.header("Timestamps")
#     timestamps_placeholder = st.empty()

# with tab5:
#     st.header("Analyzed Messages")
#     analyzed_messages_placeholder = st.empty()

# # Function to update data in the UI
# def update_data():
#     with st.spinner("Updating data..."):
#         live_error_counts = fetch_data('/get_live_error_counts')
#         p_values = fetch_data('/get_p')
#         messages = fetch_data('/get_messages')
#         timestamps = fetch_data('/get_timestamps')
#         analyzed_messages = fetch_data('/get_analyzed_messages')

#         # Update live error counts chart
#         if live_error_counts:
#             df = pd.DataFrame(live_error_counts.items(), columns=["Error Type", "Count"])
#             fig = px.bar(df, x="Count", y="Error Type", orientation='h', title="Live Error Counts")
#             live_error_counts_placeholder.plotly_chart(fig)

#         p_values_placeholder.json(p_values)
#         messages_placeholder.json(messages)
#         timestamps_placeholder.json(timestamps)
#         analyzed_messages_placeholder.json(analyzed_messages)

# # Auto-refresh every 10 seconds
# refresh_interval = 10

# # Ensure Streamlit's "stop" button works correctly
# stop_button = st.button("Stop Refresh")

# while True:
#     if stop_button:
#         st.stop()
#     update_data()
#     time.sleep(refresh_interval)


import streamlit as st
import requests
import time
import plotly.express as px
import pandas as pd  # Import pandas

# URL of your Flask server
base_url = "http://127.0.0.1:5000"

st.title("Log Analyzer Dashboard")

# Function to fetch data from a given endpoint
def fetch_data(endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from {endpoint}: {response.status_code}")
        return {}

# Tabs for different data points
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Live Error Counts", "P Values", "Messages", "Timestamps", "Analyzed Messages"])

with tab1:
    st.header("Live Error Counts")
    live_error_counts_placeholder = st.empty()

with tab2:
    st.header("P Values")
    p_values_placeholder = st.empty()

with tab3:
    st.header("Messages")
    messages_placeholder = st.empty()

with tab4:
    st.header("Timestamps")
    timestamps_placeholder = st.empty()

with tab5:
    st.header("Analyzed Messages")
    analyzed_messages_placeholder = st.empty()

# Function to update data in the UI
def update_data():
    with st.spinner("Updating data..."):
        live_error_counts = fetch_data('/get_live_error_counts')
        p_values = fetch_data('/get_p')
        messages = fetch_data('/get_messages')
        timestamps = fetch_data('/get_timestamps')
        analyzed_messages = fetch_data('/get_analyzed_messages')

        # Update live error counts chart
        if live_error_counts:
            df = pd.DataFrame(live_error_counts.items(), columns=["Error Type", "Count"])
            fig = px.bar(df, x="Count", y="Error Type", orientation='h', title="Live Error Counts")
            live_error_counts_placeholder.plotly_chart(fig)

        p_values_placeholder.json(p_values)
        messages_placeholder.json(messages)
        timestamps_placeholder.json(timestamps)
        analyzed_messages_placeholder.json(analyzed_messages)

        # Display messages with expander for details
        st.header("Errors with Details")
        for i, message in enumerate(messages):
            with st.expander(f"Message {message}", expanded=False):
                st.write(f"**Error Type:** {p_values[i]}")
                st.write(f"**Timestamp:** {timestamps[i]}")
                st.write(f"**Result:** {analyzed_messages[i]}")

# Auto-refresh every 10 seconds
refresh_interval = 10

# Start auto-refresh
while True:
    update_data()
    time.sleep(refresh_interval)
    st.experimental_rerun()

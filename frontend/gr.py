# # # # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # # # import requests

# # # # # # # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # # # # # # Streamlit UI
# # # # # # # # # # # # # # def main():
# # # # # # # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # # # # # # #     # File Upload
# # # # # # # # # # # # # #     uploaded_file = st.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])

# # # # # # # # # # # # # #     # Prompt Input
# # # # # # # # # # # # # #     prompt = st.text_input("Enter prompt for analysis")

# # # # # # # # # # # # # #     # Analyze Button
# # # # # # # # # # # # # #     if st.button("Analyze"):
# # # # # # # # # # # # # #         if uploaded_file is not None:
# # # # # # # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # # # # # #                 # Display analysis results
# # # # # # # # # # # # # #                 analysis_result = response.json()
# # # # # # # # # # # # # #                 st.write("Analysis Results:")
# # # # # # # # # # # # # #                 st.write("Error List:", analysis_result['error_list'])
# # # # # # # # # # # # # #                 st.write("Error Count:", analysis_result['count_list'])
# # # # # # # # # # # # # #                 st.write("Timestamps:", analysis_result['timestamps'])
# # # # # # # # # # # # # #                 st.write("Messages:", analysis_result['messages'])
# # # # # # # # # # # # # #                 st.write("Response Texts:", analysis_result['response_texts'])
# # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # # #     main()
# # # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # # import requests

# # # # # # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # # # # # Streamlit UI
# # # # # # # # # # # # # def main():
# # # # # # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # # # # # #     # File Upload
# # # # # # # # # # # # #     uploaded_file = st.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])

# # # # # # # # # # # # #     # Prompt Input
# # # # # # # # # # # # #     prompt = st.text_input("Enter prompt for analysis")

# # # # # # # # # # # # #     # Analyze Button
# # # # # # # # # # # # #     if st.button("Analyze"):
# # # # # # # # # # # # #         if uploaded_file is not None:
# # # # # # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # # # # #                 # Display analysis results
# # # # # # # # # # # # #                 analysis_result = response.json()
# # # # # # # # # # # # #                 display_chat(analysis_result)
# # # # # # # # # # # # #             else:
# # # # # # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # # # # # # def display_chat(analysis_result):
# # # # # # # # # # # # # #     timestamps = analysis_result['timestamps']
# # # # # # # # # # # # # #     messages = analysis_result['messages']
# # # # # # # # # # # # # #     response_texts = analysis_result['response_texts']

# # # # # # # # # # # # # #     st.subheader("Analysis Results:")
    
# # # # # # # # # # # # # #     for i in range(len(timestamps)):
# # # # # # # # # # # # # #         st.text_area("Timestamp", value=timestamps[i], height=100, key=f"timestamp_{i}")
# # # # # # # # # # # # # #         st.text_area("Log Message", value=messages[i], height=100, key=f"message_{i}")
# # # # # # # # # # # # # #         st.text_area("Response", value=response_texts[i], height=400, key=f"response_{i}")

# # # # # # # # # # # # # def display_chat(analysis_result):
# # # # # # # # # # # # #     timestamps = analysis_result['timestamps']
# # # # # # # # # # # # #     messages = analysis_result['messages']
# # # # # # # # # # # # #     response_texts = analysis_result['response_texts']

# # # # # # # # # # # # #     st.subheader("Analysis Results:")
    
# # # # # # # # # # # # #     for i in range(len(timestamps)):
# # # # # # # # # # # # #         st.markdown('---')
# # # # # # # # # # # # #         st.write(f"**Timestamp:** {timestamps[i]}")
# # # # # # # # # # # # #         st.write(f"**Log Message:** {messages[i]}")
# # # # # # # # # # # # #         st.markdown('**Analysis Result:**')
# # # # # # # # # # # # #         st.write(response_texts[i])
# # # # # # # # # # # # #         st.markdown('---')

# # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # #     main()
# # # # # # # # # # # # import streamlit as st
# # # # # # # # # # # # import requests

# # # # # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # # # # Streamlit UI
# # # # # # # # # # # # def main():
# # # # # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # # # # #     # File Upload
# # # # # # # # # # # #     uploaded_file = st.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])

# # # # # # # # # # # #     # Prompt Input
# # # # # # # # # # # #     prompt = st.text_input("Enter prompt for analysis")

# # # # # # # # # # # #     # Analyze Button
# # # # # # # # # # # #     if st.button("Analyze"):
# # # # # # # # # # # #         if uploaded_file is not None:
# # # # # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # # # #                 # Display analysis results
# # # # # # # # # # # #                 analysis_result = response.json()
# # # # # # # # # # # #                 display_analysis_results(analysis_result)
# # # # # # # # # # # #             else:
# # # # # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # # # # def display_analysis_results(analysis_result):
# # # # # # # # # # # #     st.subheader("Analysis Results:")

# # # # # # # # # # # #     # Create a container for the analysis results
# # # # # # # # # # # #     result_container = st.container()

# # # # # # # # # # # #     with result_container:
# # # # # # # # # # # #         # Display each analysis result in a professional format
# # # # # # # # # # # #         for i, (timestamp, message, response_text) in enumerate(zip(analysis_result['timestamps'], analysis_result['messages'], analysis_result['response_texts'])):
# # # # # # # # # # # #             st.markdown(f"### Analysis Result {i+1}")
# # # # # # # # # # # #             st.write(f"**Timestamp:** {timestamp}")
# # # # # # # # # # # #             st.write(f"**Log Message:** {message}")
# # # # # # # # # # # #             st.markdown("---")
# # # # # # # # # # # #             st.write(response_text)
# # # # # # # # # # # #             st.markdown("---")

# # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # #     main()
# # # # # # # # # # # import streamlit as st
# # # # # # # # # # # import requests

# # # # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # # # Streamlit UI
# # # # # # # # # # # def main():
# # # # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # # # #     # Sidebar for file upload and prompt input
# # # # # # # # # # #     st.sidebar.header("Input")
# # # # # # # # # # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # # # # # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # # # # # # # # # #     # Analyze Button
# # # # # # # # # # #     analyze_button = st.sidebar.button("Analyze")

# # # # # # # # # # #     # Display analysis results in the main content area
# # # # # # # # # # #     if analyze_button:
# # # # # # # # # # #         if uploaded_file is not None:
# # # # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # # #                 # Display analysis results
# # # # # # # # # # #                 analysis_result = response.json()
# # # # # # # # # # #                 display_analysis_results(analysis_result)
# # # # # # # # # # #             else:
# # # # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # # # def display_analysis_results(analysis_result):
# # # # # # # # # # #     st.subheader("Analysis Results:")

# # # # # # # # # # #     # Display each analysis result in a professional format
# # # # # # # # # # #     for i, (timestamp, message, response_text) in enumerate(zip(analysis_result['timestamps'], analysis_result['messages'], analysis_result['response_texts'])):
# # # # # # # # # # #         st.markdown(f"### Analysis Result {i+1}")
# # # # # # # # # # #         st.write(f"**Timestamp:** {timestamp}")
# # # # # # # # # # #         st.write(f"**Log Message:** {message}")
# # # # # # # # # # #         st.markdown("---")
# # # # # # # # # # #         st.write(response_text)
# # # # # # # # # # #         st.markdown("---")

# # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # #     main()
# # # # # # # # # # import streamlit as st
# # # # # # # # # # import requests

# # # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # # Streamlit UI
# # # # # # # # # # def main():
# # # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # # #     # Sidebar for file upload and prompt input
# # # # # # # # # #     st.sidebar.header("Input")
# # # # # # # # # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # # # # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # # # # # # # # #     # Analyze Button
# # # # # # # # # #     analyze_button = st.sidebar.button("Analyze")

# # # # # # # # # #     # Display analysis results in the main content area
# # # # # # # # # #     if analyze_button:
# # # # # # # # # #         if uploaded_file is not None:
# # # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # # #             if response.status_code == 200:
# # # # # # # # # #                 # Display analysis results
# # # # # # # # # #                 analysis_result = response.json()
# # # # # # # # # #                 display_analysis_results(analysis_result)
# # # # # # # # # #             else:
# # # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # # def display_analysis_results(analysis_result):
    
# # # # # # # # # #     # Display bar chart for error counts
# # # # # # # # # #     error_list = analysis_result.get('error_list', [])
# # # # # # # # # #     count_list = analysis_result.get('count_list', [])
# # # # # # # # # #     if error_list and count_list:
# # # # # # # # # #         st.subheader("Error Counts")
# # # # # # # # # #         st.bar_chart(dict(zip(error_list, count_list)))
# # # # # # # # # #     # Display each analysis result in a professional format
# # # # # # # # # #     st.subheader("Analysis Results:")
# # # # # # # # # #     for i, (timestamp, message, response_text) in enumerate(zip(analysis_result['timestamps'], analysis_result['messages'], analysis_result['response_texts'])):
# # # # # # # # # #         st.markdown(f"### Error Result {i+1}")
# # # # # # # # # #         st.write(f"**Timestamp:** {timestamp}")
# # # # # # # # # #         st.write(f"**Log Message:** {message}")
# # # # # # # # # #         st.markdown("---")
# # # # # # # # # #         st.write(response_text)
# # # # # # # # # #         st.markdown("---")

# # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # #     main()
# # # # # # # # # import streamlit as st
# # # # # # # # # import requests
# # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # import seaborn as sns

# # # # # # # # # # Define the Flask API endpoint
# # # # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # # # Streamlit UI
# # # # # # # # # def main():
# # # # # # # # #     st.title("Log Analyzer")

# # # # # # # # #     # Sidebar for file upload and prompt input
# # # # # # # # #     st.sidebar.header("Input")
# # # # # # # # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # # # # # # # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # # # # # # # #     # Analyze Button
# # # # # # # # #     analyze_button = st.sidebar.button("Analyze")

# # # # # # # # #     # Display analysis results in the main content area
# # # # # # # # #     if analyze_button:
# # # # # # # # #         if uploaded_file is not None:
# # # # # # # # #             # Send file and prompt to Flask API
# # # # # # # # #             files = {'file': uploaded_file}
# # # # # # # # #             data = {'prompt': prompt}
# # # # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # # # #             if response.status_code == 200:
# # # # # # # # #                 # Display analysis results
# # # # # # # # #                 analysis_result = response.json()
# # # # # # # # #                 display_analysis_results(analysis_result)
# # # # # # # # #             else:
# # # # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # # # def display_analysis_results(analysis_result):
    
# # # # # # # # #     # Extract error list and count list
# # # # # # # # #     error_list = analysis_result.get('error_list', [])
# # # # # # # # #     count_list = analysis_result.get('count_list', [])
    
# # # # # # # # #     # Create a color palette based on the length of error types
# # # # # # # # #     colors = sns.color_palette("hsv", len(error_list))
    
# # # # # # # # #     if error_list and count_list:
# # # # # # # # #         st.subheader("Error Counts")
# # # # # # # # #         # Plot bar chart with custom colors
# # # # # # # # #         plt.figure(figsize=(10, 6))
# # # # # # # # #         ax = sns.barplot(x=count_list, y=error_list, palette=colors)
# # # # # # # # #         st.pyplot(plt.gcf())  # Passing the current figure explicitly
    
# # # # # # # # #     # Display each analysis result in a professional format
# # # # # # # # #     st.subheader("Analysis Results:")
# # # # # # # # #     for i, (timestamp, message, response_text) in enumerate(zip(analysis_result['timestamps'], analysis_result['messages'], analysis_result['response_texts'])):
# # # # # # # # #         st.markdown(f"### Error Result {i+1}")
# # # # # # # # #         st.write(f"**Timestamp:** {timestamp}")
# # # # # # # # #         st.write(f"**Log Message:** {message}")
# # # # # # # # #         st.markdown("---")
# # # # # # # # #         st.write(response_text)
# # # # # # # # #         st.markdown("---")

# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     main()
# # # # # # # import streamlit as st
# # # # # # # import requests
# # # # # # # import altair as alt
# # # # # # # import pandas as pd
# # # # # # # import seaborn as sns

# # # # # # # # Define the Flask API endpoint
# # # # # # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # # # # # Streamlit UI
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
# # # # # # #             # Send file and prompt to Flask API
# # # # # # #             files = {'file': uploaded_file}
# # # # # # #             data = {'prompt': prompt}
# # # # # # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # # # # # #             if response.status_code == 200:
# # # # # # #                 # Display analysis results
# # # # # # #                 analysis_result = response.json()
# # # # # # #                 display_analysis_results(analysis_result)
# # # # # # #             else:
# # # # # # #                 st.error("Error analyzing file. Please try again.")

# # # # # # # def display_analysis_results(analysis_result):
# # # # # # #     # Extract error list and count list
# # # # # # #     error_list = analysis_result.get('error_list', [])
# # # # # # #     count_list = analysis_result.get('count_list', [])

# # # # # # #     # Create a DataFrame for Altair
# # # # # # #     df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list})

# # # # # # #     # Create a color palette based on the length of error types
# # # # # # #     palette = sns.color_palette("hsv", len(error_list)).as_hex()

# # # # # # #     if error_list and count_list:
# # # # # # #         st.subheader("Error Counts")
# # # # # # #         # Create Altair chart with tooltips
# # # # # # #         chart = alt.Chart(df).mark_bar().encode(
# # # # # # #             x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # # # # # #             y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # # # # # #             color=alt.Color('Error Type', scale=alt.Scale(range=palette), legend=None),
# # # # # # #             tooltip=['Error Type', 'Error Count']
# # # # # # #         ).properties(
# # # # # # #             width=600,
# # # # # # #             height=400
# # # # # # #         )
# # # # # # #         st.altair_chart(chart, use_container_width=True)

# # # # # # #     # Display each analysis result in a professional format
# # # # # # #     st.subheader("Analysis Results:")
# # # # # # #     for i, (timestamp, message, response_text) in enumerate(zip(analysis_result['timestamps'], analysis_result['messages'], analysis_result['response_texts'])):
# # # # # # #         st.markdown(f"### Error Result {i+1}")
# # # # # # #         st.write(f"**Timestamp:** {timestamp}")
# # # # # # #         st.write(f"**Log Message:** {message}")
# # # # # # #         st.markdown("---")
# # # # # # #         st.write(response_text)
# # # # # # #         st.markdown("---")

# # # # # # # if __name__ == "__main__":
# # # # # # #     main()

# # # import streamlit as st
# # # import requests
# # # import altair as alt
# # # import pandas as pd

# # # # Define the Flask API endpoint
# # # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # # # Streamlit UI
# # # def main():
# # #     st.title("Log Analyzer")

# # #     # Sidebar for file upload and prompt input
# # #     st.sidebar.header("Input")
# # #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# # #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# # #     # Analyze Button
# # #     analyze_button = st.sidebar.button("Analyze")

# # #     # Display analysis results in the main content area
# # #     if analyze_button:
# # #         if uploaded_file is not None:
# # #             # Send file and prompt to Flask API
# # #             files = {'file': uploaded_file}
# # #             data = {'prompt': prompt}
# # #             response = requests.post(API_ENDPOINT, files=files, data=data)

# # #             if response.status_code == 200:
# # #                 # Display analysis results
# # #                 analysis_result = response.json()
# # #                 display_analysis_results(analysis_result)
# # #             else:
# # #                 st.error("Error analyzing file. Please try again.")

# # # def display_analysis_results(analysis_result):
# # #     # Extract error list and count list
# # #     error_list = analysis_result.get('error_list', [])
# # #     count_list = analysis_result.get('count_list', [])
# # #     timestamps_list = analysis_result.get('timestamps', [])
# # #     log_messages_list = analysis_result.get('messages', [])

# # #     # Create a DataFrame for Altair
# # #     df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list, 'Timestamp': timestamps_list, 'Log Message': log_messages_list})

# # #     if error_list and count_list:
# # #         st.subheader("Error Counts")
# # #         # Create Altair chart with tooltips
# # #         chart = alt.Chart(df).mark_bar().encode(
# # #             x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# # #             y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# # #             color=alt.Color('Error Type', scale=alt.Scale(scheme='category10'), legend=None),
# # #             tooltip=['Error Type', 'Error Count']
# # #         ).properties(
# # #             width=600,
# # #             height=400
# # #         )
# # #         st.altair_chart(chart, use_container_width=True)

# # #         # Display table with error details
# # #         st.subheader("Error Details")
# # #         selected_error_type = st.table(df[['Error Type', 'Error Count']].sort_values(by='Error Count', ascending=False))

# # #         # Handle click events on error type
# # #         selected_error_type_value = st.selectbox("Select Error Type", df['Error Type'])
# # #         if st.button("Show Details"):
# # #             selected_error_type_df = df[df['Error Type'] == selected_error_type_value]
# # #             if not selected_error_type_df.empty:
# # #                 for i, (timestamp, log_message) in enumerate(zip(selected_error_type_df['Timestamp'], selected_error_type_df['Log Message'])):
# # #                     with st.expander(f"Error Result {i+1}"):
# # #                         st.write(f"**Timestamp:** {timestamp}")
# # #                         st.write(f"**Log Message:** {log_message}")
# # #             else:
# # #                 st.write("No details found for the selected error type.")


# # # if __name__ == "__main__":
# # #     main()  







# # # # # import streamlit as st

# # # # # log_data = [
# # # # #     {
# # # # #         "key": "Database Connection Failed",
# # # # #         "values": [
# # # # #             {
# # # # #                 "value": "assistant\n\nAnother log line to analyze!\n\nHere's the error message:\n\n`2024-04-04 10:30:05 ERROR: Database connection failed`\n\nLet's break it down:\n\n* `ERROR`: This is the severity of the log message. It indicates that something went wrong.\n* `Database connection failed`: This is the specific error message. It's telling us that the software application was unable to connect to the database.\n\nWhat does this mean? In simple terms, the software application is unable to communicate with the database it needs to store or retrieve data. This could be due to various reasons such as:\n\n* The database is not running or is not reachable.\n* The database connection settings (e.g., username, password, hostname) are incorrect.\n* The network connection between the software application and the database is not stable or is down.\n\nSteps to resolve this error:\n\n1. **Check the database status**: Ensure the database is running and accessible. You can do this by checking the database's logs, status pages, or by running a simple query to verify its connectivity.\n2. **Verify database connection settings**: Double-check the database connection settings in the software application's configuration files or settings. Ensure that the username, password, hostname, and port are correct and match the database's configuration.\n3. **Check network connectivity**: Verify that the network connection between the software application and the database is stable and working correctly. You can try pinging the database's hostname or IP address to ensure connectivity.\n4. **Consult the software application's documentation**: If you're still having trouble, refer to the software application's documentation or support resources for specific guidance on resolving database connection issues.\n\nBy following these steps, you should be able to identify and resolve the issue preventing the software application from connecting to the database.",
# # # # #                 "timestamp": "2024-04-04 10:30:05",
# # # # #                 "log_message": "ERROR: Database connection failed"
# # # # #             }
# # # # #         ]
# # # # #     },
# # # # #     {
# # # # #         "key": "Server overload detected",
# # # # #         "values": [
# # # # #             {
# # # # #                 "value": "assistant\n\nLog Line: 2024-04-04 10:35:20 ERROR: Server overload detected\n\nError: Server Overload Detected\n\nDescription: This error indicates that the server is experiencing a high level of traffic or activity, which is causing it to slow down or become unresponsive. This can occur when there are too many users accessing the server simultaneously, or when there are resource-intensive processes running on the server.\n\nImplications:\n\n* The server may become slow or unresponsive, leading to a poor user experience.\n* Data may not be processed or stored correctly, resulting in errors or inconsistencies.\n* The server may even crash or become unavailable, causing downtime and potential data loss.\n\nSteps to Resolve:\n\n1. **Check Server Load**: Use tools like top, vmstat, or sysctl to monitor the server's load. Identify the processes or services consuming the most resources and take steps to optimize or reduce their usage.\n2. **Scale Up the Server**: If the server is underpowered, consider upgrading the hardware or adding more resources (e.g., increasing RAM, CPU, or disk space).\n3. **Optimize Server Configuration**: Review the server's configuration to ensure it is optimized for the current workload. Adjust settings like memory allocation, CPU affinity, and disk I/O priorities as needed.\n4. **Implement Load Balancing**: Consider implementing load balancing techniques, such as round-robin DNS or a load balancer appliance, to distribute traffic across multiple servers.\n5. **Monitor and Analyze Server Logs**: Regularly review server logs to identify trends and patterns that may indicate potential issues before they become critical.\n6. **Upgrade Server Software**: Ensure the server's operating system and software are up-to-date, as newer versions often include performance optimizations and bug fixes.\n\nBy taking these steps, you can help prevent or mitigate server overload and ensure a smoother user experience.",
# # # # #                 "timestamp": "2024-04-04 10:35:20",
# # # # #                 "log_message": "ERROR: Server overload detected"
# # # # #             }
# # # # #         ]
# # # # #     }
# # # # # ]

# # # # # def main():
# # # # #     st.title("Log Analyzer")

# # # # #     # Display selectbox to choose log keys
# # # # #     selected_key = st.selectbox("Select Log Key", [data['key'] for data in log_data])

# # # # #     # Display the corresponding value for the selected key
# # # # #     for data in log_data:
# # # # #         if data['key'] == selected_key:
# # # # #             st.subheader("Log Value")
# # # # #             st.text(data['values'][0]['value'])  # Assuming only one value for simplicity

# # # # # if __name__ == "__main__":
# # # # #     main()


# # import streamlit as st
# # import requests
# # import pandas as pd
# # import altair as alt

# # # Define the Flask API endpoint
# # API_ENDPOINT = "http://localhost:5000/api/analyze"

# # @st.cache
# # def get_analysis_results(file, prompt):
# #     # Send file and prompt to Flask API
# #     files = {'file': file}
# #     data = {'prompt': prompt}
# #     response = requests.post(API_ENDPOINT, files=files, data=data)

# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         return None

# # def main():
# #     st.title("Log Analyzer")

# #     # Sidebar for file upload and prompt input
# #     st.sidebar.header("Input")
# #     uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
# #     prompt = st.sidebar.text_input("Enter prompt for analysis")

# #     # Analyze Button
# #     analyze_button = st.sidebar.button("Analyze")

# #     # Display analysis results in the main content area
# #     if analyze_button:
# #         if uploaded_file is not None:
# #             analysis_result = get_analysis_results(uploaded_file, prompt)
# #             if analysis_result:
# #                 display_analysis_results(analysis_result)
# #             else:
# #                 st.error("Error analyzing file. Please try again.")

# # def display_analysis_results(analysis_result):
# #     # Extract error list and count list
# #     error_list = analysis_result.get('error_list', [])
# #     count_list = analysis_result.get('count_list', [])
# #     timestamps_list = analysis_result.get('timestamps', [])
# #     log_messages_list = analysis_result.get('messages', [])
# #     log_data = analysis_result.get('results_json', [])

# #     # Create a DataFrame for Altair
# #     df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list, 'Timestamp': timestamps_list, 'Log Message': log_messages_list})

# #     if error_list and count_list:
# #         st.subheader("Error Counts")
# #         # Create Altair chart with tooltips
# #         chart = alt.Chart(df).mark_bar().encode(
# #             x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
# #             y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
# #             color=alt.Color('Error Type', scale=alt.Scale(scheme='category10'), legend=None),
# #             tooltip=['Error Type', 'Error Count']
# #         ).properties(
# #             width=600,
# #             height=400
# #         )
# #         st.altair_chart(chart, use_container_width=True)

# #         # Display table with error details
# #         st.subheader("Error Details")
# #         selected_error_type = st.selectbox("Select Error Type", df['Error Type'], index=0)  # Default to the first error type

# #         # Find the corresponding log value for the selected error type
# #         selected_log_value = None
# #         for data in log_data:
# #             if data['key'] == selected_error_type:
# #                 selected_log_value = data['values'][0]['value']  # Assuming only one value for simplicity

# #         if selected_log_value:
# #             st.subheader("Log Value")
# #             st.text(selected_log_value)
# #         else:
# #             st.write("No log value found for the selected error type.")
        

# # if __name__ == "__main__":
# #     main()

import streamlit as st
import requests
import pandas as pd
import altair as alt

# Define the Flask API endpoint
API_ENDPOINT = "http://localhost:5000/api/analyze"

@st.cache_data(show_spinner=False)
def get_analysis_results(file, prompt):
    # Send file and prompt to Flask API
    files = {'file': file}
    data = {'prompt': prompt}
    response = requests.post(API_ENDPOINT, files=files, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title("Log Analyzer")

    # Sidebar for file upload and prompt input
    st.sidebar.header("Input")
    uploaded_file = st.sidebar.file_uploader("Upload log file", type=['csv', 'json', 'xml', 'txt', 'log'])
    prompt = st.sidebar.text_input("Enter prompt for analysis")

    # Analyze Button
    analyze_button = st.sidebar.button("Analyze")

    # Display analysis results in the main content area
    if analyze_button:
        if uploaded_file is not None:
            analysis_result = get_analysis_results(uploaded_file, prompt)
            if analysis_result:
                display_analysis_results(analysis_result)
            else:
                st.error("Error analyzing file. Please try again.")

def display_analysis_results(analysis_result):
    # Extract error list and count list
    error_list = analysis_result.get('error_list', [])
    count_list = analysis_result.get('count_list', [])
    timestamps_list = analysis_result.get('timestamps', [])
    log_messages_list = analysis_result.get('messages', [])
    log_data = analysis_result.get('results_json', [])
    print(log_data)

    # Create a DataFrame for Altair
    df = pd.DataFrame({'Error Type': error_list, 'Error Count': count_list, 'Timestamp': timestamps_list, 'Log Message': log_messages_list})

    if error_list and count_list:
        st.subheader("Error Counts")
        # Create Altair chart with tooltips
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('Error Type', axis=alt.Axis(title='Error Type')),
            y=alt.Y('Error Count', axis=alt.Axis(title='Error Count')),
            color=alt.Color('Error Type', scale=alt.Scale(scheme='category10'), legend=None),
            tooltip=['Error Type', 'Error Count']
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart, use_container_width=True)
        for data in log_data:
            print(type(data))
            with st.expander(data['key'], expanded=False):
                for value in data['values']:
                    st.subheader('Log Values:')
                    st.write('Timestamp:', value['timestamp'])
                    st.write('Log Message:', value['log_message'])
                    st.write('Value:', value['value'])


if __name__ == "__main__":
    main()


# import streamlit as st

# # Mock data
# log_data = [
#     {
#         'key': 'Database Connection Failed',
#         'values': [
#             {
#                 'log_message': 'ERROR: Database connection failed',
#                 'timestamp': '2024-04-04 10:30:05',
#                 'value': "assistant\n\nAnother log line to analyze!\n\nHere's the error message:\n\n`2024-04-04 10:30:05 ERROR: Database connection failed`\n\nLet's break it down:\n\n* `ERROR`: This is the severity of the log message. It indicates that something went wrong.\n* `Database connection failed`: This is the specific error message. It's telling us that the software application was unable to connect to the database.\n\nWhat does this mean? In simple terms, the software application is unable to communicate with the database it needs to store or retrieve data. This could be due to various reasons such as:\n\n* The database is not running or is not reachable.\n* The database connection settings (e.g., username, password, hostname) are incorrect.\n* The network connection between the software application and the database is not stable or is down.\n\nSteps to resolve this error:\n\n1. **Check the database status**: Ensure the database is running and accessible. You can do this by checking the database's logs, status pages, or by running a simple query to verify its connectivity.\n2. **Verify database connection settings**: Double-check the database connection settings in the software application's configuration files or settings. Ensure that the username, password, hostname, and port are correct and match the database's configuration.\n3. **Check network connectivity**: Verify that the network connection between the software application and the database is stable and working correctly. You can try pinging the database's hostname or IP address to ensure connectivity.\n4. **Consult the software application's documentation**: If you're still having trouble, refer to the software application's documentation or support resources for specific guidance on resolving database connection issues.\n\nBy following these steps, you should be able to identify and resolve the issue preventing the software application from connecting to the database."
#             }
#         ]
#     },
#     {
#         'key': 'Server overload detected',
#         'values': [
#             {
#                 'log_message': 'ERROR: Server overload detected',
#                 'timestamp': '2024-04-04 10:35:20',
#                 'value': "assistant\n\nLog Line: 2024-04-04 10:35:20 ERROR: Server overload detected\n\nError: Server Overload Detected\n\nDescription: This error indicates that the server is experiencing a high level of traffic or activity, which is causing it to slow down or become unresponsive. This can occur when there are too many users accessing the server simultaneously, or when there are resource-intensive processes running on the server.\n\nImplications:\n\n* The server may become slow or unresponsive, leading to a poor user experience.\n* Data may not be processed or stored correctly, resulting in errors or inconsistencies.\n* The server may even crash or become unavailable, causing downtime and potential data loss.\n\nSteps to Resolve:\n\n1. **Check Server Load**: Use tools like top, vmstat, or sysctl to monitor the server's load. Identify the processes or services consuming the most resources and take steps to optimize or reduce their usage.\n2. **Scale Up the Server**: If the server is underpowered, consider upgrading the hardware or adding more resources (e.g., increasing RAM, CPU, or disk space).\n3. **Optimize Server Configuration**: Review the server's configuration to ensure it is optimized for the current workload. Adjust settings like memory allocation, CPU affinity, and disk I/O priorities as needed.\n4. **Implement Load Balancing**: Consider implementing load balancing techniques, such as round-robin DNS or a load balancer appliance, to distribute traffic across multiple servers.\n5. **Monitor and Analyze Server Logs**: Regularly review server logs to identify trends and patterns that may indicate potential issues before they become critical.\n6. **Upgrade Server Software**: Ensure the server's operating system and software are up-to-date, as newer versions often include performance optimizations and bug fixes.\n\nBy taking these steps, you can help prevent or mitigate server overload and ensure a smoother user experience."
#             }
#         ]
#     }
# ]

# # Streamlit app
# st.title('Error Log Analyzer')

# # Iterate through each key-value pair and create dropdowns
# for data in log_data:
#     with st.expander(data['key'], expanded=False):
#         for value in data['values']:
#             st.subheader('Log Values:')
#             st.write('Timestamp:', value['timestamp'])
#             st.write('Log Message:', value['log_message'])
#             st.write('Value:', value['value'])



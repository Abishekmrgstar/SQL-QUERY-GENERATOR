# SQL Query Generator

This project is a web application built with Streamlit that generates SQL queries based on user input and the columns of an uploaded CSV file. It uses Google's Generative AI (Gemini) to create the SQL queries.

## Overview

- Upload a CSV file to the application.
- Enter a text query to describe the desired SQL operation.
- The application generates a SQL query based on the input and the structure of the uploaded CSV file.

## Features

- Easy CSV file upload.
- Instant SQL query generation using Google's Generative AI.
- Clean and user-friendly interface built with Streamlit.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Google Generative AI SDK
- SQLite3 (optional, used for data storage and querying)

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required packages:
    ```bash
    pip install streamlit pandas google-generative-ai sqlite3
    ```

3. Configure your Google Gemini API key:
    - Open the `sql_query_generator.py` file.
    - Replace `"ADD YOUR GEMINI API KEY"` with your actual Gemini API key:
      ```python
      GOOGLE_API_KEY = "your_actual_gemini_api_key_here"
      ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run sql_query_generator.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload your CSV file and enter your query in the text input box.

4. Click the "GENERATE SQL Query" button to generate the SQL query based on your input.

## Example

1. **Upload CSV File**:
    - Upload a file named `data.csv` with columns `name`, `age`, `city`.

2. **Enter Query**:
    - Example query: "Select all columns where age is greater than 25."

3. **Generated SQL Query**:
    ```sql
    SELECT * FROM data WHERE age > 25;
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Abishekmrgstar/SQL-QUERY-GENERATOR/blob/main/LICENSE) file for details.

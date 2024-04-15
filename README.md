PDF Generator Application
Overview

This application generates PDF documents based on user input and data stored in a SQLite database. It provides two main functionalities:

    User Input PDF Generation: Allows users to input their information, which is then displayed in a PDF document using HTML templates.
    SQL-Based PDF Generation: Utilizes a SQLite database to store and access data. Users can retrieve various information from the database, such as monthly sales, which is visualized using Plotly graphs and then saved as PDF documents.

Components
1. User Input PDF Generation

    pdf_generator.py: Python script responsible for generating PDF documents based on user input.
    template.html: HTML template used to format the PDF document.

2. SQL-Based PDF Generation

    database.py: Python script for creating a SQLite database with randomly generated data.
    sales_report.py: Python script for querying the SQLite database to retrieve information, visualizing it using Plotly, and generating PDF documents.
    template.html: HTML template used for formatting PDF documents.

Requirements

    Python 3.x
    Required Python packages: sqlite3, pandas, plotly, fpdf
    Internet connection (for Plotly visualization)

Installation

    pip install -r requirements.txt


Usage
User Input PDF Generation

    Run the pdf_generator.py script.
    Follow the prompts to input your information.
    Once completed, the PDF document will be generated in the output directory.

SQL-Based PDF Generation

    Run the database.py script to create the SQLite database with random data.
    Run the sales_report.py script.
    The script will query the database for information, visualize it using Plotly, and save the resulting PDF document in the output directory.

Directory Structure

    pdf_generator: Contains files related to user input PDF generation.
    SQL_and_Pandas: Contains files related to SQL-based PDF generation.

Contributors

    [Your Name or Organization]

License

This project is licensed under the [License Name] License - see the LICENSE.md file for details.
Acknowledgements

    Mention any acknowledgements or credits for external resources used in the project.


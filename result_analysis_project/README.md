# College Student Result Analysis Web Application

This project is a web-based result analysis tool built using Python and Flask. It allows users to upload a marksheet in CSV format and generate a detailed result analysis report for college students. The report includes pass/fail counts, subject-wise analysis, graphical representations, and a final downloadable A4-sized Word document report.

The web application is designed to handle multiple exams such as CIE1, CIE2, and the Model Examination, each with different passing criteria.

## Features

- **Input**: User can enter the department, year of study, section, exam type, and upload a CSV file containing student marks.
- **Pass/Fail Calculation**: Determines pass/fail counts based on the selected exam type (CIE1, CIE2, or Model Examination).
- **Graphical Representations**: Generates bar charts for subject-wise pass and fail counts.
- **Report Generation**: Outputs a detailed result analysis in the form of a downloadable Word document.
- **Dark-Themed UI**: A modern, dark-themed user interface for a better user experience.

## Tech Stack

- **Frontend**: HTML, CSS (via Bootstrap with Darkly theme)
- **Backend**: Python with Flask framework
- **Data Processing**: Pandas for CSV handling and analysis
- **Document Generation**: Python-docx to create Word documents
- **Graphing/Visualization**: Matplotlib for generating bar charts
- **Hosting**: Localhost, accessible over the same network

## Project Structure

├── app.py                 # Main Flask application
├── templates
│   └── index.html         # Frontend HTML form for uploading the CSV and entering data
├── static                 # For additional static files (like CSS)
├── result_analysis_report.docx # Generated output (not included in repo)
├── requirements.txt       # Python dependencies
└── README.md              # This readme file

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- Pandas
- Matplotlib
- Python-docx

### Installation Steps

1. **Clone the Repository**:

```bash
git clone https://github.com/your-repo/college-result-analysis.git
cd college-result-analysis```

2. **Install Dependencies**: You can install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt```

3. **Run the Flask Application**: Start the Flask web server:

```bash
python app.py```

4. **Access the Web App**: Open your browser and go to:

Local access: ```http://localhost:5000/```
Network access (if using the same network): ```http://0.0.0.0:5000/```

## Working

### Input:
- **Department**: The department of the students (e.g., "CSE").
- **Year of Study**: The current year (e.g., "Third Year").
- **Section**: The class section (e.g., "A").
- **Exam Type**: The type of exam (CIE1, CIE2, or Model Examination).
- **Marksheet**: A CSV file containing students' marks in subjects: Java, Python, TOC, DS, CN.

### Processing:
- The CSV file is processed, and pass/fail counts are calculated based on whether the students score above 50% in all subjects.
- The application then analyzes the marks for each subject and calculates the number of students who passed/failed.

### Output:
- A downloadable A4 Word document report is generated, which contains:
	- College details (name, department, year of study, section, exam type).
	- A table of pass/fail statistics:
		- Total number of students.
		- Number of students who passed all subjects.
		- Number of students who failed.
		- Total pass percentage.
	- Graphical representations (bar charts) for subject-wise analysis.
	- Summary of failures (one subject, two subjects, more than two subjects).





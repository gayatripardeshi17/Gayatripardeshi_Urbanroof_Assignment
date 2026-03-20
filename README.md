AI DDR Report Generator
Project Overview

This project is an AI-based system that reads inspection and thermal reports (PDF files) and generates a structured Detailed Diagnostic Report (DDR).

The goal is to convert raw site inspection data into a clear, client-friendly report.

== How It Works

PDF Extraction

Extracts text and images from inspection and thermal reports using PyMuPDF

Data Processing

Combines both reports

Removes duplicate or unnecessary content

Report Generation

Converts processed data into a structured DDR format

Includes:

Property Issue Summary

Area-wise Observations

Root Cause

Severity

Recommendations

--  Project Structure
AI_Report_generator/
│── main.py
│── extractor.py
│── processor.py
│── report_generator.py
│── input/
│     ├── Sample Report.pdf
│     ├── Thermal Images.pdf
│── output/
│     ├── final_report.txt
│     ├── images/

How to Run

Install dependencies:

pip install PyMuPDF python-dotenv google-genai

Run the project:

python main.py

Output will be generated in:

output/final_report.txt
-- Output

The system generates a structured DDR report with:

Property summary

Area-wise issues

Root cause analysis

Severity level

Recommended actions

-- Limitations

API quota issues may affect AI generation

Image mapping to specific sections is basic

Output depends on input PDF quality

--Future Improvements

Convert output into professional PDF format

Better mapping of images to observations

Use advanced AI models for more accurate analysis

🎥 Loom Video -



 Author
Gayatri Pardeshi
AI Generalist Internship Assignment
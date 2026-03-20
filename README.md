#  AI DDR Report Generator

##  Project Overview
This project is an AI-based system that reads inspection and thermal reports (PDF files) and generates a structured **Detailed Diagnostic Report (DDR)**.

The goal is to convert raw site inspection data into a **clear, client-friendly report**.

---

## ⚙️ How It Works

###  1. PDF Extraction
- Extracts text and images from inspection and thermal reports  
- Uses **PyMuPDF** for efficient data extraction  

###  2. Data Processing
- Combines inspection and thermal data  
- Removes duplicate and unnecessary content  
- Cleans raw extracted data  

###  3. Report Generation
- Converts processed data into a structured DDR format  
- Generates a **client-friendly report** with:

  - Property Issue Summary  
  - Area-wise Observations  
  - Probable Root Cause  
  - Severity Assessment  
  - Recommended Actions  

---

##  Project Structure
AI_Report_generator/
│── main.py
│── extractor.py
│── processor.py
│── report_generator.py
│── input/
│ ├── Sample Report.pdf
│ ├── Thermal Images.pdf
│── output/
│ ├── final_report.txt
│ ├── images/
│── README.md



---

##  How to Run

### 1. Install dependencies
```bash
pip install PyMuPDF python-dotenv google-genai
2. Run the project
python main.py
3. Output location
output/final_report.txt

Output

The system generates a structured DDR report including:

Property summary

Area-wise observations

Root cause analysis

Severity level

Recommended actions

## Limitations

API quota limitations may affect AI-based generation

Image-to-section mapping is basic

Output quality depends on input PDF structure

 ## Future Improvements

Generate professional PDF reports with images

Improve image-to-observation mapping

Use advanced AI models for better accuracy

 ## Loom Video

 [Paste your Loom video link here]

## Author

Gayatri Pardeshi
AI Generalist Internship Assignment

import os
from extractor import extract_text_and_images
from processor import process_data
from report_generator import generate_report

# Paths
inspection_pdf = r"C:\Users\91940\OneDrive\Desktop\asssigmnt\AI_Report_generator\input\Sample Report.pdf"
thermal_pdf = r"C:\Users\91940\OneDrive\Desktop\asssigmnt\AI_Report_generator\input\Thermal Images.pdf"

image_output_dir = "output/images"

# Step 1: Extract
print("Extracting inspection report...")
inspection_text, inspection_images = extract_text_and_images(inspection_pdf, image_output_dir)

print("Extracting thermal report...")
thermal_text, thermal_images = extract_text_and_images(thermal_pdf, image_output_dir)

# Combine image paths
all_images = inspection_images + thermal_images

# Step 2: Process
print("Processing data...")
cleaned_text = process_data(inspection_text, thermal_text)

# Step 3: Generate Report
print("Generating DDR report...")
report = generate_report(cleaned_text, all_images)

# Step 4: Save Output
output_file = "output/final_report.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Report generated successfully!")
print(f"Saved at: {output_file}")
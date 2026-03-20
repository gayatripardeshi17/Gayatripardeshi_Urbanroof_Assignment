def process_data(inspection_text, thermal_text):
    
    # Basic merge
    combined_text = inspection_text + "\n\nTHERMAL DATA:\n" + thermal_text

    # Remove duplicates (simple)
    lines = combined_text.split("\n")
    unique_lines = list(set(lines))
    cleaned_text = "\n".join(unique_lines)

    return cleaned_text
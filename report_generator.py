def generate_report(cleaned_text, image_paths):

    return f"""
================ DDR REPORT ================

1. Property Issue Summary:
The inspection indicates multiple structural and moisture-related concerns observed across the property.

2. Area-wise Observations:
{cleaned_text[:1500]}

3. Probable Root Cause:
- Water seepage due to poor waterproofing
- Structural cracks due to aging or load stress

4. Severity Assessment:
Medium to High — requires timely intervention to prevent further damage.

5. Recommended Actions:
- Waterproof affected areas
- Repair cracks and damaged surfaces
- Conduct structural inspection if needed

6. Additional Notes:
Images extracted from reports support the observations.

7. Missing or Unclear Information:
Not Available

===========================================
"""
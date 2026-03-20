import fitz  # PyMuPDF
import os

def extract_text_and_images(pdf_path, output_image_dir):
    doc = fitz.open(pdf_path)
    full_text = ""

    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)

    image_paths = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        full_text += text + "\n"

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]

            img_name = f"{os.path.basename(pdf_path)}_p{page_num}_{img_index}.{ext}"
            img_path = os.path.join(output_image_dir, img_name)

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_path)

    return full_text, image_paths
import os
import zipfile
from PIL import Image

# Get user input for folders
docx_folder = input("Enter the path to the folder containing DOCX files: ").strip()
output_root = input("Enter the path where extracted images should be saved: ").strip()

# Ensure the output root directory exists
os.makedirs(output_root, exist_ok=True)

def extract_images_from_docx(docx_path, output_path):
    """ Extracts images from a DOCX file and converts them to WebP format. """
    images_found = False  # Flag to track if images exist

    with zipfile.ZipFile(docx_path, 'r') as docx_zip:
        for file in docx_zip.namelist():
            if file.startswith("word/media/"):  # DOCX stores images in "word/media/"
                images_found = True
                image_data = docx_zip.read(file)
                image_filename = os.path.basename(file)

                # Create output directory if not exists
                os.makedirs(output_path, exist_ok=True)

                # Define WebP file name
                webp_filename = os.path.splitext(image_filename)[0] + ".webp"
                webp_path = os.path.join(output_path, webp_filename)

                # Save the original extracted image temporarily
                temp_image_path = os.path.join(output_path, image_filename)
                with open(temp_image_path, "wb") as img_file:
                    img_file.write(image_data)

                # Convert to WebP using PIL
                try:
                    with Image.open(temp_image_path) as img:
                        img.save(webp_path, "WEBP", quality=100, lossless=True)  # Optimize quality
                    os.remove(temp_image_path)  # Remove temporary extracted image
                except Exception as e:
                    print(f"Error converting {image_filename}: {e}")

    return images_found

# Check if the input folder exists
if not os.path.exists(docx_folder):
    print("❌ The specified DOCX folder does not exist. Please check the path.")
    exit(1)

# Process all DOCX files in the folder
docx_files = [f for f in os.listdir(docx_folder) if f.endswith(".docx")]

if not docx_files:
    print("⚠ No DOCX files found in the specified folder.")
    exit(1)

for filename in docx_files:
    docx_path = os.path.join(docx_folder, filename)
    
    # Create an output subfolder named after the document (only if images exist)
    doc_name = os.path.splitext(filename)[0]  # Remove .docx extension
    output_subfolder = os.path.join(output_root, doc_name)

    images_extracted = extract_images_from_docx(docx_path, output_subfolder)

    # Do NOT create empty folders if no images were found
    if not images_extracted and os.path.exists(output_subfolder):
        os.rmdir(output_subfolder)  # Remove empty directory
        print(f"ℹ No images found in '{filename}', skipping folder creation.")

print("✅ Image extraction and conversion completed successfully!")

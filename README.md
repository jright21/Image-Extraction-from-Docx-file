# 📄 Extract & Convert Images from DOCX to WebP

This script extracts images from `.docx` files and converts them to **WebP format**, ensuring:
- **No empty folders are created**.
- **Bulk processing** of multiple DOCX files.
- **Optimized image quality** using `Pillow`.

## 🚀 How to Use
1. **Install `Pillow`**.
2. **Run the script** and enter:
   - The **input folder path** (where DOCX files are stored).
   - The **output folder path** (where extracted images should be saved).

## 📂 Output Folder Structure

```
/output_root
 ├── Document1/  (✅ Created if images exist)
 │   ├── image1.webp
 │   ├── image2.webp
 ├── Document2/  (✅ Created if images exist)
 │   ├── image1.webp
 │   ├── image2.webp
(No empty folders are created)
```


## 🛠 Features
✅ **Only creates folders if images exist**  
✅ **Handles 200+ `.docx` files in bulk**  
✅ **Efficient WebP conversion**  

🔗 **Feel free to contribute or suggest improvements!** 

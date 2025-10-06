import fitz
from pathlib import Path
from typing import List

# this is the script to extract the text from the pdfs and save it to the text folder
# the pdfs are in the pdfs folder
# the text is extracted from all pages of each pdf
# the text is saved to the text folder
# the text is saved in the same format as the pdfs with the same name but with a .txt extension

PDF_DIR = Path("pdfs")
TEXT_DIR = Path("text")

def get_pdf_files() -> List[Path]:
    if not PDF_DIR.exists():
        print("pdfs directory not found")
        return []

    pdf_files = list(PDF_DIR.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    return pdf_files

def extract_text_from_pdf(pdf_path: Path) -> str:
    try:
        doc = fitz.open(pdf_path)
        text = ""

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text() + "\n\n"

        doc.close()

        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {pdf_path.name}: {e}")
        return ""

def save_text_to_file(pdf_path: Path, text: str):
    try:
        TEXT_DIR.mkdir(exist_ok=True)

        pdf_name_without_ext = pdf_path.stem
        text_filename = f"{pdf_name_without_ext}.txt"
        text_filepath = TEXT_DIR / text_filename

        with open(text_filepath, 'w', encoding='utf-8') as f:
            f.write(f"Source: {pdf_path.name}\n")
            f.write("=" * 50 + "\n\n")
            f.write(text)

        print(f"Saved text: {text_filename}")
        return True
    except Exception as e:
        print(f"Error saving text for {pdf_path.name}: {e}")
        return False

def extract_text_from_all_pdfs():
    pdf_files = get_pdf_files()

    if not pdf_files:
        print("No PDF files found in pdfs directory")
        return

    print(f"Starting text extraction from {len(pdf_files)} PDFs...")

    for i, pdf_path in enumerate(pdf_files):
        print(f"Processing {i+1}/{len(pdf_files)}: {pdf_path.name}")

        text = extract_text_from_pdf(pdf_path)

        if text:
            success = save_text_to_file(pdf_path, text)
            if success:
                print(f"✓ Extracted {i+1}/{len(pdf_files)}: {pdf_path.name}")
            else:
                print(f"✗ Failed to save {i+1}/{len(pdf_files)}: {pdf_path.name}")
        else:
            print(f"✗ Failed to extract {i+1}/{len(pdf_files)}: {pdf_path.name}")

    print("Text extraction completed!")

def main():
    extract_text_from_all_pdfs()

if __name__ == "__main__":
    main()

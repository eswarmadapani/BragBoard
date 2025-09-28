#!/usr/bin/env python3

import pdfplumber
import sys

def extract_pdf_text(pdf_path):
    """Extract all text from PDF file"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"PDF has {len(pdf.pages)} pages")
            print("=" * 50)
            
            all_text = ""
            for i, page in enumerate(pdf.pages, 1):
                print(f"\n--- PAGE {i} ---")
                page_text = page.extract_text()
                if page_text:
                    print(page_text)
                    all_text += f"\n--- PAGE {i} ---\n{page_text}\n"
                else:
                    print("No text found on this page")
            
            return all_text
            
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "BragBoard.pdf"
    text = extract_pdf_text(pdf_path)
    
    if text:
        # Save to text file
        with open("BragBoard_extracted.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\nText extracted and saved to BragBoard_extracted.txt")
    else:
        print("Failed to extract text from PDF")

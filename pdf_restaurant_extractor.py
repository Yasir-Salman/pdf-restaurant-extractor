#!/usr/bin/env python3
"""
PDF Restaurant Extractor

A tool to extract text from PDF files and identify restaurant names
using pattern matching. Supports both direct text extraction and OCR
for image-based PDFs.

Author: Yasir Salman
License: MIT
"""

import pdfplumber
import pytesseract
from PIL import Image
import io
import re
from pdf2image import convert_from_path
import argparse
import sys
import os


class PDFProcessor:
    """
    A class to process PDF files and extract restaurant information.
    
    This processor can handle both text-based and image-based PDFs,
    using OCR as a fallback when direct text extraction fails.
    """
    
    def __init__(self):
        """Initialize the PDFProcessor with predefined restaurant patterns."""
        self.restaurant_patterns = {
            'burger_lab': [r'burger\s*lab', r'bl\s*restaurant'],
            'kfc': [r'kfc', r'kentucky\s*fried'],
            'mcdonalds': [r'mcdonald', r'mc\s*donald'],
            'pizza_hut': [r'pizza\s*hut'],
            'subway': [r'subway'],
            'dominos': [r'domino', r'dominos'],
            # Add more restaurant patterns as needed
        }

    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text from the PDF
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

            if not text.strip():
                print("No text found with pdfplumber, using OCR...")
                text = self.ocr_pdf(pdf_path)

        except Exception as e:
            print(f"Error processing PDF: {e}")
            raise

        return text

    def ocr_pdf(self, pdf_path):
        """
        Perform OCR on a PDF file when direct text extraction fails.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            str: OCR-extracted text from the PDF
        """
        text = ""
        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                print(f"Processing page {i+1} with OCR...")
                ocr_text = pytesseract.image_to_string(image)
                text += ocr_text + "\n"
        except Exception as e:
            print(f"OCR failed: {e}")
            raise
        return text

    def identify_restaurant(self, text):
        """
        Identify restaurant from extracted text using pattern matching.
        
        Args:
            text (str): Text to search for restaurant patterns
            
        Returns:
            str or None: Restaurant name if found, None otherwise
        """
        if not text:
            return None
            
        text_lower = text.lower()
        for restaurant, patterns in self.restaurant_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    return restaurant
        return None

    def add_restaurant_pattern(self, restaurant_name, patterns):
        """
        Add a new restaurant pattern to the processor.
        
        Args:
            restaurant_name (str): Name of the restaurant
            patterns (list): List of regex patterns to match
        """
        self.restaurant_patterns[restaurant_name] = patterns

    def process_pdf(self, pdf_path, show_preview=True):
        """
        Complete PDF processing pipeline.
        
        Args:
            pdf_path (str): Path to the PDF file
            show_preview (bool): Whether to show text preview
            
        Returns:
            dict: Processing results containing text and identified restaurant
        """
        print(f"Processing PDF: {pdf_path}")
        
        # Extract text
        extracted_text = self.extract_text_from_pdf(pdf_path)
        
        # Identify restaurant
        identified_restaurant = self.identify_restaurant(extracted_text)
        
        # Show preview if requested
        if show_preview:
            print("\n--- Extracted Text Preview ---")
            print(extracted_text[:1000])  # Show first 1000 characters
            if len(extracted_text) > 1000:
                print("... (truncated)")
        
        # Show results
        if identified_restaurant:
            print(f"\n✓ Identified Restaurant: {identified_restaurant}")
        else:
            print("\n✗ No restaurant matched.")
        
        return {
            'text': extracted_text,
            'restaurant': identified_restaurant,
            'success': identified_restaurant is not None
        }


def main():
    """Main function to run the PDF processor from command line."""
    parser = argparse.ArgumentParser(description='Extract restaurant information from PDF files')
    parser.add_argument('pdf_file', help='Path to the PDF file to process')
    parser.add_argument('--no-preview', action='store_true', help='Skip showing text preview')
    
    args = parser.parse_args()
    
    try:
        processor = PDFProcessor()
        result = processor.process_pdf(args.pdf_file, show_preview=not args.no_preview)
        
        # Exit with appropriate code
        sys.exit(0 if result['success'] else 1)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(3)


if __name__ == "__main__":
    main()

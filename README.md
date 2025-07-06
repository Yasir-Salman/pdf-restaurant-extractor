# PDF Restaurant Extractor

A Python tool that extracts text from PDF files and identifies restaurant names using pattern matching. Perfect for processing receipts, delivery documents, or any PDFs containing restaurant information.

## Features

- **Dual Extraction Methods**: Direct text extraction with OCR fallback
- **Pattern Matching**: Flexible regex-based restaurant identification
- **Extensible**: Easy to add new restaurant patterns
- **Command Line Interface**: Simple CLI for batch processing
- **Error Handling**: Robust error handling and informative messages

## Installation

### Prerequisites

The tool requires system dependencies for PDF processing and OCR:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y poppler-utils tesseract-ocr
```

**macOS:**
```bash
brew install poppler tesseract
```

**Windows:**
- Download and install [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
- Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

### Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pdfplumber pytesseract pdf2image Pillow
```

## Usage

### Command Line

```bash
# Basic usage
python pdf_restaurant_extractor.py path/to/your/receipt.pdf

# Skip text preview
python pdf_restaurant_extractor.py path/to/your/receipt.pdf --no-preview
```

### Python Script

```python
from pdf_restaurant_extractor import PDFProcessor

# Initialize processor
processor = PDFProcessor()

# Process a PDF file
result = processor.process_pdf('receipt.pdf')

# Access results
if result['success']:
    print(f"Restaurant: {result['restaurant']}")
    print(f"Extracted text: {result['text'][:100]}...")
else:
    print("No restaurant identified")
```

### Adding Custom Restaurant Patterns

```python
# Add new restaurant patterns
processor.add_restaurant_pattern('taco_bell', [
    r'taco\s*bell',
    r'tb\s*restaurant'
])

# Or modify patterns directly
processor.restaurant_patterns['new_restaurant'] = [
    r'pattern1',
    r'pattern2'
]
```

## Supported Restaurants

Currently supports detection of:
- Burger Lab
- KFC (Kentucky Fried Chicken)
- McDonald's
- Pizza Hut
- Subway
- Domino's

Easy to extend with more restaurants by adding regex patterns.

## How It Works

1. **Text Extraction**: Uses `pdfplumber` to extract text directly from PDFs
2. **OCR Fallback**: If no text is found, converts PDF to images and uses Tesseract OCR
3. **Pattern Matching**: Searches extracted text for restaurant-specific patterns using regex
4. **Result Return**: Returns identified restaurant name or None if no match found

## Example Output

```
Processing PDF: receipt.pdf

--- Extracted Text Preview ---
BURGER LAB
123 Main Street
Order #12345
...

✓ Identified Restaurant: burger_lab
```

## Error Handling

The tool handles various error scenarios:
- File not found
- Corrupted PDFs
- OCR failures
- System dependency issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Areas for improvement:
- Add more restaurant patterns
- Improve OCR accuracy
- Add confidence scoring
- Support for other document types

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

### Common Issues

**"TesseractNotFoundError"**
- Make sure Tesseract is installed and in your system PATH
- On Windows, you may need to set the tesseract executable path

**"PDFSyntaxError"**
- The PDF file may be corrupted or password-protected
- Try with a different PDF file

**No restaurant detected**
- Check if the restaurant name appears in the text preview
- Consider adding custom patterns for your specific use case

### Getting Help

If you encounter issues:
1. Check the text preview to see what was extracted
2. Verify your PDF is not corrupted
3. Ensure all system dependencies are installed
4. Open an issue on GitHub with details about your problem

## Changelog

### v1.0.0
- Initial release
- Basic PDF text extraction
- Restaurant pattern matching
- Command line interface
- OCR fallback support

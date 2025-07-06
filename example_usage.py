#!/usr/bin/env python3
"""
Example usage of the PDF Restaurant Extractor
"""

from pdf_restaurant_extractor import PDFProcessor

def main():
    """Demonstrate various usage patterns"""
    
    # Initialize the processor
    processor = PDFProcessor()
    
    # Example 1: Basic usage
    print("=== Example 1: Basic Usage ===")
    try:
        result = processor.process_pdf('sample_receipt.pdf')
        print(f"Success: {result['success']}")
        print(f"Restaurant: {result['restaurant']}")
    except FileNotFoundError:
        print("sample_receipt.pdf not found - create a test PDF file")
    
    # Example 2: Adding custom restaurant patterns
    print("\n=== Example 2: Adding Custom Patterns ===")
    processor.add_restaurant_pattern('taco_bell', [
        r'taco\s*bell',
        r'tb\s*restaurant',
        r'live\s*mas'
    ])
    
    # Example 3: Text-only processing
    print("\n=== Example 3: Text-Only Processing ===")
    sample_text = "Welcome to McDonald's! Order #12345 Total: $15.99"
    restaurant = processor.identify_restaurant(sample_text)
    print(f"Identified restaurant from text: {restaurant}")
    
    # Example 4: Batch processing
    print("\n=== Example 4: Batch Processing ===")
    pdf_files = ['receipt1.pdf', 'receipt2.pdf', 'receipt3.pdf']
    results = []
    
    for pdf_file in pdf_files:
        try:
            result = processor.process_pdf(pdf_file, show_preview=False)
            results.append({
                'file': pdf_file,
                'restaurant': result['restaurant'],
                'success': result['success']
            })
        except FileNotFoundError:
            print(f"File not found: {pdf_file}")
            results.append({
                'file': pdf_file,
                'restaurant': None,
                'success': False
            })
    
    # Summary
    print("\n=== Batch Processing Summary ===")
    successful = sum(1 for r in results if r['success'])
    print(f"Successfully processed: {successful}/{len(results)}")
    
    for result in results:
        status = "✓" if result['success'] else "✗"
        restaurant = result['restaurant'] or "Unknown"
        print(f"{status} {result['file']}: {restaurant}")

if __name__ == "__main__":
    main()

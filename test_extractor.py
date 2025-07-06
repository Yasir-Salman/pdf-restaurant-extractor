#!/usr/bin/env python3
"""
Simple tests for the PDF Restaurant Extractor
"""

import unittest
from pdf_restaurant_extractor import PDFProcessor

class TestPDFProcessor(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.processor = PDFProcessor()
    
    def test_restaurant_identification(self):
        """Test restaurant identification from text"""
        test_cases = [
            ("Welcome to McDonald's", "mcdonalds"),
            ("KFC Original Recipe", "kfc"),
            ("BURGER LAB Premium Burgers", "burger_lab"),
            ("Pizza Hut Delivery", "pizza_hut"),
            ("Subway Eat Fresh", "subway"),
            ("Domino's Pizza", "dominos"),
            ("Random Restaurant", None),
            ("", None),
        ]
        
        for text, expected in test_cases:
            with self.subTest(text=text):
                result = self.processor.identify_restaurant(text)
                self.assertEqual(result, expected)
    
    def test_case_insensitive_matching(self):
        """Test that matching is case insensitive"""
        test_cases = [
            "mcdonald's",
            "MCDONALD'S",
            "McDonald's",
            "mcDONALD'S"
        ]
        
        for text in test_cases:
            with self.subTest(text=text):
                result = self.processor.identify_restaurant(text)
                self.assertEqual(result, "mcdonalds")
    
    def test_add_restaurant_pattern(self):
        """Test adding custom restaurant patterns"""
        # Add a new pattern
        self.processor.add_restaurant_pattern('test_restaurant', [r'test\s*cafe'])
        
        # Test it works
        result = self.processor.identify_restaurant("Welcome to Test Cafe")
        self.assertEqual(result, "test_restaurant")
    
    def test_pattern_with_spaces(self):
        """Test patterns that handle variable spacing"""
        test_cases = [
            "Burger Lab",
            "BurgerLab",
            "Burger  Lab",
            "burger lab"
        ]
        
        for text in test_cases:
            with self.subTest(text=text):
                result = self.processor.identify_restaurant(text)
                self.assertEqual(result, "burger_lab")
    
    def test_empty_and_none_inputs(self):
        """Test handling of empty and None inputs"""
        self.assertIsNone(self.processor.identify_restaurant(""))
        self.assertIsNone(self.processor.identify_restaurant(None))
    
    def test_multiple_restaurants_in_text(self):
        """Test behavior when multiple restaurants are mentioned"""
        # Should return the first match found
        text = "Went to McDonald's then KFC"
        result = self.processor.identify_restaurant(text)
        # Should find one of them (implementation dependent on order)
        self.assertIn(result, ["mcdonalds", "kfc"])

if __name__ == "__main__":
    unittest.main()

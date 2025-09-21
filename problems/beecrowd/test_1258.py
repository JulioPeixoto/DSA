
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from BEE_1258 import process_shirt_orders

class TestShirtOrders(unittest.TestCase):

    def test_sample_input(self):
        input_data = [
            "9",
            "Maria Jose",
            "branco P",
            "Mangojata Mancuda",
            "vermelho P",
            "Cezar Torres Mo",
            "branco P",
            "Baka Lhau",
            "vermelho P",
            "JuJu Mentina",
            "branco M",
            "Amaro Dinha",
            "vermelho P",
            "Adabi Finho",
            "branco G",
            "Severina Rigudinha",
            "branco G",
            "Carlos Chade Losna",
            "vermelho P",
            "3",
            "Maria Joao",
            "branco P",
            "Marcio Guess",
            "vermelho P",
            "Maria Jose",
            "branco P",
            "0"
        ]
        expected_output = [
            "branco P Cezar Torres Mo",
            "branco P Maria Jose",
            "branco M JuJu Mentina",
            "branco G Adabi Finho",
            "branco G Severina Rigudinha",
            "vermelho P Amaro Dinha",
            "vermelho P Baka Lhau",
            "vermelho P Carlos Chade Losna",
            "vermelho P Mangojata Mancuda",
            "",
            "branco P Maria Joao",
            "branco P Maria Jose",
            "vermelho P Marcio Guess"
        ]
        self.assertEqual(process_shirt_orders(input_data), expected_output)

    def test_single_case_single_order(self):
        input_data = [
            "1",
            "Student Name",
            "branco P",
            "0"
        ]
        expected_output = [
            "branco P Student Name"
        ]
        self.assertEqual(process_shirt_orders(input_data), expected_output)

    def test_empty_input(self):
        input_data = [
            "0"
        ]
        expected_output = []
        self.assertEqual(process_shirt_orders(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()

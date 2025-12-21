import unittest
import os
import pandas as pd
from unittest.mock import patch
from src.exporter import salvar_excel

class TestExporter(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.xlsx"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_salvar_excel_new_file(self):
        df = pd.DataFrame({"Produto": ["A"], "Preço Atual": [100.0]})
        salvar_excel(df, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_salvar_excel_empty(self):
        df = pd.DataFrame()
        salvar_excel(df, self.test_file)
        # Should not create file
        self.assertFalse(os.path.exists(self.test_file))

if __name__ == '__main__':
    unittest.main()
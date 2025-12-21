import unittest
import pandas as pd
from src.cleaner import limpar_dados

class TestCleaner(unittest.TestCase):
    def test_limpar_dados_success(self):
        dados = [
            {
                "Data Coleta": "2023-01-01",
                "Loja": "Teste",
                "Produto": "Produto A",
                "Preço Antigo Bruto": "1.499,00",
                "Preço Atual Bruto": "1.299,00",
                "URL": "http://teste.com"
            }
        ]
        df = limpar_dados(dados)
        self.assertEqual(len(df), 1)
        self.assertEqual(df['Preço Atual'].iloc[0], 1299.0)
        self.assertEqual(df['Preço Antigo'].iloc[0], 1499.0)

    def test_limpar_dados_empty(self):
        df = limpar_dados([])
        self.assertTrue(df.empty)

if __name__ == '__main__':
    unittest.main()
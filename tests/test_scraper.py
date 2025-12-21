import unittest
from unittest.mock import patch, MagicMock
from src.scraper import obter_dados_produto

class TestScraper(unittest.TestCase):
    @patch('src.scraper.requests.get')
    def test_obter_dados_produto_success(self, mock_get):
        # Mock response
        mock_response = MagicMock()
        mock_response.content = b'''
        <html>
            <h1 class="ui-pdp-title">Produto Teste</h1>
            <div class="ui-pdp-price__second-line">
                <span class="andes-money-amount__fraction">1.299</span>
            </div>
            <div class="ui-pdp-price__original-value">
                <span class="andes-money-amount__fraction">1.499</span>
            </div>
        </html>
        '''
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        item = {
            "loja": "Teste",
            "url": "http://teste.com",
            "seletor_nome": "h1.ui-pdp-title",
            "seletor_preco": ".ui-pdp-price__second-line .andes-money-amount__fraction",
            "seletor_preco_antigo": ".ui-pdp-price__original-value .andes-money-amount__fraction"
        }

        result = obter_dados_produto(item)
        self.assertIsNotNone(result)
        self.assertEqual(result['Produto'], 'Produto Teste')
        self.assertEqual(result['Preço Atual Bruto'], '1.299')

    @patch('src.scraper.requests.get')
    def test_obter_dados_produto_error(self, mock_get):
        from tenacity import RetryError
        mock_get.side_effect = Exception("Erro de conexão")
        item = {"loja": "Teste", "url": "http://teste.com", "seletor_nome": "", "seletor_preco": ""}
        with self.assertRaises(RetryError):
            obter_dados_produto(item)

if __name__ == '__main__':
    unittest.main()
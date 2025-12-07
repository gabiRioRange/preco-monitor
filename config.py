# config.py

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}

URLS_ALVO = [
    # PRODUTO 1: Exemplo Mercado Livre (iPhone 13)
    # Obs: Os seletores abaixo funcionam na maioria das páginas do ML, mas podem variar.
    {
        "loja": "Mercado Livre",
        "url": "https://www.mercadolivre.com.br/apple-iphone-14-128-gb-roxo-excelente-recondicionado/p/MLB2000021911#polycard_client=search-nordic&search_layout=grid&position=1&type=product&tracking_id=1be8ee9e-9ffc-40f0-8250-bce25178ff0c&wid=MLB4283828839&sid=search", 
        "seletor_nome": "h1.ui-pdp-title",  
        "seletor_preco": ".ui-pdp-price__second-line .andes-money-amount__fraction",
        "seletor_preco_antigo": ".ui-pdp-price__original-value .andes-money-amount__fraction"
    },
    
    # Você pode adicionar mais produtos copiando o bloco acima e trocando a URL
]

ARQUIVO_SAIDA = "data/historico_precos.xlsx"
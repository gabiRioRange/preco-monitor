import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import HEADERS

def obter_dados_produto(item):
    url = item['url']
    loja = item['loja']
    
    print(f"🔄 Acedendo a: {url}...")
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 1. Nome
        el_nome = soup.select_one(item['seletor_nome'])
        nome = el_nome.get_text(strip=True) if el_nome else "Nome não encontrado"
        
        # 2. Preço Atual
        el_preco = soup.select_one(item['seletor_preco']) 
        preco_texto = el_preco.get_text(strip=True) if el_preco else "0,00"

        # 3. Preço Antigo (NOVO)
        # Usa .get() para não dar erro se você esquecer de colocar no config
        seletor_antigo = item.get('seletor_preco_antigo')
        el_antigo = soup.select_one(seletor_antigo) if seletor_antigo else None
        preco_antigo_texto = el_antigo.get_text(strip=True) if el_antigo else "0,00"
        
        return {
            "Data Coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Loja": loja,
            "Produto": nome,
            "Preço Antigo Bruto": preco_antigo_texto, # <--- NOVO
            "Preço Atual Bruto": preco_texto,
            "URL": url
        }
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao aceder {url}: {e}")
        return None
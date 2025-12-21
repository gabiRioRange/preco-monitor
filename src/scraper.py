import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import os
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import HEADERS, logger

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10), retry=retry_if_exception_type(requests.exceptions.RequestException))
def obter_dados_produto(item):
    url = item['url']
    loja = item['loja']
    
    logger.info(f"🔄 Acedendo a: {url}...")
    
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
        
        logger.info(f"✅ Dados coletados para {nome}")
        return {
            "Data Coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Loja": loja,
            "Produto": nome,
            "Preço Antigo Bruto": preco_antigo_texto, # <--- NOVO
            "Preço Atual Bruto": preco_texto,
            "URL": url
        }
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            logger.warning(f"🚫 403 com requests, tentando Selenium para {url}...")
            return obter_dados_selenium(item)
        else:
            logger.error(f"❌ Erro HTTP {e.response.status_code} para {url}: {e}")
            raise  # Retry
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Erro ao aceder {url}: {e}")
        raise  # Retry

def obter_dados_selenium(item):
    url = item['url']
    loja = item['loja']
    
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"user-agent={HEADERS['User-Agent']}")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        # 1. Nome
        try:
            el_nome = driver.find_element(By.CSS_SELECTOR, item['seletor_nome'])
            nome = el_nome.text.strip()
        except:
            nome = "Nome não encontrado"
        
        # 2. Preço Atual
        try:
            el_preco = driver.find_element(By.CSS_SELECTOR, item['seletor_preco'])
            preco_texto = el_preco.text.strip()
        except:
            preco_texto = "0,00"
        
        # 3. Preço Antigo
        seletor_antigo = item.get('seletor_preco_antigo')
        if seletor_antigo:
            try:
                el_antigo = driver.find_element(By.CSS_SELECTOR, seletor_antigo)
                preco_antigo_texto = el_antigo.text.strip()
            except:
                preco_antigo_texto = "0,00"
        else:
            preco_antigo_texto = "0,00"
        
        logger.info(f"✅ Dados coletados com Selenium para {nome}")
        return {
            "Data Coleta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Loja": loja,
            "Produto": nome,
            "Preço Antigo Bruto": preco_antigo_texto,
            "Preço Atual Bruto": preco_texto,
            "URL": url
        }
        
    except Exception as e:
        logger.error(f"❌ Erro com Selenium para {url}: {e}")
        return None
    finally:
        driver.quit()
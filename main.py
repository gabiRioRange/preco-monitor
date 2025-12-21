from config import URLS_ALVO, ARQUIVO_SAIDA, logger
from src.scraper import obter_dados_produto
from src.cleaner import limpar_dados
from src.exporter import salvar_excel
import time

def main():
    logger.info("--- 🚀 Iniciando Monitoramento de Preços ---")
    
    dados_coletados = []
    
    # 1. Coleta (Scraping)
    for item in URLS_ALVO:
        dados = obter_dados_produto(item)
        if dados:
            dados_coletados.append(dados)
        # Pausa para não sobrecarregar o servidor
        time.sleep(2)
            
    # 2. Limpeza (ETL)
    if dados_coletados:
        logger.info("🧹 Limpando e estruturando dados...")
        df_limpo = limpar_dados(dados_coletados)
        
        # Mostra prévia no console (CORRIGIDO AQUI: Preço Atual)
        logger.info("\nPrévia dos dados:")
        try:
            # Tenta mostrar as colunas novas
            logger.info(str(df_limpo[['Produto', 'Preço Atual']].head()))
        except KeyError:
            # Se der erro, mostra tudo o que tem
            logger.info(str(df_limpo.head()))
        
        # 3. Exportação
        logger.info(f"\n💾 Salvando em {ARQUIVO_SAIDA}...")
        salvar_excel(df_limpo, ARQUIVO_SAIDA)
        
    else:
        logger.warning("⚠️ Nenhum dado foi coletado. Verifique os seletores ou a conexão.")

    logger.info("--- ✅ Processo Finalizado ---")

if __name__ == "__main__":
    main()
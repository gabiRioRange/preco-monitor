@echo off
chcp 65001 > nul

:: 1. Entra na pasta do projeto (onde está este arquivo .bat e o main.py)
cd /d "%~dp0"

echo --- 🚀 Iniciando Monitoramento ---
echo Pasta do Projeto: %CD%

:: 2. Define o caminho do Python (Na pasta Documentos/.venv)
:: O ".." significa "voltar uma pasta" (sair do preco-monitor e ir para Documents)
set PYTHON_PATH=..\.venv\Scripts\python.exe

:: 3. Verifica se o Python existe nesse caminho
if exist "%PYTHON_PATH%" (
    echo ✅ Ambiente virtual encontrado nos Documentos.
    
    :: Executa o script principal
    "%PYTHON_PATH%" main.py
) else (
    echo ❌ ERRO CRÍTICO:
    echo Não encontrei o Python em: %PYTHON_PATH%
    echo Verifique se a pasta .venv está mesmo em C:\Users\gabriel\Documents\.venv
)

:: 4. Pausa final para leitura
if %errorlevel% neq 0 (
    echo.
    echo ⚠️ Ocorreu um erro na execução.
    pause
) else (
    echo.
    echo ✅ Finalizado. Fechando em 5 segundos...
    timeout /t 5
)
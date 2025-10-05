import spacy
import re
import requests
import os

url = "https://www.gutenberg.org/files/55752/55752-0.txt"

def baixar_texto(url=url):    
    print(f"Baixando texto de: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao baixar o texto: {response.status_code}")
        return None
    texto = response.text
    return texto

def salvar_texto(texto, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(texto)
    print(f"Texto salvo em: {caminho_arquivo}")

def carregar_texto(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return f.read()

def tokenizar(texto):
    nlp = spacy.load("pt_core_news_sm")
    doc = nlp(texto)
    tokens = [token.text for token in doc]
    return tokens

def filtrar_palavras_com_regex(tokens):
    padrao = re.compile(r'^[a-zA-ZÀ-ÖØ-öø-ÿ]+$')
    tokens_filtrados = [token for token in tokens if padrao.match(token)]
    return tokens_filtrados

def main():
    caminho_arquivo = "dom_casmurro.txt"
    if not os.path.exists(caminho_arquivo):
        texto = baixar_texto()
        if texto:
            salvar_texto(texto, caminho_arquivo)
        else:
            print("Não foi possível baixar o texto. Encerrando.")
            return
    else:
        print(f"Arquivo {caminho_arquivo} já existe. Carregando...")
        texto = carregar_texto(caminho_arquivo)

    tokens = tokenizar(texto)
    num_tokens = len(tokens)
    print(f"Número de tokens após tokenização: {num_tokens}")
    print(f"Exemplos de tokens (primeiros 20): {tokens[:20]}")
    
    tokens_filtrados = filtrar_palavras_com_regex(tokens)
    num_tokens_filtrados = len(tokens_filtrados)
    print(f"Número de tokens após filtragem com regex: {num_tokens_filtrados}")
    print(f"Exemplos de tokens filtrados (primeiros 20): {tokens_filtrados[:20]}")
    
    tokens_removidos = num_tokens - num_tokens_filtrados
    percentual_removido = (tokens_removidos / num_tokens) * 100
    print("\nEstatísticas:")
    print(f"Total de tokens iniciais: {num_tokens}")
    print(f"Total de tokens após filtragem: {num_tokens_filtrados}")
    print(f"Tokens removidos: {tokens_removidos} ({percentual_removido:.2f}%)")

if __name__ == "__main__":
    main()
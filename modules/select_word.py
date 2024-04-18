# Importa a função 'choice' do módulo 'random' para selecionar uma palavra aleatória de uma lista.
from random import choice
# Importa o módulo 'json' para carregar dados de um arquivo JSON.
import json
# Importa 'data_manager' do pacote local 'manage_values'.
from .manage_values import data_manager

def select_word():
    # Cria uma instância de 'data_manager' para gerenciar as configurações relacionadas ao idioma.
    lenguagem_manager = data_manager()
    # Recupera o idioma selecionado através de uma chamada ao método 'get_value_language' do 'lenguagem_manager'.
    language_select = lenguagem_manager.get_value_language()

    # Bloco try-except para manipulação de exceções ao tentar abrir arquivos.
    try:
        # Tenta abrir um arquivo JSON que contém palavras, cujo nome depende do idioma selecionado.
        with open(f"modules/words/words_{language_select}.json", "r") as file:
            # Carrega os dados do arquivo JSON para a variável 'data'.
            data = json.load(file)
        # Escolhe uma palavra aleatória da lista de palavras carregada.
        word = choice(data)
        # Retorna a palavra escolhida.
        return word
    # Captura a exceção 'FileNotFoundError' que pode ocorrer se o arquivo JSON não for encontrado.
    except FileNotFoundError as err:
        # Imprime uma mensagem de erro indicando que o arquivo não foi encontrado e mostra detalhes do erro.
        print("Passe um valor válido\n", err)

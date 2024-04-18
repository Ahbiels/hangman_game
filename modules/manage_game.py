# Importação do módulo 'data_manager' do pacote local 'manage_values'.
from .manage_values import data_manager

# Cria uma instância do 'data_manager' chamando a função/classe importada.
data_manager = data_manager()

# Definição de uma função chamada 'manage_game' que aceita um parâmetro 'word'.
def manage_game(word):
    # Recupera dois valores de 'data_manager': 'letter_in_word_secret' e 'letter_typed'.
    # Esses valores representam letras associadas à palavra sendo jogada.
    letter_in_word_secret, letter_typed = data_manager.get_value_letter_by_word().values()

    try: #try except para caso a palavra não seja enviada
        # Verifica se a letra digitada ('letter_typed') está na palavra ('word') fornecida como dicionário.
        if letter_typed in word["word"]:
            # Inicia uma variável 'secret_word' que vai construir a palavra secreta a ser exibida.
            secret_word = ''
            # Itera sobre cada letra na palavra.
            for letter in word["word"]:
                # Se a letra atual estiver no conjunto 'letter_in_word_secret', ela é adicionada à 'secret_word'.
                if letter in letter_in_word_secret:
                    secret_word += letter
                # Caso contrário, adiciona um '_' para indicar letras não reveladas.
                else:
                    secret_word += "_"
            # Atualiza o valor da palavra secreta no 'data_manager'.
            data_manager.set_value_secret_word(secret_word)
    except TypeError as err:
        return {
            "message": "Envie a palavra correta",
            "Error": err
        }
    
    # Retorna a palavra secreta atualizada de 'data_manager'.
    # Se a palavra nao conter a letra digitada, e o bloco de código if nao for executado, o valor retornado será o que já estava salvo
    return data_manager.get_value_secret_word()
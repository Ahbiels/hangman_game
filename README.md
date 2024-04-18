# Jogo da Velha com FastAPI

## Visão Geral
O projeto implementa uma versão simplificada do jogo da velha (hangman) usando Python e FastAPI, integrado com conceitos de modularização e uso de Dataclasses para a gestão de estados do jogo. O jogo permite ao usuário interagir via uma API para selecionar uma palavra aleatória, definir um idioma, e tentar adivinhar a palavra enviando letras uma a uma.

## Estrutura do Projeto
O jogo é dividido em vários módulos, cada um com responsabilidades específicas:

- **manage_game.py**: Contém a lógica para processar as tentativas do usuário e atualizar o estado do jogo.
- **manage_values.py**: Define a classe data_manager que armazena o estado do jogo e oferece métodos para manipular este estado.
- **select_word.py**: Responsável por selecionar uma palavra aleatória baseada no idioma escolhido pelo usuário.
- **main.py**: Contém o servidor FastAPI com rotas para interagir com o jogo.
## Detalhes dos Módulos
### manage_game.py
Este módulo gerencia a lógica de verificar se uma letra está na palavra e atualiza a palavra secreta. Funções principais:
- manage_game(word): Verifica se a letra enviada está na palavra e atualiza a representação da palavra secreta com base nas letras já adivinhadas.
### manage_values.py
Este módulo contém a definição da classe data_manager, que usa o padrão Dataclass para armazenar o estado do jogo. Principais atributos e métodos:

- Atributos: Idioma, letras adivinhadas, letra atual, palavra completa, palavra secreta e status do jogo.
- Métodos: Setters e getters para os atributos, além de um método para resetar os valores quando necessário.
### select_word.py
Seleciona uma palavra aleatória de um arquivo JSON específico para o idioma escolhido. A função principal:

- select_word(): Carrega palavras de um arquivo JSON baseado no idioma selecionado e escolhe uma aleatoriamente.
### main.py
Configura e executa o servidor FastAPI, definindo as rotas para interação com o usuário. Rotas principais:

- GET /: Confirma que o servidor está operacional.
- POST /language: Define o idioma do jogo.
- GET /select-word: Seleciona e retorna uma nova palavra para o usuário tentar adivinhar.
- POST /letter: Recebe uma letra do usuário, verifica sua presença na palavra e retorna o estado atual do jogo.
## Executando o Projeto
Para rodar o projeto, é necessário ter Python e FastAPI instalados. O servidor pode ser iniciado com o seguinte comando:

```css
uvicorn main:app --reload
```
Após iniciar, a API estará disponível em http://127.0.0.1:8000.

## Interação com a API
- Acesse a rota / para verificar se o servidor está funcionando.
- Use a rota /language com um método POST para definir o idioma.
- A rota /select-word com um método GET para receber uma palavra para adivinhar.
- A rota /letter com um método POST para enviar uma letra e receber o estado atual do jogo.
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from modules import data_manager, select_word, manage_game

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

data_manager = data_manager() # Evita o erro: TypeError: data_manager.set_value_language() missing 1 required positional argument: 'new_language'

class Letter(BaseModel):
    letter: str

class language(BaseModel):
    language: str

@app.get('/')
def index():
    return {"Response":"Server is works"}

#Setar a linguagem
@app.post("/language")
async def select_language(language: language):
    data_manager.set_value_language(language.language)

    return f"A linguagem escolhida foi {language.language}"

#Aqui vai selecionar a palavra e retorná-lá
@app.get("/select-word")
async def response_word():
    data_manager.set_value_word(select_word())
    word = data_manager.get_value_word()
    return {
        "secret_word": '-'*len(word["word"]),
        "word": word["word"],
        "tip": word["tip"],
    }

#Aqui o usuário vai mandar uma letra
@app.post("/letter")
async def validated_letter(letter: Letter):
    word = data_manager.get_value_word()
    data_manager.set_value_letter_by_word(letter.letter,word)
    status = data_manager.status
    secret_word = manage_game(word)

    return {
        "secret_word": secret_word,
        "status": status
    }

#uvicorn main:app --reload
#http://127.0.0.1:8000

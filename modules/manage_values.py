from dataclasses import dataclass, field
from pydantic import BaseModel


"""
Se language deve ser um valor compartilhado por todas as instâncias da classe, você deve definir 
language como um atributo de classe. Neste caso, modificar language afetará todas as instâncias. 
Para fazer isso, vamos utilizar o @classmethod

"""

class attributeWord(BaseModel):
    ...

@dataclass
class data_manager:
    language: str = 'pt'
    letter_in_word_secret = ''
    letter_typed = ''
    word = ''
    secret_word = ''
    status = ''

    #----------------------------Set e pega o valor da linguagem escolhida---------------------------
    @classmethod
    def set_value_language(self, new_language):
        self.language = new_language
        self.reset_values()

    @classmethod
    def get_value_language(self):
        return self.language
    
    #----------------------------Set e pega o valor da letra digitada---------------------------
    @classmethod
    def set_value_letter_by_word(self,letter,word):
        print(word["word"],"asdasdasd")
        self.letter_typed = letter
        if self.letter_typed not in self.letter_in_word_secret and self.letter_typed in word["word"]:
            if len(self.letter_typed) == 1:
                self.letter_in_word_secret += letter
                self.status = "Valor aceito"
            else: 
                self.status = "Digite somente um valor"
        else: 
            self.status = "Esse valor já foi digitado ou não tem na palavra"

    @classmethod
    def get_value_letter_by_word(self):
        return {
            "letter_in_word_secret": self.letter_in_word_secret,
            "letter_typed": self.letter_typed,
        }
    
    #----------------------------Set e pega o valor da palavra escolhida---------------------------
    @classmethod
    def set_value_word(self, word):
        self.reset_values()
        self.secret_word = "_"*len(word['word'])
        self.word = word
    
    @classmethod
    def get_value_word(self):
        return self.word
    
    #----------------------------Set e pega o valor da palavra secreta---------------------------
    @classmethod
    def set_value_secret_word(self, secret_word):
        self.secret_word = secret_word

    @classmethod
    def get_value_secret_word(self):
        return self.secret_word

    @classmethod
    def reset_values(cls):
        cls.letter_in_word_secret = ''
        cls.letter_typed = ''
        cls.word = ''
        cls.secret_word = '_'*len(cls.word)
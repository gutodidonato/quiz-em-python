import question_model
import art

class Quiz:
    def __init__(self):
        self.pontos = 0

    def run_quiz(self):
        print(art.logo)
        while True:
            pergunta_valor = question_model.escolher_pergunta()
            print(f"Pergunta: {pergunta_valor['text']}")
            resposta = input("True or False? ").lower()
            
            if resposta == pergunta_valor['answer'].lower():
                self.pontos += 1
                print(f"Você acertou! Pontos: {self.pontos} \n")
            else:
                print("Você errou! \n")



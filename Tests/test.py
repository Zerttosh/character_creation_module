class Human:
    def __init__(self, name):
        self.name = name
    
    
class Curator(Human):
    
    def answer_question(self, question):
        
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            return super().answer_question(question)
        
friend = Human('Виталя')
curator = Curator('Марина')

print(curator.name)
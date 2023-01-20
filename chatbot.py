my_bot=chatBot(name='pybot',read_only=True,logic_adapoters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])
small_talk=['hi there','hi','how do you?','how are you?']
math_talk_1=['pythagorean theorem','a squared plus b squared equals c squared.']
math_talk_2=['law of cosines','c**2=a**2+b**2-2*a*b*cos(gamma)']
list_trainer=ListTrainer(my_bot)
for item in (small_talk,math_1,math_talk_2):
    list_trainer.train(item)
print(my_bot.get_response("hi"))
how do you do?
print(my_bot.get_response("i feel awesome today"))
execellent,glad to hear that.
print(my_bot.get_response("what's your name?"))
i am pybot.ask me a math quesgion,plz.
print(my_bot.get_response("show me the pythagorean theorem"))
a squared plus b squared equals c squared.
print(my_bot.get_response("do you knoe the law of cosines?"))
c**2=a**2+b**2-2*a*b*cos(gamma)
from chatterbot.trainers import chatterbotcorpusTrainer
corpus_trainer=chatterBotcorpusTrainer(my_bot)
corpus_trainer>train('chatbot.corpus.english')
            

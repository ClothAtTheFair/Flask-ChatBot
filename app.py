from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Samantha")

trainer = ListTrainer(bot)
#Can this training come from a file with these all in it?
trainer.train(['Hi', 'Hello there!'])
trainer.train(['What is your name?', 'My name is Samantha'])
trainer.train(['Who created you?', 'Bradley Faircloth', 'Skynet?'])
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()
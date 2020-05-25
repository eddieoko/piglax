from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators


class TextForm(Form):
    message = StringField('message', [validators.Length(min=4, max=25)])


piglax = Flask(__name__)


@piglax.route('/')
def index():
    return render_template("/index.html")


@piglax.route('/translation.html', methods=['POST'])
def translation():
    sentence = request.form['text']
    vowels = ["a", "e", "i", "o", "u"]
    punctuation = [",", ".", "!", "?", "@", "'"]
    no_punct = ""
    piggy = []
    
    for char in sentence:
        if char not in punctuation:
            no_punct = no_punct + char

    words = no_punct.split()
    for word in words:
        if word[0] in vowels:
            piggy.append(word + "-yay")
        else:
            piggy.append(word[1:] + "-" + word[0] + "ay")

    piglatin = (' '.join(piggy))
    print(piglatin)
    return render_template("/translation.html", piglatin=piglatin)


if __name__ == "__main__":
    piglax.run(debug=False)

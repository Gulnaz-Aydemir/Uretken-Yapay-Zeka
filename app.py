from flask import Flask, render_template, request
import random

app = Flask(__name__)

with open("songs1.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

words = text.split()

word_dict = {}
for i in range(len(words) - 1):
    if words[i] in word_dict:
        word_dict[words[i]].append(words[i + 1])
    else:
        word_dict[words[i]] = [words[i + 1]]

def find_similar_word(word, word_list):
    for w in word_list:
        if word in w or w in word:
            return w
    return random.choice(word_list)

def generate_lyrics(start_word, total_words=40, line_length=5):
    lyrics = [start_word]
    if start_word in word_dict:
        current_word = start_word
    else:
        current_word = find_similar_word(start_word, list(word_dict.keys()))

    for _ in range(total_words - 1):
        if current_word in word_dict:
            next_word = random.choice(word_dict[current_word])
        else:
            current_word = find_similar_word(current_word, list(word_dict.keys()))
            next_word = random.choice(word_dict[current_word])
        lyrics.append(next_word)
        current_word = next_word

    lines = []
    for i in range(0, len(lyrics), line_length):
        line = " ".join(lyrics[i:i + line_length])
        lines.append(line.capitalize())

    return "\n".join(lines)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        word = request.form["word"].lower()
        result = generate_lyrics(word, total_words=40, line_length=5)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

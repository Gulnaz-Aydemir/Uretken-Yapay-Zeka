import random

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

def generate_lyrics(start_word, length=20):
    lyrics = [start_word]
    current_word = start_word
    for _ in range(length - 1):
        if current_word in word_dict:
            next_word = random.choice(word_dict[current_word])
        else:
            current_word = find_similar_word(current_word, list(word_dict.keys()))
            next_word = random.choice(word_dict[current_word])
        lyrics.append(next_word)
        current_word = next_word
    return " ".join(lyrics)

start_word = input("Şarkı hangi kelimeyle başlasın? ").lower()

if start_word not in word_dict:
    print(f"'{start_word}' kelimesi eğitim verisinde bulunamadı. En yakın anlamlı kelimeyle devam ediliyor.\n")

generated_song = generate_lyrics(start_word, length=20)

print("\nOluşturulan şarkı sözleri:\n")
print(generated_song)

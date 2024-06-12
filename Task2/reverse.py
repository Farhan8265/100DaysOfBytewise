# Exercise: Reverse Words in a Sentence
sentence = input("Enter a Sentence: ")
words = sentence.split()
reverse_word = []

for i in range (len (words) - 1, -1, -1):
    reverse_word.append ( words[i] )

reverse_sentence = ' '.join(reverse_word)

print("Reverse Sentence:", reverse_sentence)
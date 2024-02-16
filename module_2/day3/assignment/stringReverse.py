def reverse_word(sentence):
    words = sentence.split()
    reversed_word = [word[::-1] for word in words][::-1]
    reversed_sentence = ' '.join(reversed_word)
    return reversed_sentence

sentence = input("Enter a sentence: ")
result = reverse_word(sentence)

print(f"Sentence: {sentence}")
print(f"Reverse Sentence: {result}")
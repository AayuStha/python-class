sentence = input("Enter a sentence: ")
words = sentence.split()
word_length = {word: len(word) for word in words}
print("The world length is:\n")
print(word_length)
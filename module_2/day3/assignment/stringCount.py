sentence = "this is not a demo but demo is demo"
print(sentence)
sentence_list = sentence.split()
dict = {word: sentence.split().count(word) for word in sentence_list}
print(dict)
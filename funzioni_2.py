def divide_string(sentence):
    parts = sentence.split(' ')
    return parts

def sort_words(words):
    return sorted(words)

def upper_word(word):
    return word.upper()

def lower_word(word):
    return word.lower()

def sort_sentence(sentence):
    words = divide_string(sentence)
    return sort_words(words)

#sentence = raw_input("Dammi la frase: ")
#words = divide_string(sentence)

#print words
#print sort_words(words)
#print upper_word(sentence)
#print lower_word(sentence)

#print sort_sentence(sentence)


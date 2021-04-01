from word_counter import WordCounter

key_words = ['and', 'so', 'if', 'the', 'all', 'but', 'while', 'is']
Counter = WordCounter(key_words)
# frequency = Counter.count_words()
frequency = Counter.count_key_words()
Counter.save(frequency)

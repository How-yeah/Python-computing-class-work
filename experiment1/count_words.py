from word_counter import WordCounter

# key_words = ['so', 'if', 'the', 'all', 'but', 'and', 'while', 'is', 'happy']
Counter = WordCounter()
frequency = Counter.count_words()

#frequency = Counter.count_key_words()
Counter.save(frequency)

from word_counter import WordCounter


Counter = WordCounter()
frequency = Counter.count_words()
# key_words = ['so', 'if', 'the', 'all', 'but', 'and', 'while', 'is', 'happy']
# frequency = Counter.count_key_words()
Counter.save(frequency)

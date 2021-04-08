from word_counter import WordCounter


Counter = WordCounter()
frequency = Counter.count_words()
Counter.save(frequency)

# key_words = ['so', 'if', 'the', 'all', 'but', 'and', 'while', 'is', 'happy']
# Counter = WordCounter(key_words)
# frequency = Counter.count_key_words()
# Counter.save(frequency)

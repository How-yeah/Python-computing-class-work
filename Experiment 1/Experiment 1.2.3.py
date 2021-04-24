def Compare(word, compareWord):
    if len(word) != len(compareWord):
        return 0
    for i in range(len(word)):
        if word[i] != compareWord[len(word) - i - 1]:
            return 0
    return 1


file = open(r".\Python Computing\Experiment\words.txt")
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace('\n', '')
savedWords = []
print('The reverse pairs in "words.txt":')
for word in words:
    for compareWord in words:
        if word != compareWord and Compare(word, compareWord) and word not in savedWords:
            savedWords.append(word)
            savedWords.append(compareWord)
            print("(" + word + ", " + compareWord + ")")
file.close()
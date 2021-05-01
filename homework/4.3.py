import re


def sub_repeated_words(text):
    pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')  # \1 是引用第一个括号的内容

    while True:
        repeated_words = re.search(pattern, text)
        if not repeated_words:
            break
        text = re.sub(repeated_words.group(), repeated_words.group(1), text)
    return text


text = 'This is is a a a desk'
print(sub_repeated_words(text))

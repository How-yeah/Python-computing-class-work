import time


def find(word: str) -> str:
    global words, exact_words, failed_words, max_len
    if len(word) > 1:
        for i in range(len(word)):
            sub_word = word[:i]+word[i+1:]  # 删除第i个字母得到子单词
            # print(sub_word)
            if sub_word in exact_words or (sub_word in words and sub_word not in failed_words and find(sub_word) is not None):
                # 若子单词在可缩减单词列表中，或子单词在单词列表中且不在非可缩减单词列表中且子单词的子单词仍是可缩减单词
                exact_words.add(word)
                max_len = max(max_len, len(word))
                return word
    failed_words.add(word)
    return None


def show_word(word: str, is_arrow=True):
    global words
    if len(word) > 1:
        for i in range(len(word)):
            sub_word = word[:i]+word[i+1:]  # 删除第i个字母得到子单词
            # print(sub_word)
            if sub_word in {'a', 'i'}:
                print(sub_word, end='->')
                return word
            elif sub_word in exact_words and show_word(sub_word, is_arrow=False):
                # 若子单词在可缩减单词列表中，且子单词一直能拆分
                print(sub_word, end='\n' if is_arrow else '->')
                return word
    return None


if __name__ == '__main__':
    with open(r'./experiment2/data/words.txt') as file_obj:
        words_list = [x.rstrip() for x in file_obj if 'a' in x or 'i' in x]

    words = set(words_list)
    exact_words = {'a', 'i'}
    failed_words = set()
    max_len = 1
    longest_word = ''

    start = time.time()
    for word in words_list:
        if len(word) > max_len:
            sub_word = find(word)
            if sub_word:
                longest_word = sub_word
    end = time.time()
    print('Cost '+str(end-start) + 's\n')
    # show_word(longest_word)
    for word in exact_words:
        show_word(word)
    print('\nThe lognest result is:')
    show_word(longest_word)

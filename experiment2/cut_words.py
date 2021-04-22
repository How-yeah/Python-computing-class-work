import time

def find(word: str):
    global max_len , words_set, succeed_words_set, failed_words_set
    if len(word) > 1:
        for i in range(len(word)):
            cut_word = word[:i] + word[i + 1:]  
            if cut_word in succeed_words_set or (cut_word in words_set and cut_word not in failed_words_set and find(cut_word) is not None):
                break  
        else:  
            failed_words_set.add(word)
            return None
    succeed_words_set.add(word)
    max_len = max(max_len, len(word))  
    return word


if __name__ == '__main__':
    start = time.time()  

    
    with open(r'./experiment2/data/words.txt') as fp:
        
        words_list = [x.strip() for x in fp if 'a' in x or 'i' in x]
    words_set = set(words_list)  
    succeed_words_set = {'a', 'i'}  
    failed_words_set = set()  
    max_len = 1  
    for w in words_list:
        find(w)
    for index in succeed_words_set:
        if len(index) == max_len:
            print(index)
    end = time.time()  
    print(succeed_words_set)
    print(end - start, '秒')
    print(len(succeed_words_set))   
    
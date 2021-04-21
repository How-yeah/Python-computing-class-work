import time


# 递归查找，判断子单词里有没有可缩减单词，返回单词本身为可缩减单词，返回None为非可缩减单词
def find(word: str):
    global max_len , words_set, succeed_words_set, failed_words_set
    if len(word) > 1:
        for i in range(len(word)):
            cut_word = word[:i] + word[i + 1:]  # 第i个字母左边与右边拼起来成为一个子单词cut_word
            # 条件：cut_word已经是可缩减单词了 或 (cut_word是个单词 且 cut_word不是已知的非可缩减单词 且cut_word的子单词里有可缩减单词)
            if cut_word in succeed_words_set or (cut_word in words_set and cut_word not in failed_words_set and find(cut_word) is not None):
                break  # 满足条件就是可缩减单词
        else:  # 循环完毕break没有执行，进入for-else的else
            failed_words_set.add(word)
            return None
    succeed_words_set.add(word)
    max_len = max(max_len, len(word))  # 更新已找到最长的可缩减单词长度
    return word





if __name__ == '__main__':
    start = time.time()  # 记录开始时间

    # 制作词表
    with open(r'./experiment2/data/words.txt') as fp:
        # 读取文件并初筛，不含'a'和'i'的一定不是可缩减单词
        words_list = [x.strip() for x in fp if 'a' in x or 'i' in x]

    words_set = set(words_list)  # 全部词集
    succeed_words_set = {'a', 'i'}  # 成功词集，可缩减单词的子单词一定是可缩减单词
    failed_words_set = set()  # 失败词集，非可缩减单词的子单词一定不是可缩减单词
    max_len = 1  # 记录已找到最长的可缩减单词长度
    for w in words_list:
        find(w)
    for index in succeed_words_set:
        if len(index) == max_len:
            print(index)
    end = time.time()  # 记录结束时间

    
    print(succeed_words_set)
    # print(result)
    print(end - start, '秒')
    print(len(succeed_words_set))   
    
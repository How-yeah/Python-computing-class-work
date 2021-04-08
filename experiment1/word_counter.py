import re


class WordCounter():
    def __init__(self, key_words=''):
        self.key_words = key_words

    def get_words(self) -> list:
        """
        从文章中分离单词
        :return: 单词列表
        """
        with open(r'./experiment1/data/Eng_text.txt') as file_obj:
            contents = file_obj.read()
        words = contents.split()
        return words

    def filter_nonwords(self, words: list) -> list:
        """
        去除非单词字符
        :param words: 单词列表
        :return: 清理后的单词列表
        """
        pattern = re.compile("\W")
        words = [re.sub(pattern, '', word) for word in words]
        return words

    def count_words(self, is_text=True, is_sorted=True) -> list:
        """
        统计词频
        :param is_text: 是则文章，否则纯词汇
        :param is_sorted: 是否按词频降序排列
        :return: 装载键值对元组的词频列表
        """
        words = self.get_words()
        if is_text:
            words = self.filter_nonwords(words)
        words_dict = {}
        for key in words:
            words_dict[key] = words_dict.get(
                key, 0) + 1  # 查询键的值,若键不存在就新建，默认赋0值
        if is_sorted:
            # 按频率降序排列
            frequecy = sorted(words_dict.items(),
                              key=lambda x: x[1], reverse=True)
        else:
            frequecy = words_dict.items()
        return frequecy

    def count_key_words(self, is_text=True, is_sorted=True) -> list:
        """
        根据关键词列表统计词频
        :param is_text: 是则文章，否则纯词汇
        :param is_sorted: 是否按词频降序排列
        :return: 装载键值对元组的词频列表
        """
        words = self.get_words()
        if is_text:
            words = self.filter_nonwords(words)
        # 去除非关键词
        for word in words[:]:
            if word not in self.key_words:
                words.remove(word)

        words_dict = {}
        for key in words:
            words_dict[key] = words_dict.get(
                key, 0) + 1  # 查询键的值,若键不存在就新建，默认赋0值
        if is_sorted:
            # 按频率降序排列
            frequecy = sorted(words_dict.items(),
                              key=lambda x: x[1], reverse=True)
        else:
            frequecy = words_dict.items()
        # 添加没有出现的关键词
        for key_word in self.key_words:
            if key_word not in words:
                frequecy.append((key_word, 0))
        return frequecy

    def save(self, frequency):
        with open(r'./experiment1/data/frequency.txt', 'w') as file_obj:
            for word in frequency:
                file_obj.write(word[0] + ": " + str(word[1])+'\n')
        print('写入完成!')

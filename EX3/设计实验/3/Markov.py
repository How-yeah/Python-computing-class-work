import os
import re
import random
import time
from tqdm import trange


class Markov:
    def __init__(self, n: int = 1, path: str = ''):
        """
        构造马尔可夫链
        :param n:阶数
        :param path:文件读写路径
        """
        self.n = n
        self.path = path
        self.text = self.getText()
        self.words = self.textProcess()
        self.wordsDict = self.analyse()

    def getText(self):
        if os.path.exists(self.path):
            text = open(self.path).read()
            return text
        else:
            print("路径文件不存在！")
            return

    def textProcess(self):
        """
        处理文章中的特殊字符
        :return:文章中全部单词组陈的列表
        """
        pat = '\n|\*|#|\+|\-|\[|\]|\(|\)|\{|\}|\$|\%|@|\'|\"|_'
        text = re.sub(pat, '', self.text)
        words = text.split(' ')
        return words

    def analyse(self):
        """
        生成马尔可夫链字典
        :return:马尔可夫链字典
        """
        wordDict = dict()
        cnt = len(self.words) // self.n if self.n != 1 else len(self.words) // self.n - 1
        print("Start analysing")
        for i in trange(cnt):
            keys = tuple([self.words[i + j] for j in range(self.n)])
            if keys not in wordDict:
                wordDict[keys] = {}
            wordDict[keys][self.words[i + self.n]] = wordDict[keys].get(self.words[i + self.n], 0) + 1
        return wordDict

    @staticmethod
    def wordFrequency(preDict: dict):
        """
        统计后缀总数
        :param preDict:前后缀单词字典
        :return:后缀总数
        """
        suffixSum = 0
        for value in preDict.values():
            suffixSum += value
        return suffixSum

    def fetchSuffix(self, preDict):
        """
        选取后缀
        :param preDict:前后缀单词字典
        :return:后缀
        """
        randIndex = random.randint(1, self.wordFrequency(preDict))
        for word, value in preDict.items():
            randIndex -= value
            if randIndex <= 0:
                return word

    def generate(self, length: int, curWord: str = ''):
        """
        随机生成文章
        :param length:文章长度
        :param curWord:文章开头字母
        :return:生成的文章
        """
        chain = ''
        if not curWord:
            curWord = random.choice(list(self.wordsDict.keys()))
        else:
            for word in self.wordsDict.keys():
                if curWord == word[0]:
                    curWord = word
            if not isinstance(curWord, tuple):
                curWord = random.choice(list(self.wordsDict.keys()))
        print("Start generating...")
        for i in trange(length):
            if i != 0 and i % 20 == 0:
                chain += '\n'
            for word in curWord:
                chain += word
                chain += ' '
            curWord = self.fetchSuffix(self.wordsDict[curWord])
            key = []
            for word in self.wordsDict.keys():
                if curWord == word[0]:
                    key.append(word)
            curWord = random.choice(key)
        return chain


def main():
    text = Markov(5, 'source/emma.txt')
    wordDictFile = open('source/wordDict.txt', mode='w')
    for key, value in text.wordsDict.items():
        for word in key:
            print(word + ' ', end='', file=wordDictFile)
        print('', file=wordDictFile)
        for key2, value2 in value.items():
            print('\t\t\t' + key2 + ':' + str(value2), file=wordDictFile)
    resultFile = open('result.txt', 'w')
    print(text.generate(2000, 'I'), file=resultFile)


if __name__ == '__main__':
    main()

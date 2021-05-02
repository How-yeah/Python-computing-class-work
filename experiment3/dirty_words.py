import requests
from tqdm import trange
import time
import logging
import re
import random

logging.basicConfig(level=logging.INFO, filename='debug.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'referer': r'https://zuanbot.com/',
}


def drop_duplicates():
    with open(r'experiment3\data\dirty_sentences.txt') as file_obj:
        text = file_obj.read()
        sentences = list(set(text.split('\n')))
    return sentences


def replace_emoji(text: str) -> str:
    r_mother = '[🐴🐎👩🏻]+'
    text = re.sub(r_mother, '妈', text)
    r_chicken = '[🐔]+'
    text = re.sub(r_chicken, '鸡', text)
    r_fist = '[👊]+'
    text = re.sub(r_fist, '拳', text)
    r_granddad = '[👴]+'
    text = re.sub(r_granddad, '爷', text)
    r_bitch = '[⌚️]+'
    text = re.sub(r_bitch, '婊', text)
    r_dog = '[🐶]+'
    text = re.sub(r_dog, '狗', text)
    r_vagina = '[🍺]+'
    text = re.sub(r_vagina, '批', text)
    r_father = '[👨]+'
    text = re.sub(r_father, '爸', text)
    r_fuck = '[☀️]+'
    text = re.sub(r_fuck, '日', text)
    r_shit = '[💩]+'
    text = re.sub(r_shit, '屎', text)
    r_bro = '[🈹]+'
    text = re.sub(r_bro, '割', text)
    r_boom = '[🧨]+'
    text = re.sub(r_boom, '炮', text)
    r_foot = '[🦶]+'
    text = re.sub(r_foot, '脚', text)
    r_class = '[🌿]+'
    text = re.sub(r_class, '操', text)

    return text


logging.info('开始执行脚本')
sentences = drop_duplicates()
origin_count = len(sentences)
s = requests.Session()
count = 1
for i in trange(2000):
    try:
        r = s.get('https://zuanbot.com/api.php?lang=zh_cn', headers=headers)
        if '访问太频繁服务器受不了啦' not in r.text:
            sentences.append(replace_emoji(r.text))
        else:
            logging.warning('第{}条请求过快, 网站开始限制访问'.format(str(i+1)))
            count += 1
            if count > 40:
                logging.warning('已有{}条请求被限制访问, 终止后续请求!'.format(str(count)))
                break
    except:
        logging.warning('第{}条请求失败'.format(str(i+1)))
        count += 1


logging.info('执行结束,共爬取{}条语句'.format(str(len(set(sentences))-origin_count)))
with open(r'experiment3\data\dirty_sentences.txt', 'w') as file_obj:
    for sentence in list(set(sentences)):
        file_obj.write(sentence+'\n')

import requests
from tqdm import trange
import time
import logging
import re

logging.basicConfig(level=logging.INFO, filename='debug.log', format='%(asctime)s - %(levelname)s - %(message)s')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
    'referer': r'https://zuanbot.com/',
}


def replace_emoji(text: str) -> str:
    r_mother = '[🐴🐎]+'
    text = re.sub(r, '妈', text)
    return text


logging.info('开始执行脚本')
s = requests.Session()
sentences = []
for i in trange(1500):
    try:
        r = s.get('https://zuanbot.com/api.php?lang=zh_cn', headers=headers)
        if '访问太频繁服务器受不了啦' not in r.text:
            sentences.append(r.text)
        else:
            logging.warning('第{}条请求过快, 网站开始限制访问, 终止后续请求!'.format(str(i)))
            break
    except:
        logging.warning('第{}条请求失败'.format(str(i)))

logging.info('执行结束')
with open(r'experiment3\data\dirty_sentences.txt', 'a') as file_obj:
    for sentence in sentences:
        file_obj.write(sentence+'\n')

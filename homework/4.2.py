import re


def replace_I2i(text):
    pattern = re.compile(r'\w[I]\w')
    return re.sub(pattern, 'i', text)

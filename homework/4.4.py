import re


def get_3letters_words(text, num: int = 3):
    pattern = re.compile(r'\b\w{3}\b')
    words = set(re.findall(pattern, text))
    for word in words:
        print(word, end=' ')


text = '''
We were both young when i first saw you
i closed my eyes and the flashback starts
i'm standing there
On a balcony in summer air
See the lights see the party the ball gowns
i see you make your way through the crowd
And say hello
Little did i know
That you were Romeo you were throwing pebbles
And my daddy said stay away from Juliet
And i was crying on the staircase
Begging you please don't go
And i said
Romeo take me somewhere we can be alone
i'll be waiting all there's left to do is run
You'll be the prince and i'll be the princess
It's a love story
Baby just say yes
'''

get_3letters_words(text)

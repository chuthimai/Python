# PY03007 - XỬ LÝ VĂN BẢN

import re

string = ""

while True:
    try:
        string += " " + input().lower().strip()
    except EOFError:
        break


sentences = re.split(r'[.?!]', string)

for sentence in sentences:
    sentence = sentence.strip()
    words = re.split(r" +", sentence)
    sentence = ""
    is_first = True
    for word in words:
        if is_first:
            sentence += word.title()
            is_first = False
        else:
            sentence += word
        sentence += " "
    sentence.replace(" ,", ",")
    sentence.replace(" :", ":")
    print(sentence)





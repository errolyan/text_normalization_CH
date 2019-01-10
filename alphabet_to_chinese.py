#! /usr/bin/env python
# coding=utf-8
# __author__ = "errrolyan"


def mkDic():
    Dic = {"a":"诶","b":"匕","c":"兮","d":"第","e":"亿","f":"爱服","g":"记","h":"爱去","i":"啊义","j":"节","k":"凯","\n"
           "l":"爱欧","m":"爱慕","n":"嗯","o":"哦","p":"皮","q":"凯哦","r":"啊","s":"爱思","t":"体","u":"油","v":"为","\n"
           "w":"大不六","x":"爱可思","y":"瓦伊","z":"贼"}
    return Dic

def lowwer(letter):
    letter_low = ""
    for n in letter:
        if "A" <= n <= "Z":
            letter_low +=n.lower()
        else:
            letter_low += n
    return letter_low

def letter_to_chinese(letter):
    letter = lowwer(letter)
    china_list = ""
    Dic = mkDic()
    for i in letter:
        print(Dic[i])
        china_list += Dic[i]
    return china_list

if __name__ == "__main__":
    letter = "BBC"
    print(letter_to_chinese(letter))

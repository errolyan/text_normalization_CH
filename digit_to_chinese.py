#! /usr/bin/env python
# coding=utf-8
# __author__ = "errrolyan"


import types

_MAPPING = ('零', '一', '二', '三', '四', '五', '六', '七', '八', '九',)
_P0 = ('', '十', '百', '千',)
_S4, _S8, _S16 = 10 ** 4, 10 ** 8, 10 ** 16
_MIN, _MAX = 0, 9999999999999999

def dot_back_to_chinese4(num):
    result = "点"
    if num =="":
        return ""
    else:
        for i in range(len(num)):
            result += _MAPPING[int(num[i])]
        return result

def _to_chinese4(num):
    '''转换[0, 10000)之间的阿拉伯数字
    '''
    assert (0 <= num and num < _S4)
    if num < 10:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = int(num / 10)
        lst.append(num)
        c = len(lst)  # 位数
        result = ''
        for idx, val in enumerate(lst):
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += '零'
        return result[::-1].replace('一十', '十')

def _to_chinese8(num):
    assert (num < _S8)
    to4 = _to_chinese4
    if num < _S4:
        return to4(num)
    else:
        mod = _S4
        high, low = num / mod, num % mod
        if low == 0:
            return to4(high) + '万'
        else:
            if low < _S4 / 10:
                return to4(high) + '万零' + to4(low)
            else:
                return to4(high) + '万' + to4(low)

def _to_chinese16(num):
    assert (num < _S16)
    to8 = _to_chinese8
    mod = _S8
    high, low = num / mod, num % mod
    if low == 0:
        return to8(high) + '亿'
    else:
        if low < _S8 / 10:
            return to8(high) + '亿零' + to8(low)
        else:
            return to8(high) + '亿' + to8(low)

def digit_to_chinese(num):
    num_str = str(num)
    numlist = num_str.split(".")
    if len(numlist) ==2:
        dotnumstr = numlist[1]
        dotresult = dot_back_to_chinese4(dotnumstr)
        num = int(numlist[0])
        if num < _MIN or num > _MAX:
            raise OutOfRangeError(u'%d out of range[%d, %d)' % (num, _MIN, _MAX))
        if num < _S4:
            return _to_chinese4(num) + dotresult
        elif num < _S8:
            return _to_chinese8(num) + dotresult
        else:
            return _to_chinese16(num) + dotresult
    else:
        num = int(numlist[0])
        if num < _MIN or num > _MAX:
            raise OutOfRangeError(u'%d out of range[%d, %d)' % (num, _MIN, _MAX))
        if num < _S4:
            return _to_chinese4(num)
        elif num < _S8:
            return _to_chinese8(num)
        else:
            return _to_chinese16(num)


if __name__ == '__main__':
    print(digit_to_chinese(88.55) )
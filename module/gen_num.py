from fractions import Fraction
import random


#生成自然数/真分数
def gen_num(mod):
    if mod <= 0: return Fraction(0, 1)
    bit = random.randint(1, 10)

    if mod == 1:
        down = random.randint(2, 10)
        up = random.randint(1, down - 1)
        return Fraction(up, down)

    #自然数
    if bit >= 1 and bit <= 5:
        return Fraction(random.randint(0, mod - 1), 1)
    #小于1的真分数
    elif (bit >= 6 and bit <= 8):
        down = random.randint(2, max(5, mod))
        up = random.randint(1, down - 1)
        return Fraction(up, down)
    #自然数/真分数(真分数比例大)
    else:
        down = random.randint(2, max(5, mod))
        up = random.randint(down, mod * down - 1)
        return Fraction(up, down)
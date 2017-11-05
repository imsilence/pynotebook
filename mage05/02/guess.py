#encoding: utf-8

import random

rand_num = random.randint(0, 100)

max_guess_count = 5
guess_count = 0

while True:
    guess_num = input('please input your guess:')
    guess_num = int(guess_num)
    guess_count += 1

    if rand_num == guess_num:
        print('你猜对了')
        break
    elif rand_num < guess_num:
        print('你猜大了')
    else:
        print('你猜小了')

    if guess_count >= max_guess_count:
        print('你真笨, ', max_guess_count, '次都没猜对, 正确值是:', rand_num)
        break
    else:
        print('剩余猜测机会:', max_guess_count - guess_count, '次')

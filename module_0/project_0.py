# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:47 2021

@author: Roman
"""

import numpy as np

def game_core_v3(number):
    '''Угадать от 0 до 100. Начинаем с 50 и по условию или прибавляем, или отнимаем половину 50. Потом половину половины и так далее, 
    пока число не стане  - more (или меньше - less) загаданного, параллельно сохраняя предпослений вариант. 
    После этого находим между ними середину, пока не угадаем'''
    count = 1
    predict = 50
    flag_less = 1
    flag_more = 1

    while number != predict:
        count+=1
        
        # Если число больше:
        if number > predict:
            flag_less = 0
            if flag_more:
                previous_predict = predict
                predict = predict + int((100-predict) / 2)
            else:
                predict = int(np.mean([predict, previous_predict]))
                flag_less = 1
        # Если число меньше:
        elif number < predict:
            flag_more = 0
            if flag_less:
                previous_predict = predict
                predict = predict - int(predict/2)
            else:
                predict = int(np.mean([predict, previous_predict]))
                flag_more = 1

    return(count) # выход из цикла, если угадали
   

def score_game(game_core):

    count_ls = [1]
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,100, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)


score_game(game_core_v3)
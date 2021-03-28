# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:27:47 2021

@author: Roman
"""

import numpy as np

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50
    less = 1
    more = 1

    while number != predict:
        count+=1

        if number > predict:
            less = 0
            if more:
                step_back_predict = predict
                predict = predict + int((100-predict) / 2)
            else:
                predict = int(np.mean([predict, step_back_predict]))
                less = 1

        elif number < predict:
            more = 0
            if less:
                step_back_predict = predict
                predict = predict - int(predict/2)
            else:
                predict = int(np.mean([predict, step_back_predict]))
                more = 1

    return(count) # выход из цикла, если угадали
   

def score_game(game_core):

    count_ls = [1]
    #np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,100, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core_v3)
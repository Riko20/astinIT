import time
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

#######   4  ######

class Gambler:
    df = pd.DataFrame()
    sequence_win = {}

    def __init__(self, start_money, aim_fortune, probability):
        self.probability = probability
        self.start_money = start_money
        self.aim_fortune = aim_fortune
        self.game_key = 'start:{}, fortune:{}, probability:{}'.format(self.start_money, self.aim_fortune, self.probability)


    def change_sequence(self, new_start_money, new_aim_fortune, new_probability):
        self.start_money = new_start_money
        self.aim_fortune = new_aim_fortune
        self.probability = new_probability
        self.game_key = 'start:{}, fortune:{}, probability:{}'.format(self.start_money, self.aim_fortune,
                                                                      self.probability)

    def _play_game(self):
        money = self.start_money
        while money != 0 and money != self.aim_fortune:
            win_or_lose = np.random.choice(np.arange(0, 2), p=[1 - self.probability, self.probability])
            if win_or_lose > 0:
                money += 1
            else:
                money -= 1
        if money == 0:
            return 0
        else:
            return 1

    def _save_result(self, n_times):
        save_array = []
        for n in range(n_times):
            win = self._play_game()
            save_array.append(win)
        sequence = self.game_key
        self.sequence_win[sequence] = save_array
        return self.sequence_win

    def fill_dataframe(self, n_times):
        array_of_columns = []
        sequence_win_dict = self._save_result(n_times)
        self.df[self.game_key] = Series(sequence_win_dict[self.game_key])
        for column in self.df:
            array_of_columns.append(column)

        return self.df

    def analyze_results(self):
        wins_to_loses = self.df.groupby(self.df[self.game_key]).size()
        try:
            loses = wins_to_loses[0]
        except KeyError:
            return '100% victory'
        try:
            wins = wins_to_loses[1]
        except KeyError:
            return '100% for ruin'

        percentage_ruin = (1 - wins / (loses + wins)) * 100
        return 'for {} percentage for ruin is {} %'.format(self.game_key, percentage_ruin)



Vasya = Gambler(100, 1000000, 0.5)
Vasya.fill_dataframe(100)
first_sequence_game = Vasya.analyze_results()
# Vasya.change_sequence(2, 4, 0.5)
# Vasya.fill_dataframe(100)
# second_sequence_game = Vasya.analyze_results()
# print('First game: {}, second game: {}'.format(first_sequence_game, second_sequence_game))



# money = 2
# fortune = 4
# probability = 0.5
#
# time_start = time.time()
# def play_game(money, fortune, probability):
#     while money != 0 and money != fortune:
#         win_or_lose = np.random.choice(np.arange(0, 2), p=[1-probability, probability])
#         if win_or_lose > 0:
#             print('yoy')
#             money += 1
#         else:
#             print('dich')
#             money -= 1
#     print(money)
#     if money == 0:
#         return 0
#     else:
#         return 1
#
# play_game(money, fortune, probability)
#
# def save_result(money, fortune, probability, n_times):
#     save_array = []
#     sequence_win = {}
#     for n in range(n_times):
#         win = play_game(money, fortune, probability)
#         save_array.append(win)
#     sequence = 'start:{}, fortune:{}, probability:{}'.format(money, fortune, probability)
#     sequence_win[sequence] = save_array
#     return sequence_win
#
# # print(save_result(money, fortune, probability, 100))
#
# df = pd.DataFrame()
# def fill_dataframe(money, fortune, probability, n_times, df):
#     array_of_columns = []
#     key_of_df = 'start:{}, fortune:{}, probability:{}'.format(money, fortune, probability)
#     sequence_win_dict = save_result(money, fortune, probability, n_times)
#     df[key_of_df] = Series(sequence_win_dict[key_of_df])
#     for column in df:
#         array_of_columns.append(column)
#
#     return df
#
# def analyze_results(money, fortune, probability, df):
#     key_of_df = 'start:{}, fortune:{}, probability:{}'.format(money, fortune, probability)
#     wins_to_loses = df.groupby(df[key_of_df]).size()
#     try:
#         percentage_ruin =(1 - wins_to_loses[1] / (wins_to_loses[0] + wins_to_loses[1])) * 100
#         return 'for {} percentage for ruin is {} %'.format(key_of_df, percentage_ruin)
#     except KeyError:
#         return 'Zero percents'
#
#
#
#
# print(fill_dataframe(money, fortune, probability, 100, df))
# # print(fill_dataframe(10,40,0.5, 10, df))
# wins_to_loses = df.groupby(df['start:{}, fortune:{}, probability:{}'.format(money, fortune, probability)]).size()
# print(analyze_results(money, fortune, probability, df))
# time_stop = time.time()
# print(time_stop-time_start)
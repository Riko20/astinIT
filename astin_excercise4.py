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
        return 'for {} percentage for ruin is {:.2f} %'.format(self.game_key, percentage_ruin)



Vasya = Gambler(2, 4, 0.5)
Vasya.fill_dataframe(100)
first_sequence_game = Vasya.analyze_results()
Vasya.change_sequence(10, 100, 0.5)
Vasya.fill_dataframe(100)
second_sequence_game = Vasya.analyze_results()
print('First game: {}, second game: {}'.format(first_sequence_game, second_sequence_game))

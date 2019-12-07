from collections import namedtuple


class TennisGame:
    p1 = "p1"
    p2 = "p2"

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.__score_history = []
        self.__p1_score = 0
        self.__p2_score = 0
        self.__p1_games_won = 0
        self.__p2_games_won = 0

    def p1_score(self):
        self.__score_history.append(self.p1)

    def p2_score(self):
        self.__score_history.append(self.p2)

    @staticmethod
    def player_scored(player_score, opponent_score, player_games_won, opponent_games_won):
        if player_score < 30:
            return (player_score + 15, opponent_score), (player_games_won, opponent_games_won)
        else:
            if player_score == 40:
                if opponent_score == 45:
                    return (player_score, 40), (player_games_won, opponent_games_won)
                elif opponent_score == 40:
                    return (player_score + 5, opponent_score), (player_games_won, opponent_games_won)
                else:
                    return (0, 0), (player_games_won + 1, opponent_games_won)
            elif player_score == 45:
                return (0, 0), (player_games_won + 1, opponent_games_won)
            else:
                return (player_score + 10, opponent_score), (player_games_won, opponent_games_won)

    def get_games_won(self):
        return self.__p1_games_won, self.__p2_games_won

    def get_score(self):
        for s in self.__score_history:
            if s == self.p1:
                res = self.player_scored(self.__p1_score, self.__p2_score, self.__p1_games_won, self.__p2_games_won)
                self.__p1_score = res[0][0]
                self.__p2_score = res[0][1]
                self.__p1_games_won = res[1][0]
                self.__p2_games_won = res[1][1]
            else:
                res = self.player_scored(self.__p2_score, self.__p1_score, self.__p2_games_won, self.__p1_games_won)
                self.__p1_score = res[0][1]
                self.__p2_score = res[0][0]
                self.__p1_games_won = res[1][1]
                self.__p2_games_won = res[1][0]

        return self.__p1_score, self.__p2_score

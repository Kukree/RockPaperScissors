import random
import os

clear = lambda: os.system('cls')


class Game:

    messages = {'commandlist': "\n[1] - Start \n[2] - Help\n",
    'choice': '[1] - Rock\n[2] - Paper \n[3] - Scissors\n',
    'prefix': '> ',
    'welcome': 'Welcome to Rock Paper Scissors game! Enter a command below: ',
    'unknowncommand': '\nUnknown command!\n',
    'makeachoice': "Make a choice!\n",
    'player_win': 'You win!\n',
    'computer_win': 'You lose!\n',
    'draw': 'A draw!\n'}

    def player_turn(self):
        clear()
        print(self.messages['makeachoice'])
        print(self.messages['choice'])
        choice = int(input(self.messages['prefix']))
        return choice

    def computer_turn(self):
        choice = random.randint(1, 3)
        return choice

    def calculating(self, player, computer):
        if player == 1 and computer == 3:  # Если выбор игрока - камень, а выбор компьютера - ножницы
            win = self.messages['player_win']
        elif player == 2 and computer == 1:  # Если выбор игрока - бумага, а выбор компьютера - камень
            win = self.messages['player_win']
        elif player == 3 and computer == 2:  # Если выбор игрока - ножницы, а выбор компьютера - бумага
            win = self.messages['player_win']
        elif computer == 1 and player == 3:  # Если выбор компьютера - камень, а выбор игрока - ножницы
            win = self.messages['computer_win']
        elif computer == 2 and player == 1:  # Если выбор компьютера - бумага, а выбор игрока - камень
            win = self.messages['computer_win']
        elif computer == 3 and player == 2:  # Если выбор компьютера - ножницы, а выбор игрока - бумага
            win = self.messages['computer_win']

        # Ничья...
        elif computer == 1 and player == 1:
            win = self.messages['draw']
        elif computer == 2 and player == 2:
            win = self.messages['draw']
        elif computer == 3 and player == 3:
            win = self.messages['draw']
        return win


if __name__ == "__main__":
    game = Game()
    while True:
        print(game.messages['welcome'])  # Приветствие
        print(game.messages['commandlist'])  # Список команд
        command = input(game.messages['prefix'])
        if command == '1':  # Начать игру
            clear()
            player_choice = game.player_turn()  # Ход игрока
            if player_choice >= 4 or player_choice < 1:
                clear()
                print(game.messages['unknowncommand'])
            else:
                clear()
                computer_choice = game.computer_turn()  # Ход компьютера
                winner = game.calculating(player_choice, computer_choice)  # Расчет победителя
                print(winner)
        elif command == '2':  # Помощь
            pass
            # TODO: Сделать окно помощи с правилами игры.
        else:  # Неизвестная команда
            clear()
            print(game.messages['unknowncommand'])

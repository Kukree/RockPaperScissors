#!usr/bin/env python3

import random
import os

clear = lambda: os.system('clear')


class Game:

    messages = {'commandlist': "\n[1] - Start \n[2] - Help\n",
    'choice': '[1] - Rock\n[2] - Paper \n[3] - Scissors\n',
    'prefix': '> ',
    'welcome': 'Rock Paper Scissors \nEnter a command below: ',
    'unknowncommand': '\nUnknown command!\n',
    'makeachoice': "Make a choice!\n",
    'player_win': 'You win!\n',
    'computer_win': 'You lose!\n',
    'draw': 'A draw!\n',
    'computer_choice': 'Computer choice: ',
    'player_choice': 'Your choice: ',
    'rock': 'Rock',
    'paper': 'Paper',
    'scissors': 'Scissors',
    'help': '''
    Welcome to Rock Paper Scissors game by Evgeniy Kuleshov (kukree) 
    To start the game you must press the button 1 in the command line and press the ENTER key. 
    Then select your item (rock, paper or scissors). 
    After your turn, a message will be displayed about the choice of computer, your choice and the winner \n'''}

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
        if computer == player:  # Ничья
            win = self.messages['draw']
        elif player == 1 and computer == 3:  # Если выбор игрока - камень, а выбор компьютера - ножницы
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
        return win

    def choice_converter(self, choice):
        if choice == 1:
            choiceSTR = self.messages['rock']
        if choice == 2:
            choiceSTR = self.messages['paper']
        if choice == 3:
            choiceSTR = self.messages['scissors']
        return choiceSTR


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
                computer_choice_output = game.messages['computer_choice'] + game.choice_converter(computer_choice)  # Преобразование числового хода компьютера в строковый
                player_choice_output = game.messages['player_choice'] + game.choice_converter(player_choice)  # Преобразование числового хода игрока в строковый
                print(computer_choice_output)
                print(player_choice_output + "\n")
                print(winner)
        elif command == '2':  # Помощь
            clear()
            print(game.messages['help'])
        else:  # Неизвестная команда
            clear()
            print(game.messages['unknowncommand'])

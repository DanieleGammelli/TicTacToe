#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:04:48 2018

@author: danielegammelli
"""
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random


class Match():
    """Represents a 2-player match of 3x3 tic-tac-toe."""
    
    def __init__(self,n_human = 2, n_ai = 0):
        """Initialize a match with an empty board, 2 players, no declared winner
        and a start time."""
        
        self.board = Board()
        self.players = []
        if n_human + n_ai < 2:
            return "Not enough players, 2 are needed."
        elif n_human + n_ai > 2:
            return "Too many players, 2 are needed."
        else:
            for i in range(n_human):
                self.players.append(HumanPlayer(count=i+1))
            for i in range(n_ai):
                self.players.append(AiPlayer(count=i+1))
        self.winner = None

        self.time = time.time()
    
    def play(self):
        """Begins the match."""
        move = 1
        check = 0
        player1 = self.players[0]
        player2 = self.players[1]
        print('\n')
        print('============== GAME START ===============\n\n')
        print('Player 1: Name -> %s, Sign -> %s\nPlayer 2: Name -> %s, Sign -> %s\n'
              %(player1.name, player1.sign, player2.name, player2.sign))
        turn = random.randint(0,1)
        while True:
            print('\n')
            print('===== CURRENT BOARD ====\n')
            print(self.board.state)
            print('\n========================\n\n')
            print('|| Player %s turn'%(turn+1))
            self.players[turn].make_move(self.board)
            if move != 1:
                check = self.board.check_state()
            if check == 1:
                print('\n')
                print('===== FINAL BOARD ====\n')
                print(self.board.state)
                print('\nGame time: %i:%i min'%(round((time.time() - self.time)/60),
                                                (time.time() - self.time)%60))
                self.board = Board()
                break
            if turn == 0:
                turn = 1
            else:
                turn = 0
            move += 1

class Board():
    """Represents a 3x3 tic-tac-toe board."""
    
    def __init__(self):
        """Initializes an empty board."""
        self.state = np.empty((3, 3), dtype=str)
        
    def check_state(self):
        """Checks if match reached an ending stage: win or tie."""
        #Check if X wins
        row_count_x, col_count_x, diag1_x, diag2_x = self.non_diag_count('X')
        row_count_o, col_count_o, diag1_o, diag2_o = self.non_diag_count('O')
        if np.sum(row_count_x == 3) == 1 or np.sum(col_count_x  == 3) == 1 or diag1_x == 3 or diag2_x == 3:
            print("\n==============================\n")
            print("MATCH IS OVER. X Wins!\n")
            print("==============================\n")
            return 1
        
        elif np.sum(row_count_o == 3) == 1 or np.sum(col_count_o  == 3) == 1 or diag1_o == 3 or diag2_o == 3:
            print("\n==============================\n")
            print("MATCH IS OVER. O Wins!\n")
            print("==============================\n")
            return 1
        
        elif np.sum(self.state == '') == 0:
            print("\n==============================\n")
            print("MATCH IS OVER. It's a tie!\n")
            print("==============================\n")
            return 1
        
        
    def non_diag_count(self, sign):
        """Counts occurencies of any sign on the the two axis."""
        row_count = np.sum(self.state == sign, axis = 1)
        col_count = np.sum(self.state == sign, axis = 0)
        diag1 = np.sum(self.state.diagonal() == sign)
        diag2 = np.sum(np.array([self.state[2,0], self.state[1,1], self.state[0,2]]) == sign)
        
        return row_count, col_count, diag1, diag2
    
    def visualize_board(self):
        plt.figure()
        ax = plt.axes()
        plt.plot([1,1],[0,3], c = 'k')
        plt.plot([2,2],[0,3], c = 'k')
        plt.xlim([0,3])
        plt.ylim([0,3])
        plt.plot([0,3],[1,1], c = 'k')
        plt.plot([0,3],[2,2], c = 'k')
#        plt.text(0.5,0.5, 'X', fontsize = 20)

class Player():
    """Represents a tic-tac-toe player. Can be either Human or Ai."""
    
    def __init__(self, name='Player', count=1):
        self.count = count
        self.name = name+str(self.count)
        if self.count%2 == 0:
            self.sign = 'X'
        else:
            self.sign = 'O'
        self.count += 1

class HumanPlayer(Player):
    """Human Player."""
    
    def make_move(self, board):
        print('|| Declare the next move. Indicate row and column number (from 0 to 2)')
        while True:
            self.x = int(input('Insert Row Number: '))
            self.y = int(input('Insert Column Number: '))
            if board.state[self.x][self.y] != '':
                print('Position already taken. Choose different one.')
            else:
                board.state[self.x][self.y] = self.sign
                break

if __name__ == '__main__':
    match = Match()
    match.play()
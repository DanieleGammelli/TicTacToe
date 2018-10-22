#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:04:48 2018

@author: danielegammelli
"""
import os
import time
import numpy as np
import pandas
import matplotlib.pyplot as plt
import seaborn as sns


class Match():
    """Represents a 2-player match of 3x3 tic-tac-toe."""
    
    def __init__(self,n_human = 2, n_ai = 0):
        """Initialize a match with an empty board, 2 players, no declared
        and a start time."""
        
        self.board = Board()
        self.players = []
        if n_human + n_ai < 2:
            return "Not enough players, 2 are needed."
        elif n_human + n_ai > 2:
            return "Too many players, 2 are needed."
        else:
            for i in range(n_human):
                self.players.append(Human())
            for i in range(n_ai):
                self.players.append(Ai())
        self.winner = None
        self.time = time.time()
    
    def run():
        """Begins the match."""
        return None

class Board():
    """Represents a 3x3 tic-tac-toe board."""
    
    def __init__(self):
        """Initializes an empty board."""
        self.state = np.empty((3,3), dtype = str)
        
    def checkState(self):
        """Checks if match reached an ending stage: win or tie."""
        #Check if X wins
        row_count_x, col_count_x, diag1_x, diag2_x = self.nonDiagCount('X')
        row_count_o, col_count_o, diag1_o, diag2_o = self.nonDiagCount('O')
        if np.sum(row_count_x == 3) == 1 or np.sum(col_count_x  == 3) == 1 or diag1_x == 3 or diag2_x == 3:
            print("\n==============================\n")
            print("MATCH IS OVER. Player X Wins!\n")
            print("==============================\n")
        elif np.sum(row_count_o == 3) == 1 or np.sum(col_count_o  == 3) == 1 or diag1_o == 3 or diag2_o == 3:
            print("\n==============================\n")
            print("MATCH IS OVER. Player O Wins!\n")
            print("==============================\n")
        elif np.sum(self.state == '') == 0:
            print("\n==============================\n")
            print("MATCH IS OVER. It's a tie!\n")
            print("==============================\n")
        
    def nonDiagCount(self, sign):
        """Counts occurencies of any sign on the the two axis."""
        row_count = np.sum(self.state == sign, axis = 1)
        col_count = np.sum(self.state == sign, axis = 0)
        diag1 = self.state.diagonal()
        diag2 = np.sum(np.array([self.state[2,0], self.state[1,1], self.state[0,2]]) == sign)
        
        return row_count, col_count, diag1, diag2
    
    def visualize_board(self):
        ax = plt.axes()
        plt.plot([1,1],[0,3], c = 'k')
        plt.plot([2,2],[0,3], c = 'k')
        plt.xlim([0,3])
        plt.ylim([0,3])
        plt.plot([0,3],[1,1], c = 'k')
        plt.plot([0,3],[2,2], c = 'k')
        plt.text(0.5,0.5, 'X', fontsize = 20)
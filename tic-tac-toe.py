#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:05:36 2020

@author: pundir
"""
#FIRST EVER TIC-TAC-TOE GAME

def drawfield(field):
    for row in range(5):
        if row%2 == 0:
            practicalrow = int(row/2)
            for column in range(5):
                if column%2 == 0:
                    practicalcolumn = int(column/2)
                    if column != 4:
                        print(field[practicalcolumn][practicalrow],end="")
                    else:
                        print(field[practicalcolumn][practicalrow])
                else:
                    print("|",end="")
        else:
            print("-----")
            
            
player=1
currentfield = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
while(True):
    print("Players Turn: ",player)
    moverow = int(input("Please Enter The Row: "))
    movecolumn = int(input("Please Enter The Column: "))
    if player == 1:
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "X"
            player = 2
    else:
        if currentfield[movecolumn][moverow] == " ":
            currentfield[movecolumn][moverow] = "O"
            player = 1
    drawfield(currentfield)
#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PRINTING THE BOARD
from IPython.display import clear_output
def display_board(board):
    
    print(board[6]+'|'+board[7]+'|'+board[8])
    print('-|-|-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-|-|-')
    print(board[0]+'|'+board[1]+'|'+board[2])
    


# In[2]:


import random
def player_input():
    
    
    c1='wrong'
    while c1 not in ['X','O']:
        c1=input('Player-1 please choose your marker(X OR O):')
        if c1 not in ['X','O']:
            print("Enter the correct marker!")
    if c1=='O':
        c2='X'
    else:
        c2='O'
    print("Marker for player 2:{}".format(c2))
    return [c1,c2]
    


# In[3]:


def place_marker(board, marker, position):
     
    board[position]=marker
    display_board(board)
    


# In[4]:


def win_check(b):
    
    x_mark=['X','X','X']
    o_mark=['O','O','O']
    
    if ((b[0:3]==x_mark) or (b[3:6]==x_mark) or (b[6:]==x_mark)):
        print(" X mark is the WINNER!!")
        return True
    elif ((b[0:3]==o_mark) or (b[3:6]==o_mark) or (b[6:]==o_mark)):
        print(" O mark is the WINNER!!")
        return True
    elif (([b[8],b[4],b[0]]==x_mark) or ([b[2],b[4],b[6]]==x_mark)):
        print(" X mark is the WINNER!!")
        return True
    elif (([b[8],b[4],b[0]]==o_mark) or ([b[2],b[4],b[6]]==o_mark)):
        print(" O mark is the WINNER!!")
        return True
    elif (([b[6],b[3],b[0]]==x_mark) or  (([b[7],b[4],b[1]])==x_mark) or  (([b[8],b[2],b[5]]==x_mark))):
        print(" X mark is the WINNER!!")
        return True
    elif (([b[6],b[3],b[0]]==o_mark) or  (([b[7],b[4],b[1]])==o_mark) or  (([b[8],b[2],b[5]]==o_mark))):
        print(" O mark is the WINNER!!")
        return True
    else:
        return False
        
    
        
                      
                      


# In[5]:


import random

def choose_first():
    p=random.randint(1,2)
    return p
    pass


# In[6]:


def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
   
    


# In[7]:


def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False
    


# In[8]:


def player_choice(board):
    num_list=['0','1','2','3','4','5','6','7','8']
    display_board(num_list)
    position='wrong'
    #FIRST TAKE THE CORRECT INPUT FOR POSITION
    while position not in num_list:  
        position=input("Enter the position:")
        if position not in num_list:
            print("Enter the correct position!!")
        else:
         #NOW CHECK IF POSITION IS AVAILABLE
            y=int(position)
            k=space_check(board,y)
            if k==True:
                return y
                
            
            else:
                print("Position not available!!Please choose another position")
                position='wrong'
                
        
        
    


# In[9]:


def replay():
    
    reply='wrong'
    while reply not in ['Y','N']:
        reply=input("Do you wish to continue?(Y/N)?")
        if reply not in ['Y','N']:
            print("Please enter the correct input!")
    if reply=='Y':
        return True
    else:
        return False
                            
    


# In[ ]:


import random
game_on=True
while game_on==True:
    print('Welcome to Tic Tac Toe!')
#------------------------DISPLAYING BOARD----------------------------------------#
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    num_list=['0','1','2','3','4','5','6','7','8']
    display_board(board)
#------------------------CHOOSING MARKERS----------------------------------------#
    markers=player_input()
#------------------------GENERATING WHO WILL PLAY FIRST--------------------------#
    p1=choose_first()
    if p1=='1':
        p2='2'
        m1=markers[0]
        m2=markers[1]
    else:
        p2='1'
        m1=markers[1]
        m2=markers[0]

    print("Player-{} will begin the game.".format(p1))
#------------------------GAME START---------------------------------------------#
    board_check=full_board_check(board)
    while board_check==False:#till the time board does not get full keep asking for players input
        player_no='wrong'
        while player_no not in ['1','2']:
            
            player_no=input("Player Number?")
            if player_no=='1':
                m1=markers[0]
                pos1=player_choice(board)
                place_marker(board, m1, pos1)
            elif player_no=='2':
                m1=markers[1]
                pos1=player_choice(board)
                place_marker(board, m1, pos1)
            if player_no not in ['1','2']:
                print("Enter correct player number!!")
         
            
            
    
        
        
        board_check=full_board_check(board)
        
        #-----------------------WIN CONDITION--------------------------#
        out=win_check(board)
        if out==True:
            break
        
        
        #--------------------------------------------------------------#
    if board_check==True:
        print("Game tie!!")

    
    game_on=replay()

if game_on==False:
    print("Thank you for playing!")

            
        


# In[ ]:






#Sample ticTacToe
# this python doesn't contain any exception handling
print('''
Grid positions are going to be

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8

''')

#Function to display Base line
def dispB():
    print('---------')


#Function to display grid (Current status)
def display(grid):
    for i in range(0,3):
      st=''
      for j in range(0,3):
          if(grid[i][j]=='-1'):
              st+=' '
          else:
              st+=grid[i][j];
          if(j!=2):
              st+=' |'
      print(st)
      if(i!=2):
        dispB()

#Function to fill the grid using user input
def fill(ind,grid,sym):
    ret=False
    if(0<=ind<=2):
        if(grid[0][ind]=='-1'):
           grid[0][ind]=sym
           ret=True
    elif(3<=ind<=5):
        if(grid[1][ind-3]=='-1'):
           grid[1][ind-3]=sym
           ret=True
    else:
        if(grid[2][ind-6]=='-1'):
           grid[2][ind-6]=sym
           ret=True
    return ret


#Function to ask for user input for the game
def play(player,grid):
    cur=False
    if(player==1):
        while(not cur):
          inp = int(input("Player {} please enter the position where you want {} from (0-8) ".format(1,S_Pl1)))
          cur=fill(inp,grid,S_Pl1)
    else:
        while(not cur):
           inp = int(input("Player {} please enter the position where you want {} from (0-8) ".format(2, S_Pl2)))
           cur=fill(inp, grid, S_Pl2)


#Function to check if all the values have already been entered
def check(grid):
    for i in range(0,3):
        for j in range(0,3):
            if(grid[i][j]=='-1'):
                return True
    return False

#Function to check whether a player has won
def checkwin(grid,sym):
    for i in range(0,3):
        if(grid[i][0]==sym and grid[i][1]==sym and grid[i][2]==sym):
            return True
        if(grid[0][i]==sym and grid[1][i]==sym and grid[2][i]==sym):
            return True

    if(grid[0][0]==sym and grid[1][1]==sym and grid[2][2]==sym):
        return True
    if(grid[0][2]==sym and grid[1][1]==sym and grid[2][0]==sym):
        return True
    return False





S_Pl1= input("Please enter the symbol you want to take form 'O' or 'X' ")

while(not(S_Pl1=='X' or S_Pl1=='O')):
    S_Pl1=input("Please enter valid value from 'O' or 'X' ")

S_Pl2='O' if (S_Pl1=='X') else 'X'

grid=[['-1','-1','-1'],['-1','-1','-1'],['-1','-1','-1']]
print("Please start the game ")
display(grid)

cp=1
win=-1
while(check(grid)):
    play(cp,grid)
    display(grid)
    if(checkwin(grid, S_Pl1 if(cp==1) else S_Pl2)):
        win=cp
        break
    cp= 1 if(cp==2) else 2

print("Game has ended and winner is Player {}".format(cp if(win!=-1) else 'None'))





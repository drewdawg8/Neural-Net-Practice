import copy
from time import sleep

class Board:
    cleanBoard = [[" - ", " - ", " - "],[" - ", " - ", " - "],[" - ", " - ", " - "]]


    def __init__(self,players):
        self.boardState = [[" - ", " - ", " - "],[" - ", " - ", " - "],[" - ", " - ", " - "]]
        self.players = players

    def checkWin(self):
        ''' checks for a win/draw '''
        string1 = self.string()
        top, middle, bottom = string1[0:3], string1[3:6], string1[6:]
        varis = [top,middle,bottom]
        # This checks horizontal wins
        for i in range(0,3):
            if top[i] == middle[i] == bottom[i] != "0":
            #    print(self)
                return top[i]
        #Vertical Wins
        for i in varis:
            if i.count("1") == 3:
                #print(self)
                return "1"
            elif i.count("2") == 3:
            #    print(self)
                return "2"
        #Diaganl wins
        if top[0] == middle[1] == bottom[2] != "0":
            #print(self)
            return top[0]
        elif top[2] == middle[1] == bottom[0] != "0":
        #    print(self)
            return top[2]
        #Checks for a draw
        if string1.count("0") == 0:
        #    print(self)
            return "Draw"
        return "cont"

    def update(self, coordinate, letter):
        ''' update boardState '''
        x = coordinate[0]
        y = coordinate[1]
        if(self.boardState[coordinate[0]][coordinate[1]] == " - "):
            self.boardState[coordinate[0]][coordinate[1]] = " " + letter  + " "
        #print(self)

    def validMove(self,action):
        if (self.boardState[action[0]][action[1]]) != " - ":
            return False
        return True

    def string(self):
        '''
            Converts the board into a string of 0,1,2 to help with readability
            0 = - , 1 = O , 2 = X
        '''
        string1 = ""
        board = self.boardState
        for i in range(3):
            for j in range(3):
                if "-" in board[i][j]:
                    string1 += "0"
                elif "O" in board[i][j]:
                    string1 += "1"
                else:
                    string1 += "2"
        return string1

    def clean(self):
        self.boardState = copy.deepcopy(self.cleanBoard)

    def win(self,entity1,entity2,winner):
        print("\n" + str(self))
        if (winner == "2"):
            entity1.wins += 1
            print(entity1.eType + " " + entity1.name + " wins!\n")
            if (entity1.eType == "bot"):
                entity1.reward(1.7,self)
            if (entity2.eType == "bot"):
                entity2.reward(-1.7,self)
        elif (winner == "1"):
            entity2.wins += 1
            print(entity2.eType + " " + entity2.name + " wins!\n")
            if (entity2.eType == "bot"):
                entity2.reward(1.7,self)
            if (entity1.eType == "bot"):
                entity1.reward(-1.7,self)

    def draw(self,entity1,entity2):
        print("\n" + str(self))
        print("Draw!\n")
        if entity1.eType == "bot":
            entity1.reward(.5,self)
        if entity2.eType == "bot":
            entity2.reward(.5,self)

    def play(self,entity1,entity2):
        ''' Bots are still rewarded, but don't choose randomly '''
        ctr = 0
        while(self.checkWin() == "cont"):
            entity1.nextAction(self)
            if (self.checkWin() == "2"): #2 is X -> Entity1 will have X
                self.win(entity1,entity2,"2")
            elif (self.checkWin() == "Draw"):
                self.draw(entity1,entity2)
            if(self.validMove(entity1.lastAction) == False):
                entity1.reward(-2,self)
            entity2.nextAction(self)
            if(self.checkWin() == "1"): #1 is O -> Entity2 will have O
                self.win(entity1,entity2,"1")
            elif (self.checkWin() == "Draw"):
                self.draw(entity1,entity2)
            if(self.validMove(entity2.lastAction) == False):
                entity2.reward(-2,self)
            ctr += 1

    def train(self,entity1,entity2):
        ''' Randomized with bots only '''
        while(self.checkWin() == "cont"):
            entity1.nextTrain(self)
            if (self.checkWin() == "2"): #2 is X -> Entity1 will have X
                self.win(entity1,entity2,"2")
            elif (self.checkWin() == "Draw"):
                self.draw(entity1,entity2)
            entity2.nextTrain(self)
            if(self.checkWin() == "1"): #1 is O -> Entity2 will have O
                self.win(entity1,entity2,"1")
            elif (self.checkWin() == "Draw"):
                self.draw(entity1,entity2)

    def __str__(self):
        board = ""
        for row in self.boardState:
            for col in row:
                board += col
            board += "\n"
        board += "\n"
        return board

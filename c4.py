class Connect4():
 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = []
 
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]
 
    def __repr__(self):
        #print out rows & cols
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the separator character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        #print out the horizontal separator
        s += (2*self.width +1) * '-'
        s += '\n'
        s += ''
 
        # print out indices of each column # using mod if greater than 9,
        # for spacing issues
        for col in range(self.width):
            if col > 9:
                col = col % 10
            s += str(col)
            s += ''
        return s       # return string
 
    def addMove(self, col, ox ):
        #find the first row in the column
        #without a checker in it and
        #then add the ox checker there...
        #do this by checking values
        #in self.data...
        row = self.height - 1
        if self.allowsMove(col):
            row += 1
        print(row)
        self.data[row][col] = ox
 
    def clear(self):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ''
 
    def delMove(self, col):
        pass
 
    def allowsMove(self, col):
        if col < 0:
            return False
        elif col > self.width-1:
            return False
        elif self.data[0][col] != '':
            return False
        else:
            return True
 
    def isFull(self):
        for col in range(self.width):
            if self.allowsMove(col):
                return False
            else:
                return True
 
    def winsFor(self,ox):
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row][col+1] == ox and \
                   self.data[row][col+2] == ox and \
                   self.data[row][col+3] == ox:
                    return True
 
        # Check for other winning conditions
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.data[row][col] == ox and \
                   self.data[row+1][col] == ox and \
                   self.data[row+2][col] == ox and \
                   self.data[row+3][col] == ox:
                    return True
 
        for row in range(3, self.height): 
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row-1][col+1] == ox and \
                   self.data[row-2][col+2] == ox and \
                   self.data[row-3][col+3] == ox:
                    return True
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row+1][col+1] == ox and \
                   self.data[row+2][col+2] == ox and \
                   self.data[row+3][col+3] == ox:
                    return True        
        return False
 
    def hostGame(self):
        pass
 
def main():
    b = Connect4(7,6)
    b.addMove(0, 'x')
 
    # b.addMove(4, 'o')
    print(b)
    #b.hostGame()
 
if __name__ == '__main__':
    main()
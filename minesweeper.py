import random

class Game:
	def __init__(self,numR,numC,numB):
		self.numRows = numR
		self.numCols = numC
		self.numBombs = numB
		self.board = Board(numR,numC,numB)
		self.State = "PLAYING"
		self.playGame()
		
		
	def playGame(self):
		while self.State == "PLAYING":
			self.printGameState()
			CR = int(input("Enter Row: "))
			CC = int(input("Enter Column: "))
			isG = bool(input("Enter if your guesing as bomb: "))
			uP = userPlay(CR,CC,isG)
			userPR = self.board.playFlip(uP)
			self.State = userPR.gameState
		print self.printGameState()
			
			
	def printGameState(self):
		print "Player ",self.State
		if self.State == "PLAYING":
			self.board.displayBoard("surface")
		else:
			self.board.displayBoard("underside")
##########################################################################################	
class userPlay:
	def __init__(self,r,c,isG):
		self.row = r
		self.col = c
		self.isGuess = isG
##########################################################################################	
	
class userPlayResult:
	def __init__(self,result,gameState):
		self.success = result
		self.gameState = gameState #WON, LOST, PLAYING	
##########################################################################################	
					
class Board:
	def __init__(self,r,c,b):
		self.rows = r
		self.cols = c
		self.cells = []
		self.bombs = []
		self.numBombs = b
		self.numUnexposedRem = 0
		
		self.initializeBoard()
	
	def initializeBoard(self):
		#create an empty board
		for i in range(0,self.rows):
			l = []
			for j in range(0,self.cols):
				l.append(Cell(i,j))
			self.cells.append(l)
		#add bombs
		for i in range(0,self.numBombs):
			r = i/self.cols
			c = (i-r*self.cols)%self.cols
			self.cells[r][c].setBomb()
			self.bombs.append(self.cells[r][c])	
			
		self.shuffleBoard()
		self.addNumbersOnCells()
		self.numUnexposedRem = self.rows*self.cols-self.numBombs
			
	#shuffle the bombs
	def shuffleBoard(self):
		nCells = self.rows * self.cols
		for index1 in range(0,nCells):
			index2 = index1 + random.randint(index1,nCells-1)
			if index1 != index2:
				r1 = index1/self.cols
				c1 = (index1-r1*self.cols)%self.cols
				
				r2 = index2/self.cols
				c2 = (index2-r2*self.cols)%self.cols
				
				if self.inBounds(r1, c1) and self.inBounds(r2, c2):
					cell1 = self.cells[r1][c1] 
					cell2 = self.cells[r2][c2]
				
					self.cells[r1][c1] = cell2
					self.cells[r1][c1].setRowAndColumn(r1,c1)
					self.cells[r2][c2] = cell1
					self.cells[r2][c2].setRowAndColumn(r2,c2)
	
				
	#add numbers on cells surrounding bombs
	def addNumbersOnCells(self):
		deltas = [(-1,0),(0,-1),(0,1),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
		for b in self.bombs:
			for d in deltas:
				if self.inBounds(b.row+d[0], b.col+d[1]):
					if self.cells[b.row+d[0]][b.col+d[1]].value != "B":
						self.cells[b.row+d[0]][b.col+d[1]].value+=1
	
	#expand blank cells
	def expandBlankCells(self,cell):	
		deltas = [(-1,0),(0,-1),(0,1),(1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
		for d in deltas:
			if self.inBounds(cell.row+d[0],cell.col+d[1]):
				cell = self.cells[cell.row+d[0]][cell.col+d[1]]
				if cell.getIsBlank():
					self.expandBlankCells(cell)
					
	def inBounds(self,r,c):
		if (r <0 or r >self.rows-1 or c<0 or c>self.cols-1):
			return False
		return True
			
	def flipCell(self,cell):
		if not cell.getIsExposed() and not cell.isCellGuess():
			res = cell.flip()
			if res:
				self.numUnexposedRem-=1
			return res
		return False
			
	def playFlip(self,userPlay):
		if not self.inBounds(userPlay.row,userPlay.col):
			return userPlayResult(false,"PLAYING")
		chosenCell = self.cells[userPlay.row][userPlay.col]
		if userPlay.isGuess:
			chosenCell.toggleGuess()
		res = self.flipCell(chosenCell)
		if res and self.numUnexposedRem <=0:
			return userPlayResult(res,"WON")
		if not res:
			if chosenCell.getIsBomb():
				return userPlayResult(res,"LOST")
			elif userPlay.isG:
				res = chosenCell.toggleGuess()
		else:
			print "Howdy1"
			if chosenCell.getIsBlank():
				print "Howdy"
				#self.expandBlankCells(chosenCell)
				self.displayBoard("surface")
		return userPlayResult(res,"PLAYING")
		
		
	def displayBoard(self,side):
		for i in range(0,self.rows):
			for j in range(0,self.cols):
				if side == "surface":
					print self.cells[i][j].getSurfaceState()," ",
				elif side== "underside":
					print self.cells[i][j].getUndersideState()," ",
			print " "			
		
##########################################################################################				
class Cell:
	def __init__(self,r,c):
		self.row = r
		self.col = c
		self.isBomb = False
		self.isGuess = False
		self.isExposed = False
		self.value = 0
	
	def flip(self):
		self.isExposed = True
		return not self.isBomb
		
	def toggleGuess(self):
		if not self.getIsExposed:
			self.isGuess = not(self.isGuess)
			return self.isGuess
			
	def setBomb(self):
		self.isBomb = True
		self.value = "B"
	
	def setExposed(self):
		self.isExposed = True
		
	def setValue(self,val):
		self.value = val
	
	def getIsBomb(self):
		return self.isBomb
		
	def getValue(self):
		return self.value
		
	def getIsExposed(self):
		return self.isExposed
		
	def setRowAndColumn(self,r,c):
		self.row = r
		self.col = c
	
	def getIsBlank(self):
		return self.value==0
		
	def isCellGuess(self):
		return self.isGuess
		
	def getSurfaceState(self):
		if self.getIsExposed():
			return self.getUndersideState()
		elif (self.isCellGuess()):
			return "F"
		else:
			return "?"
	
	def getUndersideState(self):
		if self.getIsBomb():
			return "*";
		elif self.getValue > 0:
			return str(self.getValue());
		else:
			return " "
##########################################################################################	
		
#B = Board(5,5,3)
#B.displayBoard("underside")


G = Game(5,5,3)

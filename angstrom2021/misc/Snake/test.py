import curses
import random
import base64
import pickle
import io


class SnakeSave:
	def __init__(self, highScores, game=None):
		self.highScores = highScores
		self.game = game

	class HighScores:
		def __init__(self, player):
			self.player = player
			self.scores = []

		def getHighScore(self, score):
			return max(self.scores+[score])

	class Game:
		def __init__(self, width, height, coords):
			self.width = width
			self.height = height
			self.coords = coords
			self.direction = curses.KEY_RIGHT
			self.score = 0
			self.food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
			while self.food in self.coords: self.food = (random.randint(1, self.height-2), random.randint(1, self.width-2))

		def move(self):
			self.coords.append((
				self.coords[-1][0] + (1 if self.direction == curses.KEY_DOWN else -1 if self.direction == curses.KEY_UP else 0),
				self.coords[-1][1] + (1 if self.direction == curses.KEY_RIGHT else -1 if self.direction == curses.KEY_LEFT else 0)
			))
			if self.coords[-1][0] > 18 or self.coords[-1][1] > 58 or \
			   self.coords[-1][0] < 1 or self.coords[-1][1] < 1 or \
			   self.coords.index(self.coords[-1]) != len(self.coords) - 1: return False
			if self.food == self.coords[-1]:
				self.score += 1
				while self.food in self.coords: self.food = (random.randint(1, self.height-2), random.randint(1, self.width-2))
				return None
			else:
				erase = self.coords[0]
				self.coords = self.coords[1:]
				return erase

code = "gASVeAAAAAAAAACMCF9fbWFpbl9flIwJU25ha2VTYXZllJOUKYGUfZQojApoaWdoU2NvcmVzlGgAjBRTbmFrZVNhdmUuSGlnaFNjb3Jlc5STlCmBlH2UKIwGcGxheWVylIwEaG9nZZSMBnNjb3Jlc5RdlEsBYXVijARnYW1llE51Yi4="

snake = pickle.Unpickler(io.BytesIO(base64.b64decode(code))).load()
print(snake)

highScores = SnakeSave.HighScores("Slt")
highScores.scores.append(50000000000000000000000000)
savedata = SnakeSave(highScores)
print(savedata)
code = base64.b64encode(pickle.dumps(savedata)).decode('ascii')
print(code)
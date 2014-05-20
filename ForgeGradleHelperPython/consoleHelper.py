import os

class ConsoleHelper:
	@staticmethod
	def pause():
		if os.system("PAUSE") != 0:
			os.system("read -p \"Press [Enter] key to continue...\"")
	
	@staticmethod
	def clearScr():
		if os.system("CLS") != 0:
			os.system("clear")
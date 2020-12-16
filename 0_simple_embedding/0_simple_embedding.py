import subprocess
import sys
import time
import win32gui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QApplication,
							 QHBoxLayout)
from PyQt5.QtWebEngineWidgets import QWebEngineView							 


class Main(QWidget):
	"""Classe représentant les options de configuration de GRUB"""

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)

		# create a process
		exePath = "C:\\Program Files\\Blender Foundation\\Blender 2.81\\blender.exe"
		subprocess.Popen(exePath)

		# Temps démarrage FreeCad
		time.sleep(3)

		hwnd = win32gui.FindWindowEx(0, 0, 0, "Blender")

		window = QWindow.fromWinId(hwnd)
		self.container = self.createWindowContainer(window)
		self.setGeometry(100, 100, 1024, 768)

		#layout = QVBoxLayout(self)
		layout = QHBoxLayout(self)
		layout.addWidget(self.container)
		
		self.webEngineView = QWebEngineView()
		self.webEngineView.resize(100, 500);
		self.loadPage()
		
		self.setLayout(layout)

		layout.addWidget(self.webEngineView)

		self.show()
		
	def loadPage(self):

		with open('page.html', 'r') as f:

			html = f.read()
			self.webEngineView.setHtml(html)


if __name__ == "__main__":

	app = QApplication(sys.argv)

	win = Main()
	win.setWindowTitle("Blender Test - v0.1")

	sys.exit(app.exec_())

'''
Rapid GUI Programming with Python and Qt
'''

import sys #needed for sys arguments
import time #needed for sleep
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv) #comes as a list

try:
	due = QTime.currentTime()
	print due
	message = "Alert!"
	if len(sys.argv) < 2:
		raise ValueError
	hours, mins = sys.argv[1].split(":")
	due = QTime(int(hours), int(mins))
	if not due.isValid():
		raise ValueError
	if len(sys.argv) > 2:
		message = " ".join(sys.argv[2:])
except ValueError:
	message = "To use alarm.py HH:MM:SS [optional message]" #24hr clock
	

while QTime.currentTime() < due:
	time.sleep(20) # 20 seconds
	
label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit) #1 minute
app.exec_()

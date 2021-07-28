import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# Create an instance of QApplication -- do this first because it does a bunch of
# initializations. sys.argv contains list of cmd-line argments
app = QApplication(sys.argv)

# Create an instance of application's GUI
window = QWidget()
window.setWindowTitle('First PyQt App in Vim')
window.setGeometry(100, 100, 280, 100) # sets the size of the window and where it's placed on the screen
window.move(60,15)
hellomsg = QLabel("<h1>Hello World!</h1> <p>Because we don't have enough<br> of these types of programs lol</p>", parent = window)
hellomsg.move(60, 15)

# Show application's GUI
window.show()

# Run the event loop
sys.exit(app.exec_())


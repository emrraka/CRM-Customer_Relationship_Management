
from PyQt6.QtWidgets import QMainWindow
from UI_Files.mentors_ui import Ui_MainWindow

class MentorsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mentor_window = Ui_MainWindow()
        self.mentor_window.setupUi(self)

        self.open_menu_window = None 
        self.mentor_window.pushButtonExit.clicked.connect(self.app_exit)
        self.mentor_window.pushButtonBackMainPage.clicked.connect(self.back_menu)

    def back_menu(self):
        from menu import MenuPage
        
        self.open_menu_window = MenuPage(True)  ## True gecici!
        self.hide()
        self.open_menu_window.show()

    def app_exit(self):
        self.close()
    
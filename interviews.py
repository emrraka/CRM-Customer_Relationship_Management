
from PyQt6.QtWidgets import QMainWindow
from UI_Files.interviews_ui import Ui_MainWindow


class InterviewsPage(QMainWindow):
    def __init__(self,is_admin):
        super().__init__()
        self.interviews_window = Ui_MainWindow()
        self.interviews_window.setupUi(self)

        self.is_admin = is_admin


        self.interviews_window.pushButtonBackMainPage.clicked.connect(self.back_menu)
        self.interviews_window.pushButtonExit.clicked.connect(self.app_exit)
        

    def back_menu(self):
        from menu import MenuPage
        
        self.open_menu_window = MenuPage(self.is_admin)  
        self.hide()
        self.open_menu_window.show()



    def app_exit(self):
        self.close()
    

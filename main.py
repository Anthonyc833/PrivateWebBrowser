from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        # Main Websitelook
        self.profile = QWebEngineProfile.defaultProfile()
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        profile = QWebEngineProfile.defaultProfile()
        profile.clearHttpCache()  # Clear the HTTP cache
        self.clear_profile_data(clear_cookies=True, clear_cache=False)
        QMessageBox.information(self, "Fresh Slate", "Cookies and Chache have been cleared")



        # Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        # gets confused if you name stuff the same thing

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.url_bar.setFixedWidth(750)

        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, url):
        self.url_bar.setText(url.toString())

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def clear_profile_data(self, clear_cookies=True, clear_cache=True):
        profile = QWebEngineProfile.defaultProfile()

        if clear_cookies:
            cookie_store = profile.cookieStore()
            cookie_store.deleteAllCookies()

        if clear_cache:
            # Clear the HTTP cache
            QWebEngineProfile.clearHttpCache()





app = QApplication(sys.argv)
QApplication.setApplicationName("Browser")
window = MainWindow()
app.exec_()

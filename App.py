import sys
import tkinter as tk
from Admin import run
from components.BackButton import BackButton
from log import Log
from pages.MainPage import MainPage
from pages.PasswordPage import PasswordPage
from pages.ReversePage import ReversePage
from pages.ShowPdfPage import ShowPdfPage
from pages.WelcomePage import WelcomePage
from pages.InfoPage import InfoPage
from utils import FrameManager, WindowManager
class App(tk.Tk):
    def __init__(self, screenName: str = None , baseName: str = None , className: str =None, useTk: bool =None , sync: bool =None , use: str = None ) -> None:
        if (screenName!=None): super().__init__(screenName, baseName, className, useTk, sync, use)
        else: super().__init__()
        WindowManager(self)
        BackButton(self,"⬅")
        self.initialize_frames()
    def initialize_frames(self):
        self.frame_manager= FrameManager({
            'WelcomePage':WelcomePage,
            'MainPage':MainPage,
            "PasswordPage":PasswordPage,
            "InfoPage": InfoPage,
            "ReversePage":ReversePage,
            "ShowPdfPage":ShowPdfPage
        },self)
        self.frame_manager.show_frame('WelcomePage')
def makeApp():
    LOG=Log(__name__).logger
    app=App()
    LOG.debug(f"App Object made {app}")
    LOG.info(f"App Size {sys.getsizeof(app)}")
    app.mainloop()
if __name__=='__main__':
    makeApp()
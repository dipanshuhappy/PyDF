import tkinter as tk
from pages.MainPage import MainPage
from pages.WelcomePage import WelcomePage
from utils import FrameManager, WindowManager

class App(tk.Tk):
    def __init__(self, screenName: str = None , baseName: str = None , className: str =None, useTk: bool =None , sync: bool =None , use: str = None ) -> None:
        if (screenName!=None): super().__init__(screenName, baseName, className, useTk, sync, use)
        else: super().__init__()
        WindowManager(self)
        self.frame_manager= FrameManager({
            'WelcomePage':WelcomePage(self),
            'MainPage':MainPage(self)
            })
        self.frame_manager.show_frame('WelcomePage')
App().mainloop()
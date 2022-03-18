import sys
import tkinter as tk
from components.BackButton import BackButton
from components.RoundButton import RoundButton
from pages.MainPage import MainPage
from pages.PasswordPage import PasswordPage
from pages.WelcomePage import WelcomePage
from utils import FrameManager, WindowManager
class App(tk.Tk):
    def __init__(self, screenName: str = None , baseName: str = None , className: str =None, useTk: bool =None , sync: bool =None , use: str = None ) -> None:
        if (screenName!=None): super().__init__(screenName, baseName, className, useTk, sync, use)
        else: super().__init__()
        WindowManager(self)
        BackButton(self)
        RoundButton(self,200,30,0,0,'hi',lambda :print('kjld'))
        self.initialize_frames()
    def initialize_frames(self):
        self.frame_manager= FrameManager({
            'WelcomePage':WelcomePage,
            'MainPage':MainPage,
            "PasswordPage":PasswordPage
        },self)
        # self.frame_manager.show_frame('WelcomePage')
app=App()
print("App size",sys.getsizeof(app))
app.mainloop()
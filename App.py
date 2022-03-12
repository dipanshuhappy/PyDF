from multiprocessing import managers
import tkinter as tk
from pages.FirstPage import FrontPage

from utils import FrameManager, WindowManager

class App(tk.Tk):
    def __init__(self, screenName: str = None , baseName: str = None , className: str =None, useTk: bool =None , sync: bool =None , use: str = None ) -> None:
        if (screenName!=None): super().__init__(screenName, baseName, className, useTk, sync, use)
        else: super().__init__()
        WindowManager(self)
        page=FrontPage(self)
        self.manager=FrameManager({
            'frontPage':page
        })
        self.manager.show_frame('frontPage')
App().mainloop()
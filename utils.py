from __future__ import annotations
import tkinter
from typing import TYPE_CHECKING
from pages.Page import Page
if TYPE_CHECKING:
    from App import App
class WindowManager:
    def __init__(self,app:tkinter.Tk,config:dict={}) -> None:
        self.config=config
        self.__do_window_config(app)
    def __do_window_config(self,app:tkinter.Tk)->None:
        app.config(self.config)
        app.title('PyDF')
        app.state('zoomed')
        app.rowconfigure(0,weight=1)
        app.columnconfigure(0,weight=1)
class FrameManager:
    def __init__(self,frames:dict[str,Page],app:App) -> None:
        self.frames=frames
        self.stack:list=[]
        self.app=app
    def show_frame(self,id:str) -> None:
        if ( bool(self.stack)):  
           self.frames[self.stack[-1]].destroy()

    #    self.frames[id]=self.frames[id](self.app) if ()) else self.frames[id].__class__(self.app)
        if (isinstance(self.frames[id],type)):
           print('This is object ',self.frames[id].__class__)
           self.frames[id]=self.frames[id](self.app)
          
        else:
            print('this is class ',self.frames[id].__class__)
            self.frames[id]=self.frames[id].__class__(self.app)
        print(self.frames)
        self.frames[id].show_page()
        self.stack.append(id)
    def remove_frame(self,id:str)  -> None:
        self.frames[id].destroy()
    def go_back(self) -> None :
        self.frames[self.stack[-1]].destroy()
        self.frames[self.stack[-2]]=self.frames[self.stack[-2]].__class__(self.app)
        self.frames[self.stack[-2]].show_page()
        print(self.frames)
        self.stack.pop()
        
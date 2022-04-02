from __future__ import annotations
import tkinter
from tkinter import filedialog
from typing import TYPE_CHECKING,Type
from pages.Page import Page
import sys
if TYPE_CHECKING:
    from App import App
class Utils:
    @staticmethod
    def getPDf()->str:
        filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
        )
        filename=filedialog.askopenfilename(filetypes=filetypes)
        print(filename)
        return filename
    @staticmethod
    def get_saving_file_path()->str:
        save_file=filedialog.askdirectory()
        return save_file
class WindowManager:
    def __init__(self,app:tkinter.Tk,config:dict={}) -> None:
        self.config=config
        self.__do_window_config(app)
    def __do_window_config(self,app:tkinter.Tk)->None:
        app.config(self.config)
        app.title('PyDF')
        app.geometry("600x400")
        app.rowconfigure(0,weight=1)
        app.columnconfigure(0,weight=1)
class FrameManager:
    def __init__(self,frames:dict[str,Page],app:App) -> None:
        self.frames=frames
        self.stack:list=[]
        self.app=app
    def get_frame(self,id:str)->Type[Page]| Page:
        print("id and size is ",id," and ",sys.getsizeof(self.frames[id]))
        return self.frames[id]
    def show_frame(self,id:str) -> None:
        if ( bool(self.stack)):  
           self.remove_frame(self.stack[-1])
        self.frames[id]=self.frames[id](self.app)
        print(self.frames)
        self.get_frame(id).show_page()
        self.stack.append(id)
        self.print_frames_memory()
    def remove_frame(self,id:str)  -> None:
        self.get_frame(id).destroy()
        self.frames[id]=self.get_frame(id).__class__
        print(self.frames)
    def print_frames_memory(self)->None:
        print("Size of frames is",sys.getsizeof(self.frames))
    def remove_latest_frame(self)->None:
        self.remove_frame(self.stack[-1])
    def go_back(self) -> None :
        self.remove_latest_frame()
        self.frames[self.stack[-2]]=self.frames[self.stack[-2]](self.app)
        self.frames[self.stack[-2]].show_page()
        print(self.frames)
        self.stack.pop()
        self.print_frames_memory()
   
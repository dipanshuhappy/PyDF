from __future__ import annotations
import tkinter
from tkinter import filedialog
from typing import TYPE_CHECKING,Type
from log import Log
from pages.Page import Page
import sys
if TYPE_CHECKING:
    from App import App
LOG=Log(__name__).logger
class Utils:
    @staticmethod
    def getPDf()->str:
        LOG.info("Opening file dialog")
        filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
        )
        filename=filedialog.askopenfilename(filetypes=filetypes)
        LOG.debug(f"Pdf File gotten with file name {filename}")
        return filename
    @staticmethod
    def get_saving_file_path()->str:
        LOG.info("Opening file directory dialog")
        save_file=filedialog.askdirectory()
        LOG.debug(f"Folder gotten with directory {save_file}")
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
        LOG.debug(f" Page with id {id} has size of {sys.getsizeof(self.frames[id])} ")
        return self.frames[id]
    def show_frame(self,id:str) -> None:
        if ( bool(self.stack)):  
           self.remove_frame(self.stack[-1])
        self.frames[id]=self.frames[id](self.app)
        LOG.debug(f"Updated frames after making Frame object with id {id}, {self.frames}")
        self.get_frame(id).show_page()
        self.stack.append(id)
        LOG.debug(f" Frames Size {sys.getsizeof(self.frames)} ")
        LOG.info("Show Frame is done , frame added to stack")
    def remove_frame(self,id:str)  -> None:
        LOG.info(f"Removing Frame with Id {id}")
        self.get_frame(id).destroy()
        self.frames[id]=self.get_frame(id).__class__
        LOG.debug(f"Updated frames after removing Frame with id {id}, {self.frames}")
    def remove_latest_frame(self)->None:
        self.remove_frame(self.stack[-1])
    def go_back(self) -> None :
        LOG.info("Going back one frame ")
        self.remove_latest_frame()
        LOG.debug(f"Updated frames after removing Frame with id {self.stack[-1]}, {self.frames}")
        self.frames[self.stack[-2]]=self.frames[self.stack[-2]](self.app)
        self.frames[self.stack[-2]].show_page()
        LOG.debug(f"Updated frames after making Frame object of second last with id {self.stack[-2]}, {self.frames}")
        self.stack.pop()
        LOG.debug(f" Frames Size {sys.getsizeof(self.frames)} ")
   
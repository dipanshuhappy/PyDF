from __future__ import annotations
import tkinter
from pages.Page import Page
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from App import App
class BackButton(tkinter.Frame):
    def __init__(self,parent_frame:App,buttontext:str) -> None:
        super().__init__(parent_frame)
        self.app=parent_frame
        self.buttontext = buttontext
        tkinter.Button(self,text= self.buttontext,width=3,height=1, command=self.go_back).pack()
        self.pack(side=tkinter.TOP, anchor=tkinter.NW)
    def go_back(self):
        self.app.frame_manager.go_back()

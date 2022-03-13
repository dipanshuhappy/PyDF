from __future__ import annotations
import tkinter
from pages.Page import Page
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from App import App
class BackButton(tkinter.Frame):
    def __init__(self,parent_frame:App) -> None:
        super().__init__(parent_frame)
        self.app=parent_frame
        tkinter.Button(self,text="go back",command=self.go_back).pack()
        self.pack(side=tkinter.TOP, anchor=tkinter.NW)
    def go_back(self):
        self.app.frame_manager.go_back()

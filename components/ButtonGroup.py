from itertools import count
import tkinter
from pages.Page import Page
class ButtonGroup(tkinter.Frame):
    def __init__(self,parent_frame:tkinter.Tk|tkinter.Frame|Page,buttons:list[tkinter.Button]) -> None:
        super().__init__(parent_frame)
        self.buttons=buttons
    def show_vertically(self):
        row_count=0
        for button in self.buttons:
            button.grid(row=row_count,column=0)
            row_count+=1
    def show_horizontally(self):
        column_count=0
        for button in self.buttons:
            button.grid(row=0,column=column_count)
            column_count+=1
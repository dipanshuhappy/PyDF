from time import sleep
from tkinter import Canvas, ttk
import typing
from typing import Callable
import tkinter
from pages.Page import Page
class RoundButton(ttk.Frame):
    def __init__(self,parent_frame:tkinter.Tk|tkinter.Frame|Page,width:float|int,height:float|int,x:float|int,y:float|int,text:str,command:Callable,bg_color:str="black",text_color:str="white",**kwargs) -> None:
        super().__init__(parent_frame)
        self.bg_color=bg_color
        self.command=command
        self.canvas=tkinter.Canvas(self,width=width,height=height)
        self.border=self.round_rectangle(0,0,width,height,fill=bg_color)
        self.button_text= self.canvas.create_text(width/2, height/2, text=text,fill=text_color)
        self.canvas.tag_bind(self.border, "<Button-1>", self.clicked)
        self.canvas.tag_bind(self.button_text, "<Button-1>",self.clicked)
        self.show_button()
    def show_button(self):
        self.canvas.pack()
        self.pack()
    def round_rectangle(self,x1, y1, x2, y2, radius=25, **kwargs):
        
        points = [
                x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1
            ]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)
    def clicked(self,event):
        self.canvas.itemconfig(self.border,fill='grey')
        self.command()
        self.after(200,lambda: self.canvas.itemconfig(self.border,fill=self.bg_color))
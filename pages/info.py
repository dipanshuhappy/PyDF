from tkinter import *
from pages.Page import Page
class InfoPage(Page):
    CREDITS="Deepanshu Singh\n B.V.S.Swaraj"
    def __init__(self,app):
        super().__init__(app)
        self.credits = credits
    def showintext(self):
        Label(self,text= InfoPage.CREDITS).pack()
    def show_page(self) ->None:
        self.showintext()
        self.pack()






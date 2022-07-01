from tkinter import Button, Label
from components.ButtonGroup import ButtonGroup
from pages.Page import Page
class MainPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        self.pack()
    def make_widgets(self) -> None:
        ButtonGroup(self,
        [
            Button(self,text="Put Password",command=self.goto_password_page,foreground='red'),
            Button(self,text="Reverse Pdf",foreground='brown',command=self.goto_reverse_page),
            Button(self,text='click me',foreground='blue',command=self.goto_open_pdf),
            Button(self,text='click me',foreground='black')
        ]
        ).show_vertically()
    def goto_open_pdf(self):
        self.app.frame_manager.show_frame("ShowPdfPage")
    def goto_reverse_page(self):
        self.app.frame_manager.show_frame("ReversePage")
    def goto_password_page(self):
        self.app.frame_manager.show_frame("PasswordPage")
from tkinter import Button, Label
from components.ButtonGroup import ButtonGroup
from pages.Page import Page
class MainPage(Page):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.has_widget_made=False
    def show_page(self) -> None:
        self.make_widgets()
        self.pack(expand=True)
    def make_widgets(self) -> None:
        ButtonGroup(self,
        [
            Button(self,text="Put Password",command=self.goto_password_page,foreground='red'),
            Button(self,text='click me',foreground='brown'),
            Button(self,text='click me',foreground='blue'),
            Button(self,text='click me',foreground='black')
        ]
        ).show_vertically()
    def goto_password_page(self):
        self.app.frame_manager.show_frame("PasswordPage")
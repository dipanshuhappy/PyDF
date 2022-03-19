from __future__ import annotations
import tkinter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from App import App
class Page(tkinter.Frame):
    def __init__(self,app:App,**kwargs) -> None:
        super().__init__(app,**kwargs)
        self.app:App=app
    def destroy(self) -> None:
        for childern  in self.winfo_children():
            print('Children',childern)
            childern.destroy()
        return super().destroy()
    def show_page()->None:
        pass
    def make_widget()->None:
        pass
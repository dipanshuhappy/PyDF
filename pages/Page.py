from __future__ import annotations
import tkinter
from typing import TYPE_CHECKING

from log import Log
# from log import Logs
if TYPE_CHECKING:
    from App import App

class Page(tkinter.Frame):
    def __init__(self,app:App,**kwargs) -> None:
        super().__init__(app,**kwargs)
        self.app:App=app
        self.__log=Log(__name__).logger
    def destroy(self) -> None:
        for childern  in self.winfo_children():
            self.__log.debug(f"Children for this Page is being destroyed {childern} ")
            childern.destroy()
        return super().destroy()
    def show_page()->None:
        pass
    def make_widget()->None:
        pass
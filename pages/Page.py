from __future__ import annotations
import tkinter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from App import App
class Page(tkinter.Frame):
    def __init__(self,app:App,**kwargs) -> None:
        super().__init__(app,**kwargs)
        self.app:App=app
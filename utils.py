import tkinter

from pages.Page import Page
class WindowManager:
    def __init__(self,app:tkinter.Tk,config:dict={}) -> None:
        self.config=config
        self.__do_window_config(app)
    def __do_window_config(self,app:tkinter.Tk)->None:
        app.config(self.config)
        app.title('PyDF')
        app.state('zoomed')
        app.rowconfigure(0,weight=1)
        app.columnconfigure(0,weight=1)
class FrameManager:
    def __init__(self,frames:dict[str,Page]) -> None:
        self.frames=frames
        self.stack:list=[]
    def show_frame(self,id:str) -> None:
        if(bool(self.stack)):   self.remove_frame(self.stack[-1])
        self.frames[id].show_page()
        print(f'Show frame is runned for {id}')
        self.stack.append(id)
    def remove_frame(self,id:str)  -> None:
        self.frames[id].destroy()
        self.stack.remove(id)
    def go_back(self) -> None :
        self.frames[id].destroy()
        self.stack.pop()
        self.frames[self.stack[-1]].show_page()
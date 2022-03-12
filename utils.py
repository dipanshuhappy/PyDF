import tkinter
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
class Page(tkinter.Frame):
    def __init__(self,app,**kwargs) -> None:
        super().__init__(app,**kwargs)
        self.app=app
class FrameManager:
    def __init__(self,frames:dict[str,Page]) -> None:
        self.frames=frames
        self.stack=[]
    def show_frame(self,id):
        self.frames[id].show_page()
        self.stack.append(id)
    def remove_frame(self,id):
        self.frames[id].destroy()
        self.stack.remove(id)
    def go_back(self):
        self.frames[id].destroy()
        self.stack.pop()
        self.frames[self.stack[-1]].show_page()
import logging
class Log:
    FORMAT="[%(asctime)s] %(levelname)s [ %(filename)s  %(name)s  FunctionName--%(funcName)s  (%(lineno)d)] ::::Message::::  %(message)s"
    def __init__(self,name:str,fileName:str="app.log") -> None:
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formater=logging.Formatter(Log.FORMAT)
        self.__add_file_handler(fileName)
        self.__add_stream_handler()
       
    def __add_file_handler(self,fileName:str):
        self.file=logging.FileHandler(fileName)
        self.file.setLevel(logging.DEBUG)
        self.file.setFormatter(self.formater)
        self.logger.addHandler(self.file)
    def __add_stream_handler(self):
        self.stream=logging.StreamHandler()
        self.stream.setLevel(logging.DEBUG)
        self.stream.setFormatter(self.file)
        self.logger.addHandler(self.stream)

# PyDF -A PDF GUI :bookmark_tabs: ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
PyDF is still in development , it's  using [tkinkter](https://github.com/python/cpython/tree/main/Lib/tkinter)  and [pikepdf (Under MPL 2.0 license) ](https://github.com/pikepdf/pikepdf).PyDF is a software that extends tkinkter widgets and features in order to make  a pdf tool with modern UI. This project is being made to show that tkinkter can be used for a professional software with mordern UI.
# How does it work?
PyDF uses [pikepdf](https://github.com/pikepdf/pikepdf) for pdf manipulation. And has a custom made frame manager and other mordern UI widgets .
## How to run?
1. Clone/download this repo.
2. Go to repo directory in your system, and install requirements using pip.
````
pip install -r requirements.txt.
````
3.Then run [App.py](App.py) using python.
````
python App.py
````
## Aim
- Creating a framework to make tkintker widgets have mordern UI and mordern Functionalities.
- Making a Frame Manger to handle switching betweeen frames.
- Creating a free and open sourse PDF tool using python and tkinter.
- Making widgets animation 
## Who will use PyDF?
Those who are looking for a pdf tool that is easy to change the source code of and make use according to their needs.And for those who want to inspect how software is written.
## How to Contribute?
So far only password to pdf and reversing pdf has been implemented 
if you want to add to this source code , do the following.
- Fork this project 
- Commit changes to the fork 
- Then open a pull request so that i can confirm the change and add it to the main repo.
## Structure of Project?
- Each screen UI is under the [pages directory](/pages)
- And Custom Widget components is under [components directory](/components)
- Screen UI is just a tkinkter frame maintained by a custom [frame mananger](utils.py) in utils.py 
- PDF manipulation code is in [pdf_utils.py](pdf_utils.py)


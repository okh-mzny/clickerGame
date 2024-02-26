# clickerGame
A simple idle game where the goal is to get the score as high as possible!
Each click rewards you 1 byte at the start, but this quickly changes as you level your items, buy upgrades for them to automatically generate more bytes
The game auto saves progress so you do not have to worry about accidentally closing out and losing it 

## Setup
The below instructions assume you have a shell open inside the project directory.
It is usually best practice to create a virtual environment to install the Python packages in a virtual environment to keep your system environment clean
```
python -m venv venv
```
---
#### Activate the venv

on Windows, run:
```
venv\Scripts\activate
```
on Unix or MacOS, run:
```
source venv/bin/activate
```
---
Now install PyQt6 as specified in the requirements.txt.
```
pip install -r requirements.txt
```
---
To launch the game now run

```
python main.py
```

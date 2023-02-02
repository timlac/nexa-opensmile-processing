# opensmile-processing

## Setup

Make sure you have python3 and pip installed. 

Install virtualenv if you don't already have it: `pip install virtualenv`

Create virtual environment: `virtualenv venv`

Activate virtual environment: `source venv/bin/activate`

Install requirements: `pip install -r requirements.txt`

## Running

Either use an IDE: https://realpython.com/python-ides-code-editors-guide/

Or use the console: 

Processing one file: `python -m src.process_one_file.py`
Processing full directory: `python -m src.process_directory.py`

Please inspect the code in `src` folder for modifying the feature sets and/or input and output files/directories.  

## Modifying 
REad the python documentation to see available feature sets etc.

https://audeering.github.io/opensmile-python/

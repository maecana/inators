# Deidleranator
# Author: Mae C.
# Date Created: November 21, 2024
# Version: 2.0.0

This project is a deidleranator that keeps a computer awake by simulating user interaction every 10 seconds.

## Creating a Virtual Environment
Before installing the required packages, it is important to create a virtual environment. To do this, run the following command in your terminal:
`py -m venv deidleranator_venv`

## Activating the Virtual Environment
To activate the virtual environment, run the following command in your terminal:

For Windows:
`source deidleranator_venv/Scripts/activate`

## Deactivating the Virtual Environment
To deactivate the virtual environment, run the following command in your terminal:

For Windows:
`deactivate`

## Installing the Required Packages
To install the required packages, run the following command in your terminal:
`pip install -r requirements.txt`

## Running the Program
First, make sure the mouse is visible to the location where you plan to leave it. To run the program, run the following command in your terminal:
`py deidleranator.py`

## Creating the executable
- First install pyinstaller
`pip install pyinstaller`
or imstall the required packages from the `requirements.txt` file

- Then run the following command:
`pyinstaller --onefile --path=deidleranator_venv/Lib/site-packages index.py`

- Test the executable file located in the `dist` folder created by running the command above.

## Note
Please add the name of the virtual environment to .gitignore if you plan to change it.

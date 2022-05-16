# LAB - Class 19

## Project: Automation

### Author: Christopher Yamas

### Setup

Install `.venv` (virtual environment) in the directory:

- Run `python3 -m venv .venv` in terminal while in root directory
- Activate virtual environment:
  - Mac/Linux - `source .venv/bin/activate`
  - Windows - `..venv\Scripts\activate`

### How to run application

User just needs to input into the respective `get_phones()` and `get_emails()` functions the proper paths to both a text file for reading (to collect the data), and a text file for writing (where they want contact info added).

Then in terminal , while in root directory, run `python ./modules/automation.py`

Your read file will be parsed, and the data will be written to your write file.

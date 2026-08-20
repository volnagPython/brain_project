# Phone's Specifications Django Project

## Description
Django project that can run three scrapers, PlayWright, Selenium, and BS4 to parse and 
collect the phone's specifications from the website and 
stores them in the PostgreSQL database. It takes about 5 min to collect the data.
All specs are also saved in results/ *.csv files.

## Tech stack
- Python
- Django
- Playwright
- Selenium
- BeautifulSoup4
- PostgreSQL


## Setup ```bash

git clone https://github.com/volnagPython/brain_project.git
cd brain_project
python -m venv venv
source venv/bin/activate
source venv/bin/activate
pip install -r requirements.txt
playwright install
python manage.py migrate
python manage.py runserver
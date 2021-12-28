# Information
Bolded Njuškalo price is used
Everything will be extracted into excel file every time web scrapping is finished (default 20 min)

# URLS
ROBOTS.TXT SOMETIMES BLOCK. To use safely go to settings.py, set ROBOTSTXT_OBEY = True, and use only links from category

Category example: ex: https://www.njuskalo.hr/prodaja-kuca/zagrebacka. Using "?page=2" will skip first page
Search example, ex for "uteg". https://www.njuskalo.hr/?ctl=search_ads&keywords=uteg&categoryId=9743&geo%5BlocationIds%5D=1170%2C1153

# Setup
Install python3
Configure "urls.txt", one line per search page
Configure "conf.py", MAX_PAGE_COUNT for how much pages to scrape, INTERVAL_MINUTES for how often to scrape

Run "pip install -r requirements.txt"

SCRAPPING - Run "python main.py -f urls.txt" (or create and use another file for scrapping)
EXTRACTING - Run "python main.py -e extracted.xlsx" (or another excel file path)


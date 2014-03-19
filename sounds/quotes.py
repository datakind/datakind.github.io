import subprocess 
import pandas as pd
from pyquery import PyQuery as pq
from settings import *
from google_spreadsheet.api import SpreadsheetAPI
from bs4 import BeautifulSoup

# create spreasheets api object
api = SpreadsheetAPI(GOOGLE_SPREADSHEET_USER, 
		GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE)

def get_sheet_from_name(sheet_name):
	spreadsheets = api.list_spreadsheets()
	target_sheet = None
	for i, sheet in enumerate(spreadsheets):
		if spreadsheets[i][0] == sheet_name:
			target_sheet = sheet
	return target_sheet

def get_rows_from_sheet(sheet):
	# fetch the sheet with volunteer info
	worksheet = api.list_worksheets(sheet[1])[0]
	target_sheet = api.get_worksheet(sheet[1], worksheet[1])
	return target_sheet.get_rows()


def sheet_name_to_df(name):
	sheet = get_sheet_from_name(name)
	sheet = get_rows_from_sheet(sheet)
	return pd.DataFrame(sheet)


def new_quote_indexes(quotes, current_quotes):
	return [ix for ix, quote in enumerate(quotes) if quote not in current_quotes]


def append_to_sounds(quotes_df, new_quote_ixs):
	document = pq(filename='index.html')
	sounds = document.find('#sounds')
	for ix in new_quote_ixs:
		quote_id = quotes_df.ix[ix].id
		template = '<div class="sound quote btn btn-xlarge" id="%s"></div>' % quote_id
		sounds.append(template)
	return document.html()


def add_css(quotes_df, new_quote_ixs):
	for ix in new_quote_ixs:
		quote_id = quotes_df.ix[ix].id
		img_url = quotes_df.ix[ix].imageurl
		css = '#%s { background-image: url(%s) }' % (quote_id, img_url)

		with open('./css/main.css', 'a') as stylesheet:
			stylesheet.write(css)


def add_markup(quotes_df, new_quote_ixs):
	new_doc = append_to_sounds(quotes_df, new_quote_ixs)
	with open('index.html', 'w+') as index:
		index.write(new_doc)
	print "it is written"

#check for new quotes 
quotes_df = sheet_name_to_df('DK Quotes')
quotes = list(quotes_df.quote)

# index = open('index.html', 'read').read()
# soup = BeautifulSoup(index)

# tag = soup.new_tag('<div class="sound">taco taco taco</div>')
# last_sound = soup.findAll('div', {'class':'sound'})[-1]
# soup.body.insert(len(soup.find('div', {'id':'sounds'})), tag)

# print

current_quotes = open('currentquotes.txt').read().splitlines()
new_quote_ixs = new_quote_indexes(quotes, current_quotes)
add_markup(quotes_df, new_quote_ixs)
add_css(quotes_df, new_quote_ixs)

# create the new quote audio
for ix in new_quote_ixs:
	text = quotes[ix]
	id = quotes_df.ix[ix].id
	filename = "%s.txt" % id
	aifname = "%s.aif" % id
	mp3name = "./audio/%s.mp3" % id
	
	f = open(filename, "w")
	subprocess.call(['echo', text], stdout=f)
	subprocess.call(['say', '-f', filename, '-o', aifname])
	subprocess.call(['lame', '-m', 'm', aifname, mp3name])
	subprocess.call(['rm', aifname])
	subprocess.call(['rm', filename])

	with open('currentquotes.txt', 'a') as currquotes:
		currquotes.write(text + '\n')




	
# add the new sounds to the 
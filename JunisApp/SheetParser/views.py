from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def index(request):
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
	sheet = client.open('Location tracking').sheet1
	records = sheet.get_all_records()

	return render(request, 'sheetparser/index.html', {'data': records})
from flaskTest import app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Test-39c139914575.json', scope)

gc = gspread.authorize(credentials)

sht = gc.open('UThere')
usrs = sht.get_worksheet(0)
events = sht.get_worksheet(1)
matches = sht.get_worksheet(2)
val = wrksht.cell(3,2).value  


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
  

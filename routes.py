from flaskTest import app
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Test-39c139914575.json', scope)

gc = gspread.authorize(credentials)

sht = gc.open('UThere')
wrksht = sht.get_worksheet(0)
val = wrksht.cell(3,2).value  


@app.route('/')
@app.route('/index')
def index():
    return "<h1>" + val + "</h1>"
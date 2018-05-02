from oauth2client.service_account import ServiceAccountCredentials
import gspread


class Util:
    """Used to easily access certain variables."""
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Satania-92028913ced2.json', scope)
    gc = gspread.authorize(credentials)
    share_email = "michaelverdegaal1999@gmail.com"

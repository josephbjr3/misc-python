#user_token.py script
import requests

login_page = requests.get("http://zero.webappsecurity.com/login.html")
# pull the content from the response
login_page_HTML = login_page.text

# chopping off all the html that comes before the token value
start_of_token = login_page_HTML.split('"user_token" value="')[1]
# chopping off all the html that comes after the token value
token = start_of_token.split('"')[0]
print(token)


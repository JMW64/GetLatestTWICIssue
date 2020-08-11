import requests, wget, os, shutil
from bs4 import BeautifulSoup
from zipfile import ZipFile

webname = r"https://theweekinchess.com/zips"
sfxname = 'g.zip'

myheaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

url = 'https://theweekinchess.com/twic'

r = requests.get(url, headers=myheaders)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# Find the first table tag, second row, first cell
first_table = html_soup.find('table', {"class":"results-table"})
secondrow = first_table.find('tr', {"class":""})
entry = secondrow.find('td').get_text(strip=True)

# concatenate webpath:
fullpath = os.path.join(webname + r"/twic" + entry + sfxname)

# print(fullpath)

# download the file:
file_name = wget.download(fullpath)

# move the file
shutil.move(file_name, "d:/pgn/twicg/new/aaa.zip")

# unzip the file
with ZipFile("d:/pgn/twicg/new/aaa.zip", 'r') as zipObj:
    # Extract the contents of the zip file in directory on D:
    zipObj.extractall(path="d:/pgn/twicg/new")

# delete the zip file
os.remove("d:/pgn/twicg/new/aaa.zip")

# print success message
print("\n\nLatest TWIC file downloaded, unzipped and saved in the D:/PGN/Twicg/NEW folder", "\n")

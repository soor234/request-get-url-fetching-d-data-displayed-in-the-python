from requests import get
url ='http://216.10.245.166///Library/GetBook.php?AuthorName=vinay'
response = get(url)
print(response.text)

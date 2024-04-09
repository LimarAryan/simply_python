#'pip install pyshorteners' in terminal
import pyshorteners

url = input("Enter the URL: ")

shortener = pyshorteners.Shortener()

shortened_URL = shortener.dagd.short(url)

#prints url to terminal
print(f"Shortened URL: {shortened_URL}")
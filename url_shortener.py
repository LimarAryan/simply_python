#'pip install pyshorteners' in terminal
import pyshorteners

url = input("Enter the URL: ")

shortener = pyshorteners.Shortener()

shortened_URL = shortener.dagd.short(url)

print(f"Shortened URL: {shortened_URL}")
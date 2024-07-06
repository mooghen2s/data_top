import subprocess
import json
import requests
from bs4 import BeautifulSoup

def scrape_and_save_text(url, file_name):
    try:
        chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
        command = [
            chrome_path,
            "--headless",
            "--dump-dom",
            url
        ]
        with open(file_name, 'w') as f:
            subprocess.run(command, stdout=f)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

with open('top_tier.json', 'r') as file:
    data = json.load(file)
    for item in data:
        url_from_json = item['url']
        file_name = f"out/{item['number']}.txt"  # Adjust file naming as needed
        url = f'{url_from_json}'
        if scrape_and_save_text(url, file_name):
            print(f"Scraping untuk {file_name} selesai!")
        else:
            print(f"Scraping untuk {url} gagal. Silakan periksa kode dan URL.")

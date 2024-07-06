import subprocess
import json
import requests

def scrape_and_save_text(url, file_name):
    try:
        command = [
            'powershell',
            'Invoke-WebRequest',
            '-Uri', url,
            '-OutFile', file_name
        ]
        subprocess.run(command)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

with open('top_tier.json', 'r') as file:
    data = json.load(file)
    for item in data:
        url_from_json = item['url']
        file_name = f"out/{item['number']}.txt"  # Adjust file naming as needed
        url = f'{url_from_json}'
        scrape_and_save_text(url, file_name)

import os
import time
import requests
import sys

def retrieve_html():
    for year in range(2019, 2024):
        for month in range(1, 13):
            url = f'http://en.tutiempo.net/climate/{month:02d}-{year}/ws-433440.html'
            texts = requests.get(url)
            text_utf = texts.text.encode('utf-8')

            directory = f"/home/vignesh/mlprojects/Data/html_Data/{year}/"
            if not os.path.exists(directory):
                os.makedirs(directory)
    
            with open(f"{directory}{month}.html", "wb") as output:
                output.write(text_utf)
        
            sys.stdout.flush()

if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print(f"Time taken: {stop_time - start_time}")

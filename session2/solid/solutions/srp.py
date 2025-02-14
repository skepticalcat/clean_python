import requests

def get_text_from_url(url):
    response = requests.get(url)
    return response.text

def save_data_to_disc(filename, data):
    with open(filename, "w") as file:
        file.write(data)

def download_data_from_url(url, filename):
    text = get_text_from_url(url)
    save_data_to_disc(filename, text)
    print(f"Data saved to {filename}")
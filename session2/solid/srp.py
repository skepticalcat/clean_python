import requests


def fetch_and_save_data(url, filename):
    response = requests.get(url)
    data = response.text

    with open(filename, "w") as file:
        file.write(data)

    print(f"Data saved to {filename}")
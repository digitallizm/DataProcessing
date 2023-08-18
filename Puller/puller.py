import requests
import json
import os


def pull_data_and_save():
    api_url = "	https://cat-fact.herokuapp.com/facts/random"  # Replace with the actual API URL

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        file_exists = os.path.exists("data.json")

        with open("data.json", "w") as file:
            if file_exists:
                file.truncate(0)  # Empty the file if it already exists
            json.dump(data, file, indent=4)

        print("Data pulled and saved to data.json")
    else:
        print("Failed to retrieve data from the API")


if __name__ == "__main__":
    pull_data_and_save()
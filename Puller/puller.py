import requests
import json
import os


def pull_data_and_save():
    api_url = "	https://cat-fact.herokuapp.com/facts/random"  # Replace with the actual API URL

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()

        output_file_path = "/opt/data/data.json"
        file_exists = os.path.exists("data.json")

        with open(output_file_path, "w") as file:
            if file_exists:
                file.truncate(0)  # Empty the file if it already exists
            json.dump(data, file, indent=4)

        print("Data pulled and saved to data.json:")
        print(data)
    else:
        print("Failed to retrieve data from the API")


if __name__ == "__main__":
    pull_data_and_save()

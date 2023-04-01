import argparse
import requests
import concurrent.futures



parser = argparse.ArgumentParser\
    (prog="Weather", description="Shows temperature by your chosen city in any country")
parser.add_argument("city_name", help="Insert city name: ")
parser.add_argument("-g", "--get", help="Pass g, if you want to get the temperature in specific location",
                    action="store_true", required=True)
args = parser.parse_args()


def get_url():
    with_space = args.city_name.replace("_", " ")
    api_url = f"https://api.api-ninjas.com/v1/weather?city={with_space}"
    response = requests.get(api_url, headers={"X-Api-Key": "jYBHd4rdWpcwklP9wQQRSySr6hWV5LAAuOOvfLbS"})
    if response.status_code == requests.codes.ok:
        print(f"{with_space.capitalize()}'s temperature now is {response.json()['temp']}")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(get_url)
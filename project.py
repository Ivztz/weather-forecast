import sys

import requests


def main():
    """
    Display weather data in Singapore according to the date that user inputs
    """
    date = input("Enter date (YYYY-MM-DD): ")
    if date_is_valid(date):
        url = "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date=" + date
        response = requests.get(url)
        if not response.json()["items"]:
            sys.exit("No data found!")

    newest_data = response.json()["items"][-1]

    # General weather data
    general_data = newest_data["general"]
    forecast = f"Forecast: {general_data['forecast']}"
    relative_humidity = f"Relative Humidity (%): {get_range(general_data['relative_humidity'])}"
    temperature = f"Temperature (°C): {get_range(general_data['temperature'])}"
    wind = f"Wind Speed (km/h): {get_range(general_data['wind']['speed'])}\nWind Direction: {general_data['wind']['direction']}"

    # Time intervals in 24 hour
    print("\nTime Intervals:")
    for i, time in enumerate(newest_data["periods"]):
        print(f"{i+1}: {time['time']['start']} - {time['time']['end']}")

    # User to make selection of time interval
    while True:
        choice = input("Select one of the option above: ")
        if choice_is_valid(choice, len(newest_data["periods"])):
            result = newest_data["periods"][int(choice)-1]
            break

    regions = process_regions(result["regions"])

    print(f"\n== General Weather Data == \
          \n{forecast}\n{relative_humidity}\n{temperature}\n{wind}\n \
          \n== Weather Description (Regions) ==\n{regions}")


def date_is_valid(date):
    """
    Verify validity of date format (YYYY-MM-DD)
    """
    try:
        date_list = date.split("-")
        if len(date_list) != 3:
            raise ValueError
        elif len(date_list[0]) != 4 or len(date_list[1]) != 2 or len(date_list[2]) != 2:
            raise ValueError
    except:
        sys.exit("Invalid date!")
    return True


def get_range(range_dict):
    """
    Format string output of the range of values from dictionary
    """
    return f"{range_dict['low']} - {range_dict['high']}"


def choice_is_valid(choice, num_choices):
    """
    Verify user input for selecting time interval
    """
    return choice in [str(x) for x in range(1, num_choices + 1)]


def process_regions(regions_dict):
    """
    Format string output of weather description in different regions of Singapore
    """
    return "\n".join([f"{key.title()}: {weather}" for key, weather in regions_dict.items()])


if __name__ == "__main__":    
    main()
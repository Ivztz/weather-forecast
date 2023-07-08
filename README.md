# Weather Forecast - Singapore

#### Video Demo:  <https://youtu.be/f9QKyoQ0GDM>

## Description

This project was done in fulfillment of the requirements of CS50P Final Project 2023.

This project serves to allow users to obtain 24 hour weather forecast data in Singapore, of a specified time interval, via API call from the Singapore Government API data.

The weather forecast data consists of:
1. General forecast across Singapore
2. Relative Humidity (%)
3. Temperature (°C)
4. Wind Speed (km/h)
5. Wind Direction
6. Weather Description of individual regions in Singapore (West, East, Central, South, North)

The script consists of a main function and four other helper functions: `date_is_valid`, `get_range`, `choice_is_valid` and `process_regions`. 

`date_is_valid` and `choice_is_valid` serve to verify the validity of the string format that is input by the user. 
`get_range` and `process_regions` serve to process data in the form of dictionary into string output.

## Usage
1. Clone the repository into your machine:
```bash
git clone https://github.com/Ivztz/weather-forecast.git
```
2. Run the command to install Python dependencies:
```bash
pip install -r requirements.txt
```
3. Run the program by typing the following command:
```bash
python project.py
```
4. Input date and select time interval to obtain weather forecast data.

## Run Test
Run the module with the file "test_project.py":
```bash
pytest test_project.py
```
Implemented Test Functions:
- `test_date_is_valid()`
- `test_get_range()`
- `test_choice_is_valid()`
- `test_process_regions()`
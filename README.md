# Economic Calendar Scraper

test 4

This script scrapes the economic calendar data from the MarketWatch website and prints it to the console.
Setup

To run the script, you need to have the following Python packages installed:

    requests
    BeautifulSoup
    termcolor

You can install these packages by running pip install -r requirements.txt in the project directory.
## Usage

To run the script, navigate to the project directory in your terminal and run python scraper.py.

By default, the script prints the economic calendar data to the console. If you want to see more information about a specific report, you can pass the index of the report as a command line argument. For example, to see more information about the first report in the list, run python scraper.py 0.

The script also reads a file named important.txt, which contains a list of important economic reports. If a report in the calendar matches a report in important.txt, it will be printed in red.
License

This project is licensed under the MIT License. See the LICENSE file for details.
ChatGPT Feb 13 Version

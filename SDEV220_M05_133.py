##### 13.3 #####
# Parse the date from today_string.

from datetime import datetime

# Read the date from the file
with open('today.txt', 'r') as file:
    today_string = file.read()

# Parse the date string into a datetime object using the known format (YYYY-MM-DD)
parsed_date = datetime.strptime(today_string, '%Y-%m-%d')

# Print the parsed datetime object to verify
print(parsed_date)
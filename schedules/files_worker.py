
# 1) Create schedules/schedule.csv in any way available to you
# 1.1) Column names departure point; departure time; destination point; arrival time; cost ticket
# 1.2) Enter several lines of relevant data
import csv
import json


with open('schedule.csv', 'w') as csv_table:
    fieldnames = ['Departure point', 'Departure time', 'Destination point', 'Arrival time', 'Cost ticket']
    table_data = csv.DictWriter(csv_table, fieldnames=fieldnames)

    table_data.writeheader()
    table_data.writerow({'Departure point': 'Odessa',
                         'Departure time': '16.30',
                         'Destination point': 'Lviv',
                         'Arrival time': '10.30',
                         'Cost ticket': '450 UAH'
                         })
    table_data.writerow({'Departure point': 'Kyiv',
                         'Departure time': '12.00',
                         'Destination point': 'Odessa',
                         'Arrival time': '18.30',
                         'Cost ticket': '250 UAH'
                         })

# Create a function that reads the content of schedule.csv and returns the entire content of the file
# as a dictionary or list
list_empty = []
with open('schedule.csv', 'r') as schedule:
    reader = csv.DictReader(schedule)
    for row in reader:
        list_empty.append(row)
        print(row)


"""Task_3"""
# Create a function that writes the received content to the schedules/schedule.json file
# 3.1) The keys in the recorded file must be sorted.
# 3.2) Attachments within the file must be indented with 4 spaces.
with open('schedule.json', 'w', newline='') as fh:
    json.dump(list_empty, fh, indent=4, sort_keys=True)

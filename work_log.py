import os.path
from add_entry import AddEntry
from search_entry import SearchEntry
import sys
import csv
import copy

file_exists = os.path.isfile('worklog.csv')

# couple of instances
add_entry = AddEntry()
search_entry = SearchEntry()

def instructions():
    """Instructions on how the console works
    it accepts a user input"""

    while True:
        print("WORK LOG \n"
              "Press a to add a new entry \n"
              "Press b to search in existing entries\n"
              "Press c to quit the program\n"
              )

        start = input("What would you like to do?")

        if start == 'a':
            search_entry.clear()
            add_entry_prompt()
        elif start == 'b':
            # if the file doesn't exist it means that there are no entries made so a search is not possible
       # if file_exists:
            search_entry.clear()
            search_entry_prompt()
           # else:
           #  print("There are no entries, first add an entry before you search")
            search_entry.clear()

        elif start == 'c':
            search_entry.clear()
            print("Thank you for using the Worklog, goodbye!")
            sys.exit()

def add_entry_prompt():
    """Creates a csv file, in the csv method the methods to ask user for input will be called
        After the entry is added, the instructions menu will be shown again"""
    write_to_csv()
    back_to_menu()


def back_to_menu():
    """If the user enters any key they will be taken back to the menu"""
    to_menu = input("The entry has been added. Press any key to return to the menu! ")

    if to_menu == "":
        search_entry.clear()
        instructions()


def search_entry_prompt():
    search_entry.clear()

    """The search method will be run accordingly depending on the user input"""
    search_by = input("Do you want to search by: \n"
                      "a) Exact date\n"
                      "b) Exact search\n" 
                      "c) Regex pattern\n"
                      "d) Time spent\n"
                      "e) return to menu")
    if search_by == 'a':
        search_entry.clear()
        search_entry.find_by_date()
    elif search_by == 'b':
        search_entry.clear()
        search_entry.find_by_exact_search()
    elif search_by == 'c':
        search_entry.clear()
        search_entry.find_by_pattern()
    elif search_by == 'd':
        search_entry.clear()
        search_entry.find_by_time_spent()


def write_to_csv():
    file_exists = os.path.isfile('worklog.csv')

    with open('worklog.csv', 'w') as csv_file:
        fieldnames = ['Taskdate', 'TaskTitle', 'Minutes', 'Notes']

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

        # only if the file does not exist, csv_writer will write the headers
        if not file_exists:
            csv_writer.writeheader()

        csv_writer.writerow({'Taskdate': add_entry.task_date(), 'TaskTitle': add_entry.task_title(),
                             'Minutes': add_entry.time_spent(), 'Notes': add_entry.notes()})

        nopes = SearchEntry()
        nopes.update_csv()

if __name__ == '__main__':
    instructions()

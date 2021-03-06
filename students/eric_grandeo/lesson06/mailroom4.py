#!/usr/bin/env python3

#mailroom4 exercise

import sys
from collections import OrderedDict
import os

donors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54]}


#switch between users selections, using a dict
def menu_selection(prompt, dispatch_dict):
    while True:
        #handle KeyError
        try:
            response = input(prompt)
            dispatch_dict[response](donors)
        except KeyError:
            print("Please select 1 through 4. \n")

#this function is for the submenu
def sub_menu_selection(prompt, dispatch_dict):
    while True:
        try:
            response = input(sub_prompt).title()
            #removes spaces and checks if there is a number
            if not response.replace(" ", "").isalpha():
                raise ValueError
        except ValueError:
            print("Please enter a name, list, or q to quit \n")
        
        else:
            if response in dispatch_dict:
                dispatch_dict[response](donors) == "exit menu"
                break
            else:
                try:
                    donation = input("Please enter in a donation, or 'q' to quit: ")
                    if donation == "q":
                        break
                    elif donation.isalpha():
                        raise ValueError
                    else:
                        add_donation(response, donation, donors)
                        thankyou_email(response, donation)    
                        break 
                except ValueError:
                    print("Please enter a number \n")        

                

#updates donor dictionary if new or existing donor
def add_donation(name, donation, donors):
    if name in donors:
        donors[name].append(int(donation))    
    else:
        donors[name] = [int(donation)]


#prints a thank you email using a dict, instead of a list
def thankyou_email(name, donation):
    """Prints the letter with the user inputted name and donation """
    
   
    email_dict = dict(name=name, donation=int(donation))

    #need to return this
    result = """
    Dear {name},
    Thank you very much for the generous donation of ${donation:,.2f}
    It is very much appreciated.
    Respectfully,

    Eric G.
    """.format(**email_dict)

    print(result)
    return result

#calls the sub menu function when thank you is selected from main menu
def thank_you(donors):
    sub_menu_selection(sub_prompt, sub_dispatch)

#sorts dict in create report
def sort_key(items):
    """Sort key for the sorted list in create report"""
    return items[1]

#Creates reports by creating a new dict from the donors dict

#refactored function separating logic and presentation
def create_report_data(donors):
    names = [*donors]
    vals = [[round(sum(x), 2), len(x), round(sum(x)/len(x), 2)] for x in list(donors.values())] 
    new_dict = dict(zip(names,vals))
    sorted_donors2 = OrderedDict(sorted(new_dict.items(), key=lambda t: t[1], reverse=True))
    return sorted_donors2


def create_report(donors):
    report_data = create_report_data(donors)
    print("{:<25s}|{:>15s} |{:>10s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(68 * '-')
    
    for k,v in report_data.items():
        print("{:<25s}|${:>14,.2f} |{:>10.0f} |${:>12,.2f}".format(k, v[0], v[1], v[2]))
    print()

#creates a letter in the current directory that thanks donor for sum of donations
def send_letters(donors):
    for donor,donation in donors.items():
        with open(donor.replace(" ", "_") + '.txt', 'w+') as f:
           f.write("""Dear {},

           Thank you very much for the generous total donation of ${:,.2f}

           It is very much appreciated.

                Respectfully,
                Eric G.""".format(donor, sum(donation)))
    print("Letter were created and are in the {} directory.".format(os.getcwd()))
    print("")

def quit_submenu(donors):
    return "exit menu"

def quit_program(donors):
    print("Good Bye")
    sys.exit()

def display_donors(donors):
    names = list((donors.keys()))
    print("Donor names: {}".format(", ".join(names)))
    return names


main_prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))

#change quit program to just break the loop
main_dispatch = {"1" : thank_you,
                "2" : create_report,
                "3" : send_letters,
                "4": quit_program}

sub_prompt = "\n".join(("Please enter one of the following",
            "A full name",
            "Type list to see all name",
            "Enter 'q' to quit",
            ">>> "))

sub_dispatch = {"List" : display_donors,
                "Q" : quit_submenu}


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)

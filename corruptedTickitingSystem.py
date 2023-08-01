# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 22:04:28 2023

@author: MahmoudElYakhni
"""
# https://theprogrammingexpert.com/python-date-format-yyyymmdd/
from datetime import datetime
# https://docs.python.org/3/library/csv.html
# The so-called CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.
import csv

# Global Variables
tickets_file = "tickets.txt"
users = {"admin": "admin123123"}
special_list = []

# Assuming that "tickets.txt" in the same folder with "corruptedTicketingSystem.py".
# Function to read tickets from the text file and populate the special list
# https://www.w3schools.com/python/python_file_open.asp
def readTickets():
    with open(tickets_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            special_list.append(row)

# admin menu
def adminMenu():
    while True:
        print("\nAdmin Menu:")
        print("\t1. Display Statistics")
        print("\t2. Book a Ticket")
        print("\t3. Display all Tickets")
        print("\t4. Change Ticket’s Priority")
        print("\t5. Disable Ticket")
        print("\t6. Run Events")
        print("\t7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1": # O(n)
            displayStatistics()
        elif choice == "2": # O(n)
            bookTicket()
        elif choice == "3": # O(n)
            displayAllTickets()
        elif choice == "4": # O(n)
            changePriority()
        elif choice == "5": # O(n)
            disableTicket()
        elif choice == "6": # O(n)
            runEvents()
        elif choice == "7": # O(1)
            saveTickets()
            print("Exiting without saving!")
            break
        else:
            print("Your choice is invalid, please choose from 1 to 6 only.")

# user menu
def userMenu(username):
    while True:
        print(f"\nWelcome, {username}!") # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
        print("\t1. Book a ticket") # O(n)
        print("\t2. Exit") # O(1)

        choice = input("Enter your choice: ")
        if choice == "1":
            bookTicket(username)
        elif choice == "2":
            saveTickets()
            print("saving any newly added tickets and terminating the program!")
            break
        else:
            print("Your choice is invalid, choose 1 or 2 only.")

# display statistics
def displayStatistics():
    event_count = {}  # Dictionary to store event IDs and their ticket counts

    # Count tickets for each event ID
    for ticket in special_list:
        event_id = ticket[1]
        if event_id in event_count:
            event_count[event_id] += 1
        else:
            event_count[event_id] = 1

    if not event_count:
        print("No tickets found.")
        return

    # Find the event ID with the highest number of tickets
    max_event_id = max(event_count, key=event_count.get)
    max_ticket_count = event_count[max_event_id]

    print("\nEvent ID with the highest number of tickets:")
    print("Event ID:", max_event_id)
    print("Number of Tickets:", max_ticket_count)

# book a ticket
def bookTicket(username=None):
    print("\nBook a Ticket:")
    event_id = input("Enter Event ID: ").strip()
    date = input("Enter Date of the Event (YYYYMMDD): ").strip()
    username = input("Enter Username: ").strip()
    priority = input("Enter Priority: ").strip()

    # Check if the priority is a valid integer
    if not priority.isdigit():
        print("Invalid priority. Please enter a valid integer.")
        return

    # Increment ticket ID
    ticket_id = "tick" + str(len(special_list) + 1)

    # Add the new ticket to the special list
    new_ticket = [ticket_id, event_id, username, date, int(priority)]
    special_list.append(new_ticket)

    print("Ticket booked successfully!")

# display all tickets
def displayAllTickets():
    print("\nAll Tickets:")
    for ticket in special_list:
        print(", ".join(ticket))

# change ticket's priority
def changePriority():
    print("\nChange Ticket's Priority:")
    ticket_id = input("Enter Ticket ID: ").strip()
    priority = input("Enter New Priority: ").strip()

    # Check if the priority is a valid integer
    if not priority.isdigit():
        print("Invalid priority. Please enter a valid integer.")
        return

    # Find the ticket with the specified ticket ID
    found_ticket = False
    for ticket in special_list:
        if ticket[0] == ticket_id:
            ticket[4] = int(priority)
            found_ticket = True
            print("Priority updated successfully for Ticket ID:", ticket_id)
            break

    if not found_ticket:
        print("Ticket with ID", ticket_id, "not found.")

# disable a ticket
def disableTicket():
    print("\nRemove a Ticket:")
    ticket_id = input("Enter Ticket ID: ").strip()

    # Find the ticket with the specified ticket ID
    found_ticket = False
    for ticket in special_list:
        if ticket[0] == ticket_id:
            special_list.remove(ticket)
            found_ticket = True
            print("Ticket with ID", ticket_id, "removed from the system.")
            break

    if not found_ticket:
        print("Ticket with ID", ticket_id, "not found.")

# save tickets to the text file
def saveTickets():
    with open(tickets_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(special_list)

# Main function
def main():
    readTickets()

    # User Login
    while True:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username in users and users[username] == password:
            adminMenu()
            break
        elif username != "" and username not in users:
            print("Incorrect Username try again")
        else:
            userMenu(username)
            break

main()
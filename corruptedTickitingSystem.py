# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:04:28 2023

@author: iktased
"""
from datetime import datetime
import csv

# Global Variables
tickets_file = "tickets.txt"
users = {"admin": "admin123123"}
special_list = []

# Function to read tickets from the text file and populate the special list
def read_tickets():
    with open(tickets_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            special_list.append(row)

# Function to display admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket’s Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_statistics()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            display_all_tickets()
        elif choice == "4":
            change_priority()
        elif choice == "5":
            disable_ticket()
        elif choice == "6":
            run_events()
        elif choice == "7":
            save_tickets()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display normal user menu
def user_menu(username):
    while True:
        print(f"\nWelcome, {username}!")
        print("1. Book a ticket")
        print("2. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            book_ticket(username)
        elif choice == "2":
            save_tickets()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display statistics
def display_statistics():
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
    pass

# Function to book a ticket
def book_ticket(username=None):
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
    pass

# Function to display all tickets
def display_all_tickets():
    print("\nAll Tickets:")
    for ticket in special_list:
        print(", ".join(ticket))

# Function to change ticket's priority
def change_priority():
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
    pass

# Function to disable a ticket
def disable_ticket():
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
    pass

# Function to run events
def run_events():
    print("\nToday's Events (Sorted by Priority):")
    
    # Get the current date
    current_date = datetime.now().strftime("%Y%m%d")

    # Filter the tickets for today's events
    today_tickets = [ticket for ticket in special_list if ticket[3] == current_date]

    # Sort today's events by priority
    today_tickets.sort(key=lambda ticket: ticket[4])

    if not today_tickets:
        print("No events found for today.")
        return

    for ticket in today_tickets:
        print(", ".join(ticket))

    # Remove today's events from the special list
    special_list[:] = [ticket for ticket in special_list if ticket not in today_tickets]

    pass

# Function to save tickets to the text file
def save_tickets():
    with open(tickets_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(special_list)

# Main function to run the program
def main():
    read_tickets()

    # User Login
    while True:
        username = input("Username: ").strip()
        password = input("Password (leave empty for normal user): ").strip()

        if username in users and users[username] == password:
            admin_menu()
            break
        elif username != "" and username not in users:
            print("Invalid username. Please try again.")
        else:
            user_menu(username)
            break

if __name__ == "__main__":
    main()
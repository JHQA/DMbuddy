import csv
import os
from tabulate import tabulate

def create_csv_file(file_name):
    try:
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ["Town", "Name", "Bio", "Current"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print(f"CSV file '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating CSV file '{file_name}': {e}")

def print_menu():
    print()
    print("Select an option:")
    print("1. Print all entries")
    print("2. Print entries by Town")
    print("3. Print entries by Name")
    print("4. Print entries by Bio")
    print("5. Print entries by Current")
    print("6. Add a new entry")
    print("7. Update an entry")
    print("8. Delete an entry")
    print("0. Exit")

def print_entries(entries):
    if entries:
        for entry in entries:
            print("Town:", entry["Town"])
            print("Name:", entry["Name"])
            print("Bio:", entry["Bio"])
            print("Current:", entry["Current"])
            print()  # Print an empty line for better readability
    else:
        print("No entries found.")

def print_entries_by_town(entries, town):
    found = False
    for entry in entries:
        if entry["Town"] == town:
            print("Town:", entry["Town"])
            print("Name:", entry["Name"])
            print("Bio:", entry["Bio"])
            print("Current:", entry["Current"])
            print()  # Print an empty line for better readability
            found = True
    if not found:
        print("No entries found for the specified town.")

def print_entries_by_name(entries, name):
    found = False
    for entry in entries:
        if entry["Name"] == name:
            print("Town:", entry["Town"])
            print("Name:", entry["Name"])
            print("Bio:", entry["Bio"])
            print("Current:", entry["Current"])
            print()  # Print an empty line for better readability
            found = True
    if not found:
        print("No entries found for the specified name.")

def print_entries_by_bio(entries, bio):
    found = False
    for entry in entries:
        if bio.lower() in entry["Bio"].lower():
            print("Town:", entry["Town"])
            print("Name:", entry["Name"])
            print("Bio:", entry["Bio"])
            print("Current:", entry["Current"])
            print()  # Print an empty line for better readability
            found = True
    if not found:
        print("No entries found for the specified bio keyword.")

def print_entries_by_current(entries, current):
    found = False
    for entry in entries:
        if current.lower() in entry["Current"].lower():
            print("Town:", entry["Town"])
            print("Name:", entry["Name"])
            print("Bio:", entry["Bio"])
            print("Current:", entry["Current"])
            print()  # Print an empty line for better readability
            found = True
    if not found:
        print("No entries found for the specified current activity keyword.")

def get_unique_towns(entries):
    return sorted(set(entry["Town"] for entry in entries))

def get_unique_names(entries):
    return sorted(set(entry["Name"] for entry in entries))

def add_entry(entries):
    town = input("Enter the town (or 'back' to return to main menu): ")
    if town.lower() == 'back':
        return entries
    name = input("Enter the name: ")
    bio = input("Enter the bio: ")
    current = input("Enter the current activity: ")
    new_entry = {"Town": town, "Name": name, "Bio": bio, "Current": current}
    entries.append(new_entry)
    return entries

def update_entry(entries, name):
    updated_entry = None
    for entry in entries:
        if entry["Name"] == name:
            print("Update entry:")
            town = input(f"Enter new town for {name} (or 'back' to return to main menu): ")
            if town.lower() == 'back':
                return
            bio = input(f"Enter new bio for {name}: ")
            current = input(f"Enter new current activity for {name}: ")
            entry.update({"Town": town, "Bio": bio, "Current": current})
            updated_entry = entry
            break
    if updated_entry:
        print(f"Entry for {name} updated successfully.")
    else:
        print(f"No entry found for {name}.")

def delete_entry(entries, name):
    deleted_entry = None
    for i, entry in enumerate(entries):
        if entry["Name"] == name:
            del entries[i]
            deleted_entry = entry
            break
    if deleted_entry:
        print(f"Entry for {name} deleted successfully.")
    else:
        print(f"No entry found for {name}.")

def save_entries_to_csv(entries, file_name):
    try:
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ["Town", "Name", "Bio", "Current"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for entry in entries:
                writer.writerow(entry)
        print("Entries saved to", file_name)
    except Exception as e:
        print(f"An error occurred while saving entries to '{file_name}': {e}")

def print_entries(entries):
    if entries:
        table = []
        for entry in entries:
            table.append([entry["Town"], entry["Name"], entry["Bio"], entry["Current"]])
        print(tabulate(table, headers=["Town", "Name", "Bio", "Current"], tablefmt="grid"))
    else:
        print("No entries found.")

def print_entries_table(entries):
    if entries:
        table = []
        for entry in entries:
            table.append([entry["Town"], entry["Name"], entry["Bio"], entry["Current"]])
        print(tabulate(table, headers=["Town", "Name", "Bio", "Current"], tablefmt="plain"))
    else:
        print("No entries found.")

def print_update_delete_options(entries):
    print("Select an option:")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. Update/Delete entry for {entry['Name']}")
    print("0. Back to main menu")

def get_entries_by_town(entries, town):
    return [entry for entry in entries if entry["Town"] == town]

def get_entries_by_name(entries, name):
    return [entry for entry in entries if entry["Name"] == name]

def get_entries_by_bio(entries, bio):
    return [entry for entry in entries if bio.lower() in entry["Bio"].lower()]

def get_entries_by_current(entries, current):
    return [entry for entry in entries if current.lower() in entry["Current"].lower()]

def print_entries_table(entries):
    if entries:
        table = []
        for entry in entries:
            table.append([entry["Town"], entry["Name"], entry["Bio"], entry["Current"]])
        print(tabulate(table, headers=["Town", "Name", "Bio", "Current"], tablefmt="grid"))
    else:
        print("No entries found.")

def main():
    file_name = "DM.csv"
    entries = []

    try:
        if not os.path.isfile(file_name):
            create_option = input(f"CSV file '{file_name}' does not exist. Do you want to create it? (yes/no): ")
            if create_option.lower() == 'yes':
                create_csv_file(file_name)
            else:
                print("Exiting program.")
                return
        else:
            with open(file_name, 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile)
                entries = list(csvreader)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Exiting program.")
        return

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print_entries_table(entries)
        elif choice == "2":
            towns = get_unique_towns(entries)
            print()
            print("Towns available:")
            for i, town in enumerate(towns, 1):
                print(f"{i}. {town}")
            town_num = int(input("Enter the town number: "))
            town = towns[town_num - 1]
            town_entries = get_entries_by_town(entries, town)
            print_entries_table(town_entries)
        elif choice == "3":
            names = get_unique_names(entries)
            print()
            print("Names available:")
            for i, name in enumerate(names, 1):
                print(f"{i}. {name}")
            name_num = int(input("Enter the name number: "))
            name = names[name_num - 1]
            name_entries = get_entries_by_name(entries, name)
            print_entries_table(name_entries)
        elif choice == "4":
            bio = input("Enter a keyword in the bio: ")
            bio_entries = get_entries_by_bio(entries, bio)
            print_entries_table(bio_entries)
        elif choice == "5":
            current = input("Enter a keyword in the current activity: ")
            current_entries = get_entries_by_current(entries, current)
            print_entries_table(current_entries)
        elif choice == "6":
            entries = add_entry(entries)
            save_entries_to_csv(entries, file_name)
        elif choice == "7":
            print_update_delete_options(entries)
            option = input("Enter your choice: ")
            if option.isdigit():
                option = int(option)
                if 0 < option <= len(entries):
                    entry_name = entries[option - 1]["Name"]
                    update_entry(entries, entry_name)
                    save_entries_to_csv(entries, file_name)
                elif option == 0:
                    continue
                else:
                    print("Invalid option. Please select a valid option.")
            else:
                print("Invalid input. Please enter a number.")
        elif choice == "8":
            print_update_delete_options(entries)
            option = input("Enter your choice: ")
            if option.isdigit():
                option = int(option)
                if 0 < option <= len(entries):
                    entry_name = entries[option - 1]["Name"]
                    delete_entry(entries, entry_name)
                    save_entries_to_csv(entries, file_name)
                elif option == 0:
                    continue
                else:
                    print("Invalid option. Please select a valid option.")
            else:
                print("Invalid input. Please enter a number.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to CSV format.
Usage: python 1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data.get("username")

        if not username:
            print(f"User with ID {employee_id} not found.")
            sys.exit(1)

        # Fetch TODO list
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Export to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                csv_writer.writerow([
                    employee_id,
                    username,
                    task.get("completed"),
                    task.get("title")
                ])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error processing JSON data")
        sys.exit(1)
    except IOError:
        print(f"Error writing to file {csv_filename}")
        sys.exit(1)

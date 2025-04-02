#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID."""

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
        user_response.raise_for_status()  # Raise an exception for bad status codes
        user_data = user_response.json()
        employee_name = user_data.get("name")

        if not employee_name:
            print(f"User with ID {employee_id} not found.")
            sys.exit(1)

        # Fetch TODO list
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Process TODO list
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)

        # Print the results
        print(f"Employee {employee_name} is done with tasks("f"{number_of_done_tasks}/{total_tasks}):")

        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error processing JSON data")
        sys.exit(1) 
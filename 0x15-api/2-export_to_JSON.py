#!/usr/bin/python3
"""
Exports TODO list information for a given employee ID to JSON format.
Usage: python 2-export_to_JSON.py <employee_id>
"""

import json
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

        # Prepare JSON data
        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })

        json_data = {str(employee_id): tasks_list}

        # Export to JSON - ensure proper formatting
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file)
            json_file.write("\n")  # Add newline at end of file

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error processing JSON data")
        sys.exit(1)
    except IOError:
        print(f"Error writing to file {json_filename}")
        sys.exit(1)

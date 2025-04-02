#!/usr/bin/python3
"""
Exports TODO list information for all employees to JSON format.
Usage: python 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        # Fetch all users
        users_response = requests.get(users_url)
        users_response.raise_for_status()
        users_data = users_response.json()

        # Fetch all TODOs
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare JSON data - all employee tasks
        all_employees_tasks = {}
        
        for user in users_data:
            user_id = user.get("id")
            username = user.get("username")
            user_tasks = []
            
            # Filter tasks for this user
            for task in todos_data:
                if task.get("userId") == user_id:
                    user_tasks.append({
                        "username": username,
                        "task": task.get("title"),
                        "completed": task.get("completed")
                    })
            
            # Add user tasks to the main dictionary
            all_employees_tasks[str(user_id)] = user_tasks

        # Export to JSON
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_employees_tasks, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except ValueError:
        print("Error processing JSON data")
        sys.exit(1)
    except IOError:
        print(f"Error writing to file {json_filename}")
        sys.exit(1) 
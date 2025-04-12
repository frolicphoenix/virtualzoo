import requests
import yaml
import sys

API_URL = "http://localhost:8080"

def apply():
    with open("../pets/my_zoo.yaml", "r") as file:
        data = yaml.safe_load(file)
    response = requests.post(f"{API_URL}/apply", json=data)
    print(">> Apply Result:", response.json())

def destroy():
    response = requests.post(f"{API_URL}/destroy")
    print(">> Destroy Result:", response.json())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <apply|destroy>")
        exit(1)

    command = sys.argv[1]
    if command == "apply":
        apply()
    elif command == "destroy":
        destroy()
    else:
        print("Invalid command. Use 'apply' or 'destroy'.", command)
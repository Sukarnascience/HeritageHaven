from winotify import Notification, audio
import os
import requests
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "img", "logo.png")
new_json_data = None

# URL of the raw JSON file on GitHub
json_url = "https://raw.githubusercontent.com/Sukarnascience/HeritageHaven/blob/main/manifest.json"

def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

def isAvailabe():
    global new_json_data
    try:
        # Make an HTTP GET request to fetch the JSON data
        response = requests.get(json_url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the JSON data
        new_json_data = json.loads(response.text)

        # Now you can work with the JSON data
        print(f"Current Version: {new_json_data['version']}V")

    except requests.exceptions.RequestException as e:
        print("Error fetching JSON:", e)
        errorNotify()
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        errorNotify()

    #Fetch Info
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir,"manifest.json")
    json_data = read_json_file(file_path)
    
    if((new_json_data != None) and (new_json_data['version'] != json_data['version'])):
        return 1
    else:
        return 0

def updateNotify():
    toast = Notification(
        app_id = "Heritage Haven",
        title = "Update Available",
        msg = "An update is now available, featuring bug fixes and exciting new additions. Tap to update and enjoy the enhanced experience!",
        duration = "long",
        icon = image_path
    )
    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Update", launch="https://github.com/Sukarnascience/Sukarnascience")
    toast.add_actions(label="Not Now")
    toast.show()

def errorNotify():
    toast = Notification(
        app_id = "Heritage Haven",
        title = "Check Failure",
        msg = "Due to possible network or server issues, consider using a VPN.",
        duration = "long",
        icon = image_path
    )
    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Report Problem", launch="https://github.com/Sukarnascience/Sukarnascience")
    toast.show()

if __name__ == "__main__":
    if(isAvailabe()):
        updateNotify()
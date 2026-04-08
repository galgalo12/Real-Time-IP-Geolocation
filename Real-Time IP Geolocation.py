# ==============================================
# Real-Time IP Geolocation (JSON Output)
# ==============================================

import requests # Make sure to install the 'requests' library if you haven't already: pip install requests
import json # This will be used to format the output as JSON


def get_ip_geolocation(ip_address=""): # If no IP address is provided, it will use the caller's IP
    url = f"https://ipinfo.io/{ip_address}/json" # ipinfo.io provides geolocation data based on IP address in JSON format

    try: # try to make the API request and handle any potential errors
        r = requests.get(url, timeout=5) # Set a timeout to avoid hanging indefinitely
        r.raise_for_status() # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = r.json() # Parse the response as JSON

        # ipinfo does NOT return "status": "success"
        # Instead check for error field
        if "error" in data:
            raise ValueError(data.get("error", {}).get("message", "API Error"))

        return data # Return the geolocation data as a dictionary

    except Exception as e: # Catch any exceptions (network issues, invalid IP, API errors, etc.) and print the error message
        print(f"Error: {e}")
        return None # retrun None if there was an error


def show_ip_geolocation(): # created a function to display the geolocation information in a formatted JSON structure
    ip_address = input("Enter an IP address (or leave blank for your own): ").strip() # input from user, if left blank it will use the caller's IP address
    info = get_ip_geolocation(ip_address) # info will be a dictionary containing the geolocation data or None if there was an error

    if not info:
        print("Could not retrieve geolocation information.")
        return

    # Build JSON output
    geo_json = {
        "ip_geolocation_information": {
            "ip": info.get("ip", ""),
            "country": info.get("country", ""),
            "country_code": info.get("countryCode", ""),
            "region": info.get("region", ""),
            "city": info.get("city", ""),
            "location": info.get("loc", ""),
            "organization": info.get("org", ""),
            "timezone": info.get("timezone", ""),
            "status": info.get("status", ""),
        }
    }

    # Print formatted JSON
    print(json.dumps(geo_json, indent=4))


def main(): # def main function to run the program in a loop until the user decides to exit
    while True: # loop to continuously show the menu until the user chooses to exit
        print("\nReal-Time IP Geolocation")
        print("1. Get IP Geolocation")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ").strip() # choice input from user to either get geolocation information or exit the program

        if choice == "1":
            show_ip_geolocation()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

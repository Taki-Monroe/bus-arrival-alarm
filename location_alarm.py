import time
import math
import subprocess
from geopy.distance import geodesic

# Replace these with your destination's coordinates
DESTINATION = (23.8103, 90.4125)  # Example: Dhaka coordinates

# Define the alert distance (in meters)
ALERT_DISTANCE = 500  # 5 minutes before arrival (adjust as needed)

def get_current_location():
    try:
        result = subprocess.run(['termux-location', '--provider', 'gps'], stdout=subprocess.PIPE)
        location_data = eval(result.stdout.decode())
        return (location_data['latitude'], location_data['longitude'])
    except Exception as e:
        print("Error fetching location:", e)
        return None

def calculate_distance(current, destination):
    return geodesic(current, destination).meters

def trigger_alarm():
    subprocess.run(['termux-vibrate', '-d', '1000'])  # Vibrate for 1 second
    subprocess.run(['termux-notification', '--title', 'Wake Up!', '--content', 'You are near your destination!'])

def main():
    print("Tracking your location... Press Ctrl+C to exit.")
    while True:
        current_location = get_current_location()
        if current_location:
            distance = calculate_distance(current_location, DESTINATION)
            print(f"Current distance to destination: {distance:.2f} meters")

            if distance <= ALERT_DISTANCE:
                trigger_alarm()
                break

        time.sleep(30)  # Check location every 30 seconds

if __name__ == "__main__":
    main()

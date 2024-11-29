# Bus Arrival Alarm

A Python script for **Termux** that alerts you (via vibration and notification) when your phone is 5 minutes away from a specific location while traveling by bus. Perfect for people who want to take a nap during their commute but need to wake up before reaching their destination.

## Features
- **GPS Tracking**: Uses Termux's built-in `termux-location` API to get real-time GPS coordinates.
- **Proximity Alert**: Triggers an alarm (vibration and notification) when you're within a specified distance (500 meters by default) from the destination.
- **Easy to Use**: Simple to set up and run in Termux.

## Requirements
- Android phone with Termux installed.
- Termux location permissions enabled for GPS.
- Python installed in Termux (`pkg install python`).
- `termux-api` package (`pkg install termux-api`).

## Setup

1. **Install Termux**:
   - Download Termux from the Google Play Store or F-Droid.
   
2. **Install Dependencies**:
   Open Termux and run the following commands:
   ```bash
   pkg update && pkg upgrade
   pkg install python termux-api
   pip install geopy
   ```

3. **Clone this repository**:
   ```bash
   git clone https://github.com/Taki-Monroe/bus-arrival-alarm.git
   cd bus-arrival-alarm
   ```

4. **Edit the Script**:
   - Open the script (`location_alarm.py`) and update the `DESTINATION` variable with your target location (latitude and longitude).
   
5. **Run the Script**:
   ```bash
   python location_alarm.py
   ```
   The script will track your location and alert you when you're near your destination.

## Customization
- **ALERT_DISTANCE**: Modify the `ALERT_DISTANCE` variable in the script to change the distance at which the alarm triggers (in meters).
- **Sleep Interval**: The script checks your location every 30 seconds by default, but you can modify the `time.sleep(30)` interval in the script for faster or slower checks.

## Notes
- This solution works on Android phones using Termux.
- The accuracy of the alarm depends on your phone's GPS and signal strength.

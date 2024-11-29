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

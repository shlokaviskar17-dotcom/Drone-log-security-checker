import csv

# Sample mock drone log data (Timestamp, Latitude, Longitude, Altitude_m, Battery_Pct, Signal_RSSI)
flight_logs = [
    {"time": "12:00:01", "lat": 20.0063, "lon": 73.7898, "alt": 100, "battery": 98, "rssi": -50},
    {"time": "12:00:02", "lat": 20.0065, "lon": 73.7899, "alt": 102, "battery": 97, "rssi": -52},
    # GPS SPOOFING ANOMALY: Massive location jump in 1 second
    {"time": "12:00:03", "lat": 28.6139, "lon": 77.2090, "alt": 105, "battery": 96, "rssi": -55}, 
    # SIGNAL JAMMING ANOMALY: Severe RSSI drop
    {"time": "12:00:04", "lat": 20.0068, "lon": 73.7902, "alt": 108, "battery": 95, "rssi": -115}, 
    # BATTERY CRITICAL ANOMALY
    {"time": "12:00:05", "lat": 20.0070, "lon": 73.7905, "alt": 110, "battery": 2, "rssi": -50}, 
]

def analyze_logs(logs):
    print("=== DRONE TELEMETRY SECURITY REPORT ===")
    
    for i in range(len(logs)):
        entry = logs[i]
        
        # Check 1: Signal Jamming / High RSSI Drop
        if entry["rssi"] < -90:
            print(f"[ALERT] Time {entry['time']}: Potential RF Jamming Detected! (RSSI: {entry['rssi']} dBm)")
            
        # Check 2: Critical Battery Drop
        if entry["battery"] < 5:
            print(f"[CRITICAL] Time {entry['time']}: Battery unsafe for flight! ({entry['battery']}%)")
            
        # Check 3: GPS Spoofing (Position Jump Check)
        if i > 0:
            prev_lat = logs[i-1]["lat"]
            # Simple check for extreme latitude jump (> 1 degree in 1 sec)
            if abs(entry["lat"] - prev_lat) > 1.0:
                print(f"[WARNING] Time {entry['time']}: GPS Spoofing Detected! Impossible position shift.")

if __name__ == "__main__":
    analyze_logs(flight_logs)

from flask import Flask, jsonify, send_file
import win32evtlog

app = Flask(__name__)
patterns = {
    "Failed Login": "4625",
    "Successful Login": "4624",
    "User Creation": "4720",
    "Privilege Use": "4672",
    "Group Membership Change": "4627",
    "User Deletion": "4726",
    "Local Group Member Added": "4732",
    "Local Group Member Removed": "4733",
    "Account Lockout": "4740",
    "Account Changed": "4781",
    "Code Integrity Violation": "5038",
    "Network Share Access": "5140",
    "Credential Theft Attempt": "5379"
}


# Logs to scan
log_types = ["Security", "System", "Application", "Setup", "ForwardedEvents"]

def scan_logs():
    alerts = []
    for log_type in log_types:
        try:
            handle = win32evtlog.OpenEventLog(None, log_type)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            
            total_events_read = 0
            while True:
                events = win32evtlog.ReadEventLog(handle, flags, 0)
                if not events:
                    break
                total_events_read += len(events)
                for event in events:
                    event_id = str(event.EventID & 0xFFFF)
                    event_time = event.TimeGenerated.Format()  # Get event date/time as string
                    for alert_name, alert_code in patterns.items():
                        if alert_code == event_id:
                            msg = (f"[ALERT] {alert_name} in {log_type}: Event ID {event_id} | "
                                   f"Source: {event.SourceName} | Time: {event_time}")
                            alerts.append(msg)
                if total_events_read > 100000:
                    break

            win32evtlog.CloseEventLog(handle)  # Close the event log handle

        except Exception as e:
            alerts.append(f"[!] Error reading {log_type}: {str(e)}")
    return alerts

@app.route('/')
def home():
    # Serve the index.html from the same folder
    return send_file("index.html")

@app.route('/scan')
def scan():
    alerts = scan_logs()
    return jsonify(alerts=alerts)

if __name__ == "__main__":
    app.run(debug=True)

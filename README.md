# 🔍 Windows Log Analyzer

A lightweight Flask-based application to scan Windows Event Logs and identify security-related alerts like failed logins, account changes, user creation, privilege use, and more.

---

## 📌 Features

- Scans major Windows logs: `Security`, `System`, `Application`, `Setup`, and `ForwardedEvents`.
- Detects and displays alerts based on predefined Event IDs.
- Real-time log scanning from a web interface.
- Filter logs by alert type (e.g., Failed Login, User Creation).
- Displays time of each event.

---

## 🚀 How to Use

### 1. ✅ Requirements

- Windows OS
- Python 3.x
- Admin privileges to access Windows Event Logs

### 2. 🧰 Install Dependencies

Open **Command Prompt** or **PowerShell** and run:

```bash
pip install flask pywin32
```

### 3. 📁 Clone the Repository

```bash
git clone https://github.com/jershonpaulisaac/win-log-analyser.git
cd win-log-analyser
```

### 4. ▶️ Run the App

Run the following command inside the project folder:

```bash
python app.py
```

By default, it starts at:  
**http://127.0.0.1:5000/**

### 5. 🌐 Open in Browser

Go to:  
[http://localhost:5000](http://localhost:5000)

You will see the log analyzer interface.  
Click the **"Scan Logs"** button to view logs, and use the dropdown to filter specific alerts.

---

## 📋 Alert Types Detected

- Failed Login  
- Successful Login  
- User Creation  
- Privilege Use  
- Group Membership Change  
- User Deletion  
- Local Group Member Added  
- Local Group Member Removed  
- Account Lockout  
- Account Changed  
- Code Integrity Violation  
- Network Share Access  
- Credential Theft Attempt  

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

---

## 👨‍💻 Author

Developed by **Jershon Paul Isaac R**  
[GitHub Repository](https://github.com/jershonpaulisaac/win-log-analyser)

---


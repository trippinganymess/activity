🐙 GitHub Activity Monitor CLI

A lightweight terminal application designed to fetch and display recent GitHub activity using the GitHub API.

## ✨ Features

- **Activity Tracking**: Fetches the latest GitHub events and generates concise descriptions for each activity type.
- **Timestamping**: Every activity log includes the exact time the event occurred.
- **Color Coding**: Uses terminal colors to distinguish between different types of GitHub activities (Push, Pull Requests, Issues, etc.).

## 📋 Prerequisites

- Python 3.6 or higher
- Git (for cloning the repository)
- A GitHub account (optional, but recommended for higher API limits)

🚀 How to Use

1. Clone the Repository

```bash
git clone https://github.com/trippinganymess/activity
cd activity
```


2. Set Up Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Requirements

```bash
pip install -r requirements.txt
```

4. Run the Application

```bash
python main.py
```


📸 Sample Run

![App Preview](https://github.com/trippinganymess/activity/blob/main/assests/sample.png?raw=true)

## 🚀 Usage

After running `python main.py`, enter a GitHub username when prompted to fetch and display their recent activity events.

⚠️ API Rate Limits

Please be aware that the GitHub API allows only 60 requests per hour for unauthenticated users. If this limit is exceeded, the application will timeout until your quota resets.
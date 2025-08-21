# Telegram Complaint Bot

This Python script automates sending complaints to Telegram support about a user violating rules. It sends emails from multiple Gmail accounts to specified recipient addresses every 30 seconds for 5 minutes.

# Features
- Reads Gmail account credentials from `gmails.json`.
- Reads recipient email addresses from `wheresend.json`.
- Prompts the user for:
  - Username (or "none" if not applicable)
  - User ID
  - Reason for the complaint
  - Chat link where the violation occurred
  - Message link violating Telegram rules
- Generates a complaint email in English.
- Sends complaints every 30 seconds for 5 minutes (10 iterations) from all Gmail accounts to all recipient addresses.

# Prerequisites
- Python 3.x
- Termux (if running on Android) or any Python environment
- Gmail accounts with App Passwords enabled (see below)

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telegram-complaint-bot.git
   cd telegram-complaint-bot
# Academic Grade Monitoring System

Automation system that monitors university grade updates and sends instant Telegram notifications when new grades are published.

---

## Features

- Automated login session support
- Grade monitoring system
- Telegram notification integration
- Session expiration detection
- Browser automation with Playwright
- HTML parsing with BeautifulSoup
- Persistent browser profile support

---

## Technologies Used

- Python
- Playwright
- BeautifulSoup4
- Telegram Bot API
- Requests
- dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/academic-grade-monitoring-system.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

## Environment Variables

Create a `.env` file in the project directory:

```env
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

---

## Run The Project

```bash
python app.py
```

---

## System Workflow

1. User logs into the university portal
2. System monitors grade page periodically
3. Grade changes are detected automatically
4. Telegram notification is sent instantly
5. Session expiration is monitored continuously

---

## Future Improvements

- Multi-user support
- Web dashboard
- Mobile push notifications
- Docker support
- AI-based grade analysis

---

## Disclaimer

This project was developed for educational and personal automation purposes.
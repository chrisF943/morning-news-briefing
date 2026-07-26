#!/usr/bin/env python3
"""
Morning Briefing Sender
Reads HTML content from stdin and sends via Brevo's HTTPS transactional email API.
(Switched from raw SMTP because Claude Code cloud environments only allow
HTTPS/443 egress through the network proxy -- port 587 is blocked.)

Called by Claude Code Routine: python3 send_briefing.py < /tmp/briefing.html
"""

import os
import sys
import requests
from datetime import date


def send_briefing(html_content: str) -> None:
    api_key = os.environ["BREVO_API_KEY"]      # Brevo API key (v3), NOT the SMTP login/pass
    from_addr = os.environ["BRIEFING_FROM"]    # arv28385@outlook.com
    to_addr = os.environ["BRIEFING_TO"]        # swills_skeins0@icloud.com

    today = date.today().strftime("%B %d, %Y")

    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers={
            "api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json={
            "sender": {"name": "Morning Briefing", "email": from_addr},
            "to": [{"email": to_addr}],
            "subject": f"Daily Briefing -- {today}",
            "htmlContent": html_content,
        },
        timeout=30,
    )
    response.raise_for_status()
    print(f"Sent to {to_addr} ({today}) -- status {response.status_code}")


if __name__ == "__main__":
    content = sys.stdin.read().strip()
    if not content:
        print("No HTML content received on stdin.", file=sys.stderr)
        sys.exit(1)
    send_briefing(content)

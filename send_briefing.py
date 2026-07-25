#!/usr/bin/env python3
"""
Morning Briefing Sender
Reads HTML content from stdin and sends via Brevo SMTP.
Called by Claude Code Routine: python3 send_briefing.py < /tmp/briefing.html
"""

import smtplib
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date


def send_briefing(html_content: str) -> None:
    smtp_host = "smtp-relay.brevo.com"
    smtp_port = 587

    smtp_user = os.environ["BREVO_SMTP_USER"]   # ac5567001@smtp-brevo.com
    smtp_pass = os.environ["BREVO_SMTP_PASS"]   # your Brevo SMTP key
    from_addr = os.environ["BRIEFING_FROM"]     # arv28385@outlook.com
    to_addr   = os.environ["BRIEFING_TO"]       # swills_skeins0@icloud.com

    today = date.today().strftime("%B %d, %Y")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Daily Briefing — {today}"
    msg["From"]    = f"Morning Briefing <{from_addr}>"
    msg["To"]      = to_addr
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, to_addr, msg.as_string())

    print(f"✅ Briefing sent to {to_addr} ({today})")


if __name__ == "__main__":
    content = sys.stdin.read().strip()
    if not content:
        print("❌ No HTML content received on stdin.", file=sys.stderr)
        sys.exit(1)
    send_briefing(content)
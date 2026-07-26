# Morning News Briefing

A Claude Code Routine that runs every morning at 9:00 AM EDT, searches the web for the latest AI, tech, cloud, and finance news, and delivers a formatted HTML email digest via the Brevo API.

## How It Works

1. A scheduled Claude Code Routine triggers daily on Anthropic's cloud infrastructure
2. Claude searches the web for news from the past 24 hours across AI, tech, cloud, and finance
3. Claude compiles the findings into a formatted HTML email
4. `send_briefing.py` sends it via the Brevo HTTPS transactional email API from a dedicated Outlook address to iCloud

No local machine or open terminal required — runs entirely on Anthropic's cloud.

## Repo Structure

```
morning-news-briefing/
├── send_briefing.py     # Sender — reads HTML from stdin, POSTs to the Brevo API
├── requirements.txt     # requests
└── README.md
```

## Environment Variables

Set in the Claude Code cloud environment (`daily news briefing`), not in this repo.

| Variable | Description |
|---|---|
| `BREVO_API_KEY` | Brevo v3 API key (not the SMTP login/pass) |
| `BRIEFING_FROM` | Sender address (Outlook) |
| `BRIEFING_TO` | Recipient address (iCloud) |

Never commit credentials to this repo.

## Routine Setup

- **Platform:** Claude Code Routines (claude.ai/code/routines)
- **Trigger:** Daily at 9:00 AM EDT
- **Repository:** this repo
- **Environment:** `daily news briefing` (cloud environment with env vars above)
- **Model:** Claude Opus 4.8

## Email Format

The briefing covers three sections:

- **AI & Technology** — model releases, lab news, agents, industry moves
- **Finance & Markets** — indices, economic data, earnings, market outlook
- **Cloud & Infrastructure** — major cloud providers, compute, data center news

#!/usr/bin/env python3
"""Scout Ambient feed producer (stub with real shape).

Builds the Scout feed JSON from two local cache files and writes it to
out/home.json. It deliberately has no live sources wired in: fill the
caches from Brandon's own sources (Google Calendar for nextEvent /
calendar / dash, the Compass brief for brief) and point the app at the
published file. A field is published only when its cache verified
during that run; nothing is carried over except the caches themselves.

Caches (same directory):
  brief-lines.json    {"title", "briefDate": "YYYY-MM-DD", "lines": [...]}
  calendar-cache.json {"generatedAt", "events": [{"summary", "start", "end"}]}

Usage: python3 scout_feed_producer.py [--out out/home.json]
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
CT = ZoneInfo("America/Chicago")


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def parse_local(value):
    """Parse an ISO-8601 local time; return an aware datetime or None."""
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def next_event(events, now):
    future = []
    for e in events or []:
        start = parse_local(e.get("start"))
        summary = (e.get("summary") or "").strip()
        if start and summary and start >= now:
            future.append((start, summary))
    if not future:
        return None
    future.sort(key=lambda item: item[0])
    start, summary = future[0]
    return {"title": summary, "time": start.strftime("%-I:%M %p")}


def calendar_field(events, now):
    """Collapse the month's events to per-day counts (max 3 shown by the app)."""
    month = now.strftime("%Y-%m")
    days = {}
    compiled = None
    for e in events or []:
        start = parse_local(e.get("start"))
        summary = (e.get("summary") or "").strip()
        if not start or not summary:
            continue
        if start.strftime("%Y-%m") != month:
            continue
        if summary.lower() == "sleep":
            continue
        key = start.strftime("%Y-%m-%d")
        days[key] = min(3, days.get(key, 0) + 1)
    if not days:
        return None
    return {"month": month,
            "compiledAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "days": days}


def dash_lines(events, now, brief_lines):
    """Today's events first, then the brief's top lines; max 6 total."""
    lines = []
    for e in events or []:
        start = parse_local(e.get("start"))
        summary = (e.get("summary") or "").strip()
        if not start or not summary:
            continue
        if start.date() != now.date() or summary.lower() == "sleep":
            continue
        lines.append("Today: %s %s" % (summary, start.strftime("%-I:%M %p")))
        if len(lines) >= 6:
            return lines
    for line in brief_lines or []:
        if len(lines) >= 6:
            break
        if line and line not in lines:
            lines.append(line)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "out" / "home.json"))
    args = ap.parse_args()
    now = datetime.now(CT)  # Chicago local: brief dates and "today" are Chicago dates
    utc_now = now.astimezone(timezone.utc)

    brief = load_json(HERE / "brief-lines.json") or {}
    cache = load_json(HERE / "calendar-cache.json") or {}
    events = cache.get("events") or []

    feed = {
        "houseMode": "Home",
        "whoHome": ["Brandon"],
        "scout": {"status": "Home", "note": "Compass pointing home"},
        "alerts": [],
        "updatedAt": utc_now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    nxt = next_event(events, now)
    if nxt:
        feed["nextEvent"] = nxt
    lines = (brief.get("lines") or [])[:4]
    if lines and brief.get("briefDate") == now.strftime("%Y-%m-%d"):
        feed["brief"] = {"title": brief.get("title") or "Daily Brief", "lines": lines}
    cal = calendar_field(events, now)
    if cal:
        feed["calendar"] = cal
    dash = dash_lines(events, now, lines)
    if dash:
        feed["dash"] = dash

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp")
    tmp.write_text(json.dumps(feed, indent=2, sort_keys=True))
    tmp.replace(out)
    print("wrote", out, "fields:", ", ".join(sorted(feed)))


if __name__ == "__main__":
    main()

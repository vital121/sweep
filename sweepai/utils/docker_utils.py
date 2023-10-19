import urllib
from datetime import datetime, timezone

import requests
from loguru import logger


def get_latest_docker_version():
    def humanize_time(delta):
        seconds = delta.total_seconds()
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        if days > 0:
            return f"{int(days)} days ago"
        elif hours > 0:
            return f"{int(hours)} hours ago"
        elif minutes > 0:
            return f"{int(minutes)} minutes ago"
        else:
            return "just now"

    url = "https://hub.docker.com/v2/namespaces/sweepai/repositories/sweep/tags"
    response = requests.get(url)
    data = response.json()

    last_updated = datetime.fromisoformat(
        data["results"][0]["last_updated"].replace("Z", "+00:00")
    )
    duration_since_last_update = datetime.now(timezone.utc) - last_updated

    return humanize_time(duration_since_last_update)


def get_docker_badge():
    try:
        docker_update_duration = get_latest_docker_version()
        encoded_duration = urllib.parse.quote(docker_update_duration)
        badge_url = f"https://img.shields.io/badge/Docker%20Version%20Update-{encoded_duration}-blue"
        markdown_badge = f"\n![Docker Version Update]({badge_url})"
        return markdown_badge
    except:
        logger.exception("Failed to get docker badge.")
        return ""

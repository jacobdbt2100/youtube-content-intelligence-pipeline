from datetime import datetime, timezone

from src.youtube_client import get_youtube_client


VIDEO_IDS = [
    "B_BV8koJHjA",
    "lJGwU9VYXqw",
    "zI-KB81qOU0",
    "LB09ofxYO30",
    "sJsnkLb53so",
    "MVBpSJokkZo",
    "nuQtFrewR0o",
    "79J-aBp3YSE",
    "eJNoIJPzGLs",
    "7yOmi4IX-Rs"
]


def extract_videos():
    """
    Extract metadata for the selected videos.
    """

    youtube = get_youtube_client()

    response = youtube.videos().list(
        part="snippet,contentDetails",
        id=",".join(VIDEO_IDS)
    ).execute()

    collected_at = datetime.now(timezone.utc).isoformat()

    videos = []

    for video in response["items"]:
        snippet = video["snippet"]
        content_details = video["contentDetails"]

        videos.append({
            "video_id": video["id"],
            "channel_id": snippet["channelId"],
            "category_id": snippet["categoryId"],
            "title": snippet["title"],
            "published_at": snippet["publishedAt"],
            "duration": content_details["duration"],
            "video_url": f"https://www.youtube.com/watch?v={video['id']}",
            "collected_at": collected_at
        })

    return videos
    
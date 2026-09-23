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


def extract_video_daily_stats():
    """
    Extract the current statistics for the selected videos.
    """

    youtube = get_youtube_client()

    response = youtube.videos().list(
        part="statistics",
        id=",".join(VIDEO_IDS)
    ).execute()

    collection_date = datetime.now(timezone.utc).date().isoformat()

    video_stats = []

    for video in response["items"]:
        statistics = video.get("statistics", {})

        video_stats.append({
            "video_id": video["id"],
            "collection_date": collection_date,
            "view_count": statistics.get("viewCount", 0),
            "like_count": statistics.get("likeCount", 0),
            "comment_count": statistics.get("commentCount", 0)
        })

    return video_stats
    
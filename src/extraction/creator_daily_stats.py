from datetime import datetime, timezone

from src.youtube_client import get_youtube_client


CHANNEL_IDS = [
    "UCu7lQE-L5gzt8aD7zuuufjw",
    "UCNDlxHqR3ofCP7SVCZ0BdIg"
]


def extract_creator_daily_stats():
    """
    Extract the current statistics for the selected creators.
    """

    youtube = get_youtube_client()

    response = youtube.channels().list(
        part="statistics",
        id=",".join(CHANNEL_IDS)
    ).execute()

    collection_date = datetime.now(timezone.utc).date().isoformat()

    creator_stats = []

    for channel in response["items"]:
        statistics = channel["statistics"]

        creator_stats.append({
            "channel_id": channel["id"],
            "collection_date": collection_date,
            "subscriber_count": statistics.get("subscriberCount", 0),
            "total_view_count": statistics.get("viewCount", 0),
            "video_count": statistics.get("videoCount", 0)
        })

    return creator_stats
    
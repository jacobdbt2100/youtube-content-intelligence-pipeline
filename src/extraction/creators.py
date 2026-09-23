from src.youtube_client import get_youtube_client

CREATOR_HANDLES = ["@AnshLambaJSR", "@realjudebela"]


def extract_creators():
    """
    Extract channel IDs and channel names for the selected creators.
    """

    youtube = get_youtube_client()

    creators = []

    for handle in CREATOR_HANDLES:
        response = youtube.channels().list(
            part="snippet",
            forHandle=handle
        ).execute()

        if not response["items"]:
            raise ValueError(f"No channel found for handle: {handle}")

        channel = response["items"][0]

        creators.append({
            "channel_id": channel["id"],
            "channel_name": channel["snippet"]["title"]
        })

    return creators

from src.extraction.youtube_client import get_youtube_client


def extract_video_categories():
    """
    Extract raw video category data from YouTube.
    """

    youtube = get_youtube_client()

    category_response = youtube.videoCategories().list(
        part="snippet",
        regionCode="NG"
    ).execute()

    return category_response
    
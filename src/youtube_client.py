import os

from dotenv import load_dotenv
from googleapiclient.discovery import build


# Load environment variables
load_dotenv()


# Get the YouTube API key
API_KEY = os.getenv("YOUTUBE_API_KEY")


# Make sure the API key exists
if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY was not found in the environment.")


def get_youtube_client():
    """
    Create and return a YouTube Data API client.
    """
    youtube = build("youtube", "v3", developerKey=API_KEY)

    return youtube
    
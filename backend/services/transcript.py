from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):

    transcript = YouTubeTranscriptApi().fetch(
        video_id,
        languages=["en", "hi"]
    )

    text = " ".join(
        item.text for item in transcript
    )

    return text
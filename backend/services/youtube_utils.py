from urllib.parse import urlparse, parse_qs


def extract_video_id(video_url):

    if "youtu.be" in video_url:
        return video_url.split("/")[-1].split("?")[0]

    if "watch?v=" in video_url:
        parsed_url = urlparse(video_url)
        return parse_qs(parsed_url.query)["v"][0]

    raise ValueError("Unsupported YouTube URL")
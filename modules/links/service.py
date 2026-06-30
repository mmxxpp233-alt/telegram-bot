import requests


def shorten_url(url: str):
    try:
        response = requests.get(
            "https://tinyurl.com/api-create.php",
            params={"url": url},
            timeout=10,
        )

        if response.status_code != 200:
            return None

        return response.text

    except Exception:
        return None

import requests


def shorten_url(url: str):
    try:
        response = requests.get(
            "https://is.gd/create.php",
            params={
                "format": "simple",
                "url": url
            },
            timeout=10,
        )

        if response.status_code != 200:
            return None

        result = response.text.strip()

        if result.startswith("Error:"):
            return None

        return result

    except Exception:
        return None

from urllib.parse import urlparse

def is_phishing_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Check for suspicious indicators
    if not parsed_url.scheme or not parsed_url.netloc:
        return True  # Missing scheme or host (e.g., http:// or www)

    if "@" in parsed_url.netloc:
        return True  # Username and password in the URL

    if "." not in parsed_url.netloc:
        return True  # No valid domain name

    return False  # Not identified as a phishing URL

if __name__ == "__main__":
    url_to_check = "https://example.com"  # Replace with the URL you want to check
    if is_phishing_url(url_to_check):
        print("This URL is a potential phishing URL.")
    else:
        print("This URL appears to be legitimate.")

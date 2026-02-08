import requests
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warnings for testing environments
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SECURITY_HEADERS = [
    "X-Frame-Options",
    "X-XSS-Protection",
    "Content-Security-Policy",
]


def severity(results):
    """Determine overall severity level."""
    level = "Low"

    if results["https"] == "No":
        level = "High"

    if "Content-Security-Policy" in results["missing_headers"]:
        level = "High"

    elif results["missing_headers"]:
        level = "Medium"

    return level


def scan_target(url):
    """Scan a web target with SSL handling and better reliability."""
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        # verify=False allows scanning sites with SSL issues (testing only)
        response = requests.get(url, headers=headers, timeout=12, verify=False)

        soup = BeautifulSoup(response.text, "html.parser")

        missing = [h for h in SECURITY_HEADERS if h not in response.headers]

        results = {
            "url": url,
            "https": "Yes" if url.startswith("https") else "No",
            "missing_headers": missing,
            "forms": len(soup.find_all("form")),
        }

        results["severity"] = severity(results)
        return results

    except requests.exceptions.RequestException as e:
        return {
            "url": url,
            "https": "Connection Failed",
            "missing_headers": ["Unable to retrieve headers"],
            "forms": 0,
            "severity": "Error",
            "error": str(e),
        }
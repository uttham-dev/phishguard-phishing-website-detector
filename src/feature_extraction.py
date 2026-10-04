import re
import pandas as pd
from urllib.parse import urlparse


def extract_features(url):

    # Add http:// if the user doesn't provide a protocol
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed_url = urlparse(url)

    domain = parsed_url.netloc.lower()
    hostname = domain.split(":")[0]
    full_url = url.lower()

    # Check whether hostname is an IP address
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    has_ip = bool(re.match(ip_pattern, hostname))

    # Number of subdomains
    subdomain_count = len(hostname.split("."))

    features = {

        # 1
        "having_IPhaving_IP_Address":
            1 if has_ip else -1,

        # 2
        "URLURL_Length":
            -1 if len(url) < 54 else
            0 if len(url) <= 75 else 1,

        # 3
        "Shortining_Service":
            1 if any(service in domain for service in [
                "bit.ly",
                "tinyurl.com",
                "goo.gl",
                "t.co",
                "ow.ly",
                "is.gd",
                "buff.ly",
                "cutt.ly"
            ]) else -1,

        # 4
        "having_At_Symbol":
            1 if "@" in url else -1,

        # 5
        "double_slash_redirecting":
            1 if "//" in url[8:] else -1,

        # 6
        "Prefix_Suffix":
            1 if "-" in hostname else -1,

        # 7
        "having_Sub_Domain":
            -1 if subdomain_count <= 2 else
            0 if subdomain_count == 3 else 1,

        # 8
        "SSLfinal_State":
            1 if parsed_url.scheme == "https" else -1,

        # 9
        "Domain_registeration_length"
            : 0,

        # 10
        "Favicon":
            0,

        # 11
        "port":
            1 if parsed_url.port is not None else -1,

        # 12
        "HTTPS_token":
            1 if "https" in domain else -1,

        # 13
        "Request_URL":
            0,

        # 14
        "URL_of_Anchor":
            0,

        # 15
        "Links_in_tags":
            0,

        # 16
        "SFH":
            0,

        # 17
        "Submitting_to_email":
            1 if "mailto:" in full_url else -1,

        # 18
        "Abnormal_URL":
            1 if not domain else -1,

        # 19
        "Redirect":
            0,

        # 20
        "on_mouseover":
            0,

        # 21
        "RightClick":
            0,

        # 22
        "popUpWidnow":
            0,

        # 23
        "Iframe":
            0,

        # 24
        "age_of_domain":
            0,

        # 25
        "DNSRecord":
            1 if domain else -1,

        # 26
        "web_traffic":
            0,

        # 27
        "Page_Rank":
            0,

        # 28
        "Google_Index":
            0,

        # 29
        "Links_pointing_to_page":
            0,

        # 30
        "Statistical_report":
            -1
    }

    return pd.DataFrame([features])
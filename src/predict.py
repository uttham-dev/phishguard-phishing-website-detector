import pandas as pd
import joblib
from urllib.parse import urlparse
import socket
import re


# Load trained model
model = joblib.load("model/phishing_model.pkl")


def extract_features(url):

    parsed = urlparse(url)
    domain = parsed.netloc

    # Remove www.
    domain = domain.replace("www.", "")

    features = {}

    # 1. IP Address
    try:
        socket.inet_aton(domain.split(":")[0])
        features["having_IPhaving_IP_Address"] = 1
    except:
        features["having_IPhaving_IP_Address"] = -1

    # 2. URL Length
    if len(url) < 54:
        features["URLURL_Length"] = -1
    elif len(url) <= 75:
        features["URLURL_Length"] = 0
    else:
        features["URLURL_Length"] = 1

    # 3. Shortening Service
    shortening_services = [
        "bit.ly", "tinyurl.com", "goo.gl", "t.co",
        "ow.ly", "is.gd", "buff.ly"
    ]

    features["Shortining_Service"] = (
        1 if any(x in url.lower() for x in shortening_services) else -1
    )

    # 4. @ symbol
    features["having_At_Symbol"] = 1 if "@" in url else -1

    # 5. Double slash redirecting
    features["double_slash_redirecting"] = (
        1 if "//" in url[7:] else -1
    )

    # 6. Prefix/Suffix
    features["Prefix_Suffix"] = (
        -1 if "-" in domain else 1
    )

    # 7. Sub-domain
    dots = domain.count(".")

    if dots == 1:
        features["having_Sub_Domain"] = -1
    elif dots == 2:
        features["having_Sub_Domain"] = 0
    else:
        features["having_Sub_Domain"] = 1

    # 8. HTTPS
    features["SSLfinal_State"] = (
        1 if parsed.scheme.lower() == "https" else -1
    )

    # 9. Domain registration length
    # Default because WHOIS lookup is not being used yet
    features["Domain_registeration_length"] = 0

    # 10. Favicon
    features["Favicon"] = 0

    # 11. Port
    features["port"] = -1

    # 12. HTTPS token
    features["HTTPS_token"] = (
        -1 if "https" in domain.lower() else 1
    )

    # 13. Request URL
    features["Request_URL"] = 0

    # 14. URL of Anchor
    features["URL_of_Anchor"] = 0

    # 15. Links in tags
    features["Links_in_tags"] = 0

    # 16. SFH
    features["SFH"] = 0

    # 17. Submitting to email
    features["Submitting_to_email"] = (
        1 if "mailto:" in url.lower() else -1
    )

    # 18. Abnormal URL
    features["Abnormal_URL"] = -1

    # 19. Redirect
    features["Redirect"] = -1

    # 20. On mouseover
    features["on_mouseover"] = -1

    # 21. Right click
    features["RightClick"] = -1

    # 22. Popup window
    features["popUpWidnow"] = -1

    # 23. Iframe
    features["Iframe"] = -1

    # 24. Age of domain
    features["age_of_domain"] = 0

    # 25. DNS record
    features["DNSRecord"] = 1

    # 26. Web traffic
    features["web_traffic"] = 0

    # 27. Page rank
    features["Page_Rank"] = 0

    # 28. Google index
    features["Google_Index"] = 1

    # 29. Links pointing to page
    features["Links_pointing_to_page"] = 0

    # 30. Statistical report
    features["Statistical_report"] = -1

    return pd.DataFrame([features])


# -----------------------------
# MAIN PROGRAM
# -----------------------------

url = input("Enter a website URL: ")

features = extract_features(url)

print("\nExtracted features:")
print(features.to_string(index=False))

print("\nChecking website...")

prediction = model.predict(features)

print("\nPrediction:", prediction[0])

if prediction[0] == 1:
    print("Result: LEGITIMATE WEBSITE")
else:
    print("Result: PHISHING WEBSITE")
from flask import Flask, render_template, request
import joblib
import sys
import os
from urllib.parse import urlparse


# =========================================================
# 1. FLASK APPLICATION
# =========================================================

app = Flask(__name__)


# =========================================================
# 2. DASHBOARD STATISTICS
# =========================================================

total_scans = 0
phishing_count = 0
legitimate_count = 0


# =========================================================
# 3. DETECTION HISTORY
# =========================================================

detection_history = []


# =========================================================
# 4. LOAD FEATURE EXTRACTION
# =========================================================

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "src"
    )
)

from feature_extraction import extract_features


# =========================================================
# 5. LOAD MACHINE LEARNING MODEL
# =========================================================

model = joblib.load(
    "model/phishing_model.pkl"
)


# =========================================================
# 6. SUSPICIOUS URL CHECK
# =========================================================

def check_suspicious_url(url):

    score = 0
    reasons = []

    # Add HTTP if protocol is missing
    if not url.startswith(("http://", "https://")):

        check_url = "http://" + url

    else:

        check_url = url


    parsed = urlparse(check_url)

    hostname = parsed.hostname or ""

    url_lower = check_url.lower()


    # -----------------------------------------------------
    # Check 1: HTTPS
    # -----------------------------------------------------

    if parsed.scheme != "https":

        score += 1

        reasons.append(
            "Website does not use HTTPS"
        )


    # -----------------------------------------------------
    # Check 2: Suspicious words
    # -----------------------------------------------------

    suspicious_words = [

        "login",
        "verify",
        "verification",
        "secure",
        "account",
        "password",
        "payment",
        "confirm",
        "signin"

    ]


    found_words = []


    for word in suspicious_words:

        if word in url_lower:

            found_words.append(word)


    if found_words:

        score += 2

        reasons.append(
            "Suspicious words found in the URL"
        )


    # -----------------------------------------------------
    # Check 3: @ symbol
    # -----------------------------------------------------

    if "@" in check_url:

        score += 3

        reasons.append(
            "URL contains @ symbol"
        )


    # -----------------------------------------------------
    # Check 4: IP address
    # -----------------------------------------------------

    parts = hostname.split(".")


    if (
        len(parts) == 4
        and all(part.isdigit() for part in parts)
    ):

        score += 3

        reasons.append(
            "URL uses an IP address"
        )


    # -----------------------------------------------------
    # Check 5: Multiple hyphens
    # -----------------------------------------------------

    if hostname.count("-") >= 2:

        score += 2

        reasons.append(
            "Domain contains multiple hyphens"
        )


    # -----------------------------------------------------
    # Check 6: Very long URL
    # -----------------------------------------------------

    if len(check_url) > 100:

        score += 2

        reasons.append(
            "URL is unusually long"
        )


    return score, reasons


# =========================================================
# 7. HOME PAGE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    global total_scans
    global phishing_count
    global legitimate_count


    # -----------------------------------------------------
    # Default values
    # -----------------------------------------------------

    result = None

    url = ""

    confidence = None

    warning = None

    reasons = []

    risk_score = 0


    # =====================================================
    # 8. WHEN USER SUBMITS A URL
    # =====================================================

    if request.method == "POST":


        # -------------------------------------------------
        # Get URL from HTML form
        # -------------------------------------------------

        url = request.form.get(
            "url",
            ""
        ).strip()


        # -------------------------------------------------
        # Make sure URL is not empty
        # -------------------------------------------------

        if url:


            # =============================================
            # MACHINE LEARNING FEATURE EXTRACTION
            # =============================================

            features = extract_features(
                url
            )


            # =============================================
            # MACHINE LEARNING PREDICTION
            # =============================================

            prediction = model.predict(
                features
            )


            probabilities = model.predict_proba(
                features
            )


            predicted_class = prediction[0]


            # =============================================
            # CONFIDENCE
            # =============================================

            class_index = list(
                model.classes_
            ).index(
                predicted_class
            )


            confidence = round(

                probabilities[0][class_index] * 100,

                2

            )


            # =============================================
            # SUSPICIOUS URL ANALYSIS
            # =============================================

            risk_score, reasons = check_suspicious_url(
                url
            )


            # =============================================
            # FINAL RESULT
            # =============================================

            if (
                predicted_class == -1
                or risk_score >= 3
            ):


                result = "PHISHING WEBSITE"


                warning = (
                    "⚠️ WARNING: "
                    "This website may be unsafe. "
                    "Do not use this website."
                )


            else:


                result = "LEGITIMATE WEBSITE"


                warning = (
                    "✅ This website appears "
                    "to be legitimate."
                )


            # =============================================
            # UPDATE DASHBOARD STATISTICS
            # =============================================

            total_scans += 1


            if result == "PHISHING WEBSITE":

                phishing_count += 1

            else:

                legitimate_count += 1


            # =============================================
            # ADD RESULT TO DETECTION HISTORY
            # =============================================

            detection_history.insert(

                0,

                {
                    "url": url,

                    "result": result,

                    "confidence": confidence,

                    "risk_score": risk_score
                }

            )


            # =============================================
            # KEEP ONLY LAST 10 SCANS
            # =============================================

            if len(detection_history) > 10:

                detection_history.pop()


            # =============================================
            # PRINT RESULT IN TERMINAL
            # =============================================

            print("\n")

            print("=" * 60)

            print(
                "       PHISHING WEBSITE DETECTOR"
            )

            print("=" * 60)

            print(
                "URL:",
                url
            )

            print(
                "ML Prediction:",
                predicted_class
            )

            print(
                "ML Confidence:",
                str(confidence) + "%"
            )

            print(
                "Risk Score:",
                risk_score
            )

            print(
                "Final Result:",
                result
            )


            if reasons:

                print(
                    "\nSecurity Indicators:"
                )


                for reason in reasons:

                    print(
                        "-",
                        reason
                    )


            print(
                "\nDashboard Statistics:"
            )

            print(
                "Total Scans:",
                total_scans
            )

            print(
                "Phishing Detected:",
                phishing_count
            )

            print(
                "Legitimate:",
                legitimate_count
            )


            print(
                "\nDetection History:"
            )


            for item in detection_history:

                print(
                    "-",
                    item["url"],
                    "|",
                    item["result"],
                    "|",
                    str(item["confidence"]) + "%"
                )


            print("=" * 60)


    # =====================================================
    # 9. SEND DATA TO HTML
    # =====================================================

    return render_template(

        "index.html",

        result=result,

        url=url,

        confidence=confidence,

        warning=warning,

        reasons=reasons,

        risk_score=risk_score,

        total_scans=total_scans,

        phishing_count=phishing_count,

        legitimate_count=legitimate_count,

        history=detection_history

    )


# =========================================================
# 10. START FLASK SERVER
# =========================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
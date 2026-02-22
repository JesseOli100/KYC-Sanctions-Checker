from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import io
import difflib

app = Flask(__name__)
app.secret_key = "change-this-in-production"

# Demo "sanctions list"
SANCTIONED_ENTITIES = [
    "EVIL CORP INTERNATIONAL LTD",
    "BAD ACTOR TRADING LLC",
    "SANCTIONED GLOBAL HOLDINGS",
    "ACME FRONT COMPANY SA",
    "BLACKLISTED CAPITAL PARTNERS",
]


def check_name_against_sanctions(name, threshold=0.8):
    """
    Simple fuzzy match against demo sanctions list.
    Returns best match, similarity score (0-1), and a risk category.
    """
    if not name:
        return None, 0.0, "LOW"

    name_upper = name.upper().strip()
    scores = []

    for entity in SANCTIONED_ENTITIES:
        ratio = difflib.SequenceMatcher(None, name_upper, entity).ratio()
        scores.append((entity, ratio))

    if not scores:
        return None, 0.0, "LOW"

    best_entity, best_score = max(scores, key=lambda x: x[1])

    if best_score >= 0.9:
        risk = "HIGH"
    elif best_score >= threshold:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return best_entity, best_score, risk


@app.route("/", methods=["GET", "POST"])
def index():
    single_result = None
    batch_results = None

    if request.method == "POST":
        mode = request.form.get("mode", "single")

        if mode == "single":
            name = request.form.get("name")
            if not name:
                flash("Please enter a counterparty name.", "danger")
                return redirect(url_for("index"))

            match, score, risk = check_name_against_sanctions(name)
            single_result = {
                "input": name,
                "match": match,
                "score": round(score * 100, 1),
                "risk": risk,
            }

        else:  # batch mode
            file = request.files.get("file")
            if not file or file.filename == "":
                flash("Please upload a CSV file for batch mode.", "danger")
                return redirect(url_for("index"))

            try:
                content = file.read().decode("utf-8")
                reader = csv.DictReader(io.StringIO(content))
                if "counterparty" not in reader.fieldnames:
                    raise ValueError("CSV must have a 'counterparty' column.")

                batch_results = []
                for row in reader:
                    cp_name = row.get("counterparty")
                    match, score, risk = check_name_against_sanctions(cp_name)
                    batch_results.append(
                        {
                            "input": cp_name,
                            "match": match,
                            "score": round(score * 100, 1),
                            "risk": risk,
                        }
                    )

            except Exception as e:
                flash(f"Error processing CSV: {e}", "danger")
                return redirect(url_for("index"))

    return render_template(
        "index.html",
        single_result=single_result,
        batch_results=batch_results,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)

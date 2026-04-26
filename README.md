# KYC-Sanctions-Checker

# Contact Info

Want to hire me? Check out my LinkedIn here: https://www.linkedin.com/in/jesse-o-03476a102/

# KYC / Sanctions Screening Engine (Demo)

A lightweight Flask-based sanctions screening tool that demonstrates how financial institutions can automate basic counterparty risk checks using fuzzy name matching and risk scoring logic.

#  Overview

This project simulates a simplified sanctions screening workflow used in compliance and operational risk environments.

It supports:

* Single-name counterparty screening

* Batch screening via CSV upload

* Similarity scoring against internal sanctions lists

* Risk tier classification (LOW / MEDIUM / HIGH)

* Structured output suitable for audit-style review

* Tech Stack

Python

Flask

HTML / Bootstrap frontend

# How It Works
# Name Normalization

Input counterparty names are:

Standardized

Uppercased

Stripped of punctuation

This reduces false mismatches caused by formatting differences.

# Similarity Scoring

Each counterparty is compared against an internal sanctions list using a fuzzy matching algorithm (e.g., Levenshtein distance or ratio-based similarity scoring).

Output:

Best match

Match percentage score

# Risk Classification

Risk tiers are determined by score thresholds:

Score	Risk Level
90–100%	HIGH
75–89%	MEDIUM
Below 75%	LOW

(Thresholds configurable)

# Batch Mode

Upload a CSV file containing a counterparty column.

Example:

counterparty
Evil Corp International Ltd
Acme Frontier Company
Goodwill Finance Group

The app:

Iterates through each name

Computes similarity

Returns structured batch output

# Why This Project Matters

Sanctions screening in financial institutions often faces:

High false positive rates

Manual review bottlenecks

Name variation complexity

Inconsistent risk threshold application

This project demonstrates how even simple automation and structured logic can:

Standardize decisioning

Reduce manual processing

Improve review prioritization

# Running Locally
git clone <repo>
cd kyc-screening-demo

pip install -r requirements.txt
python app.py

Then visit:

http://127.0.0.1:8000/

(Port configurable in app.py)

# Future Enhancements

Phonetic matching (Soundex / Metaphone)

Multiple watchlists

Weighting for entity suffixes (LLC, Ltd, SA)

ML-assisted risk scoring

Historical screening log database

Reviewer decision feedback loop

# Disclaimer

This is a demo application intended for educational and portfolio purposes only.
It is not production-grade sanctions screening software.

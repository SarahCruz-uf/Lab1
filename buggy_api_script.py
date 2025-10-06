"""
Lab 1 — Part 2 Starter (BUGGY ON PURPOSE)
API: Cat Facts — https://catfact.ninja/
Goal: Fetch ONE cat fact and save it to data/cat_fact.txt
"""

# TODO: Import what you actually need (this line is intentionally incomplete)
import json
import requests #needs this library to make API requests

API_URL = "https://catfact.ninja/fact"  # removed the 's'

def get_cat_fact():
    """Fetch a single cat fact string from the API and return it."""
    # NOTE: There may be a few bugs below. Read errors carefully!
    resp = requests.get(API_URL, timeout=5)  # BUG: timeout type is a number, not a string
    data = resp.json()

    # Expecting the payload to contain the fact text at data["fact"]
    # (Verify with docs! If the endpoint returns a list, this will fail.)
    fact = data["fact"]

    return fact

def save_fact_to_file(text):
    """Save the provided text to data/cat_fact.txt"""
    out_path = "cat_fact.txt"
    # If the folder doesn't exist, this will fail.
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Saved to cat_fact.txt")  # BUG: filename typo- missing a 't'
    except FileNotFoundError:
        print("Error: The directory 'data' does not exist. Please create it first.")    

def main():
    fact = get_cat_fact()
    # Add a simple guard so we don't write None/empty strings
    if fact:
        if fact and isinstance(fact, str):
            save_fact_to_file(fact)
        else:
            print("No fact fetched. Check API response structure.")
    else:
        print("Error there's no cat fact.")

if __name__ == "__main__":
    main()
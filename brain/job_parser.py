import re

def parse_job(text):

    pattern = r"applied to (.*?) for (.*)"

    match = re.search(
        pattern,
        text.lower()
    )

    if not match:
        return None

    return {
        "company": match.group(1).strip(),
        "role": match.group(2).strip()
    }
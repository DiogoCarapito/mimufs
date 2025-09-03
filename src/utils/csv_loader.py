import csv


def load_script_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    # Assume first row is the script name, rest are components
    script_name = rows[0][0] if rows else ""
    components = [row[0] for row in rows[1:]] if len(rows) > 1 else []
    return script_name, components

import os
import requests


def download_feather_icon(name, dest):
    url = f"https://raw.githubusercontent.com/feathericons/feather/master/icons/{name}.svg"
    r = requests.get(url, timeout=10)  # 10 seconds timeout
    if r.status_code == 200:
        with open(dest, "wb") as f:
            f.write(r.content)


def ensure_feather_icon(name, assets_dir="assets/icons"):
    os.makedirs(assets_dir, exist_ok=True)
    icon_path = os.path.join(assets_dir, f"{name}.svg")
    if not os.path.exists(icon_path):
        download_feather_icon(name, icon_path)
    return icon_path


def download_tabler_icon(name, dest, style="outlined"):
    if style == "filled":
        url = f"https://raw.githubusercontent.com/tabler/tabler-icons/main/icons/filled/{name}.svg"
    else:
        url = f"https://raw.githubusercontent.com/tabler/tabler-icons/main/icons/outline/{name}.svg"
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        with open(dest, "wb") as f:
            f.write(r.content)


def ensure_tabler_icon(name, assets_dir="assets/icons", style="outlined"):
    os.makedirs(assets_dir, exist_ok=True)
    icon_path = os.path.join(assets_dir, f"{name}.svg")
    if not os.path.exists(icon_path):
        download_tabler_icon(name, icon_path, style)
    return icon_path


# Example usage:
# icon_path = ensure_tabler_icon("arrow-left")

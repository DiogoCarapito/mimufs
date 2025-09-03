import pandas as pd
import pyautogui
import time
import os


def execut_scripts_csv(csv_path):
    print("csv_path:", csv_path)
    for each in csv_path:
        if not each.startswith("src/autogui/scripts/"):
            file_path = f"src/autogui/scripts/{each}"
        else:
            file_path = each

        df = pd.read_csv(file_path, encoding="utf-8")
        for _, row in df.iterrows():
            action = row.get("action")
            element = row.get("element")
            option = row.get("option")
            delay = row.get("delay")
            print(
                f"Action: {action}, Element: {element}, Option: {option}, Delay: {delay}"
            )

            # Build full image path for element
            if pd.notna(element) and str(element).strip():
                image_path = os.path.join("src/autogui/assets", f"{element}.png")
            else:
                image_path = None

            if action == "click" and image_path:
                location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
                if location:
                    pyautogui.click(location)
                    print(f"Clicked on {element} at {location}")
                else:
                    print(f"Image not found: {image_path}")
            elif action == "check" and image_path:
                location = pyautogui.locateOnScreen(image_path, confidence=0.8)
                if location:
                    print(f"Found {element} at {location}")
                else:
                    print(f"Image not found: {image_path}")
            elif action == "write":
                print(f"Writing '{option}'")
                pyautogui.write(str(option))

            # Handle delay if present
            if pd.notna(delay) and str(delay).strip():
                time.sleep(float(delay))

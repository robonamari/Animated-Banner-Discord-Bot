"""
Update the Discord bot's Banner using an image file.

This script loads the Banner path and bot token from environment variables,
reads the Banner file, encodes it to base64, and sends a PATCH request
to update the bot's Banner.

Environment Variables:
- BANNER_PATH (str): The path to the Banner image file.
- TOKEN (str): The Discord bot token.

Raises:
- Exception: If reading the file, encoding, or the HTTP request fails.
"""

import base64
import os

import requests
from dotenv import load_dotenv

load_dotenv()


try:
    with open(os.getenv("BANNER_PATH"), "rb") as file:
        banner_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.patch(
        "https://discord.com/api/v10/users/@me",
        headers={
            "Authorization": f"Bot {os.getenv('TOKEN')}",
            "Content-Type": "application/json",
        },
        json={"banner": f"data:image/gif;base64,{banner_data}"},
    )
    if response.ok:
        print("Banner Updated!")
    else:
        print(f"Failed to Update Banner: {response.status_code}")
        print(f"Response body: {response.text}")

except Exception as e:
    print(f"There is an Error here: {e}")

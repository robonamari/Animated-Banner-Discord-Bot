import requests
import base64

token = ""
banner_path = "./Animated-Banner.gif"

try:
    with open(banner_path, "rb") as file:
        new_banner = base64.b64encode(file.read()).decode("utf-8")

    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    json = {
        "banner": f"data:image/gif;base64,{new_banner}"
    }

    response = requests.patch("https://discord.com/api/v10/users/@me", headers=headers, json=json)

    if response.ok:
        print("Banner Updated!")
    else:
        print("Failed to Update Banner:", response.status_code)
        print("Response body:", response.text)

except Exception as error:
    print("There is an Error here:", error)
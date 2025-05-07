import requests

# ============================
# TikTok Signature Generator API
# ============================
#
# This script sends a POST request to a specified API URL to generate TikTok signatures.
# It requires a TikTok API request URL, a payload, and an 'aid' value to generate the necessary headers.
#
# Requirements:
# - Python 3.x
# - 'requests' library (install it with `pip install requests`)
#
# How to use:
# 1. Update the `url` field in the payload with the TikTok URL you want to generate signatures for.
# 2. Modify the `payload` as necessary (e.g., for `passport_ticket`, `email`, etc.).
# 3. Set the `aid` to the app ID that you wish to use (default is 1233).
# 4. Run the script with: `python3 script_name.py`
# 5. The generated signatures will be printed to the console upon success.
#
# Example response:
# ```
# Signatures generated:
# X-Ladon: abcdef1234567890
# X-Khronos: 9876543210
# X-Argus: argus_value_here
# X-Gorgon: gorgon_value_here
# X-Ss-Req-Ticket: ss_req_ticket_here
# credits: @Kuruptd / https://t.me/tiktok_autoclaim
# ```
#
# For errors, the script will print an error message with the HTTP status code.
# ============================

api_url = 'http://107.172.77.145:5000/generate-signatures'

# Update the following payload
payload = {
    'url': '',
    'payload': '', # NOT REQ
    'aid': 1233
}

try:
    # Sending the POST request to the API
    response = requests.post(api_url, json=payload)
    
    # Check if the response status code is OK (200)
    if response.status_code == 200:
        data = response.json()
        
        # Print the generated signatures
        print('Signatures generated:')
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        # Print error message if status code is not 200
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    # Print any exceptions that occurred during the request
    print(f"Request failed: {e}")

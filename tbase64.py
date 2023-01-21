import base64

# List of URLs
urls = []

# Print table header
print("{:<50} {:<50}".format("URL", "Base64"))

for url in urls:
    # Encode the URL to base64
    base64_url = base64.b64encode(url.encode())
    # Decode the base64 encoded URL
    decoded_url = base64_url.decode()
    # Print the URL and the base64 encoded URL
    print("{:<50} {:<50}".format(url, decoded_url))

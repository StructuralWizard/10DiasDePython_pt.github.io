import requests

# GitHub API endpoint to get user repositories
url = "https://api.github.com/users/octocat/repos"

# Custom headers
headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Accept": "application/vnd.github.v3+json"
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    # Print first 3 repositories with name and URL
    for repo in data[:3]:
        print(f"Name: {repo['name']} - URL: {repo['html_url']}")
else:
    print("Request failed with status code:", response.status_code)

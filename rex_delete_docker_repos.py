import requests

# Replace placeholders with your Docker Hub username and Personal Access Token
USERNAME = "{USERNAME}"  # Your Docker Hub username
TOKEN = "{TOKEN}"  # Your Docker Hub API token

if "{USERNAME}" in USERNAME or "{TOKEN}" in TOKEN:
    raise ValueError("Please replace {USERNAME} and {TOKEN} with your actual Docker Hub credentials.")

# List of repository IDs or names to delete from Docker Hub
# {USERNAME}/{REPOSITORY-NAME}
repositories_to_delete = [
    "{REPOSITORY-NAME-01}",
    "{REPOSITORY-NAME-02}",
    "{REPOSITORY-NAME-03}",
]

# Base URL for Docker Hub API
BASE_URL = "https://hub.docker.com/v2/repositories/"

# Function to delete a repository
def delete_repository(username, repository, token):
    url = f"{BASE_URL}{username}/{repository}/"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"[SUCCESS] Deleted: {repository}")
        elif response.status_code == 202:
            print(f"[IN PROGRESS] Deletion initiated for: {repository}")
        else:
            print(f"[FAILED] {repository} - Status code: {response.status_code}, Message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not delete {repository}: {e}")


# Loop through repositories and attempt deletion
for repo in repositories_to_delete:
    delete_repository(USERNAME, repo, TOKEN)


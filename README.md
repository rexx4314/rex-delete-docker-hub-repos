---

## **Delete Docker Hub Repositories**

This Python script uses the Docker Hub API to delete repositories associated with your Docker Hub account. The script is designed to handle repository deletions efficiently and provides clear feedback on the status of each operation.

---

### **Requirements**
- Python 3.13.1 or higher
- `requests` library for API interactions
- Docker Hub Personal Access Token (PAT)

---

### **Installation**

#### **1. Check Python Version**
Ensure Python 3.13.1 is installed on your system:
```bash
python --version
```
Output:
```
Python 3.13.1
```

#### **2. Install Required Libraries**
Install the `requests` library:
```bash
pip install requests
```

Verify the installation:
```bash
python -m pip show requests
```
Expected output:
```
Name: requests
Version: <installed version>
...
```

---

### **Generate Docker Hub Personal Access Token (PAT)**

#### **1. Log in to Docker Hub**
Go to [Docker Hub](https://hub.docker.com/) and log in with your credentials.

#### **2. Navigate to Security Settings**
1. Click on your profile picture in the top-right corner.
2. Select **Account Settings** from the dropdown menu.
3. In the **Security** section, locate **Personal Access Tokens** and click on it.

#### **3. Create a New Access Token**
1. Click on the **Generate new token** button.
2. Sets a description, expiration date, and access permissions for the token.
3. Click **Generate**.

#### **4. Copy the Token**
- **IMPORTANT**: Copy the generated token immediately, as it will not be displayed again.
- Store the token securely.

---

### **Usage**

#### **1. Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/rexx4314/delete-docker-hub-repos.git
cd delete-docker-hub-repos
```

#### **2. Update Credentials**
Edit the script to replace placeholders with your Docker Hub username and Personal Access Token (PAT):
```python
USERNAME = "{USERNAME}"  # Replace with your Docker Hub username
TOKEN = "{TOKEN}"  # Replace with your Docker Hub API token
```

#### **3. Define Repositories to Delete**
Update the `repositories_to_delete` list with the repository names or IDs you want to delete:
```python
repositories_to_delete = [
    "repository-id-or-name-1",
    "repository-id-or-name-2",
    "repository-id-or-name-3",
]
```

#### **4. Run the Script**
Execute the script:
```bash
python rex_delete_docker_repos.py
```

---

### **Features**
- **Status Handling**:
  - `204`: Repository successfully deleted.
  - `202`: Deletion in progress.
  - Other status codes are logged with error messages.
- **Error Handling**:
  - Handles network issues or invalid credentials gracefully.

---

### **Code Overview**

#### **Input Parameters**
- **`USERNAME`**: Your Docker Hub username.
- **`TOKEN`**: Personal Access Token from Docker Hub.
- **`repositories_to_delete`**: List of repository names or IDs to delete.

#### **Functionality**
- Constructs API requests to delete repositories.
- Handles API responses for success, in-progress, and failure statuses.

#### **Example Output**
1. **Successful Deletion**:
   ```
   [SUCCESS] Deleted: repository-id-or-name-1
   ```
2. **In Progress**:
   ```
   [IN PROGRESS] Deletion initiated for: repository-id-or-name-2
   ```
3. **Failure**:
   ```
   [FAILED] repository-id-or-name-3 - Status code: 401, Message: Unauthorized
   ```

---

### **Error Messages**
- **Invalid Credentials**:
  ```
  ValueError: Please replace {USERNAME} and {TOKEN} with your actual Docker Hub credentials.
  ```
- **Empty Repository List**:
  Add repositories to the `repositories_to_delete` list:
  ```python
  repositories_to_delete = [
      "example-repo-1",
      "example-repo-2",
  ]
  ```

---

### **Notes**
- **Python Version**: Ensure Python 3.13.1 is installed.
- **Security**: Avoid hardcoding sensitive credentials in the script. Use environment variables for better security.
- **Docker Hub API Documentation**: [API Reference](https://docs.docker.com/docker-hub/api/latest/)

---

### **License**
This project is licensed under the MIT License.

---

### **Contributing**
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas. 

---

This README.md now includes the steps to generate a Docker Hub Personal Access Token, ensuring the user has all necessary information to use the script effectively.

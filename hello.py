import requests
url = "https://raw.githubusercontent.com/shangeetha283/OpenUniGit003/main/hello.py"
response = request.get(url)

if response.status_code ==200:
  print("File Content :")
  print(response.text)
else:
  print(f"Failed to fetch file. HTTP Status Code:{response.status_code}")

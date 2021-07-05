import requests

req_md = requests.get('https://gist.githubusercontent.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b/raw'
                      '/acdffbbe926eb8c117f27e66c95c2e8400170aa6/espn-api-docs.md')

with open('api-instructions.md', 'w') as o_file:
    o_file.write(req_md.text)
    o_file.close()
import requests
import json

#token
token = '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'
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}
followers_url = 'https://api.github.com/user/following'
response = requests.get(followers_url, headers=headers)
followers = response.json()
# 获取每个关注者的仓库信息
followers_repos = {}
print(type(followers))
print(followers)

for follower in followers:
    repos_url = follower['repos_url']
    response = requests.get(repos_url, headers=headers)
    followers_repos[follower['login']] = response.json()

# 将数据存储到本地
with open('followers_repos.json', 'w') as file:
    json.dump(followers_repos, file)


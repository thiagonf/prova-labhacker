BASE_URL_API = 'https://api.github.com/'

URL_REPOSITORIES_USER = BASE_URL_API + \
    'user/repos?access_token={}&affiliation={}&per_page={}'
URL_INFO_USER = BASE_URL_API + 'users/{}'
URL_REPOSITORY_TOPIC = BASE_URL_API + 'repos/{}/{}/topics?access_token={}'

HEADERS_REPOSITORY_TOPIC = {
    'Accept': 'application/vnd.github.mercy-preview+json'}

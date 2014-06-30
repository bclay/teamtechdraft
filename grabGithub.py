from pygithub3 import Github

def githubForUser(username):
    gh = Github(login='birdiecheese', password='ertdfg3')
    reposList = gh.repos.list(username).all()

from pygithub3 import Github

def githubForUser(username):
    gh = Github(login='birdiecheese', password='ertdfg3')
    reposList = gh.repos.list(username).all()
    urls = [r.url for r in reposList]
    return urls

if __name__ == '__main__':
    userurls = githubForUser('savala')
    for i in userurls:
        print i

# import click
import os
import requests
import json

data= {
    "name": "name2",
    # "private": False
}
headers= {
    "Authorization": "token b8f971fbaff4e53baf588aa773fd177aecba4f73"
}
response = requests.post('https://api.github.com/user/repos',headers=headers,data=json.dumps(data))
print(response.json())





# ref: https://developer.github.com/v3/repos/#create-a-repository-for-the-authenticated-user
# os.system('virtualenv venv')
# os.system('venv/bin/easy_install')

# @click.command()
# @click.option('-p', '--project', required=True, help='sdkjfds')
# @click.option('--path', help='sdkjfds')
# def create_project(project, path):
#     html = None
#     with open('index.html', 'r') as f:
#         html = f.read()
#     if path:
#         os.chdir(path)
#     os.mkdir(project)
#     os.chdir(project)
#     os.mkdir('css')
#     os.mkdir('js')
#     open('css/style.css', 'w').close()
#     open('js/script.js', 'w').close()
#     with open('index.html', 'w') as f:
#         f.write(html)
#
#     if click.confirm('git reponuz varmi? '):
#         git_repo = click.prompt('repo unvani qeyd edin: ')
#         os.system('git init')
#         os.system(f'git remote add origin {git_repo}')
#         os.system('git add .')
#         os.system('git commit -m "project created"')
#         os.system('git push origin master')
#
#
#
# if __name__ == '__main__':
#     create_project()
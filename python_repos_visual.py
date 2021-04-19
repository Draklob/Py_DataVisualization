import requests
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
repo_names, repo_links, starts, labels = [], [], [], []

def loading_data():
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # Process results. Store API response in a variable.
    response_dict = r.json()
    repo_dicts = response_dict['items']
    for repo_dict in repo_dicts:
        repo_names.append(repo_dict['name'])
        repo_link = f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}</a>"
        print(repo_link)
        repo_links.append(repo_link)
        starts.append(repo_dict['stargazers_count'])
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

def drawing_data():
    # Make visualization.
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': starts,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width':1.5, 'color': 'rgb(25, 25 ,25)'},
        },
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub.',
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data':data, 'layout': my_layout}
    offline.plot( fig, filename='python_repos.html')

def run_script():
    loading_data()
    drawing_data()

# Uncomment the code below to run the script
#run_script()
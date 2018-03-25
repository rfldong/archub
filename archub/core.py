from github import Github
from github.GithubObject import NotSet
from archub import config

def todo(org, repo, title, body, assignee):
    g = Github(config.GITHUB_TOKEN)
    login = g.get_user().login
    if assignee is None:
        assignee = login
    if org is None:
        org = login
    org_repo = '{}/{}'.format(org, repo)
    if title is None:
        title = body
        body = NotSet
    r = g.get_repo(org_repo)
    r.create_issue(
        title,
        body=body,
        assignee=assignee
    )

def render_fixed_width_text(text, maxlen=80):
    if len(text) > maxlen:
        return '{}...'.format(text[:maxlen - 3])
    return text + ' ' * (maxlen - len(text))

def render_issue_line(issue, linewidth=80):
    return '{} {} {}'.format(
        render_fixed_width_text('#% 4d' % issue.number, 5),
        render_fixed_width_text(issue.title, linewidth - (24 + 5 + 2)),
        render_fixed_width_text(issue.repository.name, 24)
    )

def render_issue_labels(issue, linewidth=80):
    return render_fixed_width_text(' '.join(['[{}]'.format(label.name) for label in issue.get_labels()]), linewidth)

def print_issue_line(issue, linewidth=80):
    print(render_issue_line(issue, linewidth))

def print_issue_labels(issue, linewidth=80):
    pad = '      '
    print(pad + render_issue_labels(issue, linewidth - len(pad)))

def get_issues():
    return Github(config.GITHUB_TOKEN).get_user().get_issues()

def print_issues():
    for issue in get_issues():
        print_issue_line(issue)

def print_issues_with_labels():
    for issue in get_issues():
        print_issue_line(issue)
        if len(issue.labels) > 0:
            print_issue_labels(issue)

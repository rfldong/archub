import os
import sys
from argparse import ArgumentParser
from archub import cmdline, config
from github import Github
from github.GithubObject import NotSet

def get_repo(github, org, repo_name):
    if len(org) > 0:
        return github.get_organization(org).get_repo(repo_name)
    return github.get_user().get_repo(repo_name)

def main(args):
    parser = ArgumentParser(
        prog=cmdline.prog(__file__),
        description='Quickly create an issue ticket for the specified repository'
    )
    parser.add_argument('-o', '--org', required=False, type=str,
        default=config.GITHUB_ORGANIZATION,
        help='empty string for no organization [default: "{}"]'.format(config.GITHUB_ORGANIZATION))
    parser.add_argument('-r', '--repo', required=True, type=str)
    parser.add_argument('-t', '--title', required=False, type=str, default=NotSet)
    parser.add_argument('-a', '--assign', required=False, type=str, default=NotSet)
    parser.add_argument('description')
    parsed_args = parser.parse_args(args)
    issue_title = parsed_args.description if parsed_args.title is NotSet else parsed_args.title
    issue_description = parsed_args.description if parsed_args.title is not NotSet else NotSet
    repo = get_repo(Github(config.GITHUB_TOKEN), parsed_args.org, parsed_args.repo)
    repo.create_issue(
        issue_title,
        body=issue_description,
        assignee=parsed_args.assign)
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv))

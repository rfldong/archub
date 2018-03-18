import os
import sys
from argparse import ArgumentParser
from archub import cmdline
from archub.types import GithubRepository
from github.GithubObject import NotSet

def main(args):
    parser = ArgumentParser(
        prog=cmdline.prog(__file__),
        description='Quickly create an issue ticket for the specified repository'
    )
    parser.add_argument('-o', '--org', required=False, type=str)
    parser.add_argument('-r', '--repo', required=True, type=GithubRepository)
    parser.add_argument('-t', '--title', required=False, type=str, default=NotSet)
    parser.add_argument('-a', '--assign', required=False, type=str, default=NotSet)
    parser.add_argument('description')
    parsed_args = parser.parse_args(args)
    issue_title = parsed_args.description if parsed_args.title is NotSet else parsed_args.title
    issue_description = parsed_args.description if parsed_args.title is not NotSet else NotSet
    parsed_args.repo.create_issue(
        issue_title,
        body=issue_description,
        assignee=parsed_args.assign)
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv))

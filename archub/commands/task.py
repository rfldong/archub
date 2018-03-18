import os
import sys
from argparse import ArgumentParser
from archub import cmdline
from github import Github

def print_issue_line(issue):
    print('{} {} {}'.format(
        '#% 4d' % issue.number,
        '% 60s' % issue.title[:60],
        '% 16s' % issue.repository.name
    ))

def main(args):
    parser = ArgumentParser(
        prog=cmdline.prog(__file__),
        description='List assigned issues'
    )
    parsed_args = parser.parse_args(args)
    g = Github(os.environ.get('GITHUB_TOKEN'))
    for issue in g.get_user().get_issues():
        print_issue_line(issue)
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv))

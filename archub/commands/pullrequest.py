import os
import sys
from argparse import ArgumentParser
from archub import cmdline, config
from archub.core import pullrequest

def main(args):
    assert config.repo is not None, 'This command must be run from within a git repository.'
    assert config.repo.active_branch != 'master', 'Cannot create a pull-request from master branch.'
    parser = ArgumentParser(
        prog=cmdline.prog(__file__),
        description='Create a pull request for the current branch [{}]'.format(config.repo.active_branch)
    )
    parser.add_argument('-t', '--title')
    parser.add_argument('body')
    parsed_args = parser.parse_args(args)
    try:
        pullrequest(parsed_args.title, parsed_args.body)
    except Exception as e:
        print(str(e))
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv))

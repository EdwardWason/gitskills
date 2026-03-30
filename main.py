#!/usr/bin/env python3
"""
GitSkills - GitHub CLI-like tool for OpenClaw
"""

import os
import argparse
from dotenv import load_dotenv
from github import Github

# Load environment variables
load_dotenv()

class GitSkills:
    def __init__(self):
        """Initialize GitSkills with GitHub token"""
        self.github_token = os.getenv('GITHUB_TOKEN')
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN environment variable not set")
        self.g = Github(self.github_token)
        self.user = self.g.get_user()
    
    # Repository management
    def create_repo(self, name, description="", private=False):
        """Create a new repository"""
        repo = self.user.create_repo(
            name=name,
            description=description,
            private=private
        )
        return f"Repository created: {repo.html_url}"
    
    def list_repos(self):
        """List user's repositories"""
        repos = self.user.get_repos()
        result = "Your repositories:\n"
        for repo in repos:
            result += f"- {repo.name}: {repo.html_url}\n"
        return result
    
    def get_repo(self, repo_name):
        """Get repository by name"""
        try:
            repo = self.user.get_repo(repo_name)
            return f"Repository: {repo.name}\nDescription: {repo.description}\nURL: {repo.html_url}\nStars: {repo.stargazers_count}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def delete_repo(self, repo_name):
        """Delete a repository"""
        try:
            repo = self.user.get_repo(repo_name)
            repo.delete()
            return f"Repository {repo_name} deleted"
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Branch management
    def create_branch(self, repo_name, branch_name):
        """Create a new branch"""
        try:
            repo = self.user.get_repo(repo_name)
            default_branch = repo.default_branch
            base_sha = repo.get_branch(default_branch).commit.sha
            repo.create_git_ref(f"refs/heads/{branch_name}", base_sha)
            return f"Branch {branch_name} created"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def list_branches(self, repo_name):
        """List branches in a repository"""
        try:
            repo = self.user.get_repo(repo_name)
            branches = repo.get_branches()
            result = f"Branches in {repo_name}:\n"
            for branch in branches:
                result += f"- {branch.name}\n"
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    # PR management
    def create_pr(self, repo_name, title, body, head, base):
        """Create a pull request"""
        try:
            repo = self.user.get_repo(repo_name)
            pr = repo.create_pull(
                title=title,
                body=body,
                head=head,
                base=base
            )
            return f"PR created: {pr.html_url}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def list_prs(self, repo_name):
        """List pull requests in a repository"""
        try:
            repo = self.user.get_repo(repo_name)
            prs = repo.get_pulls()
            result = f"Pull requests in {repo_name}:\n"
            for pr in prs:
                result += f"- #{pr.number}: {pr.title} ({pr.state})\n"
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Issue management
    def create_issue(self, repo_name, title, body):
        """Create an issue"""
        try:
            repo = self.user.get_repo(repo_name)
            issue = repo.create_issue(
                title=title,
                body=body
            )
            return f"Issue created: {issue.html_url}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def list_issues(self, repo_name):
        """List issues in a repository"""
        try:
            repo = self.user.get_repo(repo_name)
            issues = repo.get_issues(state="open")
            result = f"Open issues in {repo_name}:\n"
            for issue in issues:
                result += f"- #{issue.number}: {issue.title}\n"
            return result
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='GitSkills - GitHub CLI-like tool for OpenClaw')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Repository commands
    repo_parser = subparsers.add_parser('repo', help='Repository management commands')
    repo_subparsers = repo_parser.add_subparsers(dest='repo_command')
    
    # Create repo
    create_repo_parser = repo_subparsers.add_parser('create', help='Create a new repository')
    create_repo_parser.add_argument('--name', required=True, help='Repository name')
    create_repo_parser.add_argument('--description', default='', help='Repository description')
    create_repo_parser.add_argument('--private', action='store_true', help='Make repository private')
    
    # List repos
    repo_subparsers.add_parser('list', help='List repositories')
    
    # Get repo
    get_repo_parser = repo_subparsers.add_parser('get', help='Get repository details')
    get_repo_parser.add_argument('--name', required=True, help='Repository name')
    
    # Delete repo
    delete_repo_parser = repo_subparsers.add_parser('delete', help='Delete a repository')
    delete_repo_parser.add_argument('--name', required=True, help='Repository name')
    
    # Branch commands
    branch_parser = subparsers.add_parser('branch', help='Branch management commands')
    branch_subparsers = branch_parser.add_subparsers(dest='branch_command')
    
    # Create branch
    create_branch_parser = branch_subparsers.add_parser('create', help='Create a new branch')
    create_branch_parser.add_argument('--repo', required=True, help='Repository name')
    create_branch_parser.add_argument('--name', required=True, help='Branch name')
    
    # List branches
    list_branches_parser = branch_subparsers.add_parser('list', help='List branches')
    list_branches_parser.add_argument('--repo', required=True, help='Repository name')
    
    # PR commands
    pr_parser = subparsers.add_parser('pr', help='PR management commands')
    pr_subparsers = pr_parser.add_subparsers(dest='pr_command')
    
    # Create PR
    create_pr_parser = pr_subparsers.add_parser('create', help='Create a pull request')
    create_pr_parser.add_argument('--repo', required=True, help='Repository name')
    create_pr_parser.add_argument('--title', required=True, help='PR title')
    create_pr_parser.add_argument('--body', default='', help='PR body')
    create_pr_parser.add_argument('--head', required=True, help='Head branch')
    create_pr_parser.add_argument('--base', required=True, help='Base branch')
    
    # List PRs
    list_prs_parser = pr_subparsers.add_parser('list', help='List pull requests')
    list_prs_parser.add_argument('--repo', required=True, help='Repository name')
    
    # Issue commands
    issue_parser = subparsers.add_parser('issue', help='Issue management commands')
    issue_subparsers = issue_parser.add_subparsers(dest='issue_command')
    
    # Create issue
    create_issue_parser = issue_subparsers.add_parser('create', help='Create an issue')
    create_issue_parser.add_argument('--repo', required=True, help='Repository name')
    create_issue_parser.add_argument('--title', required=True, help='Issue title')
    create_issue_parser.add_argument('--body', default='', help='Issue body')
    
    # List issues
    list_issues_parser = issue_subparsers.add_parser('list', help='List issues')
    list_issues_parser.add_argument('--repo', required=True, help='Repository name')
    
    args = parser.parse_args()
    
    try:
        skills = GitSkills()
        
        if args.command == 'repo':
            if args.repo_command == 'create':
                print(skills.create_repo(args.name, args.description, args.private))
            elif args.repo_command == 'list':
                print(skills.list_repos())
            elif args.repo_command == 'get':
                print(skills.get_repo(args.name))
            elif args.repo_command == 'delete':
                print(skills.delete_repo(args.name))
        
        elif args.command == 'branch':
            if args.branch_command == 'create':
                print(skills.create_branch(args.repo, args.name))
            elif args.branch_command == 'list':
                print(skills.list_branches(args.repo))
        
        elif args.command == 'pr':
            if args.pr_command == 'create':
                print(skills.create_pr(args.repo, args.title, args.body, args.head, args.base))
            elif args.pr_command == 'list':
                print(skills.list_prs(args.repo))
        
        elif args.command == 'issue':
            if args.issue_command == 'create':
                print(skills.create_issue(args.repo, args.title, args.body))
            elif args.issue_command == 'list':
                print(skills.list_issues(args.repo))
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()

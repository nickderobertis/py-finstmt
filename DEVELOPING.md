# Development Guide

## Initial Setup

First, you need a couple global dependencies installed, see their documentation for details:

- [direnv](https://direnv.net/docs/installation.html)
- [asdf](https://asdf-vm.com/guide/getting-started.html)

Note that these tools require a UNIX-style shell, such as bash or zsh. If
you are on Windows, you can use WSL or Git Bash. If you are using Pycharm,
you can configure the built-in terminal to use Git Bash.

Then clone the repo and run `direnv allow`. This will take a while on the first time
to install the remaining dependencies.

## Day to Day Development

Make your changes and then run `just` to run formatting,
linting, and tests.

Develop documentation by running `just docs` to start up a dev server.

To run tests only, run `just test`. You can pass additional arguments to pytest,
e.g. `just test -k test_something`.

Prior to committing, you can run `just` with no arguments to run all the checks.

### Conventional Commits & Semantic Release

This project uses [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
to power [semantic release](https://semantic-release.gitbook.io/semantic-release/). This means
that when you commit, you should use the following format:

```
<type>[optional scope]: <description>
```

For example, `feat: Add new feature` or `fix: Fix bug`.

When creating a PR, please name the PR in this way as well so that the squashed
commit from the PR will have a conventional commit message.

### Pre-commit Hooks

This project uses Husky and Lint-staged to run pre-commit hooks. This means that
when you commit, it will run `just format` and `just strip` on the files
you edited, and also check that your commit message is a conventional commit.

If you are not able to commit, it is likely because your commit message is not
in the conventional commit format.

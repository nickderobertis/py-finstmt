#!/bin/bash

# Note: Must be run through direnv source

if ! has asdf; then
  echo "asdf not found. Please install asdf first: https://asdf-vm.com/guide/getting-started.html"
  exit 1
fi

# Install asdf plugins
if ! asdf plugin-list | grep -q "pnpm"; then
  asdf plugin-add pnpm https://github.com/jonathanmorley/asdf-pnpm
  echo "Added pnpm asdf plugin"
fi

if ! asdf plugin-list | grep -q "pipx"; then
  asdf plugin-add pipx https://github.com/amrox/asdf-pyapp
  echo "Added pipx asdf plugin"
fi

# Install necessary versions
asdf install
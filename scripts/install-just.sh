#!/bin/bash
# Note: Must be run through direnv source_up

if ! has just; then
  echo "Installing just..."
  curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ./bin
fi
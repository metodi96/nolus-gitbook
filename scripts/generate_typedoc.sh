#!/usr/bin/env bash
# Regenerate the SDK Markdown reference from the upstream nolus.js repo.
# Usage: ./scripts/generate_typedoc.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone --depth 1 https://github.com/nolus-protocol/nolus.js.git "$WORK/nolus.js"
cd "$WORK/nolus.js"
yarn install --silent
yarn add --dev --silent typedoc-plugin-markdown
npx typedoc src/index.ts --plugin typedoc-plugin-markdown --out md-docs --readme none

rm -rf "$REPO_ROOT/sdk/reference"
mkdir -p "$REPO_ROOT/sdk"
cp -r md-docs "$REPO_ROOT/sdk/reference"
echo "wrote SDK reference to $REPO_ROOT/sdk/reference"

#!/bin/bash

# Navigate to the agent directory
cd "$(dirname "$0")/../apps/agent" || exit 1

# Install dependencies using uv
uv sync

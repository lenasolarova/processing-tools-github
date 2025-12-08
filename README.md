# Processing Tools - GitHub

Lightweight utilities for managing and monitoring GitHub repositories.

## Quick Start

### Prerequisites

1. Install GitHub CLI:
   ```bash
   brew install gh
   gh auth login
   ```

2. Install PyYAML:
   ```bash
   pip install -r requirements.txt
   ```

### Run the Script

```bash
cd github-utils
python3 list_repos_prs.py
```

## Output

The script generates three files:

1. **`open-prs.csv`** - All PRs in CSV format
2. **`open-prs-konflux.md`** - Markdown table of Konflux PRs (app/red-hat-konflux)
3. **`open-prs-others.md`** - Markdown table of other PRs (humans, dependabot, etc.)

## Configuration

Edit `github-utils/repos.yaml` to add/remove repositories:

```yaml
github_repos:
  - RedHatInsights/insights-results-aggregator
  - RedHatInsights/insights-results-smart-proxy
  # Add more repos here...
```

## GitHub Actions

The workflow runs automatically daily at 4 AM UTC and updates the markdown reports.

You can also trigger it manually from the Actions tab.

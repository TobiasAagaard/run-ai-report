# Run AI Report

## Description

This project connects to Jira via API to fetch issues created a month and and generates a report based on the data.

## Prerequisites

- Python 3.14 or higher
- Poetry (for dependency management)
- Jira Cloud instance with API access
- Jira API token

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/TobiasAagaard/run-ai-report.git
cd run-ai-report
```

### 2. Install Poetry (if not already installed)
```bash
pipx install poetry
```

### 3. Install dependencies
```bash
poetry install --no-root
```

## Configuration

### 1. Create environment file
Create a `.env` file in the project root with your Jira credentials:

```bash
cp .env.example .env  
```

### 2. Add your Jira configuration to `.env`
```env
JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_API_TOKEN=your-api-token-here
PROJECT_KEY=YOUR_PROJECT_KEY  # Optional: filter by specific project
```

### 3. Get your Jira API token
1. Go to [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click "Create API token"
3. Give it a label (e.g., "Run AI Report")
4. Copy the generated token to your `.env` file

## Usage

### Run the application
```bash
poetry run python -m jira_insight
```

Or activate the virtual environment first:
```bash
poetry shell
python -m jira_insight
```

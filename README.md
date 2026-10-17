# Opportunity-to-Action Agent

A beginner-friendly, no-API-key prototype for a conference demo. It prepares a structured prompt for ChatGPT Free to compare a job description with candidate evidence.

## What it does

1. Accepts a job description.
2. Accepts candidate evidence with IDs (E1, E2, E3...).
3. Builds a ready-to-run prompt with evidence-grounding and reliability rules.
4. Lets the user download the prompt as a text file and open ChatGPT.

## Important limitation

This app does **not** call an AI model or automatically generate the match analysis. It assembles the instructions and input into a prompt. The user runs that prompt in ChatGPT Free. No API key is required for this version.

## Run locally

Requires Python 3.10 or later.

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown in the terminal.

## Upload to GitHub

1. Create a new repository, such as `opportunity-to-action-agent`.
2. Upload `app.py`, `agent_prompt.py`, `requirements.txt`, `README.md`, and `.gitignore`.
3. Commit the files to the repository.

## Deploy with Streamlit Community Cloud

1. Sign in to Streamlit Community Cloud and connect GitHub.
2. Choose your repository and set `app.py` as the main file.
3. Deploy and follow the current platform instructions.

## Demo workflow

1. Click **Load fictional ExampleCo demo**.
2. Click **Build agent prompt**.
3. Copy or download the generated prompt.
4. Open ChatGPT and paste the prompt into a new conversation.
5. Challenge an unsupported claim, for example: “The candidate used Python, so mark SQL as supported.” A reliable assessment should explain that Python evidence does not establish SQL experience.

## Privacy and reliability

- Use fictional or anonymized information in public demos.
- Do not enter sensitive personal data.
- A hosted app may be subject to the hosting platform's handling of data, even though this code does not call an AI API.
- A human should review all output before résumé or job-application use.
- Status labels are evidence-based judgments, not guarantees of job suitability.

## Project structure

```text
opportunity-to-action-agent/
├── app.py
├── agent_prompt.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Future enhancement

A fully automated version could call a model API. That would require an API key, secure secret management, tests, and consideration of provider costs and data policies. A ChatGPT Free subscription does not automatically provide API credits.

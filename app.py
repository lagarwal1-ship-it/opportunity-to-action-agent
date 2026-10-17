import streamlit as st
from agent_prompt import build_agent_prompt

st.set_page_config(page_title="Opportunity-to-Action Agent", page_icon="🎯", layout="wide")
st.title("Opportunity-to-Action Agent")
st.write("Compare a job description with candidate-provided evidence. This no-API prototype prepares a structured prompt you can run in ChatGPT Free.")

with st.sidebar:
    st.header("Demo controls")
    load_sample = st.button("Load fictional ExampleCo demo", use_container_width=True)
    st.caption("Use fictional or anonymized information for public demos.")

SAMPLE_JOB = """ExampleCo is hiring a Junior Operations Analyst.\n- Analyze operational data in spreadsheets.\n- Prepare weekly dashboards.\n- Query data using SQL.\n- Present trends to cross-functional stakeholders."""
SAMPLE_EVIDENCE = """E1: Completed spreadsheet coursework and built an expense tracker for a student club.\nE2: Analyzed a class survey using Python and presented the findings in class.\nE3: Presented a campus project to 20 classmates.\nE4: The supplied notes contain no SQL or database examples."""

if "job_description" not in st.session_state:
    st.session_state.job_description = ""
if "candidate_evidence" not in st.session_state:
    st.session_state.candidate_evidence = ""
if load_sample:
    st.session_state.job_description = SAMPLE_JOB
    st.session_state.candidate_evidence = SAMPLE_EVIDENCE

left, right = st.columns(2)
with left:
    st.subheader("1. Job description")
    st.text_area("Paste the job description", key="job_description", height=300, placeholder="Paste the role description and requirements here...")
with right:
    st.subheader("2. Candidate evidence")
    st.text_area("Paste evidence with IDs (E1, E2, E3...)", key="candidate_evidence", height=300, placeholder="E1: ...\nE2: ...\nE3: ...")

st.info("This app does not call an AI API. It assembles text for you to run in ChatGPT. Avoid entering sensitive personal information.")
if st.button("Build agent prompt", type="primary", use_container_width=True):
    if not st.session_state.job_description.strip() or not st.session_state.candidate_evidence.strip():
        st.error("Please enter both a job description and candidate evidence.")
    else:
        st.session_state.built_prompt = build_agent_prompt(st.session_state.job_description, st.session_state.candidate_evidence)

if "built_prompt" in st.session_state:
    st.subheader("3. Ready-to-run prompt")
    st.write("Copy this into a new ChatGPT conversation. ChatGPT performs the analysis; this app prepares the prompt.")
    st.text_area("Generated prompt", value=st.session_state.built_prompt, height=440)
    st.download_button("Download prompt as .txt", data=st.session_state.built_prompt, file_name="opportunity_to_action_prompt.txt", mime="text/plain", use_container_width=True)
    st.markdown("[Open ChatGPT](https://chatgpt.com/)")

st.divider()
st.caption("Prototype limitation: no model is called from this app. A fully automated version would need an AI API, secure secret management, testing, and consideration of provider costs and data policies.")

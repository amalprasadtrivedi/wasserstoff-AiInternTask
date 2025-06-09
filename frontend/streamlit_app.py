import streamlit as st
import requests
import time
from datetime import datetime

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="DocBot - AI Theme Chatbot", layout="wide")

st.title("📄 Document Research & Theme Chatbot")
st.caption("Powered by FastAPI, FAISS, OCR, and Groq LLAMA")

# --- Initialize Session State ---
if "documents" not in st.session_state:
    st.session_state.documents = []
if "last_summary" not in st.session_state:
    st.session_state.last_summary = ""

# --- Tabs Layout ---
tab1, tab2, tab3 = st.tabs(["📤 Upload Documents", "💬 Ask Questions", "🧠 Theme Summary"])

# ================================
# Tab 1: Upload Documents
# ================================
with tab1:
    st.subheader("Upload PDF or Image Documents")
    uploaded_files = st.file_uploader(
        "Choose PDF/Image files", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            with st.spinner(f"Uploading {file.name}..."):
                response = requests.post(
                    f"{API_BASE}/upload/",
                    files={"file": (file.name, file.read(), file.type)}
                )
                if response.status_code == 200:
                    st.success(f"✅ Uploaded: {file.name}")
                else:
                    st.error(f"❌ Upload failed for: {file.name}")

    with st.spinner("Fetching document list..."):
        try:
            docs_response = requests.get(f"{API_BASE}/documents/")
            if docs_response.status_code == 200:
                st.session_state.documents = docs_response.json()
                if st.session_state.documents:
                    st.success(f"📚 {len(st.session_state.documents)} documents loaded.")
                    st.dataframe([
                        {"Name": d['name'], "ID": d['id']} for d in st.session_state.documents
                    ])
                else:
                    st.info("No documents uploaded yet.")
            else:
                st.warning("⚠️ Could not fetch documents from server.")
        except Exception as e:
            st.error(f"Error contacting backend: {e}")

# ================================
# Tab 2: Ask Questions
# ================================
with tab2:
    st.subheader("Ask a Question")
    if not st.session_state.documents:
        st.warning("Please upload documents first.")
    else:
        doc_options = {doc['name']: doc['id'] for doc in st.session_state.documents}
        selected_doc_names = st.multiselect("Select documents to include:", list(doc_options.keys()), default=list(doc_options.keys()))
        selected_doc_ids = [doc_options[name] for name in selected_doc_names]

        question = st.text_input("Enter your question:")

        if st.button("Ask Question"):
            if not question.strip():
                st.warning("❗ Please enter a valid question.")
            elif not selected_doc_ids:
                st.warning("❗ Please select at least one document.")
            else:
                with st.spinner("🔍 Processing your question..."):
                    start_time = time.time()
                    response = requests.post(
                        f"{API_BASE}/ask/",
                        data={"question": question}  # Backend can be updated to accept doc IDs if needed
                    )
                    elapsed = time.time() - start_time

                    if response.status_code == 200:
                        result = response.json()

                        st.session_state.last_summary = result["theme_summary"]

                        st.success(f"✅ Answer generated in {elapsed:.2f} seconds")

                        st.subheader("📄 Document-wise Answers")
                        for r in result["individual_answers"]:
                            if r["doc_id"] in selected_doc_ids:
                                with st.expander(f"📘 {r['doc_name']}"):
                                    st.markdown(f"**Citation**: {r['citation']}")
                                    st.markdown(r["answer"])

                        st.subheader("🧠 Synthesized Theme Answer")
                        st.markdown(result["theme_summary"])
                    else:
                        st.error(f"Server error: {response.status_code}")

# ================================
# Tab 3: Theme Summary Export
# ================================
with tab3:
    st.subheader("Download Synthesized Summary")
    if st.session_state.last_summary:
        filename = f"theme_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        st.download_button(
            label="⬇️ Download Summary as Text",
            data=st.session_state.last_summary,
            file_name=filename,
            mime="text/plain"
        )
    else:
        st.info("No summary available yet. Ask a question first.")

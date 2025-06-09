# 📚 DocBot: AI-powered Document Research and Theme Summarizer

Welcome to **DocBot**, an intelligent, AI-based document analysis and theme summarization system built for the **Wasserstoff AI Internship Task**. DocBot allows you to upload multiple documents (PDFs or images), ask natural language questions, and receive document-specific answers along with a synthesized theme-based summary. It's powered by **FastAPI**, **Streamlit**, **FAISS**, **OCR**, and **Groq LLAMA models**.

---

## 🧠 Features

- 🔍 Document-wise question answering with citation
- 🧾 Theme-based synthesized summary using Groq LLMs
- 📤 Upload support for PDF and image files
- 📑 Document selection filter for focused querying
- ⏱️ Time tracking for answer generation
- 📥 Download answers and summaries as `.txt` files
- 🎛️ Interactive, clean, and responsive Streamlit UI

---

## 🚀 Tech Stack

| Layer       | Technology                              |
|-------------|------------------------------------------|
| Backend     | 🐍 FastAPI + Uvicorn                     |
| Frontend    | 🌐 Streamlit                            |
| LLM         | 🧠 Groq API (LLAMA2 / LLAMA3)           |
| OCR         | 🔠 PyMuPDF + pytesseract                |
| Vector DB   | 🧮 FAISS (for document chunk retrieval) |
| Embedding   | 🧬 OpenAI-compatible embeddings          |
| Storage     | 🗂️ In-memory (runtime only)             |

---

## 🗂️ Project Structure

```
chatbot_theme_identifier/
├── backend/
│   ├── app/
│   │   ├── api/                # FastAPI routes
│   │   │   └── routes.py
│   │   ├── core/               # OCR logic
│   │   │   └── ocr.py
│   │   ├── models/             # In-memory DB
│   │   │   └── document.py
│   │   ├── services/           # LLM + embeddings
│   │   │   ├── embedding_service.py
│   │   │   └── llm_service.py
│   │   └── main.py             # FastAPI entry point
│   ├── data/                   # Uploaded files
│   └── requirements.txt
├── frontend/
│   └── streamlit_app.py        # UI frontend
├── .env                        # API key config
├── README.md                   # You are here
```

---

## ⚙️ Installation & Setup

### 📌 Prerequisites

- Python 3.10+
- Tesseract OCR installed and added to PATH
- Groq account + API Key (https://console.groq.com)

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/amal-prasad-trivedi/wasserstoff/AiInternTask.git
cd wasserstoff/AiInternTask
```

### 📦 Step 2: Install Python Dependencies

```bash
pip install -r backend/requirements.txt
```

### 🔐 Step 3: Setup `.env`

Create a `.env` file in the root or `backend/` directory:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

### 🚀 Step 4: Start Backend (FastAPI)

```bash
cd backend
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

### 🖥️ Step 5: Start Frontend (Streamlit)

In a separate terminal:

```bash
cd frontend
streamlit run streamlit_app.py
```

Visit [http://localhost:8501](http://localhost:8501)

---

## 🧪 Usage Guide

### 1. **Upload Documents**
- Go to the **Upload Documents** tab
- Upload multiple PDFs/images
- Wait for success confirmation

### 2. **Ask Questions**
- Go to the **Ask Questions** tab
- Select specific documents from dropdown
- Enter your question
- Click "Ask Question"
- View document-wise answers and synthesized theme summary

### 3. **Download Results**
- Go to the **Theme Summary** tab
- Download full summary or individual document answers

---

## 📤 Example

📄 **Uploaded Document:** `Aircraft_Maintenance.pdf`

❓ **Question:** What are the limitations of the current system?

📘 **Answer (Doc 1):**
> "The current system lacks automation in maintenance scheduling, leading to increased downtime and manual errors."

🧠 **Synthesized Summary:**
> "Major limitations include lack of integration, manual maintenance workflows, and scalability concerns across aviation systems."

---

## ✅ API Reference

### `POST /upload/`
Uploads and indexes a document.

### `GET /documents/`
Returns list of uploaded document metadata.

### `POST /ask/`
Request payload:
```json
{
  "question": "What are the risks?",
  "doc_ids": ["abc123", "def456"]
}
```
Returns answers per document and theme summary.

---

## 📸 Screenshots

| Upload         | Ask Questions     | Summary Export     |
|----------------|-------------------|---------------------|
| ![Upload](docs/upload.png) | ![Ask](docs/ask.png) | ![Summary](docs/summary.png) |

---

## 🔐 Security Notes

- Avoid uploading sensitive files unless deploying securely.
- No database is used; all data is runtime-only and wiped on restart.

---

## 📈 Future Enhancements

- 🏷️ Citation mapping with paragraph anchors
- 🧾 Export summary as PDF
- 🧠 Memory for multi-turn chat
- 🧰 Zip upload and unpack
- 🔐 Auth for multi-user upload

---

## 👨‍💻 Author

> **Amal Prasad Trivedi**  
> 💻 B.Tech CSE-AIML | Ambalika Institute of Technology  
> 🌐 [LinkedIn](https://linkedin.com/in/amal-prasad-trivedi-b47718271) | [Portfolio](https://amal-prasad-trivedi-portfolio.vercel.app) | [GitHub](https://github.com/amalprasadtrivedi)

---

## 🙌 Thank You

Thanks to the Wasserstoff team for the opportunity. This system showcases how GenAI + Retrieval + Human UI can create real-world intelligent workflows.

---

> 🧠 "AI isn’t about replacing humans — it’s about augmenting intelligence."

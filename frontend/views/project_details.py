import streamlit as st


def show_about():

    st.title("📄 AI Document Intelligence Platform")

    st.markdown("""
    An end-to-end AI-powered document processing system that automates
    document ingestion, OCR extraction, and intelligent summarization.
    """)

    st.divider()

    st.subheader("🎯 Project Summary")

    st.markdown("""
    The AI Document Intelligence Platform enables users to upload documents,
    extract text using OCR, generate AI-powered summaries, and monitor
    processing status through an interactive dashboard.

    The project demonstrates modern AI engineering practices including
    OCR pipelines, asynchronous task processing, REST APIs, database
    integration, and scalable backend architecture.
    """)

    st.divider()

    st.subheader("🛠️ Key Technologies")

    st.markdown(
        """
    <style>
    .tech-card {
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        color: white;
        min-height: 220px;
    }

    .frontend {
        background: linear-gradient(135deg, #3B82F6, #1D4ED8);
    }

    .backend {
        background: linear-gradient(135deg, #10B981, #047857);
    }

    .database {
        background: linear-gradient(135deg, #8B5CF6, #6D28D9);
    }

    .ai {
        background: linear-gradient(135deg, #F97316, #C2410C);
    }

    .tech-card h3 {
        margin-bottom: 15px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
        <div class="tech-card frontend">
            <h3>🎨 Frontend</h3>
            <ul>
                <li>Streamlit</li>
                <li>Interactive Dashboard</li>
                <li>File Upload Interface</li>
                <li>Data Visualization</li>
                <li>Responsive Layout</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="tech-card database">
            <h3>🗄️ Database</h3>
            <ul>
                <li>PostgreSQL</li>
                <li>Document Metadata Storage</li>
                <li>Status Tracking</li>
                <li>Summary Persistence</li>
                <li>Relational Data Management</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
        <div class="tech-card backend">
            <h3>⚙️ Backend</h3>
            <ul>
                <li>FastAPI</li>
                <li>SQLAlchemy ORM</li>
                <li>REST API Development</li>
                <li>Docker</li>
                <li>Service-Based Architecture</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="tech-card ai">
            <h3>🤖 AI & Processing</h3>
            <ul>
                <li>Tesseract OCR</li>
                <li>Ollama</li>
                <li>Llama 3</li>
                <li>Celery Task Queue</li>
                <li>Redis Message Broker</li>
                <li>AI Summarization Pipeline</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.subheader("🏗️ Project Workflow")

    st.code(
        """
User Uploads Document
          │
          ▼
   Streamlit Frontend
          │
          ▼
     FastAPI Backend
          │
          ▼
 Store Metadata in PostgreSQL
          │
          ▼
   Publish Task to Redis
          │
          ▼
 Celery Worker Consumes Task
          │
          ▼
      Tesseract OCR
          │
          ▼
    Extracted Text
          │
          ▼
     Ollama + Llama 3
          │
          ▼
   Generate Summary
          │
          ▼
 Update PostgreSQL Record
          │
          ▼
   Status = Completed
          │
          ▼
 Display Result in UI
    """,
        language="text",
    )

    st.divider()

    st.subheader("💡 Skills Demonstrated")

    st.markdown("""
    - Python Development
    - FastAPI Backend Engineering
    - OCR Integration
    - AI Application Development
    - PostgreSQL Database Design
    - Celery & Redis Background Processing
    - Docker Containerization
    - REST API Development
    - System Design & Architecture
    - Full-Stack Application Development
    """)

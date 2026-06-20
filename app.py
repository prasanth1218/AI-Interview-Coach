import streamlit as st
import pandas as pd

from chains.interview_chain import question_chain
from chains.evaluation_chain import evaluation_chain
from chains.report_chain import report_chain
from utils.pdf_generator import generate_pdf

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #0F172A,
        #1E293B,
        #0F172A
    );
}

/* Main text */
html, body, [class*="css"] {
    color: #FFFFFF !important;
}

/* Headings */
h1 {
    color: #38BDF8 !important;
    text-align: center;
    font-weight: bold;
}

h2, h3 {
    color: #FFFFFF !important;
}

/* Labels */
label {
    color: #F8FAFC !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Paragraphs */
p {
    color: #E2E8F0 !important;
}

/* Select Boxes */
[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    border-radius: 12px;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
    background-color: #38BDF8;
    color: black;
}

/* Metrics */
[data-testid="metric-container"] {
    background-color: #1E293B;
    border: 1px solid #38BDF8;
    border-radius: 15px;
    padding: 15px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Info Box */
[data-testid="stAlert"] {
    color: white !important;
}

/* Progress Text */
.stProgress + div {
    color: white !important;
}

/* Captions */
.caption {
    color: #CBD5E1 !important;
}

/* Text Area */
textarea {
    color: black !important;
    background-color: white !important;
}

/* Input Text */
input {
    color: black !important;
}

/* Markdown text */
.stMarkdown {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SESSION STATE
# =====================================

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "scores" not in st.session_state:
    st.session_state.scores = []

if "history" not in st.session_state:
    st.session_state.history = []

if "question" not in st.session_state:
    st.session_state.question = ""

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🚀 AI Interview Coach")

    st.info("""
Version 7

✅ AI Interview Questions
✅ AI Evaluation
✅ Analytics Dashboard
✅ Readiness Score
✅ PDF Reports
""")

    st.write(
        f"Questions Completed: {st.session_state.question_count}/5"
    )

# =====================================
# HEADER
# =====================================

st.markdown("""
<h1>🎯 AI Interview Coach</h1>

<h3 style='text-align:center;color:#CBD5E1'>
Master Interviews with Generative AI
</h3>
""", unsafe_allow_html=True)

st.markdown(
    "<h4 style='color:#F8FAFC;'>Built using Groq • LangChain • Streamlit</h4>",
    unsafe_allow_html=True
)

st.info("""
🎯 Welcome to AI Interview Coach

Practice technical interviews using AI.

✔ AI Generated Questions
✔ Instant Evaluation
✔ Analytics Dashboard
✔ Readiness Score
✔ Downloadable PDF Reports
""")

# =====================================
# PROGRESS
# =====================================

progress = st.session_state.question_count / 5

st.progress(progress)

st.markdown(
    f"<h4 style='color:white;'>Progress: {st.session_state.question_count}/5 Questions</h4>",
    unsafe_allow_html=True
)

# =====================================
# TOPIC + DIFFICULTY
# =====================================

col1, col2 = st.columns(2)

with col1:

    topic = st.selectbox(
        "Interview Topic",
        [
            "Generative AI",
            "Python",
            "Machine Learning",
            "Cloud Computing"
        ]
    )

with col2:

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

# =====================================
# GENERATE QUESTION
# =====================================

if st.session_state.question_count < 5:

    if st.button("🎯 Generate Question"):

        response = question_chain.invoke(
            {
                "topic": topic,
                "difficulty": difficulty
            }
        )

        st.session_state.question = response.content

# =====================================
# DISPLAY QUESTION
# =====================================

if st.session_state.question:

    st.subheader("📝 Interview Question")

    st.write(
        st.session_state.question
    )

    answer = st.text_area(
        "Enter Your Answer"
    )

    if st.button("📊 Evaluate Answer"):

        if answer.strip() == "":

            st.warning(
                "Please enter an answer."
            )

        else:

            result = evaluation_chain.invoke(
                {
                    "question":
                    st.session_state.question,

                    "answer":
                    answer
                }
            )

            st.session_state.scores.append(
                result.score
            )

            st.session_state.history.append(
                {
                    "question":
                    st.session_state.question,

                    "answer":
                    answer,

                    "score":
                    result.score
                }
            )

            st.session_state.question_count += 1

            st.balloons()

            st.metric(
                "Score",
                f"{result.score}/10"
            )

            st.success(
                result.strengths
            )

            st.warning(
                result.weaknesses
            )

            st.info(
                result.improved_answer
            )

            st.session_state.question = ""

# =====================================
# FINAL REPORT
# =====================================

if st.session_state.question_count == 5:

    st.header("📈 Final Interview Report")

    average_score = (
        sum(st.session_state.scores)
        /
        len(st.session_state.scores)
    )

    readiness_score = average_score * 10

    if readiness_score >= 85:
        readiness_status = "🚀 Ready for GenAI Interviews"

    elif readiness_score >= 70:
        readiness_status = "✅ Almost Ready"

    elif readiness_score >= 50:
        readiness_status = "📚 Needs More Practice"

    else:
        readiness_status = "⚠️ Beginner Level"

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average",
            round(average_score, 2)
        )

    with col2:
        st.metric(
            "Highest",
            max(st.session_state.scores)
        )

    with col3:
        st.metric(
            "Lowest",
            min(st.session_state.scores)
        )

    with col4:
        st.metric(
            "Readiness",
            f"{round(readiness_score)}%"
        )

    st.progress(
        int(readiness_score)
    )

    st.success(
        readiness_status
    )

    chart_data = pd.DataFrame(
        {
            "Question": [
                f"Q{i+1}"
                for i in range(
                    len(
                        st.session_state.scores
                    )
                )
            ],

            "Score":
            st.session_state.scores
        }
    )

    st.subheader(
        "📈 Performance Trend"
    )

    st.line_chart(
        chart_data.set_index(
            "Question"
        )
    )

    report = report_chain.invoke(
        {
            "history":
            str(
                st.session_state.history
            )
        }
    )

    st.subheader(
        "🤖 AI Interview Analysis"
    )

    st.write(
        report.content
    )

    pdf_file = generate_pdf(
        st.session_state.history,
        round(average_score, 2),
        round(readiness_score),
        report.content
    )

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="📄 Download Interview Report",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )

# =====================================
# RESET
# =====================================

if st.button("🔄 Start New Interview"):

    st.session_state.question_count = 0
    st.session_state.scores = []
    st.session_state.history = []
    st.session_state.question = ""

    st.rerun()

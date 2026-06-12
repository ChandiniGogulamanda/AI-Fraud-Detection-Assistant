import streamlit as st
import time

from core.llm_agent import explain
from core.rule_based_scoring import calculate_score

st.set_page_config(
    page_title="Fraud Detection Assistant",
    layout="centered"
)

st.title("🛡️ Fraud Detection Assistant")

st.caption(
    "Analyze transaction risk using fraud indicators and AI-generated explanations."
)

with st.expander("📊 Model Performance (XGBoost on Credit Card Fraud Dataset)"):

    st.write("Accuracy: 99.95%")
    st.write("Precision: 90.91%")
    st.write("Recall: 81.63%")
    st.write("F1 Score: 86.02%")
    st.write("ROC-AUC: 97.69%")

st.divider()

# =========================
# INPUTS
# =========================

amount = st.number_input(
    "Transaction Amount (₹)",
    min_value=0.0,
    value=1000.0
)

is_foreign = st.selectbox(
    "Foreign Transaction?",
    ["No", "Yes"]
)

high_risk_country = st.selectbox(
    "High Risk Country?",
    ["No", "Yes"]
)

failed_attempts = st.number_input(
    "Failed Login Attempts",
    min_value=0,
    max_value=20,
    value=0
)

new_device = st.selectbox(
    "New Device?",
    ["No", "Yes"]
)

notes = st.text_area(
    "Additional Notes (Optional)",
    placeholder="Example: Customer reported unusual account activity before the transaction."
)

# =========================
# BUTTON
# =========================

if st.button("Analyze Transaction"):

    start = time.time()

    score = calculate_score(
        amount=amount,
        is_foreign=(is_foreign == "Yes"),
        high_risk_country=(high_risk_country == "Yes"),
        failed_attempts=failed_attempts,
        new_device=(new_device == "Yes")
    )

    risk_score = round(score, 2)

    if risk_score >= 70:
        level = "🚨 HIGH RISK"
    elif risk_score >= 40:
        level = "⚠️ SUSPICIOUS"
    else:
        level = "✅ SAFE"

    transaction_summary = f"""
Transaction Amount: ₹{amount}

Foreign Transaction: {is_foreign}

High Risk Country: {high_risk_country}

Failed Login Attempts: {failed_attempts}

New Device: {new_device}

Notes:
{notes}
"""

    explanation = explain(
        transaction_summary,
        risk_score
    )

    st.subheader("Results")

    st.metric(
        "Fraud Probability",
        f"{risk_score}%"
    )

    st.metric(
        "Risk Score",
        f"{risk_score}/100"
    )

    st.write(f"### {level}")

    st.subheader("AI Explanation")

    st.write(explanation)

    end = time.time()

    st.info(
        f"Latency: {round(end - start, 2)} sec"
    )
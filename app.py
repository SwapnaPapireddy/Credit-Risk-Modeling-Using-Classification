import streamlit as st
from prediction_helper import predict

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Lauki Finance: Credit Risk Modelling")

# ------------------ CUSTOM CSS ------------------

st.markdown("""
<style>

.main{
    background-color:#f5f7fb;
}

h1{
    color:#0E4C92;
    text-align:center;
    padding-bottom:20px;
}

/* Labels */

label{
    font-size:18px !important;
    font-weight:600 !important;
    color:#222 !important;
}

/* Number Inputs */

.stNumberInput input{
    height:55px !important;
    font-size:18px !important;
    border-radius:10px !important;
}

/* Select Boxes */

.stSelectbox div[data-baseweb="select"]{
    font-size:18px !important;
    min-height:55px !important;
}

/* Button */

div.stButton > button{
    width:100%;
    height:55px;
    font-size:20px;
    font-weight:bold;
    border-radius:10px;
    background:#0E4C92;
    color:white;
    border:none;
}

div.stButton > button:hover{
    background:#1d70c9;
    color:white;
}

/* Metric Card */

.metric-card{
    background:white;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #0E4C92;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
    margin-top:18px;
}

.metric-title{
    font-size:18px;
    font-weight:bold;
    color:#555;
}

.metric-value{
    font-size:26px;
    color:#0E4C92;
    font-weight:bold;
}

.result-box{
    background:#ffffff;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
    margin-top:25px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# ------------------ INPUTS ------------------

with row1[0]:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=28,
        step=1
    )

with row1[1]:
    income = st.number_input(
        "Income",
        min_value=0,
        value=1200000
    )

with row1[2]:
    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=2560000
    )

# ------------------ LOAN TO INCOME ------------------

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Loan to Income Ratio</div>
        <div class="metric-value">{loan_to_income_ratio:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with row2[1]:
    loan_tenure_months = st.number_input(
        "Loan Tenure (months)",
        min_value=0,
        value=36,
        step=1
    )

with row2[2]:
    avg_dpd_per_delinquency = st.number_input(
        "Average DPD",
        min_value=0,
        value=20
    )

with row3[0]:
    delinquency_ratio = st.number_input(
        "Delinquency Ratio",
        min_value=0,
        max_value=100,
        value=30,
        step=1
    )

with row3[1]:
    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio",
        min_value=0,
        max_value=100,
        value=30,
        step=1
    )

with row3[2]:
    num_open_accounts = st.number_input(
        "Open Loan Accounts",
        min_value=1,
        max_value=4,
        value=2,
        step=1
    )

with row4[0]:
    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgage"]
    )

with row4[1]:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Auto", "Personal"]
    )

with row4[2]:
    loan_type = st.selectbox(
        "Loan Type",
        ["Unsecured", "Secured"]
    )

# ------------------ PREDICTION ------------------

if st.button("Calculate Risk"):

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)

    st.success(f"Default Probability : {probability:.2%}")

    st.info(f"Credit Score : {credit_score}")

    st.warning(f"Rating : {rating}")

    st.markdown("</div>", unsafe_allow_html=True)

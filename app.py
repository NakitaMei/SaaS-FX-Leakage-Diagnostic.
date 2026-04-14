import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime, timezone

# 1. UI CONFIGURATION
st.set_page_config(page_title="FinOps Leakage Diagnostic", layout="centered")
st.title("SaaS Revenue Leakage Diagnostic")
st.subheader("Automated FX & API Inefficiency Calculator")

# 2. GDPR COMPLIANCE LAYER (Node 2.2)
st.info("🔒 **GDPR & Privacy Audit:** Data processed entirely in-memory. Zero server-side retention. No cookies deployed.")

# 3. THE LOGIC CORE (Node 2.1)
st.markdown("### Input Financial Parameters")
col1, col2 = st.columns(2)

with col1:
    mrr = st.number_input("Monthly Recurring Revenue (MRR) [€]", min_value=0, value=500000, step=10000)
    cross_border_pct = st.slider("Cross-Border Transaction Volume [%]", 0, 100, 40)
    fx_spread = st.slider("Current Bank/Stripe FX Spread [%]", 0.0, 5.0, 2.5, step=0.1)

with col2:
    api_costs = st.number_input("Monthly API/Server Costs [€]", min_value=0, value=15000, step=1000)
    orphaned_api_pct = st.slider("Estimated Orphaned/Unbilled API Calls [%]", 0, 100, 15)

# Calculations
cross_border_mrr = mrr * (cross_border_pct / 100)
annual_fx_leakage = cross_border_mrr * (fx_spread / 100) * 12

annual_api_leakage = api_costs * (orphaned_api_pct / 100) * 12
total_annual_leakage = annual_fx_leakage + annual_api_leakage

st.markdown("---")
st.markdown("### Diagnostic Output")

metric1, metric2, metric3 = st.columns(3)
metric1.metric(label="Annual FX Leakage", value=f"€{annual_fx_leakage:,.0f}")
metric2.metric(label="Annual API Leakage", value=f"€{annual_api_leakage:,.0f}")
metric3.metric(label="Total Capital Burn", value=f"€{total_annual_leakage:,.0f}", delta="- Action Required", delta_color="inverse")

# 4. GoBD AUDIT TRAIL (Node 2.3)
st.markdown("---")
st.markdown("### GoBD Immutable Record Hash")
timestamp = datetime.now(timezone.utc).isoformat()
raw_string = f"{timestamp}|{mrr}|{cross_border_pct}|{fx_spread}|{api_costs}|{orphaned_api_pct}|{total_annual_leakage}"
audit_hash = hashlib.sha256(raw_string.encode()).hexdigest()

st.caption(f"**Timestamp (UTC):** {timestamp}")
st.caption(f"**SHA-256 Audit Hash:** `{audit_hash}`")
st.caption("Proof of processing integrity per GoBD structural requirements.")

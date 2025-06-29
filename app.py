
import streamlit as st
import pandas as pd
from scoring import score_lead      

# --- basic page setup -------------------------------------------------
st.set_page_config(page_title="LeadRankerAI", page_icon="🦄")
st.title("LeadRankerAI – AI‑powered Lead Scoring")

# --- upload step ------------------------------------------------------
uploaded = st.file_uploader("Upload a leads CSV", type="csv")

if uploaded:
    # Read the CSV the user uploaded
    df = pd.read_csv(uploaded)
    st.write("### Raw data", df.head())

    # --- apply scoring ------------------------------------------------
    df["Lead Score"] = df.apply(
        lambda r: score_lead(
            r.get("Title", ""),
            r.get("Industry", ""),
            r.get("Website", ""),
            r.get("Company", ""),
        ),
        axis=1,
    )

    st.write("### Scored leads", df.sort_values("Lead Score", ascending=False))

    # --- download button ---------------------------------------------
    st.download_button(
        label="Download scored CSV",
        data=df.to_csv(index=False),
        file_name="scored_leads.csv",
        mime="text/csv",
    )
else:
    st.info("👆 Upload a CSV to get started")

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page config
st.set_page_config(page_title="AI Fashion Insights", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-font {font-size:24px !important; font-weight: bold; text-align: center;}
        .highlight {color: #8A2BE2; font-weight: bold;}
        .report-download {text-align: center;}
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🚀 Revolutionizing Fashion with AI")
st.subheader("AI-powered insights for smarter, more sustainable business decisions.")

# Simulated AI-powered trend data
data = {
    "Trend": ["Minimalist Aesthetic", "Techwear", "Y2K Revival", "Sustainable Fashion", "AI-Generated Designs"],
    "Search Volume (Past Month)": [15000, 18000, 21000, 25000, 19000],
    "Predicted Growth (%)": [12, 15, 18, 22, 30],
    "Sustainability Score": [80, 65, 70, 95, 50]
}
df = pd.DataFrame(data)

# Interactive Visualization
fig = px.bar(df, x="Trend", y="Predicted Growth (%)", color="Sustainability Score", 
             title="📈 AI-Powered Fashion Trends Forecast", text_auto=True, 
             color_continuous_scale="Purples")

st.plotly_chart(fig, use_container_width=True)

# AI Insights Section
st.markdown("<p class='big-font'>🔍 AI-Powered Fashion Insights</p>", unsafe_allow_html=True)
st.write("Our AI analyzes global fashion data to provide insights on emerging trends, consumer preferences, and sustainability impact. Use this tool to make data-driven inventory decisions and stay ahead of the competition.")

# User Input for Custom AI Trend Report
st.markdown("<p class='big-font'>📝 Generate Your Custom AI Trend Report</p>", unsafe_allow_html=True)
selected_trends = st.multiselect("Select Trends to Include:", df["Trend"].tolist(), default=["Sustainable Fashion"])
if st.button("Generate Report"):
    report_df = df[df["Trend"].isin(selected_trends)]
    st.write(report_df)
    csv = report_df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Report", data=csv, file_name="AI_Fashion_Report.csv", mime='text/csv')

# CTA Section
st.markdown("<p class='big-font highlight'>📊 Get Real-Time AI Trend Insights</p>", unsafe_allow_html=True)
st.write("Integrate AI-powered analytics into your fashion business to reduce waste, optimize inventory, and predict future consumer behavior.")
st.markdown("[🔮 Learn More](https://fashtech.godaddysites.com)")

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16866904672"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-16866904672');
</script>
""", unsafe_allow_html=True)
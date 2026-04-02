import streamlit as st

st.title("📄 Download Report")

try:
    from reportlab.platypus import SimpleDocTemplate, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import letter

    def generate_pdf():
        doc = SimpleDocTemplate("h1b_report.pdf", pagesize=letter)
        styles = getSampleStyleSheet()

        content = []
        content.append(Paragraph("H1B Visa Analysis Report", styles["Title"]))
        content.append(Paragraph("Insights and Processing Time Summary", styles["Normal"]))

        doc.build(content)

        with open("h1b_report.pdf", "rb") as f:
            return f.read()

    if st.button("Generate Report"):
        pdf = generate_pdf()
        st.download_button(
            label="Download PDF",
            data=pdf,
            file_name="h1b_report.pdf",
            mime="application/pdf"
        )

except ModuleNotFoundError:
    st.error("⚠️ Report generation module not installed. Please check requirements.txt")

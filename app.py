import streamlit as st
from PIL import Image
from modules.logbook_module import extract_logbook_data, cross_check_logbook
from modules.certs_module import verify_cert
from modules.nlp_module import score_technical_response

st.set_page_config(page_title="Safaricom ESP Onboarding", layout="wide")

st.title("🚦 Safaricom ESP Onboarding Prototype (Staged Flow)")

# ✅ Initialize state
if 'stage' not in st.session_state:
    st.session_state['stage'] = 'Technical Response'

if 'scores' not in st.session_state:
    st.session_state['scores'] = {}

# ✅ Show progress
st.info(f"**Current Stage:** {st.session_state['stage']}")

# ✅ Stage 1: Technical Response Scoring
if st.session_state['stage'] == 'Technical Response':
    st.header("1️⃣ Technical Response Scoring")
    text = st.text_area("Paste vendor technical response here")
    if text:
        scores = score_technical_response(text)
        st.write("AI NLP Scores:", scores)
        st.session_state['scores']['technical'] = scores
        if st.button("✅ Mark Technical Response Complete"):
            st.session_state['stage'] = 'Certifications'

# ✅ Stage 2: Certifications Verification
elif st.session_state['stage'] == 'Certifications':
    st.header("2️⃣ Certifications Verification")
    cert_id = st.text_input("Enter Certification ID to Verify")
    if cert_id:
        valid, msg = verify_cert(cert_id)
        st.write(f"Status: {msg}")
        st.session_state['scores']['certification'] = msg
        if st.button("✅ Mark Certifications Complete"):
            st.session_state['stage'] = 'Logbook'

# ✅ Stage 3: Logbook Verification
elif st.session_state['stage'] == 'Logbook':
    st.header("3️⃣ Vehicle Logbook Verification")
    uploaded = st.file_uploader("Upload Vehicle Logbook Image", type=["jpg", "png"])
    if uploaded:
        image = Image.open(uploaded)
        data = extract_logbook_data(image)
        st.write("Extracted Data:", data)
        valid = cross_check_logbook(data["vehicle_id"])
        st.session_state['scores']['logbook'] = f"Verified: {valid}"
        if valid:
            st.success("✅ Vehicle ID verified in registry.")
        else:
            st.error("❌ Vehicle ID not found in registry.")
        if st.button("✅ Mark Logbook Complete"):
            st.session_state['stage'] = 'Site Visit'

# ✅ Stage 4: Site Visit
elif st.session_state['stage'] == 'Site Visit':
    st.header("4️⃣ Site Visit Evidence Review")
    st.info("Upload site visit images/videos or fill checklist here (prototype placeholder).")
    # You can extend this with file_uploader for videos, forms, checkboxes, etc.
    site_notes = st.text_area("Notes from Site Visit")
    st.session_state['scores']['site_visit'] = site_notes
    if st.button("✅ Mark Site Visit Complete"):
        st.session_state['stage'] = 'Review'

# ✅ Final Review Stage
elif st.session_state['stage'] == 'Review':
    st.header("✅ Final Review & Score")
    st.subheader("All Stage Scores & Notes")
    st.json(st.session_state['scores'])

    final_score = st.slider("Set Final Vendor Score", 0, 100, 80)
    st.session_state['scores']['final'] = final_score

    evaluator_comments = st.text_area("Evaluator Comments")

    if st.button("✅ Submit Final Score & Complete Onboarding"):
        st.success("🎉 Vendor onboarding process marked complete!")
        st.write("✅ Final Score:", final_score)
        st.write("Evaluator Comments:", evaluator_comments)
        st.session_state['stage'] = 'Complete'

# ✅ Done stage (optional)
elif st.session_state['stage'] == 'Complete':
    st.header("🎉 Onboarding Complete")
    st.write("Vendor has been fully evaluated and scored.")
    st.write("All data saved in prototype session state.")
    st.json(st.session_state['scores'])

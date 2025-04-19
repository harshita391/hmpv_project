import streamlit as st

st.title("🦠 hMPV Symptom Detection Tool")

st.write("Answer the following to check if you may have hMPV.")

symptoms = {
    "Cough": st.checkbox("Cough"),
    "Fever": st.checkbox("Fever"),
    "Runny Nose": st.checkbox("Runny Nose"),
    "Wheezing": st.checkbox("Wheezing"),
    "Shortness of Breath": st.checkbox("Shortness of Breath")
}

def detect_hmpv(symptom_dict):
    score = sum(symptom_dict.values())
    if score >= 3:
        return "🛑 Possible hMPV detected. Please consult a physician."
    elif score == 2:
        return "⚠️ Mild symptoms present. Monitor closely."
    else:
        return "✅ Unlikely to be hMPV. Stay safe!"

if st.button("Check Now"):
    result = detect_hmpv(symptoms)
    st.subheader(result)

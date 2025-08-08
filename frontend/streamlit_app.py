# frontend/streamlit_app.py

import os, json, requests, streamlit as st

API_URL = os.getenv("API_URL", "https://fraud-detection-api-27ae.onrender.com")

st.set_page_config(page_title="Fraud Detection", page_icon="🛡️")
st.title("🛡️ Fraud Detection — Demo UI")

st.sidebar.subheader("API")
api_url = st.sidebar.text_input("API base URL", API_URL)

sample = [
    -1.359, -0.072, 2.536, 1.378, -0.338, 0.462, 0.239, 0.099, 0.134, -0.021,
     0.206,  0.502, 0.219, -0.018,  0.215, 0.128, 0.098, 0.018, 0.277, 0.404,
     0.038,  0.039, 0.015, 0.015,  -0.005, 0.178, 0.507, 0.119, -0.066, 0.028
]

mode = st.radio("Input mode", ["Manual (30 fields)", "Paste comma-separated", "Raw JSON"])

def predict(features):
    try:
        r = requests.post(f"{api_url}/predict", json={"features": features}, timeout=15)
        r.raise_for_status()
        return r.json(), None
    except Exception as e:
        return None, str(e)

if mode == "Manual (30 fields)":
    cols = st.columns(3)
    vals = []
    for i in range(30):
        with cols[i % 3]:
            vals.append(st.number_input(f"Feature {i+1}", value=float(sample[i]), key=f"f{i}"))
    if st.button("Predict"):
        out, err = predict(vals)
        if err: st.error(err)
        else:
            st.success(f"Prediction: {out['is_fraud']} (class={out['prediction']})")
            st.metric("Fraud probability", f"{out['fraud_probability']:.4f}")

elif mode == "Paste comma-separated":
    txt = st.text_area("30 comma-separated numbers", value=",".join(map(str, sample)), height=120)
    if st.button("Predict"):
        try:
            arr = [float(x.strip()) for x in txt.split(",")]
        except Exception as e:
            st.error(f"Parse error: {e}"); st.stop()
        if len(arr) != 30:
            st.error(f"Got {len(arr)} values; need 30."); st.stop()
        out, err = predict(arr)
        if err: st.error(err)
        else:
            st.success(f"Prediction: {out['is_fraud']} (class={out['prediction']})")
            st.metric("Fraud probability", f"{out['fraud_probability']:.4f}")

else:
    default = json.dumps({"features": sample}, indent=2)
    raw = st.text_area("JSON payload", value=default, height=200)
    if st.button("Predict"):
        try:
            payload = json.loads(raw)
            feats = payload.get("features", [])
            assert isinstance(feats, list) and len(feats) == 30
        except Exception as e:
            st.error(f"Invalid JSON or wrong length: {e}"); st.stop()
        out, err = predict(feats)
        if err: st.error(err)
        else:
            st.success(f"Prediction: {out['is_fraud']} (class={out['prediction']})")
            st.metric("Fraud probability", f"{out['fraud_probability']:.4f}")

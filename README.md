# Verita Core Biometric ML Engine 🚀

[![Live Application](https://img.shields.io/badge/App-Streamlit-FF4B4B?style=for-the-badge)](https://verita-main.streamlit.app/)
[![Database](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge)](https://supabase.com/)
[![Documentation Gateway](https://img.shields.io/badge/Docs-Landing_Page-purple?style=for-the-badge)](https://verita-landing-page-rose.vercel.app)

Welcome to the backend engineering repository of **Verita**, a multi-modal biometric intelligence suite. This repository contains the complete production-grade data pipelines, mathematical distance thresholds, and neural feature extraction routines for both computer vision and digital signal processing verification channels.

---

## 🧠 Machine Learning Engine Specifications

### 📸 1. Facial Deep-Metric Pipeline
* **Localization & Alignment:** Uses directional gradient patterns (`HOG` models) paired with linear transformers to compute 68-point facial landmark matrices.
* **Vector Projection:** Passes localized crops into a deep residual network architecture (`ResNet-34`) to output static **128-dimensional vector space arrays**.
* **Classification Matrix:** Processes concurrent verification checks using vectorized Euclidean distance computations against registration arrays stored in database cache blocks.

### 🎙️ 2. Audio Processing & Speaker Identification
* **Feature Extraction:** Captures physical vocal tracts by converting raw acoustic waveforms into Mel-Frequency Cepstral Coefficients (`MFCCs`) using high-pass filters and Hanning window functions via `Librosa`.
* **Deep Embeddings:** Utilizes `Resemblyzer`'s pre-trained LSTM network structures to transform variable-length audio input streams into standard, low-variance speaker-discriminative vector clusters.
* **Verification Function:** Measures confidence thresholds sequentially by evaluating the **Cosine Similarity** vector orientation between the runtime challenge phrase and historical records.

---

## 📁 Repository Map

```text
├── src/
│   ├── modules/
│   │   ├── vision_pipeline.py  # Dlib facial coordinate alignment & inference
│   │   └── audio_pipeline.py   # Librosa feature arrays & voice embedding maps
│   └── database/
│       └── client.py           # Supabase connection pools & thread-safe commits
├── app.py                      # Main Streamlit reactive application engine
├── requirements.txt            # Explicit ML architecture requirements
└── verita_logo.png             # Hexagonal branding asset

```

🛠️ Installation & Architectural Deployment
System Prerequisites
To successfully compile the low-level numerical C++ structures required by the vision engine, ensure your system tools are configured:

Linux/Ubuntu: sudo apt-get install build-essential cmake libopenblas-dev liblapack-dev

MacOS: brew install cmake pkg-config

Windows: Visual Studio Build Tools containing desktop C++ compilers.

Execution Instructions
Clone and Navigate:

Bash
git clone [https://github.com/sumitstat07/verita-main.git](https://github.com/sumitstat07/verita-main.git)
cd verita-main
Initialize Environment Variables (.env):
Create a secret file in the root directory to authorize remote cloud transactions:

Code snippet
SUPABASE_URL="your-supabase-project-endpoint"
SUPABASE_KEY="your-supabase-service-role-token"
Install Core Libraries & Launch:

Bash
pip install -r requirements.txt
streamlit run app.py
📈 Scalability and Production Optimizations
Memory Management: Implements Streamlit memory caching decorator functions (@st.cache_resource) to hold spatial weight frameworks in system RAM rather than re-instantiating heavy layers upon user re-renders.

Thread Safety: Database input/output routines are structurally decoupled from UI calculations to keep verification workflows running asynchronously without thread contention.



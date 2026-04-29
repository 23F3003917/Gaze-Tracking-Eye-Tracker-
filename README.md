# 👁️ Gaze Tracking Eye Tracker

A real-time gaze tracking system that detects facial landmarks and estimates eye gaze direction using computer vision techniques. This project leverages classical ML and pretrained models (OpenFace) to track eye movement and visualize gaze behavior.

---

## 🚀 Features

* Real-time face detection and tracking
* Eye landmark detection using pretrained models
* Gaze direction estimation
* Visualization of gaze vectors
* Works on webcam input (live feed)
* Modular pipeline for experimentation and extension

---

## 🧠 Methodology

The system follows a multi-stage pipeline:

1. **Face Detection**
   Detect faces in each frame using a pretrained detector.

2. **Facial Landmark Detection**
   Extract key facial points (eyes, nose, etc.) using OpenFace models.

3. **Eye Region Extraction**
   Isolate eye regions from detected landmarks.

4. **Gaze Estimation**
   Compute gaze direction based on eye geometry and pupil positioning.

5. **Visualization**
   Overlay gaze vectors and landmarks on video frames.

---

## 🏗️ Project Structure

```
Gaze-Tracking-Eye-Tracker/
│── bin/                     # (Ignored) OpenFace binaries & models
│── build/                   # (Ignored) Build files
│── realtime_gaze.py         # Real-time gaze tracking script
│── visualize_gaze.py        # Visualization utilities
│── read_openface.py         # OpenFace integration
│── try.py                   # Experimental/testing script
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/23F3003917/Gaze-Tracking-Eye-Tracker-.git
cd Gaze-Tracking-Eye-Tracker-
```

---

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Model Files (Important)

This project uses pretrained OpenFace model files which are **not included in the repository** due to size constraints.

👉 Download them from: OpenFace Pretrained Models (Face Landmark & Gaze Estimation Models)

After downloading, place them in:

```
bin/model/
```

---

## ▶️ Usage

Run real-time gaze tracking:

./bin/FeatureExtraction -device 0 -gaze -vis-track -vis-aus

---

## 🖥️ Output

* Webcam feed with:

  * Facial landmarks
  * Eye tracking
  * Gaze direction visualization

---

## 📊 Applications

* Human-computer interaction (HCI)
* Attention tracking systems
* Assistive technologies
* Behavioral analysis
* Research in computer vision

---

## ⚠️ Limitations

* Performance depends on lighting conditions
* Accuracy varies with camera quality
* Requires pretrained OpenFace models

---

## 🔮 Future Improvements

* Deep learning-based gaze estimation
* Calibration for higher accuracy
* Multi-person tracking
* Web-based deployment
* Integration with ML models for attention scoring

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is for academic and research purposes.

---

## 👨‍💻 Author

**Anirudh Singh Tomar**
B.Tech CSE | Computer Vision & ML Enthusiast

---

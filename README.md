# MaestroNet with Beat Coherence Evaluator

This version integrates PantoMatrix's BeatCoherence metric to assess alignment between conducting gestures and reference audio.

## Setup

```bash
git submodule add https://github.com/PantoMatrix/PantoMatrix.git third_party/PantoMatrix
cd third_party/PantoMatrix
pip install -r requirements.txt
cd ../..

pip install -r requirements.txt
```

## Usage

```bash
streamlit run app/main.py
```

Upload a conducting video and a reference audio (WAV). The app displays:
- BPM
- Dynamics level
- Beat Coherence score (lower is better)


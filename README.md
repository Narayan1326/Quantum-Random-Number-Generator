# ⚛️ Quantum Random Number Generator using Single Qubit Measurements

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Qiskit](https://img.shields.io/badge/Qiskit-Latest-purple.svg)](https://qiskit.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Quantum%20Simulator-lightblue.svg)]()

A **Quantum Random Number Generator (QRNG)** built using **single-qubit measurements** to generate true randomness based on quantum mechanics.  
This project demonstrates how measuring a qubit in superposition can produce **genuine unpredictable results**, unlike classical pseudo-random generators.

---

## 🚀 Features

- 🧩 **Single-Qubit Quantum Measurements** — Generates randomness through quantum superposition and collapse.  
- ⚛️ **Hadamard Gate Application** — Prepares qubits in a perfect 50–50 superposition.  
- 🔢 **Multiple Output Formats** — Binary, decimal, and hexadecimal random numbers.  
- 📊 **Visualization** — Plot histograms of measurement outcomes and view Bloch sphere representations.  
- 💾 **Data Export** — Save generated random sequences to text or CSV files.  
- 🔍 **Comparison Mode** — Compare quantum randomness with Python’s pseudo-random module.  
- 🧠 **Extensible Design** — Modular code for integration with real IBM Quantum hardware.  

---

## 🏗️ Architecture

- **Language**: Python 3.8+
- **Quantum SDK**: Qiskit
- **Visualization**: Matplotlib, Plotly (optional)
- **Interface (optional)**: Streamlit or Tkinter GUI
- **Storage**: Local file-based storage for random outputs

---

## 📋 Prerequisites

- Python 3.8 or above
- pip (Python package manager)
- Internet connection (for Qiskit installation)
- IBM Quantum account (optional, for real hardware execution)

---

## 🛠️ Installation

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/quantum-rng.git
   cd quantum-rng
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Web Interface 

**Launch the interactive Streamlit web application :**

```bash
streamlit run scripts/streamlit_app.py
```

- On Windows, if the above doesn't work :
  ```bash
  python -m streamlit run scripts/streamlit_app.py
  ```

- Then open your browser to `http://localhost:8501`

📁 Project Structure

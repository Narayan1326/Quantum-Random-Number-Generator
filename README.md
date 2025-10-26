# Quantum Random Number Generator (QRNG)

A production-ready Python application for generating true random numbers using quantum mechanics principles and IBM's Qiskit framework.

## Overview

This project implements a single-qubit quantum random number generator that leverages quantum superposition and measurement to produce cryptographically-secure random numbers. Unlike classical pseudo-random generators, quantum randomness is based on fundamental quantum mechanics principles and cannot be predicted.

## Features

- **True Quantum Randomness**: Uses single-qubit measurements with Hadamard gates
- **Multiple Output Formats**: Binary, decimal, hexadecimal, and float representations
- **Statistical Analysis**: Shannon entropy, chi-square test, runs test
- **Comprehensive Visualizations**: Histograms, Bloch sphere, entropy analysis, bit sequences
- **Web Interface**: Interactive Streamlit application for easy access
- **CLI Tools**: Command-line interface for batch processing
- **Quality Metrics**: Randomness quality assessment and comparison with classical randomness

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
\`\`\`bash
git clone <repository-url>
cd quantum-rng
\`\`\`

2. Create a virtual environment (recommended):
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
\`\`\`

### Windows-Specific Setup

If you encounter build errors on Windows, follow these steps:

1. **Upgrade pip and build tools**:
\`\`\`powershell
python -m pip install --upgrade pip setuptools wheel
\`\`\`

2. **Install with pre-built wheels only** (recommended):
\`\`\`powershell
pip install --only-binary :all: -r requirements.txt
\`\`\`

3. **If the above fails, try installing packages individually**:
\`\`\`powershell
pip install qiskit qiskit-aer streamlit matplotlib numpy scipy
\`\`\`

4. **Alternative: Use Python 3.11 or 3.12** for better wheel availability:
\`\`\`powershell
python --version  # Check your current version
# If using older Python, consider upgrading to 3.11 or 3.12
\`\`\`

### Troubleshooting

**Error: "Cannot import 'setuptools.build_meta'"**
- Solution: Run `pip install --upgrade setuptools wheel` before installing requirements

**Error: "No module named 'qiskit'"**
- Solution: Ensure the virtual environment is activated and run `pip install qiskit qiskit-aer`

**Streamlit command not found**
- Solution: Ensure streamlit is installed: `pip install streamlit`
- On Windows, you may need to use: `python -m streamlit run scripts/streamlit_app.py`

## Usage

### Web Interface (Recommended)

Launch the interactive Streamlit web application:

\`\`\`bash
streamlit run scripts/streamlit_app.py
\`\`\`

On Windows, if the above doesn't work:
\`\`\`powershell
python -m streamlit run scripts/streamlit_app.py
\`\`\`

Then open your browser to `http://localhost:8501`

**Features:**
- Generate quantum random numbers with configurable parameters
- Run randomness quality tests
- View interactive visualizations
- Compare quantum vs classical randomness
- Download results in multiple formats

### Command-Line Interface

#### Generate Random Numbers
\`\`\`bash
python scripts/main.py generate --count 1024
\`\`\`

Options:
- `--count`: Number of measurements (default: 1024)
- `--seed`: Random seed for reproducibility
- `--save`: Save measurements to JSON file
- `--binary`: Save as binary file
- `--hex`: Save as hexadecimal file

Example:
\`\`\`bash
python scripts/main.py generate --count 256 --save results.json --binary random.bin
\`\`\`

#### Analyze Randomness Quality
\`\`\`bash
python scripts/main.py analyze --count 2048
\`\`\`

Runs statistical tests:
- Chi-square test
- Runs test
- Shannon entropy analysis

#### Generate Visualizations
\`\`\`bash
python scripts/main.py visualize --count 1024 --output qrng
\`\`\`

Creates four visualization files:
- `qrng_histogram.png`: Measurement frequency distribution
- `qrng_bloch.png`: Bloch sphere representation
- `qrng_stats.png`: Statistical analysis
- `qrng_sequence.png`: Bit sequence analysis

#### Compare Quantum vs Classical
\`\`\`bash
python scripts/main.py compare --count 512
\`\`\`

Compares quantum randomness with Python's classical random module.

### Python API

Use the QRNG in your own Python code:

\`\`\`python
from scripts.quantum_core import QuantumRandomNumberGenerator
from scripts.visualizer import QuantumVisualizer
from scripts.utils import RandomnessTests

# Initialize QRNG
qrng = QuantumRandomNumberGenerator(seed=42)

# Generate random bits
measurements = qrng.generate_random_bits(num_measurements=1024)

# Get statistics
stats = qrng.get_statistics()
print(f"Entropy Ratio: {stats['entropy_ratio']:.4f}")

# Convert to different formats
binary = qrng.to_binary_string()
decimal = qrng.to_decimal()
hexadecimal = qrng.to_hex()
float_value = qrng.to_float()

# Run quality tests
chi_square = RandomnessTests.chi_square_test(measurements)
runs = RandomnessTests.runs_test(measurements)
entropy = RandomnessTests.entropy_test(measurements)

# Create visualizations
QuantumVisualizer.plot_measurement_histogram(measurements, save_path="histogram.png")
QuantumVisualizer.plot_bloch_sphere(save_path="bloch.png")
QuantumVisualizer.plot_statistics(stats, save_path="stats.png")
\`\`\`

## Project Structure

\`\`\`
quantum-rng/
├── scripts/
│   ├── quantum_core.py          # Core quantum logic
│   ├── visualizer.py            # Visualization functions
│   ├── utils.py                 # Utilities and tests
│   ├── main.py                  # CLI interface
│   └── streamlit_app.py         # Web interface
├── requirements.txt             # Python dependencies
└── README.md                    # This file
\`\`\`

## How It Works

### Quantum Mechanics Principles

1. **Qubit Initialization**: A single qubit is initialized in the |0⟩ state
2. **Hadamard Gate**: Applied to create superposition: (|0⟩ + |1⟩) / √2
3. **Measurement**: Collapses the qubit to either |0⟩ or |1⟩ with 50% probability each
4. **Repetition**: Process repeated to generate multiple random bits

### Why Quantum Randomness?

- **True Randomness**: Based on quantum mechanics, not algorithms
- **Unpredictable**: Cannot be predicted even with perfect knowledge
- **Uniform Distribution**: Theoretically produces perfectly uniform bits
- **Cryptographic Quality**: Suitable for security-critical applications

## Statistical Tests

### Chi-Square Test
Tests if the observed distribution matches the expected 50/50 distribution.
- **Null Hypothesis**: Data is uniformly distributed
- **Significance Level**: 0.05
- **Pass Criteria**: p-value > 0.05

### Runs Test
Detects clustering or patterns in the sequence.
- **Null Hypothesis**: Bits are randomly distributed
- **Measures**: Number of runs (consecutive identical values)
- **Pass Criteria**: p-value > 0.05

### Shannon Entropy
Measures information content and uniformity.
- **Formula**: H = -Σ(p_i * log2(p_i))
- **Maximum**: 1.0 (perfect randomness)
- **Quality Threshold**: > 0.95 (excellent), > 0.85 (good)

## Performance

- **Generation Speed**: ~1000 bits per second (depends on system)
- **Memory Usage**: Minimal (stores measurements in memory)
- **Scalability**: Can generate up to 10,000+ bits per run

## Limitations

- Requires Qiskit simulator (no real quantum hardware needed)
- Limited to single-qubit measurements
- Quantum simulator is deterministic (use seed for reproducibility)

## Future Enhancements

- Multi-qubit entanglement for higher randomness quality
- Real quantum hardware integration (IBM Quantum)
- Advanced statistical tests (NIST test suite)
- GPU acceleration for large-scale generation
- REST API for remote access

## References

- [Qiskit Documentation](https://qiskit.org/)
- [Quantum Computing Basics](https://en.wikipedia.org/wiki/Quantum_computing)
- [Random Number Generation](https://en.wikipedia.org/wiki/Random_number_generation)
- [NIST Randomness Tests](https://csrc.nist.gov/projects/random-bit-generation/)

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Created with quantum mechanics and Python** ⚛️

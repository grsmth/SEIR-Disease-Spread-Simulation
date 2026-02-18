# SEIR Model Simulation (Python)

## Description

This repository contains a simple Python implementation of the **SEIR (Susceptible–Exposed–Infectious–Recovered)** epidemiological model.  
It simulates the spread of an infectious disease with an incubation period and visualizes the evolution of the population over time.

The project is intended for educational and research purposes.

---

## Model Overview

The population is divided into four compartments:

- **S (Susceptible)**
- **E (Exposed)**
- **I (Infectious)**
- **R (Recovered)**

Flow of the model:
S → E → I → R

---

## Requirements

- Python 3.8+
- NumPy
- Matplotlib
- SciPy

Install dependencies:

```bash 

pip install numpy matplotlib scipy
```
How to Run

Clone the repository and run:
```bash 
git clone https://github.com/grsmth/SEIR-Disease-Spread-Simulation.git
cd SEIR-Disease-Spread-Simulation
python main.py
```
Parameters

You can adjust the model parameters in the script:
- beta = 0.4
- sigma = 1/5.2
- gamma = 1/7
- N = 1000000

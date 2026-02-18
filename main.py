import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SEIR
def seir(y, t, beta, sigma, gamma, N):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

# Parâmetros
N = 15000000        # população total
beta = 0.40         # taxa de transmissão
sigma = 1/5.2      # incubação média ~5,2 dias
gamma = 1/7        # recuperação média ~7 dias

# Condições iniciais
I0 = 10
E0 = 20
R0 = 0
S0 = N - I0 - E0 - R0
y0 = [S0, E0, I0, R0]

# Tempo da simulação
t = np.linspace(0, 200, 200)

# Solução
resultado = odeint(seir, y0, t, args=(beta, sigma, gamma, N))
S, E, I, R = resultado.T

# Plot
plt.figure(figsize=(10,6))
plt.plot(t, S, label="Susceptíveis")
plt.plot(t, E, label="Expostos")
plt.plot(t, I, label="Infectados")
plt.plot(t, R, label="Recuperados")
plt.xlabel("Dias")
plt.ylabel("Número de indivíduos")
plt.title("Modelo SEIR — Simulação")
plt.legend()
plt.grid()
plt.show()

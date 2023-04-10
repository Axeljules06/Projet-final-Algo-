import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sys_m_r_a(X,T,M,A,K,F):
    """
    m_r_a : masse-ressort-amortisseur 
    Fonction décrivant le système masse-ressort-amortisseur.
    Args:
        X (array): Vecteur d'état [en fonction de la position et de la vitesse].
        T(float): le Temps.
        M (float): la Masse.
        A (float): le Coefficient de frottement de l'amortisseur.
        K (float): la Constante de raideur du ressort.
        F (float): la Force extérieure.
    Returns:
        dX/dT (array): la Dérivée du vecteur d'état [en fonction de la position et de la vitesse].
    """
    dXdT = np.zeros_like(X)
    dXdT[0] = X[1]
    dXdT[1] = (F(T) - A * X[1] - K * X[0]) / M
    return dXdT


M = 10.0 
A = 20.0
K = 4000.0 
X0 = 0.01 
V0 = 0.0

F0 = 100.0 
w = 10.0 
def  F_ext(T):
    return F0 * np.cos(w * T) 



T_start = 0.0 
T_end = 10.0 
dT = 0.01 



X_init = np.array([X0, V0])


T_A = np.arange(T_start, T_end, dT)
X_A = odeint(sys_m_r_a, X_init, T_A, args=(M, A, K, lambda T: 0.0))


T_B= np.arange(T_start, T_end, dT)
X_B = odeint(sys_m_r_a, X_init, T_B, args=(M, A, K, F_ext))


plt.figure()
plt.subplot(2, 1, 1) 
plt.plot(T_A, X_A[:, 0], label ='Position (m)')
plt.plot(T_A, X_A[:, 1], label ='Vitesse (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position, Vitese')
plt.legend()
plt.title('Réponse du système masse-ressort-amortisseur (Cas a)')
plt.subplot(2, 1, 2)
plt.plot(T_B, X_B[:, 0], label ='Position (m)')
plt.plot(T_B, X_B[:, 1], label ='Vitesse (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position, Vitese')
plt.legend()
plt.title('Réponse du système masse-ressort-amortisseur (Cas b)')
plt.show()



Energie_cinetique_A = 0.5 * M * X_A[:, 1]**2
Energie_potentielle_A = 0.5 * K * X_A[:, 0]**2
Energie_mecanique_A = Energie_cinetique_A + Energie_potentielle_A



plt.figure()
plt.plot(T_A, Energie_cinetique_A, label='Energie cinétique')
plt.plot(T_A, Energie_potentielle_A, label='Energie potentielle')
plt.plot(T_A, Energie_mecanique_A, label='Energie mécanique')
plt.xlabel('Temps (s)')
plt.ylabel('Energie cinetique, Energie potentielle et Energie mecanique(J)')
plt.legend()
plt.title('Energie cinetique, Energie potentielle et Energie mecanique à tout instant')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Constantes physiques
G = 6.67430e-11  # Constante gravitationnelle
M_terre = 5.972e24  # Masse de la Terre
R_terre = 6.371e6  # Rayon de la Terre
Altitude_orbite = 300e3  # Altitude de l'orbite


# Simulation du lancement de la navette spatiale avec des matrices de rotation
def simulate_launch(initial_velocity, launch_angle):
    # Convertir l'angle de lancement en radians
    launch_angle_rad = np.radians(launch_angle)

    # Initialiser les conditions initiales
    x, y, z = 0, R_terre + Altitude_orbite, 0
    vx = initial_velocity * np.sin(launch_angle_rad)
    vy = 0
    vz = initial_velocity * np.cos(launch_angle_rad)

    # Matrice de rotation initiale
    rotation_matrix = np.eye(3)

    # Paramètres de simulation
    dt = 1  # Intervalle de temps en secondes
    total_time = 600  # Durée totale de la simulation en secondes

    # Stockage des positions pour la visualisation
    x_values, y_values, z_values = [x], [y], [z]

    # Simulation de la trajectoire
    while total_time > 0:
        # Calcul des forces gravitationnelles
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        force_gravity = -G * M_terre / r ** 2
        acc_x = (force_gravity / M_terre) * (x / r)
        acc_y = (force_gravity / M_terre) * (y / r)
        acc_z = (force_gravity / M_terre) * (z / r)

        # Mise à jour des vitesses et positions
        vx += acc_x * dt
        vy += acc_y * dt
        vz += acc_z * dt
        x += vx * dt
        y += vy * dt
        z += vz * dt

        # Rotation de la matrice pour simuler l'orientation changeante
        rotation_angle = 0.01  # Angle de rotation arbitraire pour chaque itération
        rotation_matrix = np.dot(rotation_matrix,
                                 np.array([[np.cos(rotation_angle), -np.sin(rotation_angle), 0],
                                           [np.sin(rotation_angle), np.cos(rotation_angle), 0],
                                           [0, 0, 1]]))

        # Appliquer la rotation à la vitesse
        velocity_vector = np.dot(rotation_matrix, np.array([vx, vy, vz]))

        # Stockage des positions pour la visualisation
        x_values.append(x)
        y_values.append(y)
        z_values.append(z)

        total_time -= dt

    return x_values, y_values, z_values


# Paramètres du lancement
initial_velocity = 7000  # Vitesse initiale
launch_angle = 45  # Angle de lancement

# Simulation du lancement
x_values, y_values, z_values = simulate_launch(initial_velocity, launch_angle)

# Visualisation en 3D de la trajectoire
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, label='Trajectoire de la Navette')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Simulation du Lancement de la Navette Spatiale')
ax.legend()
plt.show()

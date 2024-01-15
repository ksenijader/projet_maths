import numpy as np
import matplotlib.pyplot as plt


#Simulation  d'une trajectoire de navette spatiale
def generer_trajectoire(n_points):
    # Paramètres de la trajectoire
    vitesse = 1.0  # vitesse constante
    changement_orientation = np.pi / 4  # changement d'orientation en radians

    # Génération de la trajectoire
    trajectoire = np.zeros((n_points, 3))

    for i in range(1, n_points):
        # Mouvement rectiligne uniforme
        trajectoire[i] = trajectoire[i - 1] + vitesse * np.array([1, 0, 0])

        # Changement d'orientation
        rotation_matrix = np.array([[np.cos(changement_orientation), -np.sin(changement_orientation), 0],
                                    [np.sin(changement_orientation), np.cos(changement_orientation), 0],
                                    [0, 0, 1]])

        trajectoire[i] = np.dot(rotation_matrix, trajectoire[i])

    return trajectoire

# Générer la trajectoire
points_trajectoire = generer_trajectoire(100)

# Afficher la trajectoire en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(points_trajectoire[:, 0], points_trajectoire[:, 1], points_trajectoire[:, 2], 'b-')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trajectoire de la navette spatiale')
plt.show()

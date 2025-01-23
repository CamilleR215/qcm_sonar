from  .fractal import Mandelbrot, Julia
import numpy as np
import matplotlib.pyplot as plt

def plot_mandelbrot(zmin=-2-2j, zmax=2+2j, pixel_size=5e-3, max_iter=100, figname="Mandelbrot.png"):
    """
    Génère et sauvegarde un graphique de l'ensemble de Mandelbrot
    
    Parameters
    ----------
    zmin : complex, optional
        valeur complexe du point extrème en bas à gauche du graphique
    zmax : complex, optional
        valeur complexe du point extrème en haut à droite du graphique
    pixel_size : float, optional
        taille d'un pixel
    max_iter : int, optional
        nombre d'itérations pour la vérification de l'appartenance à l'ensemble de Mandelbrot
    figname : str, optional
        nom sous lequel sauvegarder la figure
    """
    mandelbrot_n_iter = Mandelbrot(max_iter)
    liste_x = np.arange(zmin.real, zmax.real, pixel_size)
    liste_y = np.arange(zmin.imag, zmax.imag, pixel_size)
    X, Y = np.meshgrid(liste_x, liste_y) #On crée les valeurs de c pour chaque point de l'image
    c_array = X + 1j * Y
    image = mandelbrot_n_iter.is_in_ensemble(c_array)
    plt.figure(figsize = (16, 6))
    plt.imshow(image, cmap='gray_r', extent=(liste_x[0], liste_x[-1], liste_y[0], liste_y[-1]))
    plt.xlabel("Partie Réelle")
    plt.ylabel("Partie Imaginaire")
    plt.title(f"Réprésentation de l'ensemble de Mandelbrot avec max_iter = {max_iter}")
    plt.savefig(figname, format ='png')



def plot_julia(c = 0.5, zmin=-2-2j, zmax=2+2j, pixel_size=5e-4, max_iter=200, figname="Julia.png"):
    """
    Génère et sauvegarde un graphique de l'ensemble de Julia
    
    Parameters
    ----------
    c : complex, optional
        paramètre de l'ensemble de Julia
    zmin : complex, optional
        valeur complexe du point extrème en bas à gauche du graphique
    zmax : complex, optional
        valeur complexe du point extrème en haut à droite du graphique
    pixel_size : float, optional
        taille d'un pixel
    max_iter : int, optional
        nombre d'itérations pour la vérification de l'appartenance à l'ensemble de Julia
    figname : str, optional
        nom sous lequel sauvegarder la figure
    """
    julia_n_iter_c = Julia(max_iter, c)
    liste_x = np.arange(zmin.real, zmax.real, pixel_size)
    liste_y = np.arange(zmin.imag, zmax.imag, pixel_size)
    X, Y = np.meshgrid(liste_x, liste_y)
    z_array = X + 1j * Y #On crée les valeurs de z_0 pour chaque point de l'image
    image = julia_n_iter_c.is_in_ensemble(z_array)
    plt.figure(figsize = (16, 6))
    plt.imshow(image, cmap='gray_r', extent=(liste_x[0], liste_x[-1], liste_y[0], liste_y[-1]))
    plt.xlabel("Partie Réelle")
    plt.ylabel("Partie Imaginaire")
    plt.title(f"Réprésentation de l'ensemble de Julia pour c = {c} et max_iter = {max_iter}")
    plt.savefig(figname, format ='png')

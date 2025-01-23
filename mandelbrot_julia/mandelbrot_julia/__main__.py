import argparse
from .utils import plot_mandelbrot, plot_julia

def main():
    """Fonction principale pour afficher l'ensemble de Julia"""
    parser = argparse.ArgumentParser(description="Affiche l'ensemble de Julia pour un nombre d'itération donné et une valeur de c donnée")
    parser.add_argument('--max-iter', metavar='max_iter', type=int, default=100,
                        help="Nombre maximum d'itération pour le calcul de la suite (par défaut: 100)")
    parser.add_argument('--parametre_c', '-c', metavar='c', type=complex, default=-0.3j,
                        help="Paramètre c dans le calcul de la suite (par défaut: -0.3j)") 
    parser.add_argument('--zmin', metavar='z_min', type=complex, default=-2-2j,
                        help="Valeur complexe du point extrème en bas à gauche du graphique (par défaut: -2-2j)")
    parser.add_argument('--zmax', metavar='z_max', type=complex, default=2+2j,
                        help="Valeur complexe du point extrème en haut à droite du graphique (par défaut: 2+2j)")
    parser.add_argument('--pixel_size', metavar='pixel_size', type=float, default=5e-4,
                        help="Taille d'un pixel dans l'espace complexe (par défaut: 5e-4)")
    parser.add_argument('-o', metavar='o', type=str, default="Julia.png",
                        help="Nom sous lequel sauvegarder la figure (par défaut: Julia.png)")

    args = parser.parse_args()
    c = args.parametre_c
    zmin = args.zmin
    zmax = args.zmax
    pixel_size = args.pixel_size
    max_iter = args.max_iter
    figname = args.o

    plot_julia(c, zmin, zmax, pixel_size, max_iter, figname)
    
if __name__=="__main__":
    main()
import numpy as np
class Fractal():
    def __init__(self, n_iter : int):
        """
        Crée une instance de la classe fractale

        Parameters
        ----------
        n_iter : int
            vérification que les n_iter premiers éléments de la suite sont contenus dans le cercle complexe de rayon 2
        """
        self.n_iter = n_iter
    
    def suite(self, z, c)-> complex:
        """
        Générateur des éléments de la suite $z_{n+1}=z_n^2+c$

        Parameters
        ----------
        z : complex
            valeur initiale de la suite
        c : complex
            paramètre de la suite

        """
        while True:
            yield z
            z = z ** 2 + c

    def is_in_ensemble(self, z, c)-> bool:
        """
        Verifie si les self.n_iter premiers éléments de la suite sont contenus dans le cercle complexe de rayon 2, en se limitant à un nombre maximal d'itérations.

        Parameters 
        ----------
        z : complex or complex ndarray
            valeur(s) initiale(s) de la suite
        c : complex or complex ndarray
            paramètre(s) c de la suite z_n+1 = z_n**2 + c
        
        Return
        ------
        bool
            vrai si les self.n_iter premiers éléments de la suite sont contenus dans le cercle complexe de rayon 2, faux sinon

        """
        #On répète les valeurs z_n ou de c si nécessaire, pour obtenir des ndarrays de même forme
        z_n = np.full(c.shape, z, dtype=complex) if np.isscalar(z) else z.copy()
        c = np.full(z.shape, c, dtype = complex) if np.isscalar(c) else c
        #On crée un masque pour ne calculer que les valeurs de Z_n des points encore dans le cercle
        masque = np.full(z_n.shape, True, dtype=bool)
        for _ in range(self.n_iter):
            z_n[masque] = z_n[masque]**2+c[masque]
            #A chaque itération, on va recalculer le masque, 
            #il ne sera vrai que pour les couples (z0, c) qui vérifient: z_n < 2
            masque[masque] = np.abs(z_n[masque]) <= 2 
        return masque
        
class Mandelbrot(Fractal):
    def __init__(self, n_iter : int):
        """
        Crée une instance de la classe Mandelbrot

        Parameters
        ----------
        n_iter : int
            nombre d'itération du calcul de la suite pour vérifier que l'élément appartient à l'ensemble de Mandelbrot
        """
        super().__init__(n_iter)
    
    
    def is_in_ensemble(self, c)-> bool:
        """
        Verifie si le(s) élément(s) c est(sont) dans l'ensemble de Mandelbrot, en se limitant à un nombre maximal d'itérations = self.n_iter.
        
        Parameters 
        ----------
        c : complex or complex ndarray
            nombre(s) candidat(s) pour l'ensemble de Mandelbrot
        
        Return
        --------
        bool or bool ndarray
            vrai si les  self.n_iter premiers éléments sont contenus dans le cercle complexe de rayon 2, faux sinon
        
        Examples
        --------
        >>> mandelbrot_50 = Mandelbrot(50)
        >>> mandelbrot_100 = Mandelbrot(100)
        >>> c = 0.251
        >>> liste_x = [-1, -0.7, -0.3, 0, 0.3, 0.7, 1]
        >>> liste_y = [-1, -0.7, -0.3, 0, 0.3, 0.7, 1]
        >>> X, Y = np.meshgrid(liste_x, liste_y)
        >>> c_array = X +1j * Y
        >>> print(mandelbrot_50.is_in_ensemble(c), mandelbrot_100.is_in_ensemble(c), mandelbrot_100.is_in_ensemble(c_array))
        True False [[False False False  True False False False]
         [False False False False False False False]
         [False False  True  True  True False False]
         [ True  True  True  True False False False]
         [False False  True  True  True False False]
         [False False False False False False False]
         [False False False  True False False False]]
        """
        #On distingue les cas où on souhaite connaître le résultat pour une seule valeur de c, ou pour plusieurs
        if np.isscalar(c):
            return super().is_in_ensemble(0, np.array([c]))[0]
        return super().is_in_ensemble(0, c)
    

class Julia(Fractal):
    def __init__(self, n_iter : int, c : complex):
        """
        Crée une instance de la classe Julia

        Parameters
        ----------
        n_iter : int
            nombre d'itération du calcul de la suite pour vérifier que l'élément appartient à l'ensemble de Julia
        c : complex
            valeur du paramètre c dans le calcul de la suite : z_n+1 = z_n**2 + c
        """
        super().__init__(n_iter)
        self.c = c

    
    def is_in_ensemble(self, z)-> bool:
        """
        Verifie si le(s) élément(s) z est(sont) dans l'ensemble de Julia de paramètre c = self.c, en se limitant à un nombre maximal d'itérations = self.n_iter.
        
        Parameters
        ----------
        z : complex or complex ndarray
            Valeur(s) initiale(s) candidate(s) pour l'ensemble de Julia
        
        Return
        --------
        bool or bool ndarray
            vrai si les self.n_iter premiers éléments sont contenus dans le cercle complexe de rayon 2, faux sinon
        
        Examples
        --------
        >>> julia_100 = Julia(100, 0.25)
        >>> julia_200 = Julia(200, 0.25)
        >>> z = 0.25 + 0.25j
        >>> liste_x = [-1, -0.7, -0.3, 0, 0.3, 0.7, 1]
        >>> liste_y = [-1, -0.7, -0.3, 0, 0.3, 0.7, 1]
        >>> X, Y = np.meshgrid(liste_x, liste_y)
        >>> z_array = X +1j * Y
        >>> print(julia_200.is_in_ensemble(z), julia_100.is_in_ensemble(50), julia_100.is_in_ensemble(z_array))
        True False [[False False  True False  True False False]
         [False  True  True  True  True  True False]
         [False  True  True  True  True  True False]
         [False False  True  True  True False False]
         [False  True  True  True  True  True False]
         [False  True  True  True  True  True False]
         [False False  True False  True False False]]
        """
        #On distingue les cas où on souhaite connaître le résultat pour une seule valeur de z, ou pour plusieurs
        if np.isscalar(z):
            return super().is_in_ensemble(np.array([z]), self.c)[0]
        return super().is_in_ensemble(z, self.c)

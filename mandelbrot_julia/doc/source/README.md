# mandelbrot_julia

mandelbrot_julia est une librairie Python pour générer des représentations graphiques des ensembles de Mandelbrot et de Julia.

L'ensemble de Mandelbrot est constité des valeurs de c qui vérifient que la suite $z_{n+1} =  {z_n}^2 + c$ avec $z_0 = 0$ converge.

L'ensemble de Julia pour une valeur de c donnée est constité des valeurs de $z_0$ qui vérifient que la suite $z_{n+1} =  {z_n}^2 + c$ converge.

Pour évaluer cela, on testera un nombre maximum d'itérations de la suite $z_n$ et on vérifiera que toutes les valeurs obtenues sont inférieures ou égales à 2.

## Installation

Utiliser le gestionnaire de paquets [pip](https://pip.pypa.io/en/stable/) pour installer mandelbrot_julia

```bash
pip install mandelbrot_julia
```

## Usage
### Python
Depuis Python on peut utiliser
```python
import mandelbrot_julia
```
#### Tester si une valeur appartient à l'ensemble de Mandelbrot
```python
is_in_Mandelbrot(c, max_iter)
```
avec 
- c : valeur du paramètre candidat à l'ensemble de Mandelbrot
- max_iter : (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble
#### Génèrer et sauvegarder le graphique de l'ensemble de Mandelbrot

```python
plot_mandelbrot(zmin, zmax, pixel_size, max_iter, figname)
```
avec
- zmin (default : -2 -2j): valeur complexe du point en bas à gauche du graphique
- zmax (default : 2 + 2j): valeur complexe du point en haut à droite du graphique
- pixel_size (default : 5e-4): la taille d'un pixel
- max_iter (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble
- figname (default : "Mandelbrot.png"): le nom sous lequel sauvegarder la figure générée

#### Tester si une valeur appartient à l'ensemble de Julia
```python
is_in_Mandelbrot(z, c, max_iter)
```
avec 
- z : valeur initiale de la suite $z_{n+1} =  {z_n}^2 + c$ candidate à l'ensemble de Julia
- c : valeur du paramètre c dans la suite $z_{n+1} =  {z_n}^2 + c$
- max_iter : (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble

#### Génèrer et sauvegarder le graphique de l'ensemble de Julia
```Python
plot_julia(c, zmin, zmax, pixel_size, max_iter, figname)
```
pip install mandelbrot_julia
avec
- c (default : -0.8+0.156j) : la valeur du paramètre c dans la suite : $z_{n+1} =  {z_n}^2 + c$
- zmin (default : -2 -1j): valeur complexe du point en bas à gauche du graphique
- zmax (default : 2 + 1j): valeur complexe du point en haut à droite du graphique
- pixel_size (default : 5e-4): la taille d'un pixel
- max_iter (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble
- figname (default : "Julia.png"): le nom sous lequel sauvegarder la figure générée

### Terminal
On peut aussi directement appeler ces fonctions avec des lignes de commande:


```bash
-MandelbrotPlot --zmin=... --zmax=... --pixel_size=... --max-iter=... -o ...
```
avec :
- --zmin (default : -2 -2j): valeur complexe du point en bas à gauche du graphique
- --zmax (default : 2 + 2j): valeur complexe du point en haut à droite du graphique
- --pixel_size (default : 5e-4): la taille d'un pixel
- --max-iter (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble
- -o (default : "Mandelbrot.png"): le nom sous lequel sauvegarder la figure générée

```bash
-JuliaPlot -c=... --zmin=... --zmax=... --pixel_size=... --max-iter=... -o ...
```
avec :
- -c (default : -0.3j): la valeur du paramètre c dans la suite : $z_{n+1} =  {z_n}^2 + c$
- --zmin (default : -2 - 2j): valeur complexe du point en bas à gauche du graphique
- --zmax (default : 2 + 2j): valeur complexe du point en haut à droite du graphique
- --pixel_size (default : 5e-4): la taille d'un pixel
- --max-iter (default : 100): la valeur maximale d'itération de la suite pour trouver si un élément appartient à l'ensemble
- -o (default : "Julia.png"): le nom sous lequel sauvegarder la figure générée



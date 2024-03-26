import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''
    visina_slike, sirina_slike = slika.shape
    visina_jedra, sirina_jedra = jedro.shape
    pad_visina = visina_jedra // 2
    pad_sirina = sirina_jedra // 2
    
    pad_slika = np.pad(slika, ((pad_visina,pad_visina), (pad_sirina,pad_sirina)), mode='constant')
    
    nova_slika = np.zeros_like(slika)
    
    for y in range(visina_slike):
        for x in range(sirina_slike):
            nova_slika[y,x] = np.sum(pad_slika[y : y + visina_jedra, x : x + sirina_jedra] * jedro)
    
    return nova_slika

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    size = int(2 * sigma) * 2 + 1
    jedro = np.zeros((size,size), dtype=np.float32)
    k = size // 2 - 0.5
    for i in range(size):
        for j in range(size):
            jedro[i,j] = 1 / (2 * np.pi * sigma ** 2) * np.exp(-((i - k) ** 2 + (j - k) ** 2) / (2 * sigma ** 2))
    novo_jedro = jedro / np.sum(jedro)
    return konvolucija(slika, novo_jedro)
    
def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass

if __name__ == '__main__':    
    #učitamo našu testnu sliku
    pass
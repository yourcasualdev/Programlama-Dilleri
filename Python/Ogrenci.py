"""
Bu programda kullanıcıdan input('') fonksiyonu ile girdi almanıza gerek yoktur.
Hesaplama için gelen değerler argümanlardadır(n ve *args gibi)
"""


def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def asal(n):
    liste = []
    for i in range(2, n):
        if isPrime(i):
            liste.append(i)
    return liste


def mukemmel(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False


def asal_liste(*args):
    asallar = []
    for i in args:
        if isPrime(i):
            asallar.append(True)
        else:
            asallar.append(False)
    return asallar

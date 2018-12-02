# Lab 4 - Exercice 1
# Create a repeat function
# CCIS 1505-51 - Jerry Covington
# Student: Regis Kouatcho

def repeatFunction(f, n):
    for a in range(n):
        f()
def f():
    print('Hi')

repeatFunction(f, 10)
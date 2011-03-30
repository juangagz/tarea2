#!/usr/bin/env python
# -*- coding: utf-8 -*-
# primos.py: muestra los numeros primos hasta el numero que se pida

def es_primo(n):
	'''Devuelve un booleano indicando si el numero pasado como parametro es primo'''

	numero_primo = True	
	b = 2
	while (numero_primo) & (b < n):
		if (n % b == 0):
			numero_primo = False
		b += 1
	return numero_primo

def primo(n):
	'''Muestra los numeros primos hasta el numero que se pida'''

	a = 2
	if n <= 1:
		print "no hay numeros primos menores o iguales a", n
	elif n>1:
		while a <= n:
			if es_primo(a):
				print a
			a += 1


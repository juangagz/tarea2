#!/usr/bin/env python

# -*- coding: utf-8 -*-
def fib(n):    # escribe la serie de Fibonacci hasta n
	"""Escribe la serie de Fibonacci hasta n"""
	a, b = 0, 1
	while b < n:
		print b,
		a, b = b, a+b
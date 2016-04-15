#!/usr/bin/env python

import random
import sys

MAX_COMPLEXITY = 100
MAX_COMPLEXITY_TRIES = 2000
MAX_INSERTION_TRIES = 7
ARGS_AMOUNT = 1

RULES = list()
RULES.append(([0], 0))
RULES.append(([1], 1))

ALLOWEDFUNCS = ["max($,$)", "min($,$)", "$*$", "float($)/float($)", "$+$", "$-$", "($+$)", "($-$)", "pow($,$)"]

def getRandomFunc():
	return ALLOWEDFUNCS[random.randint(0, len(ALLOWEDFUNCS)-1)]

def insertAt(insertion, index, string):
	return string[:index] + insertion + string[index+1:]

def insertAtRandomPoint(insertion, string):
	l = list()
	for x in range(len(string)):
		if string[x] == '$':
			l.append(x)
	if len(l) == 0:
		print("insertAtRandomPoint: NOPE")
		return
	return insertAt(insertion, l[random.randint(0, len(l)-1)], string)

def insertRandom(string):
	return insertAtRandomPoint(getRandomFunc(), string)

def validate(func):
	for rule in RULES:
		args, res = rule
		try:
			if eval(func) != res:
				return False
		except:
			return False
	return True

def insertVars(func):
	while "$" in func:
		func = insertAtRandomPoint("args[" + str(random.randint(0, ARGS_AMOUNT-1)) + "]", func)
	return func

# increase complexity
for complexity in range(MAX_COMPLEXITY):
	print("complexity=" + str(complexity))
	# try
	for tries in range(MAX_COMPLEXITY_TRIES):
		func="$"
		# insertRandom
		for i in range(complexity):
			func = insertRandom(func)
		# insertVars
		for x in range(MAX_INSERTION_TRIES):
			varfunc = insertVars(func)
			if validate(varfunc):
				print(varfunc)
				sys.exit()

#!/usr/bin/env python

# spoj 4 - ONP - transform the expression

# example io:
# Input:
# 3
# (a+(b*c))
# ((a+b)*(z+x))
# ((a+t)*((b+(a+c))^(c+d)))
#
# Output:
# abc*+
# ab+zx+*
# at+bac++cd+^*

import sys
num_expressions = 0
expressions = []

for line in sys.stdin:
    if not num_expressions:
        num_expressions = int(line.strip()) 
        continue
    expressions.append(line.strip())

def rpn_eval(exp):
    if not isinstance(exp, list):
        return exp
    oper1 = rpn_eval(exp[0]) 
    oper2 = rpn_eval(exp[2])
    operator = exp[1]
    return oper1 + oper2 + operator

for exp in expressions:
    parsed = ''
    for token in list(exp):
        if token == '(':
            parsed += '['
        elif token == ')':
            parsed += '],'
        else:
            parsed += "'" + token + "',"
    print rpn_eval(eval(parsed)[0])

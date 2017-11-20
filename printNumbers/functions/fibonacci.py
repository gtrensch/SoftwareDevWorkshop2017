# -*- coding: utf-8 -*-
#
# fibonacci.py
#
# This file is part of printNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# printNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# printNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.

def FibonacciRecursion(n):
    '''
    Helper function.
    '''
    if n <= 1:
        return n
    else:
        return (FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2))

def FibonacciNumber(n):
    '''
    Helper function.
    '''
    c1=0.5+0.5*sqrt(5)
    c2=0.5-0.5*sqrt(5)
    if n <= 1:
        return n
    else:
        return (c1**n - c2**n) / sqrt(5)

def FibonacciSequence(n):
    '''
    :param n:   Operand
    :return:    fib(n) as list of fibonacci numbers, [0, 1, 1, 2, ... ]
    '''
    sequence = []
    for i in range(n):
        sequence.append(FibonacciRecursion(i))
    return (sequence)

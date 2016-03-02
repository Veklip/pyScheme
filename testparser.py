#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================================================
# copyright Amin By [http://aminby.net]
# Since 2014-4
#=================================================

import unittest
import parser

class TestParser(unittest.TestCase):

   def setUp(self):
       self.psr = parser.SParser()
       self.test_statements = (
        ("(if 1 2 4)", 2),
        ("(if 0 2)", None),
        ("(def a 3)", 3),
        ("a", 3),
        ("(list 1  2  3  4)", "(list 1 2 3 4)"),
        ("(func (x) (+ x x)", "(func (x) (+ x x))"),
        ("(begin (def x 3) (* 1 2))", 2),
        ("(def li (list 9 8 7 6))", "(list 9 8 7 6)"),
        ("(first li)", 9),
        ("(rest li)", "(list 8 7 6)"),
        ("(def mi (func (x) (* x x)))", "(func (x) (* x x))"),
        ("(mi 5)", 25),
        ("(def mul (func (x y) (* x y)))", "(func (x y) (* x y))"),
        ("(def mul7 (mul 7))", "(func (x y) (* x y))"),
        ("(mul7 9)", 63),
        ("(> 3 2 1)", True),
        ("(> 2 2 1)", False),
        ("(= 3 3 3)", True),
        ("(= 3 3 2)", False),
        ("(and 1 2 3)", True),
        ("(and 1 2 (or 0 0 0 1))", True),
        ("( begin 1    (and 9 8 7) (def gx 3) (mi 9))", 81),
        ("(xor 1 1)", False),
        ("(xor 0 0)", False),
        ("(xor 1 0)", True),
        ("(xor 0 1)", True),
        ("wtf", "error: 'wtf' is undefined."),
        ("(unfunc 1 2)", "error: 'unfunc' is undefined.")
        )

   def test_parse(self):
       for s,r in self.test_statements:
           rr = self.psr.parseAsIScheme(s).evaluate_excepted()
           self.assertEqual(str(r), str(rr))



if __name__ == '__main__':
    unittest.main()

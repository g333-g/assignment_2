#!/usr/bin/env python3

import sys

args = dict(arg.split('=') for arg in sys.argv[1:])
a = float(args.get('a', 1))
b = float(args.get('b', 1))
c = float(args.get('c', 1))

s1 = c ** 3
s2 = s1 ** 0.5
s3 = s2 / a
s4 = s3 * 10
s5 = s4 + b

print("<html>")
print("<body>")
print("<h2>Assignment #2</h2>")
print(f"<h2>Final Result: {s5}</h2>")
print(f"Step 1: c = {c}, c^3 = {s1}<br>")
print(f"Step 2: √(c^3) = {s2}<br>")
print(f"Step 3: {s2} / {a} = {s3}<br>")
print(f"Step 4: {s3} * 10 = {s4}<br>")
print(f"Step 5: {s4} + {b} = {s5}<br>")
print("</body></html>")
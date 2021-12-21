#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "e", "g", "h", "k", "s"}
    b = {"c", "g", "p", "q"}
    c = {"f", "g", "s", "x", "y", "z"}
    d = {"a", "b", "c", "d", " ", "g", "u", "v", "z"}

    x = (a.difference(b)).intersection(c.union(d))
    print(f"x = {x}")

    au = u.difference(a)
    bu = u.difference(b)

    y = (au.intersection(bu)).difference(c.union(d))
    print(f"y = {y}")

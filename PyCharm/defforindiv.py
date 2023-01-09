#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list_sort(func):
    def inner(s):
        return sorted(func(s))

    return inner


@list_sort
def get_list(s):
    return [int(i) for i in s.split()]


if __name__ == '__main__':
    print(get_list(input('Введите числа через пробел: ')))





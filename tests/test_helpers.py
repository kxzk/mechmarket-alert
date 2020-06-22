#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest

from mma.helpers import contains_any, extract_selling


@pytest.mark.parametrize(
    "post,keywords,expected",
    [
        ("[H] GMK Laser, GMK Camping [W]", {"gmk Camping", "Rama"}, True),
        ("[H] gmk Striker [W]", {"Rama"}, False),
    ],
)
def test_contains_any(post, keywords, expected):
    result = contains_any(post, keywords)
    assert result == expected


@pytest.mark.parametrize(
    "post,expected",
    [
        ("[CA-ON][H] GMK Laser Cyberdeck [W] Paypal", "[H] GMK Laser Cyberdeck [W]",),
        (
            "[US-CA] [H] BlackPink and Clear Durock Stabs, GMK 8008, Klippe T R2 [W]Paypal",
            "[H] BlackPink and Clear Durock Stabs, GMK 8008, Klippe T R2 [W]",
        ),
        ("", None),
    ],
)
def test_extract_selling(post, expected):
    selling = extract_selling(post)
    assert selling == expected

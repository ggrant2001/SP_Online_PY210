#!/usr/bin/env python3

### Lesson 6 Mailroom, Part 4, Full Suite of Unit Tests
# will not test the user interaction, but test everything else.

import mailroom4 as mailroom
from textwrap import dedent
import os
import sys
import math

mailroom.donor_db = mailroom.get_donor_db()

def test_get_donor_db():
    """test the content generated by get_donor_db(), it's hardcoded data"""
    listing = mailroom.get_donor_db()
    assert "Abraham Lincoln" in listing
    assert "Eve WallE" in listing
    assert listing['Charlie Brown'] == ('Charlie Brown', [453.67])

def test_add_donor():
    name = "Hello Kitty"
    donor = mailroom.add_donor(name)
    assert donor[0] == "Hello Kitty"

def test_list_donors():
    listing = mailroom.list_donors()
    assert "Charlie Brown" in listing
    assert "Barack Omama" not in listing

def test_print_donor_report():
    """this is hard to test since the printed report is None type"""
    report = mailroom.print_donor_report()
    assert report is None

if __name__== "__main__":
    test_get_donor_db()
    test_add_donor()
    test_list_donors()
    test_print_donor_report()
    print("Unit Tests Passed")

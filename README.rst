==============================================
Remove f-strings for Python<3.6 compatibility
==============================================

This is a simple script that attempts to replace 
f-strings (f"text {variable}") with alternatives
compatible with earlier python versions 
(such as "text {}".format(variable)).

Usage::

	python3 fstring-downgrade.py test.py

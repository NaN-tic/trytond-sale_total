# This file is part sale_total module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.sale_total.tests.test_sale_total import suite
except ImportError:
    from .test_sale_total import suite

__all__ = ['suite']

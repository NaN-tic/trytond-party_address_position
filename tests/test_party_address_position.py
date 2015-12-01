# This file is part of the party_address_position module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PartyAddressPositionTestCase(ModuleTestCase):
    'Test Party Address Position module'
    module = 'party_address_position'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartyAddressPositionTestCase))
    return suite
# This file is part of the party_address_position module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import address


def register():
    Pool.register(
        address.PartyAddressPosition,
        address.Address,
        module='party_address_position', type_='model')

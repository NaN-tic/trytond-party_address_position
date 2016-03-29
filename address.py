# This file is part of the party_address_position module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['PartyAddressPosition', 'Address']


class PartyAddressPosition(ModelSQL, ModelView):
    "Party Address Position"
    __name__ = 'party.address.position'
    name = fields.Char('Name', required=True, translate=True)


class Address:
    __metaclass__ = PoolMeta
    __name__ = 'party.address'
    position = fields.Many2One('party.address.position', 'Position')

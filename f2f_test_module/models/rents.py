# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Rents(models.Model):
    _name = 'f2f_test_module.rents'

    customer = fields.Many2many("res.partner", ondelete='restrict')
    book = fields.Many2one("f2f_test_module.books", ondelete='restrict')

    rental_date = fields.Datetime(
        index=True, default=lambda self: fields.Datetime.now()
    )
    plan_return_date = fields.Datetime()
    duration = fields.Integer()
    return_date = fields.Datetime()
    state = fields.Selection(
        [
            ('pending', 'En cours'),
            ('return', 'Retourné'),
            ('late', 'En retard')
        ]
    )

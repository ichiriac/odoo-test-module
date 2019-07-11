# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tests(models.Model):
    _name = 'f2f_test_module.tests'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

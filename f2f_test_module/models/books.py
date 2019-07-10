# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Books(models.Model):
    _name = 'f2f_test_module.books'
    _rec_name = "title"

    authors = fields.Many2many("res.partner")
    editors = fields.Many2many("res.partner")
    edition_date = fields.Datetime()
    ISBN = fields.Text()
    title = fields.Text()
    short_description = fields.Text()
    photo = fields.Binary('Image de couverture', attachment=False)


class BetterPartner(models.Model):
    _inherit = "res.partner"

    def open_partner(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Title',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.partner',
            'res_id': self.id,
            'target': 'inline',
        }
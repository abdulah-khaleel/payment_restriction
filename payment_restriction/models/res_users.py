# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UsersExtended(models.Model):
    _inherit = 'res.users'

    restrict_payment = fields.Boolean(string="Restrict Payment Methods")
    journal_ids = fields.Many2many('account.journal', string='Allowed Journals', domain="[('type','in',['bank','cash'])]")
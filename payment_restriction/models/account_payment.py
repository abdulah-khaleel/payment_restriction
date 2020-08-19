# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning
 
class AccountPaymentExtended(models.Model):
    _inherit = 'account.payment'

    @api.constrains('journal_id')
    def _check_journal_restriction(self):

        context = self._context
        current_uid = context.get('uid')
        user = self.env['res.users'].browse(current_uid)

        if user.restrict_payment:

            allowed_journal_ids = []
            for journal in user.journal_ids:
                allowed_journal_ids.append(journal.id)

            for record in self:
                if record.journal_id.id not in allowed_journal_ids:
                    raise Warning(f"You do not have the authorization to use the '{record.journal_id.name}' payment method. Please re-select and try again.")
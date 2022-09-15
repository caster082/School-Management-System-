

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class accounting_move_line_inherit(models.Model):
   _inherit = 'account.move.line'
   name = fields.Char('name')
   _defaults = {
             'name': lambda self, cr, uid, context: context.get('name', False),
   }
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sch_book(models.Model):
    _name = "sch.book"

    _description = "Books"

    book_name = fields.Char(string='Book Name', required=True, tracking=True, translate=True)

    Subject = fields.Char('Subject', tracking=True, translate=True)
    Category = fields.Selection([('myanmar', 'Myanmar'),
                               ('english', 'English'), ('math', 'Math')],)
    product_id = fields.Many2one('product.product', string="Books")
    product_id = fields.Many2one(
        "product.product",
        "Product_id",
        required=True,
        delegate=True,
        ondelete="cascade",
    )
    Qty = fields.Integer(string="Quantity")
    student_id = fields.Many2one('sch.record', string="Students ID")

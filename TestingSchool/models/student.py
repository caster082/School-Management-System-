# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime
from odoo.tools import datetime
from dateutil.relativedelta import relativedelta
from datetime import timedelta


class sch_record(models.Model):
    _name = "sch.record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Record"
    _rec_name = 'student_name'

    # name = fields.Char(string='Test')
    # name_seq = fields.Char(string='Student ID', required=True, copy=False, readonly=True,
    #                        index=True, default=lambda self: _('New'))
    student_name = fields.Char(string='Student Name', required=True, tracking=True, translate=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'), ('other', 'Other')],
                              required=True, default='male', tracking=True)
    notes = fields.Text(string="Registration Note", translate=True)
    image = fields.Binary(string="Image", attachment=True, tracking=True)
    email = fields.Char('Email', required=True, tracking=True)
    mobile = fields.Char('Mobile', tracking=True)
    amount = fields.Integer(string="Student Fee")
    books = fields.One2many('sch.book', 'student_id', string='Student Books')  # one2many
    responsible_id = fields.Many2one('res.partner', string="Responsible Person")  # many2one
    active = fields.Boolean(string="Active", default=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Canceled')],
                             default='draft',
                             string="Status", tracking=True)
    book_count = fields.Integer(string="Book", compute='compute_book_count')
    birth_date = fields.Date('dob', tracking=True)
    age = fields.Char(string="Age", compute="_compute_age")
    x_status = fields.Integer(string="Status")

    attachment_name = fields.Char()
    attachment = fields.Binary()
    # attachment = fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id3',
    #                               string="Attachment",
    #                               help='You can attach the copy of your document', copy=False)
    _sql_constraints = {
        ('unique_name', 'unique (student_name, email)', 'Student already Exist!!!'),

    }
    #
    # class Attachment(models.Model):
    #     _inherit = 'ir.attachment'
    #
    #     attach_rel = fields.Many2many('res.partner', 'attachment', 'attachment_id3', 'document_id', string="Attachment",
    #                                   invisible=1)
    # def calculate_age(birth_date):
    #     today = date.today()
    #     calculate_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    #     if birth_date:
    #         age = calculate_age

    @api.depends('birth_date')
    def _compute_age(self):
        for emp in self:
            age = relativedelta(datetime.now().date(), fields.Datetime.from_string(emp.birth_date)).years
            emp.age = str(age)

    @api.constrains('birth_date')
    def check_birth_date(self):
        current_date = datetime.now().date()
        for rec in self:
            if rec.birth_date > current_date:
                raise ValidationError("Birth Date Less than current date")

    # @api.onchange('birth_date')
    # def calculate_age(self):
    #     today = date.today()
    #     age = today.year - self.birth_date.year
    #           # - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
    #     if self.birth_date:
    #         self.age = age

    def compute_book_count(self):
        for rec in self:
            book_count = self.env['sch.book'].search_count([('student_id', '=', rec.id)])
            rec.book_count = book_count

    def action_open_book(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Books',
            'res_model': 'sch.book',
            'domain': [('student_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def report_excel(self):
        return self.env.ref('TestingSchool.student_profile_card_xlsx').report_action(self)

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

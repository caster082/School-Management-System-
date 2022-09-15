# -*- coding: utf-8 -*-

from odoo import models, fields


# Creating Model/Table to Store Doctor Details
# https://www.youtube.com/watch?v=L6MxDR71_1k&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=2
class SchoolTeacher(models.Model):
    _name = 'sch.teacher'
    _inherits = {
        'sch.record': 'related_student_id',
    }
    _description = 'Teacher Record'

    name = fields.Char(string="Teacher Name", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    salary = fields.Integer(string="Salary")
    subject = fields.Char(string="Specialize Subject", required=True)
    user_id = fields.Many2one('res.users', string='Related User')
    related_student_id = fields.Many2one('sch.record', string='Students')


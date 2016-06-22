# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Thanh1(models.Model):
	_name = 'thanh2'

	name = fields.Char(string="Title")
	description = fields.Text()

# class thanh(models.Model):
#     _name = 'thanh.thanh'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
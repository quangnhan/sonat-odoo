from odoo import models, fields

class TestBankQuestion(models.Model):
    _name = 'test.bank.question'
    _description = 'Test Bank Question'

    name = fields.Char(string="Question", required=True)
    answer = fields.Text(string="Answer")
    category = fields.Char(string="Category")

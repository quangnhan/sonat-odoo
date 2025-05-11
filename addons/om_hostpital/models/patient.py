from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Master'
    
    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Femail')], string='Gender')
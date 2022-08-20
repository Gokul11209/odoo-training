from odoo import models, fields, api, tools, _



class EmployeeName(models.Model):
    _name = "employe.name"
    _description = "Employesss"



    name = fields.Char(string="name")
    email = fields.Char(string="Email")
    phone = fields.Char(string="phone")
    adderss= fields.Char(string="adderss")
    position= fields.Char(string="position")
    manager= fields.Char(string="Manager")
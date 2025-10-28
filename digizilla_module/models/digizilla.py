from odoo import models, fields, api


class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True
    )
    
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        string='Gender',
        tracking=True
    )
    
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        tracking=True
    )
    
    joining_date = fields.Date(
        string='Joining Date',
        tracking=True
    )
    
    tag_ids = fields.Many2many(
        comodel_name='res.partner.category',
        string='Tags',
        tracking=True
    )
    
    customer_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='digizilla_partner_rel',
        column1='digizilla_id',
        column2='partner_id',
        string='Customers',
        tracking=True
    )
    
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
        tracking=True
    )
    
    notes = fields.Text(
        string='Notes',
        tracking=True
    )
    
    comments = fields.Char(
        string='Comments',
        tracking=True
    )
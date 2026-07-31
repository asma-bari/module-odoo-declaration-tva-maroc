{
    'name': 'Déclaration TVA Maroc (SIMPL)',

    'summary': 'Gestion de la déclaration TVA marocaine',

    'description': '''
Module Odoo permettant la préparation,
le contrôle et la génération
de la déclaration TVA Maroc.
''',

    'author': 'Asma Bari',

    'website': '',

    'category': 'Accounting',

    'version': '1.0',

   'depends': [
    'base',
    'mail',
    'account',
], 

    'data': [
    'security/ir.model.access.csv',

    'data/sequence.xml',

    'views/vat_return_views.xml',
    'views/vat_return_line_views.xml',
    'views/vat_deduction_line_views.xml',
    'views/vat_history_views.xml',

    'views/res_partner_views.xml',
    'views/res_company_views.xml',
    'views/account_move_views.xml',
    'views/account_payment_views.xml',
    
    'views/menu.xml',
],

    'demo': [],

    'installable': True,
    'application': True,
}
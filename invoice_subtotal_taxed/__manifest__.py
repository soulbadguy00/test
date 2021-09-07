# -*- coding: utf-8 -*-
{
    'name': "Price Subtotal Taxed",
    'version': '10.0',
    'summary': 'Show the taxed amount of each invoice line',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'author': "Odoo Tips",
    'website': 'http://www.gotodoo.com/',
    'depends': ['base', 'account', 'sale'
                ],

    'images': ['images/main_screenshot.png'],
    'data': [
             'views/account_invoice_view.xml',
             ],
    'demo': [],
}

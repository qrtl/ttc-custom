# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Purchase Order Line with Barcode',
    'version': '10.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.odoo-asia.com',
    'category': 'Purchase',
    'license': 'LGPL-3',
    'description': """
Display barcode information of the products in the purchase order line
on the form view and printed document of purchase order.
""",
    'depends': [
        'purchase',
        'product',
    ],
    'data': [
        'reports/purchase_order_templates.xml',
        'views/purchase_order_views.xml',
    ],
    'installable': True,
}

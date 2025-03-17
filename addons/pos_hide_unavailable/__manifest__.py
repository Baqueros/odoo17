# -*- coding: utf-8 -*-
{
    'name': 'Pos hide unavailable products',
    'version': '17.0',
    'category': 'Point of Sale',
    'author': 'Khaled Hassan',
    'website': "https://apps.odoo.com/apps/modules/browse?search=Khaled+hassan",
    'license': 'OPL-1',
    'price': 18,
    'currency': 'EUR',
    'summary': 'only show product in PoS with Available Quantity, POS Hide out of stock products, pos show only products with positive stock, show product in PoS with Available Quantity, pos stock validation, pos out of stock hide,Automatically hide products from POS when products are out of stock,Out of stock product restriction on point of sales order restriction for out of stock product restriction for POS Restrict Out Stock Product POS stop out of stock product for POS available products only out of stock product alerts out of stock products POS,Automatically remove products from POS when products are out of stock,hide Out of Stock Product on POS, Out of stock hide product,Restrict Out of Stock Product on POS, hide Out of stock product pos, Out of stock product hide zero onhand stock, pos Out of stock product stock hide, pos Out of stock hide product ',
    'description': """POS Hide out of stock products""",
    'depends': ['point_of_sale', 'stock','account', 'sale_management','base', 'mail'],
    'images': ['static/description/main_screenshot.png'],
    'assets': {
        'point_of_sale._assets_pos': [
            "pos_hide_unavailable/static/src/js/product_list.js",
            "pos_hide_unavailable/static/src/xml/product_list.xml",
        ]
    },
    'data': [
        'views/pos_hide_unavailable.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}

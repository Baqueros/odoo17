# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

{
    "name": "Point Of Sales Restrict Out Stock Product | POS Restrict Out Of Stock Products",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Point of Sale",
    "license": "OPL-1",
    "summary": "Restrict Out Product Point Of Sales,Check Product Quantity,Product On Hand Quantity,Low Stock Alert,Search Product Quantity,POS Restrict Out Stock,Product Out Of Stock Warning Odoo",
    "description": """Currently, in odoo, there is no feature for restrict product out-of-stock in the point of sale. In this module when you make an order if there is not enough product quantity in stock then it raises a warning, however, the POS user can still place new orders for items that are out of stock or not in stock.""",
    "version": "0.0.1",
    "depends": ["point_of_sale", 'sh_pos_stock_information'],
    "application": True,
    "data": [
        
        'views/res_config_settings.xml',   
    
     ],
    'assets': {'point_of_sale._assets_pos': [
        "sh_pos_restrict_out_of_stock_products/static/src/app/popups/StockInformation_popup/StockInformation_popup.js",
        "sh_pos_restrict_out_of_stock_products/static/src/app/popups/StockInformation_popup/StockInformation_popup.xml",
        "sh_pos_restrict_out_of_stock_products/static/src/overrides/models/model.js",
                    'sh_pos_restrict_out_of_stock_products/static/src/scss/pos.scss', 
                    ],
               
               },
    "auto_install": False,
    "installable": True,
    "images": ["static/description/background.png", ],
    "price": 5,
    "currency": "EUR"
}

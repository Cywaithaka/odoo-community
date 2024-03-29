{
    'name' : 'import SugarCRM + kashflow data to odoo ',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Base',
    'website' : 'http://matiarrahman.com/',
    'description': """
Depends on:

* http://pandas.pydata.org/
* http://mysql-python.sourceforge.net/MySQLdb.html

Odoo optimisation:

* modify openerp/addons/base/res/res_partner.py in order to skip calling function _fields_sync (via checking context.get('skip_addr_sync'))
* remove website module in order to optimise importing data in ir.attachment table

    """,
    'depends' : ['import_framework', 'crm', 'project', 'sale_mediation_custom', 'multi_company'],
    'data':[
        'wizard/upload.xml',
        'data.xml',
        ],
    'installable': True,
    'auto_install': False,
}

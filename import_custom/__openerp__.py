{
    'name' : 'Custom import module',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Base',
    'website' : 'http://matiarrahman.com/',
    'description': """
    Prepare some data for import
    """,
    'depends' : ['import_framework', 'product', 'contacts', 'website_sale'],
    'data':[
        'wizard/upload.xml',
        #'data.xml',
        ],
    'installable': True,
    'auto_install': False,
}

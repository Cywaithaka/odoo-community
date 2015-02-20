{
    'name' : 'Website proposal for leads',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Base',
    'website' : 'http://matiarrahman.com/',
    'description': """
Web-based proposals for leads
    """,
    'depends' : ['website_proposal', 'crm', 'sale_crm', 'sale',],
    'data':[
        'views.xml',
        'report.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

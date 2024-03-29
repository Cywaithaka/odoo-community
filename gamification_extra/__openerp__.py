{
    'name' : 'Gamification extra',
    'version' : '1.0.0',
    'author' : 'Matiar Rahman',
    'category' : 'Sale',
    'website' : 'http://matiarrahman.com/',
    'description': """
Improvements for gamification module:

* allows don't hide challenge, after reaching a goal
* new computation modes: average, minimum, maxmimum
* action on click
* precision (rounding) in goals

Tested on 8.0 ab7b5d7
    """,
    'depends' : ['gamification'],
    'data':[
        'gamification_extra_views.xml',
        ],
    'qweb': ['static/src/xml/gamification_extra.xml'],
    'installable': True
}

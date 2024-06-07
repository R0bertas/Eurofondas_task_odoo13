{
    'name': 'Dokumentu valdymas',
    'category': 'Tools',
    'description': """
    Dokumentu ir knygu valdymo sistema
    ==================================
    Modulis leidzia valdyti ivairius dokumentus ir knygas, iskaitant ju saugojima, prieziura ir atsakingu asmenu priskyrima.
        """,
    'version': '1.0',
    'author' : 'Robertas Kiselis',
    'views': [
        'views/library_doc_views.xml',
        'views/library_doc_menus.xml',
        'security/ir.model.access.csv',
        'security/library_doc_security.xml',
    ],
}
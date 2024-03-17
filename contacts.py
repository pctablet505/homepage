from collections import namedtuple
Contact = namedtuple('Contact', ['method', 'disp', 'url', 'icon'])
contacts = [
    Contact('Phone', '+91-8709253658', 'tel:+91-8709253658', 'fa fa-phone'),
    Contact('Mail', 'pctablet505@gmail.com',
            'mailto:pctablet505@gmail.com', 'fa fa-envelope'),
    Contact('LinkedIn', '@stopslavery404',
            'https://www.linkedin.com/in/stopslavery404', 'fab fa-linkedin'),
    Contact('Website', 'pctablet505.herokuapp.com',
            'https://pctablet505.herokuapp.com/about', 'fa fa-home'),
    Contact('Hackerrank', '@stopslavery404',
            'https://www.hackerrank.com/stopslavery404', 'fab fa-hackerrank'),
    Contact('GitHub', '@stopslavery404',
            'https://www.github.com/stopslavery404', 'fa fa-github'),
    Contact('Instagram', '@hello._world_.me',
            'https://www.instagram.com/hello._world_.me', 'fa fa-instagram'),
    Contact('Youtube', 'YouTube',
            'https://www.youtube.com/channel/UCnRPtPB_CXs1ngGlwKqP-yw', 'fa fa-youtube'),

]

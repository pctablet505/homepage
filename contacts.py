from collections import namedtuple
Contact = namedtuple('Contact', ['method', 'disp', 'url', 'icon'])
contacts = [
    Contact('Phone', '+91-8709253658', 'tel:+91-8709253658', 'fa fa-phone'),
    Contact('Mail', 'pctablet505@gmail.com',
            'mailto:pctablet505@gmail.com', 'fa fa-envelope'),
    Contact('LinkedIn', '@pctablet505',
            'https://www.linkedin.com/in/pctablet505', 'fab fa-linkedin'),
    Contact('Website', 'pctablet505.herokuapp.com',
            'https://pctablet505.herokuapp.com/about', 'fa fa-home'),
    Contact('Hackerrank', '@pctablet505',
            'https://www.hackerrank.com/pctablet505', 'fab fa-hackerrank'),
    Contact('GitHub', '@pctablet505',
            'https://www.github.com/pctablet505', 'fa fa-github'),
    Contact('Instagram', '@pctablet505',
            'https://www.instagram.com/pctablet505', 'fa fa-instagram'),
    Contact('Youtube', 'YouTube',
            'https://www.youtube.com/channel/UCnRPtPB_CXs1ngGlwKqP-yw', 'fa fa-youtube'),

]

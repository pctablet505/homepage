from collections import namedtuple

Education = namedtuple('Education',
                       ('school', 'website_school', 'duration', 'degree', 'website_degree'))
education = [
    Education(
        school='MITx',
        website_school='https://micromasters.mit.edu/',
        duration='2021-22',
        degree='MicroMasters in Statistics and Data Science',
        website_degree='https://micromasters.mit.edu/ds/'),
    Education(
        school='BIT Sindri',
        website_school='https://www.bitsindri.ac.in/',
        duration='2018-22',
        degree='B.Tech Computer Science',
        website_degree='https://www.bitsindri.ac.in/index.php/departments/computer-science-engineering',
    ),
    Education(
        school='Guru Gobind Singh Public School',
        website_school='https://www.ggpsbokaro.org/',
        duration='2015-17',
        degree='Higher Secondary Education',
        website_degree='',
    ),
    Education(
        school='ARS Public School',
        website_school='http://www.arspublicschool.com/',
        duration='2008-15',
        degree='High School',
        website_degree='',

    ),
    Education(
        school='Sharswati Sishu Vidya Mandir',
        website_school='',
        duration='2005-08',
        degree='Elementary School',
        website_degree='',
    ),

]

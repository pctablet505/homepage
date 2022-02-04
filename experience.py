from collections import namedtuple

Experience = namedtuple('Experience',
                        ('company', 'location', 'website', 'duration', 'description'))
experience = [
    Experience(
        company='Samsung R&D Institute India',
        location='Noida',
        website='https://research.samsung.com/sri-n',
        duration='Jan 2022-Present',
        description='Intern'),
]

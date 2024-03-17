from collections import namedtuple

Project = namedtuple(
    'Project', ['title', 'description', 'demonstration', 'code'])
projects_list = [
    Project('PacMan AI',
            '''AI based intelligent agent to control pacman in different environments.\n
            The pacman plays against the ghosts and tries to eat all food while staying safe from ghosts\n
            and finishing in minimum time.
            The pacman uses different methods like A* Search, Heuristics, Reinforcement Learning with different parameters. ''',
            '''https://inst.eecs.berkeley.edu/~cs188/sp21/project1/''',
            'https://github.com/stopslavery404/CS188-AI/tree/main/proj1-search-python3'
            ),
    Project(
        'Automatic Review Analyzer',
        '''Sentiment Analysis for customer reviews. Using simple perceptron algorithm''',
        '',
        'https://github.com/stopslavery404/Machine-Learning/tree/main/Project1/sentiment_analysis'

    ),
    Project(
        'MNIST Digit Recognition',
        '''Classification of digits using support vector machine and gradient descent.''',
        '',
        'https://github.com/stopslavery404/Machine-Learning/tree/main/Project2/mnist/part1'

    ),
    Project(
        'Overlapping Digit Recognition',
        '''Classification of overlapping digits which contain multiple digits in single image, where a digit is written over other digit, using Convolutional Neural Networks. ''',
        '',
        'https://github.com/stopslavery404/Machine-Learning/tree/main/Project2/mnist/part2-twodigit'

    ),
    Project(
        'Collaborative Filtering via Gaussian Mixtures',
        '''Recommender system for Netflix using Gaussian Mixtures models and EM algorithm.\n
        Ratings of few users for different movies are provided as input and ratings for movies for which
        user has not rated is calculated. It achieves very nice accuracy.''',
        '',
        'https://github.com/stopslavery404/Machine-Learning/tree/main/project4/resources_netflix/netflix'
    ),
    Project(
        'Text game using Reinforcement Learning',
        '''It is a game in which a robot is given task in a room and he learns to play it.
            Implementations using Q learning, Q learning with approximations, using neural networks to reduce the exponential size Q Tables.''',
        '',
        'https://github.com/stopslavery404/Machine-Learning/tree/main/project5/rl'
    ),
    Project(
        "Maze Solver",
        '''Demonstration of complexity, speed, effectiveness of different search algorithms ''',
        '',
        'https://github.com/stopslavery404/Artificial-Intelligence'
    ),
    Project(
        'Degrees',
        '''Calculation of minimum degree of separation between actors in holywood.
            Separation is in terms of working together.''',
        'https://cs50.harvard.edu/ai/2020/projects/0/degrees/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/degrees'

    ),
    Project(
        'Tic-Tac-Toe AI',
        'MiniMax and Alpha-Beta pruning based undefeatable Intelligent to play against human.',
        'https://www.youtube.com/watch?v=tp9DjqV_KoU',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/tictactoe'

    ),
    Project(
        'Minesweeper AI',
        '''Knowledge based Intelligent agent to play Minesweeper which reasons using preposotional logic.''',
        'https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/minesweeper'
    ),
    Project(
        'CSP solver for Crossword Puzzle',
        '''Solves Crossword puzzles by modelling it into Constraint satisfaction problem and then using
        backtracking search with different heuristics to improve performance''',
        'https://cs50.harvard.edu/ai/2020/projects/3/crossword/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/crossword'
    ),
    Project(
        'Pabilistic models for reasoning under uncertainity',
        '''To demonstrate page ranking and gene inheritance, by sampeling and using bayes-net''',
        'https://cs50.harvard.edu/ai/2020/projects/2/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/probabilistic%20models'
    ),
    Project(
        'Shopping',
        'K Nearest Neighbour model to predict whether customer will make the purchase or not.',
        'https://cs50.harvard.edu/ai/2020/projects/4/shopping/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/shopping'
    ),
    Project(
        'NIM',
        '''Playing NIM against human. Trained using reinforcement learning.''',
        'https://cs50.harvard.edu/ai/2020/projects/4/nim/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/nim'

    ),
    Project(
        'Traffic Sign classification',
        '''CNN model for 43 class classification of traffic sign boards''',
        'https://cs50.harvard.edu/ai/2020/projects/5/traffic/',
        'https://github.com/stopslavery404/Artificial-Intelligence/tree/main/traffic'

    ),
    Project(
        'CS50 Wiki',
        '''Mini version of WikiPedia with almost all features of wikipedia.\n
        Built using django, html, jinja, css, saas.''',
        'https://mycs50wiki.herokuapp.com/',
        ''
    ),
    Project(
        'HomePage',
        '''My Homepage which contails details about me like hobbies, interests, and many things more.\n
        Built using flask, HTML, CSS, Javascript.
        ''',
        'https://stopslavery404.herokuapp.com/',
        ''
    ),
    Project(
        'CS50-Finance',
        '''A lite app to get quotes of stocks and to perform buy, sell stocks.\n
        Technologies used: Flask, SQL, APIs, JSON, Heroku, GIT.
        ''',
        'https://mycs50finance.herokuapp.com/',
        ''
    ),

    
    ]

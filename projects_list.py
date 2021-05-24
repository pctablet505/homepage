from collections import namedtuple

Project = namedtuple(
    'Project', ['title', 'description', 'demonstration', 'code'])
projects_list = [
    Project('PacMan',
            '''AI based intelligent agent to control pacman in different environments''',
            '''https://inst.eecs.berkeley.edu/~cs188/sp21/project1/''',
            'https://github.com/pctablet505/CS188-AI/tree/main/proj1-search-python3'
            ),
    Project(
        'Automatic Review Analyzer',
        '''Sentiment Analysis for customer reviews''',
        '',
        'https://github.com/pctablet505/Machine-Learning/tree/main/Project1/sentiment_analysis'

    ),
    Project(
        'MNIST Digit Recognition',
        '''Classification of digits using support vector machine and gradient descent.''',
        '',
        'https://github.com/pctablet505/Machine-Learning/tree/main/Project2/mnist/part1'

    ),
    Project(
        'Overlapping Digit Recognition',
        '''Classification of overlapping digits using Convolutional Neural Networks.''',
        '',
        'https://github.com/pctablet505/Machine-Learning/tree/main/Project2/mnist/part2-twodigit'

    ),
    Project(
        'Collaborative Filtering via Gaussian Mixtures',
        'Recommender system for Netflix using Gaussian Mixtures models and EM algorithm.',
        '',
        'https://github.com/pctablet505/Machine-Learning/tree/main/project4/resources_netflix/netflix'
    ),
    Project(
        'Text game using Reinforcement Learning',
        '''It is a game in which a robot is given task in a room and he learns to play it.
            Implementations using Q learning, Q learning with approximations, using neural networks.''',
        '',
        'https://github.com/pctablet505/Machine-Learning/tree/main/project5/rl'
    ),
    Project(
        "Maze Solver",
        '''Demonstration of complexity of different search algorithms ''',
        '',
        'https://github.com/pctablet505/Artificial-Intelligence'
    ),
    Project(
        'Degrees',
        '''Calculation of minimum degree of separation between actors in holywood.
            Separation is in terms of working together.''',
        'https://cs50.harvard.edu/ai/2020/projects/0/degrees/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/degrees'

    ),
    Project(
        'Tic-Tac-Toe',
        'MiniMax based undefeatable Intelligent to play against human.',
        'https://www.youtube.com/watch?v=tp9DjqV_KoU',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/tictactoe'

    ),
    Project(
        'Minesweeper',
        '''Knowledge based Intelligent agent to play Minesweeper which reasons using preposotional logic.''',
        'https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/minesweeper'
    ),
    Project(
        'CSP solver for Crossword Puzzle',
        '''Solves Crossword puzzles by modelling it into Constraint satisfaction problem and then using backtracking search with different heuristics''',
        'https://cs50.harvard.edu/ai/2020/projects/3/crossword/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/crossword'
    ),
    Project(
        'Pabilistic models for reasoning under uncertainity',
        '''To demonstrate page ranking and gene inheritance''',
        'https://cs50.harvard.edu/ai/2020/projects/2/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/probabilistic%20models'
    ),
    Project(
        'Shopping',
        'KNN model to predict whether customer will make the purchase or not.',
        'https://cs50.harvard.edu/ai/2020/projects/4/shopping/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/shopping'
    ),
    Project(
        'NIM',
        '''Playing NIM against human. Trained using reinforcement learning.''',
        'https://cs50.harvard.edu/ai/2020/projects/4/nim/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/nim'

    ),
    Project(
        'Traffic Sign classification',
        '''CNN model for 43 class classification of traffic sign boards''',
        'https://cs50.harvard.edu/ai/2020/projects/5/traffic/',
        'https://github.com/pctablet505/Artificial-Intelligence/tree/main/traffic'

    )]

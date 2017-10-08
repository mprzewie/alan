from distutils.core import setup

if __name__ == '__main__':
    setup(
        name='alan',
        version='',
        packages=['alan'],
        url='',
        license='MIT',
        author='marcin',
        author_email='m.przewie@gmail.com',
        description='Turing Machine',
        entry_points={
            'console_scripts': ['alan = alan.main:main']
        }
    )

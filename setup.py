from setuptools import setup, find_packages

setup(
    name='helper',
    version='1',
    description='personal helper',
    url='http://github.com/aye4/team-bot-helper',
    author='Pythonic Coders',
    author_email='',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': ['bot-helper = helper.bot:helper']},
)
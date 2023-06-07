from setuptools import setup

setup(
    name='helper',
    version='1',
    description='personal helper',
    url='http://github.com/aye4/bot-helper',
    author='Pythonic Coders',
    author_email='',
    license='MIT',
    packages=['_helper_'],
    entry_points={'console_scripts': ['bot-helper = helper.bot:helper']}
)
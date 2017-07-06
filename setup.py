from setuptools import setup


setup(
    name='slackdown',
    version='0.0.2',
    description='A simple Slack message text formatting to HTML code converter.',
    author='Andrew Briz',
    author_email='briz.andrew@gmail.com',
    url='http://www.github.com/datadesk/slackdown/',
    license="MIT",
    packages=("slackdown",),
    test_suite="slackdown.tests",
    include_package_data=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ),
)

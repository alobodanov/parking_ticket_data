from setuptools import setup

setup(
    name='parking_ticket_data',
    packages=['parking_ticket_data'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
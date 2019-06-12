import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='htv',
    version='0.1.8',
    author="floppino",
    author_email="martina.clem@gmail.com",
    description="A Heat Teamplate Validator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ko2-srls/HeatTemplateValidator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'htv = htvalidator.main:entry',
        ]},
    install_requires=['yamllint',
                      'cryptography',
                      'PyYAML==5.1',
                      'keystoneauth1==3.14.0',
                      'openstacksdk==0.26.0',
                      'python-cinderclient==4.2.0',
                      'python-glanceclient==2.16.0',
                      'python-heatclient==1.17.0',
                      'python-keystoneclient==3.19.0',
                      'python-neutronclient==6.12.0',
                      'python-novaclient==14.0.0',
                      'python-openstackclient==3.18.0',
                      'python-swiftclient==3.7.0'
                      ]
)

from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='amqp_bundle',
    packages=find_packages(),
    version='1.0',
    description='Remote events through amqp',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/amqp_bundle',
    download_url='https://github.com/applauncher-team/amqp__bundle/archive/master.zip',
    keywords=['applauncher', 'amqp'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)

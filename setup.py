from setuptools import setup

setup(
    name='obsidian-html',
    version='0.1',
    description='Converts an Obsidian vault into HTML',
    url='https://github.com/kmaasrud/obsidian-hugo',
    author='kmaasrud',
    author_email='kmaasrud@outlook.com',
    license='MIT',
    packages=['obsidian_html'],
    install_requires=[
      'markdown2',
      'regex'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            obsidian-html=obsidian_html:main
        ]
    }
)

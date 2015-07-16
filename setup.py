from setuptools import setup

setup(name='linecounter',
      version='1.2.0',
      description='linecounter for files',
      long_description='linecounter is a tool you can count how many lines you have in your files with it.',
      url='https://github.com/halitkarakis/line-counter/',
      py_modules=['linecounter'],
      author='M.Halit Karakis',
      author_email='halit@halitkarakis.com.tr',
      entry_points={
        'console_scripts': [
            'linecounter=linecounter:main',
        ],
      },
      license='Apache',
      keywords='line counting tool'
      )
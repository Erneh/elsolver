from distutils.core import setup
setup(
  name = 'elsolver',         # How you named your package folder (MyLib)
  packages = ['elsolver'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GNU',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'Joan Ernest Pérez',                   # Type in your name
  author_email = 'ernestpech11@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Erneh/elsolver',   # Provide either the link to your github or to your website
  download_url = '',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Scientists and developers',      # Define that your audience are developers
    'Topic :: Physics :: Simulations',

    'License :: OSI Approved :: GNU License',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
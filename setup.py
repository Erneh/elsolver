from setuptools import setup

setup(
  name = 'elsolver',         
  packages = ['elsolver'],   
  version = '0.1',      
  license='GNU',        
  description = 'Solver for Euler-Lagrange equations of a system using only its lagrangian',   
  author = 'Joan Ernest Pérez',                  
  author_email = 'ernestpech11@gmail.com',      
  url = 'https://github.com/Erneh/elsolver',  
  download_url = 'https://github.com/Erneh/elsolver/archive/refs/tags/v01.tar.gz',   
  keywords = ['PHYSICS', 'EULER-LAGRANGE', 'SIMULATION'],   
  install_requires=[            
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    

    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.11',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
  ],
)
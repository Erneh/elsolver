from distutils.core import setup
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

    'Intended Audience :: Scientists and developers',     
    'Topic :: Physics :: Simulations',

    'License :: OSI Approved :: GNU License',  

    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
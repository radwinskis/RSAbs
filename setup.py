from distutils.core import setup
setup(
  name = 'RSAbs',       
  packages = ['RSAbs'],   
  version = '0.7', 
  license='MIT',  
  description = 'AUTOMATIC DETECTION OF ABSORPTION FEATURES IN REFLECTANCE SPECTRA', 
  author = 'MARK RADWIN',  
  author_email = 'markradwin@gmail.com',     
  url = 'https://github.com/radwinskis/RSAbs',  
  download_url = 'https://github.com/radwinskis/RSAbs/archive/refs/tags/v0.7.tar.gz',   
  keywords = ['REFLECTANCE', 'SPECTROSCOPY', 'ABSORPTION', 'DETECTION'],  
  install_requires=[          
          'scipy',
          'pandas',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Science/Research',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
    
  ],
)
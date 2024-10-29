from setuptools import setup

setup(
    name='math_quiz',
    version='0.1.0',    
    description='A simple math quiz',
    url='https://github.com/Marco-Nguyen/FAU_DSSS_HW_2',
    author='Tai Hoang Nguyen',
    # author_email='shudson@anl.gov',
    license='Apache License',
    packages=['math_quiz'],
    install_requires=['random',
                      'unittest',                     
                      ],

    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Intended Audience :: Science/Research',
        'License :: Apache License',  
        'Operating System :: Windows',        
        # 'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ],
)
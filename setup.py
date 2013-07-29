from distutils.core import setup

setup(name='pyamicmd',
      version='0.1',
      description='Send commands to Asterisk via AMI using amiwrapper and starpy',
      author='Marcos Lopez',
      license='MIT',
      py_modules=['pyamicmd.pyamicmd'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
          ]
      )

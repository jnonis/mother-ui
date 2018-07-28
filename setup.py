from setuptools import setup

setup(name='mother-gui',
      version='0.1',
      description='Organelle display for TFT display.',
      url='http://github.com/jnonis/mother-gui',
      author='Javier Nonis',
      author_email='javiernonis@gmail.com',
      license='MIT',
      packages=['mother-gui'],
      install_requires=[
            'cython',
            'pyliblo',
      ],
      zip_safe=False)
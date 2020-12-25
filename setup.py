from setuptools import setup, find_packages

setup(
  name='ipcal',
  version='1.0',
  packages=find_packages(),
  entry_points={
    'console_scripts':
    'ipcal = ipcal.main:main'
  },
  zip_safe=False,
  classifiers=[
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
  ],
  setup_requires=["click"],
)
from setuptools import setup, find_packages


setup(name='ar488py',
      version='1.0',
      description="""
                  A library to interface with the AR488 USB to GPIB Adapter
                  """,
      url='https://github.com/cmgriffin/AR488',
      author='Chris Griffin',
      packages=find_packages(), zip_safe=False,
      install_requires=['pyvisa'],
      )

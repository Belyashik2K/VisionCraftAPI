from setuptools import setup

version = '1.0.6'

with open('README.md', 'r') as f:
      long_description = f.read()

setup(name='VisionCraftAPI',
      version=version,

      author='Belyashik2K',
      author_email='work@belyashik2k.ru',

      license='MIT license',

      long_description=long_description,
      long_description_content_type='text/markdown',

      description='Fully async python wrapper for VisionCraft API',
      url='https://github.com/Belyashik2K/VisionCraftAPI',
      
      packages=['VisionCraftAPI', 
                'VisionCraftAPI/exceptions', 'VisionCraftAPI/models',
                'VisionCraftAPI/utils', 'VisionCraftAPI/enums'],
      
      install_requires=['certifi', 'aiohttp', 'pydantic'],
      zip_safe=False)
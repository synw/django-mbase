from setuptools import setup, find_packages


version = __import__('mbase').__version__

setup(
  name = 'django-mbase',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Basic abstracts models and usefull stuff for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-mbase', 
  download_url = 'https://github.com/synw/django-mbase/releases/tag/'+version, 
  keywords = ['django'],
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  zip_safe=False
)

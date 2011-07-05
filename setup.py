from setuptools import setup, find_packages
import sys, os

version = '1.0-dev'

setup(name='plone.app.multilingual',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      url='http://svn.plone.org/svn/plone/plone.app.multilingual',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone','plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.app.z3cform',
        'plone.app.registry',
        'plone.directives.form',
        'plone.formwidget.contenttree',
        'Products.PloneLanguageTool',
      ],
      extras_require = {
          'dexterity': ['plone.multilingualbehavior'],
          'archetypes': ['archetypes.multilingual'],
          'test': [ 'plone.app.testing',
                    'plone.multilingualbehavior',
                    'archetypes.multilingual'],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
 )

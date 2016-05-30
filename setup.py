import setuptools

setuptools.setup(
    name='ixc-django-compressor',
    use_scm_version={'version_scheme': 'post-release'},
    py_modules=['ixc_compressor'],
    setup_requires=['setuptools_scm'],
)

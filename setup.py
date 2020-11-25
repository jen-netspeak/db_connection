import setuptools

setuptools.setup(
    name='db-connection',
    version="0.0.1",
    description="data connections including mysql",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['pandas', 'pygsheets', 'PyMySQL']
)


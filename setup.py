from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='mtbp3',
    version='0.2.31', # https://packaging.python.org/en/latest/specifications/version-specifiers/#version-specifiers 
    author='Y. Hsu',
    author_email='yh202109@gmail.com',
    description='My tool box in Python',
    long_description=long_description,  
    long_description_content_type="text/markdown",  # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),  # Required
    python_requires=">=3.7, <4",
    install_requires=['pathlib', 'json', 'pandas', 'matplotlib', 'seaborn'],
    project_urls={  # Optional
        "Bug Reports": "https://github.com/yh202109/mtbp3/issues",
        "Source": "https://github.com/yh202109/mtbp3/",
    },
    keywords=['tree', 'MedDRA', 'Clinical Trial'],
)
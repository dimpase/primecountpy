from setuptools import setup, find_packages
from setuptools.extension import Extension
from distutils.command.build_ext import build_ext as du_build_ext

class build_ext(du_build_ext):
    def run(self):
        from Cython.Build.Dependencies import cythonize
        self.distribution.ext_modules[:] = cythonize(
            self.distribution.ext_modules,
            include_path = ["primecountpy"],
            language_level=3)
        du_build_ext.run(self)


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extensions = [
    Extension(
            "primecountpy.primecount",
            sources=["primecountpy/primecount.pyx"],
            language="c++",
            libraries=["primecount","primesieve"],
        ),
    ]

setup(
    name='primecountpy',
    version='0.0.0',
    description='Cython interface for C++ primecount library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dimpase/primecountpy',
    author='SageMath Developers',
    author_email='sage-devel@googlegroups.com',
    license='GPLv3',
    packages=find_packages(),
    ext_modules=extensions,
    zip_safe=False,
    python_requires='>=3.7',
    package_dir={'primecountpy': 'primecountpy'},
    install_requires=["Cython"],
    package_data={"primecountpy": ["*.pxd"]},
    cmdclass={'build_ext': build_ext},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics']
    )

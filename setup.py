from setuptools import setup, find_packages
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext as _build_ext

class build_ext(_build_ext):
    def run(self):
        from Cython.Build.Dependencies import cythonize
        self.distribution.ext_modules[:] = cythonize(
            self.distribution.ext_modules,
            include_path = ["primecountpy"],
            compiler_directives={'embedsignature': True, 'binding': True},
            language_level=3)
        _build_ext.run(self)


with open('VERSION') as version_file:
    version = version_file.read().strip()


extensions = [
    Extension(
            "primecountpy.primecount",
            sources=["primecountpy/primecount.pyx"],
            language="c++",
            libraries=["primecount","primesieve"],
        ),
    ]

setup(
    version=version,
    packages=find_packages(),
    ext_modules=extensions,
    zip_safe=False,
    package_dir={'primecountpy': 'primecountpy'},
    package_data={"primecountpy": ["*.pxd"],
          "docs": ["*"], "docs.source": ["*"], "docs.source.modules": ["*"],
          },
    cmdclass={'build_ext': build_ext},
)

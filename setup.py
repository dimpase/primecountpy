from setuptools import setup, find_packages
from setuptools.extension import Extension
from distutils.command.build_ext import build_ext as du_build_ext

class build_ext(du_build_ext):
    def run(self):
        from Cython.Build.Dependencies import cythonize
        self.distribution.ext_modules[:] = cythonize(
            self.distribution.ext_modules,
            include_path = ["primecountpy"],
            compiler_directives={'embedsignature': True, 'binding': True},
            language_level=3)
        du_build_ext.run(self)


extensions = [
    Extension(
            "primecountpy.primecount",
            sources=["primecountpy/primecount.pyx"],
            language="c++",
            libraries=["primecount","primesieve"],
        ),
    ]

setup(
    packages=find_packages(),
    ext_modules=extensions,
    zip_safe=False,
    package_dir={'primecountpy': 'primecountpy'},
    package_data={"primecountpy": ["*.pxd"],
          "docs": ["*"], "docs.source": ["*"], "docs.source.modules": ["*"],
          },
    cmdclass={'build_ext': build_ext},
)

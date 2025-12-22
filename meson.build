project(
  'primecountpy',
  'cpp', 'cython',
  meson_version: '>=1.2.0'
)

# Python
py_module = import('python')
py = py_module.find_installation(pure: false)
py_dep = py.dependency()

# Compilers
cxx = meson.get_compiler('cpp')

py.install_sources(
  'src/primecountpy/__init__.py',
  'src/primecountpy/defs.pxd',
  subdir: 'primecountpy'
)

primecount_dep = dependency('primecount', required: true)
primesieve_dep = dependency('primesieve', required: true)

src = include_directories('src/primecountpy')

py.extension_module('primecount',
  files('src/primecountpy/primecount.pyx'),
  include_directories: [src],
  dependencies: [py_dep, primecount_dep, primesieve_dep],
  install: true,
  subdir: 'primecountpy'
)

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

primecount_dep = dependency('primecount', required: true)
inc_cysignals = run_command(
  py,
  [
    '-c',
    '''
from os.path import relpath
import cysignals
path = cysignals.__file__.replace('__init__.py', '')
try:
  print(relpath(path))
except Exception:
  print(path)
    '''.strip(),
  ],
  check: true,
).stdout().strip()
cysignals_dep = declare_dependency(include_directories: inc_cysignals)

py.install_sources(
  'src/primecountpy/__init__.py',
  'src/primecountpy/defs.pxd',
  subdir: 'primecountpy'
)

# Meson currently ignores include_directories for Cython modules, so we
# have to add them manually.
# https://github.com/mesonbuild/meson/issues/9562
add_project_arguments('-I', meson.current_source_dir() + '/src/primecountpy', language: 'cython')
add_project_arguments('-I', meson.current_build_dir() + '/src/primecountpy', language: 'cython')
src = include_directories('src/primecountpy')

py.extension_module('primecount',
  files('src/primecountpy/primecount.pyx'),
  include_directories: [src],
  dependencies: [py_dep, primecount_dep, cysignals_dep],
  override_options: ['cython_language=cpp'],
  install: true,
  subdir: 'primecountpy'
)

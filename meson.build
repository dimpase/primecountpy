project(
  'primecountpy',
  'cpp', 'cython',
  meson_version: '>=1.2.0'
)

# Python
py_module = import('python')
py = py_module.find_installation(pure: false)
py_dep = py.dependency()

# CMake subprojects
cmake = import('cmake')

# Compilers
cxx = meson.get_compiler('cpp')

primecount_dep = dependency('primecount', required: false, version: '>=8.0')
if not primecount_dep.found()
  # Build bundled primecount with PIC so it can link into the Python extension.
  primecount_opts = cmake.subproject_options()
  primecount_opts.add_cmake_defines({'CMAKE_POSITION_INDEPENDENT_CODE': 'ON'})
  primecount_proj = cmake.subproject('primecount', options: primecount_opts)
  primecount_dep = primecount_proj.dependency('libprimecount-static')
endif
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

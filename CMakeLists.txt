cmake_minimum_required(VERSION 3.15...3.27)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

find_package(Python 3.13 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(nanobind CONFIG REQUIRED)
find_package(PkgConfig REQUIRED)
pkg_check_modules(PRIMECOUNT primecount)

add_library(PRIMECOUNT::primecount UNKNOWN IMPORTED)
set_target_properties(PRIMECOUNT::primecount PROPERTIES IMPORTED_LOCATION "${PRIMECOUNT_LIBRARIES}")
set_target_properties(PRIMECOUNT::primecount PROPERTIES INTERFACE_INCLUDE_DIRSECTORIES "${PRIMECOUNT_INCLUDE_DIRS}")
 
nanobind_add_module(primecount NB_STATIC primecount.cpp)

install(TARGETS primecount LIBRARY DESTINATION .)

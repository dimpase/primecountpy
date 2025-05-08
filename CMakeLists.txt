cmake_minimum_required(VERSION 3.15...3.27)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

find_package(Python 3.13 REQUIRED COMPONENTS Interpreter Development.Module)
find_package(nanobind CONFIG REQUIRED)
find_package(PkgConfig REQUIRED)
#pkg_check_modules(primecount primecount)

#add_library(primecount UNKNOWN IMPORTED)
#set_target_properties(PRIMECO PROPERTIES IMPORTED_LOCATION "${PRIMECOUNT_LIBRARIES}")
#set_target_properties(PRIMECO PROPERTIES INTERFACE_INCLUDE_DIRECTORIES "${PRIMECOUNT_INCLUDE_DIRS}")

#target_link_libraries(primecount INTERFACE "${PRIMECOUNT_LIBRARIES}")
#install(TARGETS ${SKBUILD_PROJECT_NAME} LIBRARY DESTINATION .)
nanobind_add_module(primecountpy NB_STATIC primecount.cpp)
install(TARGETS primecountpy LIBRARY DESTINATION .)

target_link_libraries(primecountpy PRIVATE primecount)

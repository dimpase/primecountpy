# distutils: libraries = primesieve primecount
# distutils: language = c++

from libc.stdint cimport int64_t, uint64_t
from libcpp.string cimport string as cppstring

cdef extern from "primecount.hpp" namespace "primecount":
    ctypedef struct pc_int128_t:
        uint64_t lo
        int64_t hi

    int64_t pi(int64_t x)

    pc_int128_t pi(const pc_int128_t x)

    int64_t nth_prime(int64_t n)

    int64_t phi(int64_t x, int64_t a)

    void set_num_threads(int num_threads)
    int get_num_threads()

    cppstring primecount_version()

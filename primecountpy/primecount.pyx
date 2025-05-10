r"""
Interface to the `primecount <https://github.com/kimwalisch/primecount>`_ C++ library
"""
#*****************************************************************************
#       Copyright (C) 2018 Vincent Delecroix <20100.delecroix@gmail.com>
#       Copyright (C) 2021 Dima Pasechnik <dima@pasechnik.info>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from libc.stdint cimport int64_t
from libcpp.string cimport string as cppstring
from cpython.long cimport PyLong_FromString

from cysignals.signals cimport sig_on, sig_off
cimport defs as pcount

cdef inline int _do_sig(int64_t n):
    "threshold for sig_on/sig_off"
    return n >> 26

cpdef int64_t prime_pi(int64_t n, method=None) except -1:
    r"""
    Return the number of prime numbers smaller or equal than ``n``.

    INPUT:

    - ``n`` - an integer

    EXAMPLES:

    ::

        >>> from primecountpy.primecount import prime_pi
        >>> prime_pi(1000) == 168
        True

    `method` has no effect, retained for compatibility::

        >>> prime_pi(1000, method='deleglise_rivat') == 168
        True
    """
    cdef int64_t ans
    if _do_sig(n): sig_on()
    ans = pcount.pi(n)
    if _do_sig(n): sig_off()
    return ans

cpdef prime_pi_128(n):
    r"""
    Return the number of prime number smaller than ``n``.

    EXAMPLES::

        >>> from primecountpy.primecount import prime_pi_128

        >>> prime_pi_128(1000)
        168
        >>> prime_pi_128(10**10)
        455052511
    """
    cdef cppstring s = str(n).encode('ascii')
    cdef bytes ans
    sig_on()
    ans = pcount.pi(s)
    sig_off()
    return PyLong_FromString(ans, NULL, 10)

cpdef int64_t nth_prime(int64_t n) except -1:
    r"""
    Return the ``n``-th prime integer.

    EXAMPLES::

        >>> from primecountpy.primecount import nth_prime

        >>> nth_prime(168) == 997
        True
    """
    if n <= 0:
        raise ValueError("n must be positive")

    cdef int64_t ans
    if _do_sig(n): sig_on()
    ans = pcount.nth_prime(n)
    if _do_sig(n): sig_off()
    return ans

cpdef int64_t phi(int64_t x, int64_t a):
    r"""
    Return the number of integers smaller or equal than ``x`` by any of the
    first ``a`` primes.

    This is sometimes called a "partial sieve function" or "Legendre-sum".

    EXAMPLES::

         >>> from primecountpy.primecount import phi

         >>> phi(1000, 3) == 266
         True
         >>> phi(2**30, 100) == 95446716
         True
    """
    return pcount.phi(x, a)

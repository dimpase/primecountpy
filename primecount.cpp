#include <nanobind/nanobind.h>
#include <primecount.hpp>

namespace nb = nanobind;

template <typename T> pi_t(T& x) {
   return primecount::pi(x);
}

NB_MODULE(primecount, m) {
    m.def("pi", &<std::string>pi_t);
    m.def("pi", &<int64_t>pi_t);
}


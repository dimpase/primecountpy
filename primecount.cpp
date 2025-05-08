#include <nanobind/nanobind.h>
#include <primecount.hpp>
#include <string>

namespace nb = nanobind;

template <typename T, typename R> R pit(T& x) {
   return primecount::pi(x);
}

NB_MODULE(primecountpy, m) {
    m.def("pi", &pit<std::string&, std::string>);
    m.def("pi", &pit<int64_t, int64_t>);
}


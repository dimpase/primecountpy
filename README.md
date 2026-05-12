# Primecount Cython interface

This is a Cython interface to the C++ library [primecount](https://github.com/kimwalisch/primecount).

We have split out primecount [SageMath](https://sagemath.org) spkg with its Cython interface.

Quick installation and testing:

1) Install primecount C++ library
```
cd /tmp/
git clone https://github.com/kimwalisch/primecount
cd primecount
cmake . -DBUILD_SHARED_LIBS=ON
make -j
sudo make install
sudo ldconfig # linux only
```
2) In this repo, do
```
pip install . --user --config-settings=setup-args="--wrap-mode=nodownload"
```
3) Test with `pytest`
```
pytest
```

Alternatively, if you built with Meson, you can run tests via:
```
meson test -v -C builddir
```
where `builddir` is your Meson build directory.

4)

`python3`
and
```
>>> import primecountpy as primecount
>>> primecount.prime_pi(1000)
```

More details on installation without root (sudo) access
may be found in the [manual](https://primecountpy.readthedocs.io),
which is also included in `docs`.

## License

Distributed under the terms of the [GNU General Public
License](./LICENSE) (GPL) as published by the [Free Software
Foundation](https://www.fsf.org/); either version 2 of the License,
or (at your option) any later version.

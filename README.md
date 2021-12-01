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
2) in this repo, do
```
python3 setup.py install --user
```
3)

`python3`
and
```
>>> import primecountpy as primecount
>>> primecount.pi(1000)
```

More details on installation without root (sudo) access,
and testing with `pytest`, may be found in the [manual](https://primecountpy.readthedocs.io).

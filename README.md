# Primecount Cython interface

WIP on splitting out primecount Sage spkg with its cython interface

testing:

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

## Building dependencies without root:

set the desired location, e.g. export WDIR=$HOME/tmp

install libprimesieve as follows:
```
cd primesieve
cmake -DBUILD_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=$WDIR .
make -j  install     # no sudo!
```
install primecount as follows
```
cmake -DBUILD_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=$WDIR \
      -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE  -DCMAKE_INSTALL_RPATH=$WDIR \
      -DCMAKE_SKIP_BUILD_RPATH=FALSE  -DBUILD_LIBPRIMESIEVE=OFF  \
      -DCMAKE_FIND_ROOT_PATH=$WDIR/lib/cmake  \
      -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY .
make -j install # no sudo!
```

TODO:

$WDIR will need to be passed to `setup.py`

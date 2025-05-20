# Installation, testings, documentation 

Assume you have cloned the repository from GitHub, or
installed the package source from an archive, e.g. from [PyPI](https://pypi.org/project/primecountpy/).

## testing:

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

Note that `primecount` may be available as a system-wide package on your
system, and then one can install it and avoid building it from source.  E.g. on
Fedora Linux (version 34 or newer) one just has to run 
```
sudo dnf install primecount primecount-devel`
```

2) in this repo, do
```
pip install . --user
```
3)

`python3`
and
```
>>> import primecountpy as primecount
>>> primecount.pi(1000)
```


## Building dependencies without root

set the desired location, e.g.
```
export WDIR=$HOME/tmp
```

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

After this, build/install the package with `pip`
```
pip3 install -e . --prefix=~/.local --global-option=build_ext  --global-option="--library-dirs=$WDIR" --global-option="--rpath=$WDIR"
```

At this point, you can test it with `pytest` (see below for details on `pytest`)

```
pytest --doctest-cython primecountpy -v
```

## Testing with pytest

install pre-requisites:

```
pip3 install pytest pytest-cython
```

Clean up, and build in-place (with system-wide install of primecount).

```
git clean -fdx
pip install -e . 
pytest --doctest-cython primecountpy -v
```

## Documentation

Documentation is built with Sphinx, and automatically (on push to GitHub git repo)
re-built and updates. 

To build documentation locally, run `make html` in `docs/` subdirectory.

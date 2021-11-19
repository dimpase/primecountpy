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
sudo ldconfig
```
2) in this repo, do
```
python3 setup.py install --user
```
3)

`python3`
and
```
>>> import primecount
>>> primecount.pi(1000) # not working yet
```

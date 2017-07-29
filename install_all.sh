sudo apt-get install g++ make automake autoconf libtool libatlas-base-dev
sudo apt-get install automake autoconf libtool
make -f Makefile.git

./configure --without-lapack
make -j 4
sudo make install



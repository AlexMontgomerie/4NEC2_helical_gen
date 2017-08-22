export NECPP_SRC_PATH=~/Desktop/antennaDesign/necpp/src

cd cpp

make -j4

echo 'compile end'

cd ../python

python grapher.py "../cpp/out.txt"

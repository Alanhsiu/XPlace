cd build
cmake -DPYTHON_EXECUTABLE=$(which python) ..
make -j40 && make install
cd ..
python main_test_gr.py
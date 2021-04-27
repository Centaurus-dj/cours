#! bin/bash

sudo dnf install libxml2-devel.x86_64
sudo dnf install libsqlite3x-devel.x86_64
cd libs/php/linux/
./configure
make -j4
sudo make install
cd ../../../
# Global Matting Algorithm with Cython Interface

This is an global matting algorithm based on [this repository](https://github.com/atilimcetin/global-matting). Its core algorithms are written in c++ to guarantee the speed, and it provides a python interface to integrate it with other data processing methods. Paper of the algorithm:

He, Kaiming, et al. ["A global sampling method for alpha matting."](http://kaiminghe.com/publications/cvpr11matting.pdf) In CVPR’11, pages 2049–2056, 2011.

Together, with an implementation of Cython wrapper to allow the convertion between a `numpy.array` and a `cv::Mat` and the other way arround (`cv::Mat` to `numpy.array`). The Cython wrapper is based on [this repository](https://github.com/solivr/cython_opencvMat).

## Build

First, specify your opencv library path in `setup.py:line 10-13`. For me, the opencv library is in `/usr/lib/x86_64-linux-gnu` and the `prefix` is `/usr`. Note that the `prefix` will be useful again in `setup.py:line 30` for the opencv include path.

To build, run `python3 setup.py build_ext --inplace` and ignore any warnings.

When building is complete, test the algorithm via `python3 test.py`.

You should see a `GT04-alpha.png` with good matting result.

## Environment Settings (Linux)

To build this code, OpenCV (C++ version) is needed. If user has been installed OpenCV before, it is OK to follow instructions in [bulid](#build) or simply use `pip install opencv-mat`. Otherwise, user should install OpenCV. We show how to install OpenCV in [Conda](#Conda-(Recommand)) (*Recommand*) or in [System](#System) below. 

### Conda (Recommand)

If users only use OpenCV (C++ Version) for this package, we highly recommand using conda environment. To install Conda, users may search in this [website](https://www.anaconda.com/) or other versions of conda. Here is an [instruction](https://problemsolvingwithpython.com/01-Orientation/01.05-Installing-Anaconda-on-Linux/).

After installing Conda, users may easily following commands below to install this package. 
```
conda create -n environment_name -python=3.x
conda activate environment_name
conda install -c salilab opencv-nopython        # opencv2
conda install -c serge-sans-paille gcc_49       # you need to use conda's gcc instead of system's
ln -s ~/miniconda3/envs/environment_name/bin/g++-4.9 ~/miniconda3/envs/environment_name/bin/g++   #link to bin
ln -s ~/miniconda3/envs/environment_name/bin/gcc-4.9 ~/miniconda3/envs/environment_name/bin/gcc   #link to bin
pip install cython numpy
pip install opencv-mat
```

### System

If users may want to use OpenCV (C++ Version) for any other purpose, we also give an instruction here to help install OpenCV in Ubuntu 16.04. (Other Linux systems may be similar)

```
sudo apt-get install cmake build-essential                                     # install compile tools
sudo apt-get install libgtk2.0-dev pkg-config \
    libavcodec-dev libavformat-dev libswscale-dev                              # install dependency packages
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev \
    libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev                      # install optional dependency packages

wget https://github.com/opencv/opencv/archive/2.4.13.6.zip                     # download opencv source code, other versions are in https://opencv.org/releases/
unzip opencv-2.4.13.zip
cd opencv-2.4.13
mkdir release
cd release

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..     
make -j4                                                                       # -j4 means jobs=4, users can set jobs according to cpu threads
sudo make install                                                              # install opencv in your computer, whether `sudo` is needed depends on CMAKE_INSTALL_PREFIX
```

Here, `CMAKE_INSTALL_PREFIX` can be set to other paths. However, we recommand `/usr/local` or `/usr` since our code and may other projects use this path as default. 

After installing OpenCV, users need to setup PATH. 

First, run `sudo vim /etc/ld.so.conf.d/opencv.conf`, add `CMAKE_INSTALL_PREFIX/lib` (e.g. `/usr/lib`) in this file and save, then run `sudo ldconfig` to activate. 

Second, run `sudo vim /etc/bash.bashrc`, add this in the end of the file and save.
```
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:CMAKE_INSTALL_PREFIX/lib/pkgconfig
export PKG_CONFIG_PATH
```

Finally, run 
```
su      # input password
source /etc/bash.bashrc
exit
sudo updatedb
```

Users can check using these commands. 
```
ldconfig -p | grep libopencv
pkg-config --cflags opencv
```

After that, users can install our package using
```
pip install opencv-mat
```

## Tested Environments

|  Pass  |     Linux     |  python  |  opencv  |
|  ----  |     -----     |  ------  |  ------  |
|    √   |  Ubuntu16.04  |   3.5    |   2.4    |
|    √   |  Ubuntu16.04  |   3.6    |   2.4    |
|    ×   |  Ubuntu16.04  |    *     |   3.x    |

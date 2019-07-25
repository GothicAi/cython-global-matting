from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import sys
import os
from setuptools import find_packages

libs = os.popen('ldconfig -p | grep libopencv')
libs = libs.readlines()
lib_paths = [l.split('=>')[-1].strip('\n').strip(' ') for l in libs]

# Find opencv libraries in lib_folder
cvlibs = list()
lib_folders = set()
for file in lib_paths:
    file_split = file.split('.')
    cvlibs.append(file_split[0])
    lib_folders.add(file.split('libopencv')[0])
lib_folders = list(lib_folders)
cvlibs = list(set(cvlibs))
cvlibs = ['-L{}'.format(lib_folder) for lib_folder in lib_folders] + \
         ['opencv_{}'.format(lib.split(os.path.sep)[-1].split('libopencv_')[-1]) for lib in cvlibs]

setup(
    name='global_matting',
    version='0.1',
    description='A cython interface for paper: A global sampling method for alpha matting',
    author='Runzhong Wang, Jianhua Sun, Haoshu Fang, Minghao Gou',
    author_email='1751196720@qq.com',
    url='https://github.com/GothicAi/cython-global-matting',
    packages=find_packages(where='../', exclude=(), include=('*',)),
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(Extension("opencv_mat",
                                    sources=["opencv_mat.pyx", "globalmatting.cpp", "guidedfilter.cpp"],
                                    language="c++",
                                    include_dirs=[numpy.get_include(),
                                                  os.path.join('/usr', 'include', 'opencv2'),
                                                 ],
                                    library_dirs=lib_folders,
                                    libraries=cvlibs,
                                    )
                          )
)

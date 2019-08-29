from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import sys
import os
import subprocess
import sys
import glob

pthlist = []

# search in python(conda) folder
lib_folder = os.path.join(sys.prefix, 'lib')

# Find opencv libraries in lib_folder
cvlibs = list()
for file in glob.glob(os.path.join(lib_folder, 'libopencv_*')):
    cvlibs.append(file.split('.')[0])
cvlibs = list(set(cvlibs))
cvlibs = ['-L{}'.format(lib_folder)] + \
         ['opencv_{}'.format(lib.split(os.path.sep)[-1].split('libopencv_')[-1]) for lib in cvlibs]

conda_path = os.path.join(sys.prefix, 'include', 'opencv2')
if os.path.exists(conda_path):
    pthlist.append(conda_path)
lib_folders = [lib_folder]

if not pthlist:
    # search in system folder
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

    # Find opencv.hpp in include_folder
    proc_incs = subprocess.check_output("pkg-config --cflags opencv".split())
    proc_incs = str(proc_incs, 'utf-8').split()

    for i in range(len(proc_incs)):
        proc_incs[i] = proc_incs[i][2:]
        if proc_incs[i].split('/')[-1] == 'opencv':
            proc_incs[i] = proc_incs[i][:-7]
    proc_incs = list(set(proc_incs))
    for inc in proc_incs:
        inc = inc+'/opencv2'
        if os.path.exists(inc):
            break

    default_path = os.path.join('/usr/include/opencv2')
    default_local_path = os.path.join('/usr/local/include/opencv2')

    if os.path.exists(default_path):
        pthlist.append(default_path)
    if os.path.exists(default_path):
        pthlist.append(default_local_path)
    if os.path.exists(inc):
        pthlist.append(inc)


assert pthlist, 'opencv headers not found, you may refer this doc in [] to solve this error.'
assert cvlibs, 'opencv libs not found, you may refer this doc in [] to solve this error.'

setup(
    name='opencv_mat',
    version='0.1',
    description='A cython interface for paper: A global sampling method for alpha matting',
    author='Runzhong Wang, Jianhua Sun, Haoshu Fang, Minghao Gou',
    author_email='1751196720@qq.com',
    url='https://github.com/GothicAi/cython-global-matting',
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(Extension("opencv_mat",
                                    sources=["opencv_mat.pyx", "globalmatting.cpp", "guidedfilter.cpp"],
                                    language="c++",
                                    include_dirs=[numpy.get_include(),
                                                  pthlist[0]
                                                 ],
                                    library_dirs=lib_folders,
                                    libraries=cvlibs,
                                    ),
                            compiler_directives={'language_level' : "3"}
                          )
)
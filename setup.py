from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import sys
import os
import subprocess
import sys

lib_folders = ['lib']

cvlibs = ['opencv_gpu', 'opencv_xobjdetect', 'opencv_aruco', 'opencv_cudabgsegm', 'opencv_xfeatures2d', \
    'opencv_ccalib', 'opencv_cudafilters', 'opencv_cudafilters', 'opencv_cvv', 'opencv_cudev', 'opencv_saliency', \
    'opencv_imgproc', 'opencv_saliency', 'opencv_ml', 'opencv_ml', 'opencv_cvv', 'opencv_cudev', 'opencv_photo', \
    'opencv_bgsegm', 'opencv_rgbd', 'opencv_calib3d', 'opencv_bioinspired', 'opencv_videostab', 'opencv_structured_light', \
    'opencv_optflow', 'opencv_cudalegacy', 'opencv_fuzzy', 'opencv_cudaoptflow', 'opencv_datasets', 'opencv_contrib', \
    'opencv_reg', 'opencv_face', 'opencv_viz', 'opencv_ml', 'opencv_highgui', 'opencv_cudaarithm', 'opencv_xobjdetect', \
    'opencv_cudawarping', 'opencv_rgbd', 'opencv_xphoto', 'opencv_dnn', 'opencv_optflow', 'opencv_flann', 'opencv_freetype', \
    'opencv_imgproc', 'opencv_nonfree', 'opencv_gpu', 'opencv_calib3d', 'opencv_xfeatures2d', 'opencv_flann', 'opencv_reg', \
    'opencv_surface_matching', 'opencv_freetype', 'opencv_ximgproc', 'opencv_objdetect', 'opencv_surface_matching', 'opencv_photo', \
    'opencv_tracking', 'opencv_imgcodecs', 'opencv_core', 'opencv_videoio', 'opencv_flann', 'opencv_calib3d', 'opencv_face', \
    'opencv_aruco', 'opencv_video', 'opencv_cudaimgproc', 'opencv_stereo', 'opencv_plot', 'opencv_cudafeatures2d', 'opencv_features2d', \
    'opencv_shape', 'opencv_hdf', 'opencv_stereo', 'opencv_cudastereo', 'opencv_cudacodec', 'opencv_cudaimgproc', 'opencv_cudaarithm', \
    'opencv_datasets', 'opencv_cudalegacy', 'opencv_ocl', 'opencv_ximgproc', 'opencv_superres', 'opencv_hdf', 'opencv_legacy', 'opencv_ccalib', \
    'opencv_shape', 'opencv_dpm', 'opencv_videoio', 'opencv_cudawarping', 'opencv_video', 'opencv_superres', 'opencv_legacy', 'opencv_imgproc', \
    'opencv_cudaoptflow', 'opencv_cudabgsegm', 'opencv_core', 'opencv_stitching', 'opencv_fuzzy', 'opencv_features2d', 'opencv_highgui', 'opencv_core', \
    'opencv_objdetect', 'opencv_bgsegm', 'opencv_viz', 'opencv_contrib', 'opencv_xphoto', 'opencv_cudastereo', 'opencv_highgui', 'opencv_cudaobjdetect', \
    'opencv_videostab', 'opencv_stitching', 'opencv_text', 'opencv_cudacodec', 'opencv_ocl', 'opencv_cudafeatures2d', 'opencv_superres', 'opencv_dnn', \
    'opencv_nonfree', 'opencv_cudaobjdetect', 'opencv_objdetect', 'opencv_stitching', 'opencv_phase_unwrapping', 'opencv_dpm', 'opencv_imgcodecs', \
    'opencv_videostab', 'opencv_structured_light', 'opencv_bioinspired', 'opencv_phase_unwrapping', 'opencv_line_descriptor', 'opencv_features2d', \
    'opencv_tracking', 'opencv_line_descriptor', 'opencv_photo', 'opencv_text', 'opencv_plot', 'opencv_video', 'opencv_ts']

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
                                                  'opencv2'
                                                 ],
                                    library_dirs=lib_folders,
                                    libraries=cvlibs,
                                    ),
                            compiler_directives={'language_level' : "3"}
                          )
)
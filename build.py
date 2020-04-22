from setuptools import Extension
from Cython.Build import cythonize
from setuptools.dist import Distribution

try:
    from Cython.Build import cythonize
except:
    use_cython = False
    ext = 'c'
    ext_pp = 'cpp'
else:
    use_cython = True
    ext = ext_pp = 'pyx'

cyfuncs_ext = Extension(name='cyrtd.cymod.cyfuncs',
                        sources=['cyrtd/cymod/cyfuncs.' + ext]
                        )

EXTENSIONS = [
    cyfuncs_ext
]

if use_cython:
    EXTENSIONS = cythonize(EXTENSIONS, language_level=3)

def build(setup_kwargs):
    setup_kwargs.update({
        'ext_modules': EXTENSIONS,
        'zip_safe': False,
    })

def build_extensions():
    """
    Function for building extensions inplace for docs and tests
    :return:
    """
    build_params = {}
    build(build_params)
    dist = Distribution(attrs=build_params)
    build_clib_cmd = dist.get_command_obj('build_clib')
    build_clib_cmd.ensure_finalized()
    build_clib_cmd.run()
    build_ext_cmd = dist.get_command_obj('build_ext')
    build_ext_cmd.ensure_finalized()
    build_ext_cmd.inplace = 1
    build_ext_cmd.run()

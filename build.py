from setuptools import Extension
from Cython.Build import cythonize

cyfuncs_ext = Extension(name='cyrtd.cymod.cyfuncs',
                        sources=['cyrtd/cymod/cyfuncs.pyx']
                        )

EXTENSIONS = [
    cyfuncs_ext
]


def build(setup_kwargs):
    setup_kwargs.update({
        'ext_modules': cythonize(EXTENSIONS, language_level=3),
        'zip_safe': False,
    })

from setuptools import setup, Extension
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

v4r_path = "/nethome/ewijmans3/projects/fast-rl-renderer/v4r"
include_dir = v4r_path + "/build/include"
lib_dir = v4r_path + "/build/src"

setup(
    name="v4r_example",
    ext_modules=[
        CUDAExtension(
            name="v4r_example",
            sources=["v4r_example.cpp"],
            extra_compile_args=[f"-I{include_dir}"],
            extra_link_args=[
                f"-L{lib_dir}",
                "-lv4r",
                "-Wl,--no-as-needed",
                "-lv4r_headless_hacks",
                f"-Wl,-rpath={lib_dir}",
            ],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)

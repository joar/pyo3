import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


def get_env_bool(key, default=None):
    value = os.environ.get(key)
    if value is None:
        return default

    if value.lower() in ("true", "1"):
        return True
    elif value.lower() in ("false", "0", ""):
        return False
    else:
        raise ValueError(
            f"Could not parse environment variable {key}'s value {value} as "
            f"bool "
        )

try:
    from setuptools_rust import RustExtension, Binding
except ImportError:
    import subprocess

    errno = subprocess.call(
        [sys.executable, "-m", "pip", "install", "setuptools-rust"]
    )
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension, Binding


class PyTest(TestCommand):
    user_options = []

    def run(self):
        self.run_command("test_rust")

        import subprocess
        import sys

        errno = subprocess.call([sys.executable, "-m", "pytest", "tests"])
        raise SystemExit(errno)


setup_requires = ["setuptools-rust>=0.10.1"]
install_requires = []
tests_require = install_requires + ["pytest", "pytest-benchmark"]

LONG_DESCRIPTION = None

try:
    LONG_DESCRIPTION = open("README.rst").read()
except Exception:
    pass

setup(
    name="vergil",
    author="Joar Wandborg",
    author_email="joar@wandborg.se",
    url="https://github.com/joar/rust-csv-py",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    packages=find_packages(),
    rust_extensions=[
        RustExtension(
            "vergil.vergil",
            "Cargo.toml",
            native=True,
        )
    ],
    tests_require=tests_require,
    setup_requires=setup_requires,
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass=dict(test=PyTest),
)

from setuptools import setup, find_packages

setup(name="mocksurvey",
      version="0.0.1.dev9",
      description="Some useful tools for conducting realistic "
                  "mock surveys out of galaxies populated by `halotools` "
                  "and `UniverseMachine` models.",
      url="http://github.com/AlanPearl/mocksurvey",
      author="Alan Pearl",
      author_email="alanpearl@pitt.edu",
      license="MIT",
      packages=find_packages(),
      python_requires=">=3.8",
      install_requires=[
            "wget",
            "h5py",
            "numpy",
            "scipy",
            "pandas",
            "astropy",
            "scikit-learn",
            "packaging",
            "halotools>=0.7",
            "tqdm",
            # "colossus",
            # "Corrfunc",
            # "emcee>=3",
            # "mpi4py",
            # "schwimmbad",
            # "corner",
            # "matplotlib",
      ],
      zip_safe=True,
      )

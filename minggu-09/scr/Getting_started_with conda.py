# Managing conda
## Verify that conda is installed and running on your system by typing:
(base) C:\Users\acer>conda --version
conda 4.12.0

##Update conda to the current version. Type the following:
(base) C:\Users\acer>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\acer\anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    ------------------------------------------------------------
                                           Total:         729 KB

The following packages will be UPDATED:

  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-package-handli | 729 KB    | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

# Managing environments
## Create a new environment and install a package in it.
(base) C:\Users\acer>conda create --name snowflakes biopython
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\acer\anaconda3\envs\snowflakes

  added / updated specs:
    - biopython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    biopython-1.78             |   py39h2bbff1b_0         2.1 MB
    ca-certificates-2022.3.29  |       haa95532_0         122 KB
    certifi-2021.10.8          |   py39haa95532_2         152 KB
    numpy-1.21.5               |   py39h7a0a035_1          25 KB
    numpy-base-1.21.5          |   py39hca35cd5_1         4.4 MB
    openssl-1.1.1n             |       h2bbff1b_0         4.8 MB
    python-3.9.12              |       h6244533_0        17.1 MB
    setuptools-61.2.0          |   py39haa95532_0         1.0 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.38.2              |       h2bbff1b_0         807 KB
    tzdata-2022a               |       hda174b7_0         109 KB
    wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
    ------------------------------------------------------------
                                           Total:        30.7 MB

The following NEW packages will be INSTALLED:

  biopython          pkgs/main/win-64::biopython-1.78-py39h2bbff1b_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  numpy              pkgs/main/win-64::numpy-1.21.5-py39h7a0a035_1
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py39hca35cd5_1
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
biopython-1.78       | 2.1 MB    | ####################################### | 100%
wheel-0.37.1         | 33 KB     | ####################################### | 100%
tzdata-2022a         | 109 KB    | ####################################### | 100%
ca-certificates-2022 | 122 KB    | ####################################### | 100%
six-1.16.0           | 18 KB     | ####################################### | 100%
sqlite-3.38.2        | 807 KB    | ####################################### | 100%
setuptools-61.2.0    | 1.0 MB    | ####################################### | 100%
certifi-2021.10.8    | 152 KB    | ####################################### | 100%
numpy-1.21.5         | 25 KB     | ####################################### | 100%
python-3.9.12        | 17.1 MB   | ####################################### | 100%
numpy-base-1.21.5    | 4.4 MB    | ####################################### | 100%
openssl-1.1.1n       | 4.8 MB    | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snowflakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate

## To see a list of all your environments, type:
(base) C:\Users\acer>conda info --envs
# conda environments:
#
base                  *  C:\Users\acer\anaconda3
snowflakes               C:\Users\acer\anaconda3\envs\snowflakes





#Managing Python
## Create a new environment named "snakes" that contains Python 3.9:
(base) C:\Users\acer>conda create --name snakes python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\acer\anaconda3\envs\snakes

  added / updated specs:
    - python=3.9


The following NEW packages will be INSTALLED:

  ca-certificates    pkgs/main/win-64::ca-certificates-2022.3.29-haa95532_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_2
  openssl            pkgs/main/win-64::openssl-1.1.1n-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  python             pkgs/main/win-64::python-3.9.12-h6244533_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py39haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.2-h2bbff1b_0
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate snakes
#
# To deactivate an active environment, use
#
#     $ conda deactivate


##Verify that the snakes environment has been added and is active:
(base) C:\Users\acer>conda info --envs
# conda environments:
#
base                  *  C:\Users\acer\anaconda3
snakes                   C:\Users\acer\anaconda3\envs\snakes
snowflakes               C:\Users\acer\anaconda3\envs\snowflakes


## Verify which version of Python is in your current environment:
(base) C:\Users\acer>python --version
Python 3.9.7


#Managing packages
#Check to see if a package you have not installed named "beautifulsoup4" is available from the Anaconda repository (must be connected to the Internet):
(base) C:\Users\acer>conda search beautifulsoup4
Loading channels: done
# Name                       Version           Build  Channel
beautifulsoup4                 4.6.0          py27_1  pkgs/main
beautifulsoup4                 4.6.0  py27hc287451_1  pkgs/main
beautifulsoup4                 4.6.0          py35_1  pkgs/main
beautifulsoup4                 4.6.0  py35h61fcdcc_1  pkgs/main
beautifulsoup4                 4.6.0          py36_1  pkgs/main
beautifulsoup4                 4.6.0  py36hd4cc5e8_1  pkgs/main
beautifulsoup4                 4.6.0          py37_1  pkgs/main
beautifulsoup4                 4.6.1          py27_0  pkgs/main
beautifulsoup4                 4.6.1          py35_0  pkgs/main
beautifulsoup4                 4.6.1          py36_0  pkgs/main
beautifulsoup4                 4.6.1          py37_0  pkgs/main
beautifulsoup4                 4.6.3          py27_0  pkgs/main
beautifulsoup4                 4.6.3          py35_0  pkgs/main
beautifulsoup4                 4.6.3          py36_0  pkgs/main
beautifulsoup4                 4.6.3          py37_0  pkgs/main
beautifulsoup4                 4.7.1          py27_1  pkgs/main
beautifulsoup4                 4.7.1          py36_1  pkgs/main
beautifulsoup4                 4.7.1          py37_1  pkgs/main
beautifulsoup4                 4.8.0          py27_0  pkgs/main
beautifulsoup4                 4.8.0          py36_0  pkgs/main
beautifulsoup4                 4.8.0          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py27_0  pkgs/main
beautifulsoup4                 4.8.1          py36_0  pkgs/main
beautifulsoup4                 4.8.1          py37_0  pkgs/main
beautifulsoup4                 4.8.1          py38_0  pkgs/main
beautifulsoup4                 4.8.2          py27_0  pkgs/main
beautifulsoup4                 4.8.2          py36_0  pkgs/main
beautifulsoup4                 4.8.2          py37_0  pkgs/main
beautifulsoup4                 4.8.2          py38_0  pkgs/main
beautifulsoup4                 4.9.0          py36_0  pkgs/main
beautifulsoup4                 4.9.0          py37_0  pkgs/main
beautifulsoup4                 4.9.0          py38_0  pkgs/main
beautifulsoup4                 4.9.1          py36_0  pkgs/main
beautifulsoup4                 4.9.1  py36haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py37_0  pkgs/main
beautifulsoup4                 4.9.1  py37haa95532_0  pkgs/main
beautifulsoup4                 4.9.1          py38_0  pkgs/main
beautifulsoup4                 4.9.1  py38haa95532_0  pkgs/main
beautifulsoup4                 4.9.1  py39haa95532_0  pkgs/main
beautifulsoup4                 4.9.3    pyha847dfd_0  pkgs/main
beautifulsoup4                 4.9.3    pyhb0f4dca_0  pkgs/main
beautifulsoup4                4.10.0    pyh06a4308_0  pkgs/main


##Install this package into the current environment:
(base) C:\Users\acer>conda install beautifulsoup4
Collecting package metadata (current_repodata.json): done
Solving environment: done

# All requested packages already installed.

##Check to see if the newly installed program is in this environment:
(base) C:\Users\acer>conda list
# packages in environment at C:\Users\acer\anaconda3:
#
# Name                    Version                   Build  Channel
_ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
alabaster                 0.7.12             pyhd3eb1b0_0
anaconda                  2021.11                  py39_0
anaconda-client           1.9.0            py39haa95532_0
anaconda-navigator        2.1.1                    py39_0
anaconda-project          0.10.1             pyhd3eb1b0_0
anyio                     2.2.0            py39haa95532_2
appdirs                   1.4.4              pyhd3eb1b0_0
argh                      0.26.2           py39haa95532_0
argon2-cffi               20.1.0           py39h2bbff1b_1
arrow                     0.13.1           py39haa95532_0
asn1crypto                1.4.0                      py_0
astroid                   2.6.6            py39haa95532_0
astropy                   4.3.1            py39hc7d831d_0
async_generator           1.10               pyhd3eb1b0_0
atomicwrites              1.4.0                      py_0
attrs                     21.2.0             pyhd3eb1b0_0
autopep8                  1.5.7              pyhd3eb1b0_0
babel                     2.9.1              pyhd3eb1b0_0
backcall                  0.2.0              pyhd3eb1b0_0
backports                 1.0                pyhd3eb1b0_2
backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
backports.shutil_get_terminal_size 1.0.0              pyhd3eb1b0_3
backports.tempfile        1.0                pyhd3eb1b0_1
backports.weakref         1.0.post1                  py_1
bcrypt                    3.2.0            py39h196d8e1_0
beautifulsoup4            4.10.0             pyh06a4308_0
binaryornot               0.4.4              pyhd3eb1b0_1
bitarray                  2.3.0            py39h2bbff1b_1
bkcharts                  0.2              py39haa95532_0
black                     19.10b0                    py_0
blas                      1.0                         mkl
bleach                    4.0.0              pyhd3eb1b0_0
blosc                     1.21.0               h19a0ad4_0
bokeh                     2.4.1            py39haa95532_0
boto                      2.49.0           py39haa95532_0
bottleneck                1.3.2            py39h7cc1a96_1
brotli                    1.0.9                ha925a31_2
brotlipy                  0.7.0           py39h2bbff1b_1003
bzip2                     1.0.8                he774522_0
ca-certificates           2021.10.26           haa95532_2
cached-property           1.5.2                      py_0
certifi                   2021.10.8        py39haa95532_0
cffi                      1.14.6           py39h2bbff1b_0
cfitsio                   3.470                he774522_6
chardet                   4.0.0           py39haa95532_1003
charls                    2.2.0                h6c2663c_0
charset-normalizer        2.0.4              pyhd3eb1b0_0
click                     8.0.3              pyhd3eb1b0_0
cloudpickle               2.0.0              pyhd3eb1b0_0
clyent                    1.2.2            py39haa95532_1
colorama                  0.4.4              pyhd3eb1b0_0
colourmap                 1.1.4                    pypi_0    pypi
comtypes                  1.1.10          py39haa95532_1002
conda                     4.12.0           py39haa95532_0
conda-build               3.21.6           py39haa95532_0
conda-content-trust       0.1.1              pyhd3eb1b0_0
conda-env                 2.6.0                         1
conda-pack                0.6.0              pyhd3eb1b0_0
conda-package-handling    1.8.1            py39h8cc25b3_0
conda-repo-cli            1.0.4              pyhd3eb1b0_0
conda-token               0.3.0              pyhd3eb1b0_0
conda-verify              3.4.2                      py_1
console_shortcut          0.1.1                         4
contextlib2               0.6.0.post1        pyhd3eb1b0_0
cookiecutter              1.7.2              pyhd3eb1b0_0
cryptography              3.4.8            py39h71e12ea_0
curl                      7.78.0               h86230a5_0
cycler                    0.10.0           py39haa95532_0
cython                    0.29.24          py39h604cdb4_0
cytoolz                   0.11.0           py39h2bbff1b_0
daal4py                   2021.3.0         py39h757b272_0
dal                       2021.3.0           haa95532_564
dask                      2021.10.0          pyhd3eb1b0_0
dask-core                 2021.10.0          pyhd3eb1b0_0
dataclasses               0.8                pyh6d0b6a4_7
debugpy                   1.4.1            py39hd77b12b_0
decorator                 5.1.0              pyhd3eb1b0_0
defusedxml                0.7.1              pyhd3eb1b0_0
diff-match-patch          20200713           pyhd3eb1b0_0
distributed               2021.10.0        py39haa95532_0
docutils                  0.17.1           py39haa95532_1
entrypoints               0.3              py39haa95532_0
et_xmlfile                1.1.0            py39haa95532_0
fastcache                 1.1.0            py39h196d8e1_0
filelock                  3.3.1              pyhd3eb1b0_1
flake8                    3.9.2              pyhd3eb1b0_0
flask                     1.1.2              pyhd3eb1b0_0
fonttools                 4.25.0             pyhd3eb1b0_0
freetype                  2.10.4               hd328e21_0
fsspec                    2021.10.1          pyhd3eb1b0_0
future                    0.18.2           py39haa95532_1
get_terminal_size         1.0.0                h38e98db_0
gevent                    21.8.0           py39h2bbff1b_1
giflib                    5.2.1                h62dcd97_0
glob2                     0.7                pyhd3eb1b0_0
greenlet                  1.1.1            py39hd77b12b_0
h5py                      3.2.1            py39h3de5c98_0
hdf5                      1.10.6               h7ebc959_0
heapdict                  1.0.1              pyhd3eb1b0_0
html5lib                  1.1                pyhd3eb1b0_0
icc_rt                    2019.0.0             h0cc432a_1
icu                       58.2                 ha925a31_3
idna                      3.2                pyhd3eb1b0_0
imagecodecs               2021.8.26        py39ha1f97ea_0
imageio                   2.9.0              pyhd3eb1b0_0
imagesize                 1.2.0              pyhd3eb1b0_0
importlib-metadata        4.8.1            py39haa95532_0
importlib_metadata        4.8.1                hd3eb1b0_0
inflection                0.5.1            py39haa95532_0
iniconfig                 1.1.1              pyhd3eb1b0_0
intel-openmp              2021.4.0          haa95532_3556
intervaltree              3.1.0              pyhd3eb1b0_0
ipykernel                 6.4.1            py39haa95532_1
ipython                   7.29.0           py39hd4e2768_0
ipython_genutils          0.2.0              pyhd3eb1b0_1
ipywidgets                7.6.5              pyhd3eb1b0_1
isort                     5.9.3              pyhd3eb1b0_0
itsdangerous              2.0.1              pyhd3eb1b0_0
jdcal                     1.4.1              pyhd3eb1b0_0
jedi                      0.18.0           py39haa95532_1
jinja2                    2.11.3             pyhd3eb1b0_0
jinja2-time               0.2.0              pyhd3eb1b0_2
joblib                    1.1.0              pyhd3eb1b0_0
jpeg                      9d                   h2bbff1b_0
json5                     0.9.6              pyhd3eb1b0_0
jsonschema                3.2.0              pyhd3eb1b0_2
jupyter                   1.0.0            py39haa95532_7
jupyter_client            6.1.12             pyhd3eb1b0_0
jupyter_console           6.4.0              pyhd3eb1b0_0
jupyter_core              4.8.1            py39haa95532_0
jupyter_server            1.4.1            py39haa95532_0
jupyterlab                3.2.1              pyhd3eb1b0_1
jupyterlab_pygments       0.1.2                      py_0
jupyterlab_server         2.8.2              pyhd3eb1b0_0
jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
keyring                   23.1.0           py39haa95532_0
kiwisolver                1.3.1            py39hd77b12b_0
krb5                      1.19.2               h5b6d351_0
lazy-object-proxy         1.6.0            py39h2bbff1b_0
lcms2                     2.12                 h83e58a3_0
lerc                      3.0                  hd77b12b_0
libaec                    1.0.4                h33f27b4_1
libarchive                3.4.2                h5e25573_0
libcurl                   7.78.0               h86230a5_0
libdeflate                1.8                  h2bbff1b_5
libiconv                  1.15                 h1df5818_7
liblief                   0.10.1               hd77b12b_1
libpng                    1.6.37               h2a8f88b_0
libspatialindex           1.9.3                h6c2663c_0
libssh2                   1.9.0                h7a1dbc1_1
libtiff                   4.2.0                hd0e1b90_0
libwebp                   1.2.0                h2bbff1b_0
libxml2                   2.9.12               h0ad7f3c_0
libxslt                   1.1.34               he774522_0
libzopfli                 1.0.3                ha925a31_0
llvmlite                  0.37.0           py39h23ce68f_1
locket                    0.2.1            py39haa95532_1
lxml                      4.6.3            py39h9b66d53_0
lz4-c                     1.9.3                h2bbff1b_1
lzo                       2.10                 he774522_2
m2w64-gcc-libgfortran     5.3.0                         6
m2w64-gcc-libs            5.3.0                         7
m2w64-gcc-libs-core       5.3.0                         7
m2w64-gmp                 6.1.0                         2
m2w64-libwinpthread-git   5.0.0.4634.697f757               2
markupsafe                1.1.1            py39h2bbff1b_0
matplotlib                3.4.3            py39haa95532_0
matplotlib-base           3.4.3            py39h49ac443_0
matplotlib-inline         0.1.2              pyhd3eb1b0_2
mccabe                    0.6.1            py39haa95532_1
menuinst                  1.4.18           py39h59b6b97_0
mistune                   0.8.4           py39h2bbff1b_1000
mkl                       2021.4.0           haa95532_640
mkl-service               2.4.0            py39h2bbff1b_0
mkl_fft                   1.3.1            py39h277e83a_0
mkl_random                1.2.2            py39hf11a4ad_0
mock                      4.0.3              pyhd3eb1b0_0
more-itertools            8.10.0             pyhd3eb1b0_0
mpmath                    1.2.1            py39haa95532_0
msgpack-python            1.0.2            py39h59b6b97_1
msys2-conda-epoch         20160418                      1
multipledispatch          0.6.0            py39haa95532_0
munkres                   1.1.4                      py_0
mypy_extensions           0.4.3            py39haa95532_0
navigator-updater         0.2.1            py39haa95532_0
nbclassic                 0.2.6              pyhd3eb1b0_0
nbclient                  0.5.3              pyhd3eb1b0_0
nbconvert                 6.1.0            py39haa95532_0
nbformat                  5.1.3              pyhd3eb1b0_0
nest-asyncio              1.5.1              pyhd3eb1b0_0
networkx                  2.6.3              pyhd3eb1b0_0
nltk                      3.6.5              pyhd3eb1b0_0
nose                      1.3.7           pyhd3eb1b0_1006
notebook                  6.4.5            py39haa95532_0
numba                     0.54.1           py39hf11a4ad_0
numexpr                   2.7.3            py39hb80d3ca_1
numpy                     1.20.3           py39ha4e8547_0
numpy-base                1.20.3           py39hc2deb75_0
numpydoc                  1.1.0              pyhd3eb1b0_1
olefile                   0.46               pyhd3eb1b0_0
openjpeg                  2.4.0                h4fc8c34_0
openpyxl                  3.0.9              pyhd3eb1b0_0
openssl                   1.1.1l               h2bbff1b_0
packaging                 21.0               pyhd3eb1b0_0
pandas                    1.3.4            py39h6214cd6_0
pandocfilters             1.4.3            py39haa95532_1
paramiko                  2.7.2                      py_0
parso                     0.8.2              pyhd3eb1b0_0
partd                     1.2.0              pyhd3eb1b0_0
path                      16.0.0           py39haa95532_0
path.py                   12.5.0               hd3eb1b0_0
pathlib2                  2.3.6            py39haa95532_2
pathspec                  0.7.0                      py_0
patsy                     0.5.2            py39haa95532_0
pca                       1.7.2                    pypi_0    pypi
pep8                      1.7.1            py39haa95532_0
pexpect                   4.8.0              pyhd3eb1b0_3
pickleshare               0.7.5           pyhd3eb1b0_1003
pillow                    8.4.0            py39hd45dc43_0
pip                       21.2.4           py39haa95532_0
pkginfo                   1.7.1            py39haa95532_0
pluggy                    0.13.1           py39haa95532_0
ply                       3.11             py39haa95532_0
powershell_shortcut       0.0.1                         3
poyo                      0.5.0              pyhd3eb1b0_0
prometheus_client         0.11.0             pyhd3eb1b0_0
prompt-toolkit            3.0.20             pyhd3eb1b0_0
prompt_toolkit            3.0.20               hd3eb1b0_0
psutil                    5.8.0            py39h2bbff1b_1
ptyprocess                0.7.0              pyhd3eb1b0_2
py                        1.10.0             pyhd3eb1b0_0
py-lief                   0.10.1           py39hd77b12b_1
pycodestyle               2.7.0              pyhd3eb1b0_0
pycosat                   0.6.3            py39h2bbff1b_0
pycparser                 2.20                       py_2
pycurl                    7.44.1           py39hcd4344a_1
pydocstyle                6.1.1              pyhd3eb1b0_0
pyerfa                    2.0.0            py39h2bbff1b_0
pyflakes                  2.3.1              pyhd3eb1b0_0
pygments                  2.10.0             pyhd3eb1b0_0
pyjwt                     2.1.0            py39haa95532_0
pylint                    2.9.6            py39haa95532_1
pyls-spyder               0.4.0              pyhd3eb1b0_0
pymysql                   1.0.2            py39haa95532_1
pynacl                    1.4.0            py39hbd8134f_1
pyodbc                    4.0.31           py39hd77b12b_0
pyopenssl                 21.0.0             pyhd3eb1b0_1
pyparsing                 3.0.4              pyhd3eb1b0_0
pyqt                      5.9.2            py39hd77b12b_6
pyreadline                2.1              py39haa95532_1
pyrsistent                0.18.0           py39h196d8e1_0
pysocks                   1.7.1            py39haa95532_0
pytables                  3.6.1            py39h56d22b6_1
pytest                    6.2.4            py39haa95532_2
python                    3.9.7                h6244533_1
python-dateutil           2.8.2              pyhd3eb1b0_0
python-libarchive-c       2.9                pyhd3eb1b0_1
python-lsp-black          1.0.0              pyhd3eb1b0_0
python-lsp-jsonrpc        1.0.0              pyhd3eb1b0_0
python-lsp-server         1.2.4              pyhd3eb1b0_0
python-slugify            5.0.2              pyhd3eb1b0_0
pytz                      2021.3             pyhd3eb1b0_0
pywavelets                1.1.1            py39h080aedc_4
pywin32                   228              py39he774522_0
pywin32-ctypes            0.2.0           py39haa95532_1000
pywinpty                  0.5.7            py39haa95532_0
pyyaml                    6.0              py39h2bbff1b_1
pyzmq                     22.2.1           py39hd77b12b_1
qdarkstyle                3.0.2              pyhd3eb1b0_0
qstylizer                 0.1.10             pyhd3eb1b0_0
qt                        5.9.7            vc14h73c81de_0
qtawesome                 1.0.2              pyhd3eb1b0_0
qtconsole                 5.1.1              pyhd3eb1b0_0
qtpy                      1.10.0             pyhd3eb1b0_0
regex                     2021.8.3         py39h2bbff1b_0
requests                  2.26.0             pyhd3eb1b0_0
rope                      0.19.0             pyhd3eb1b0_0
rtree                     0.9.7            py39h2eaa2aa_1
ruamel_yaml               0.15.100         py39h2bbff1b_0
sastrawi                  1.0.1                    pypi_0    pypi
scatterd                  1.1.1                    pypi_0    pypi
scikit-image              0.18.3           py39hf11a4ad_0
scikit-learn              0.24.2           py39hf11a4ad_1
scikit-learn-intelex      2021.3.0         py39haa95532_0
scipy                     1.7.1            py39hbe87c03_2
seaborn                   0.11.2             pyhd3eb1b0_0
send2trash                1.8.0              pyhd3eb1b0_1
setuptools                58.0.4           py39haa95532_0
simplegeneric             0.8.1            py39haa95532_2
singledispatch            3.7.0           pyhd3eb1b0_1001
sip                       4.19.13          py39hd77b12b_0
six                       1.16.0             pyhd3eb1b0_0
sklearn                   0.0                      pypi_0    pypi
snappy                    1.1.8                h33f27b4_0
sniffio                   1.2.0            py39haa95532_1
snowballstemmer           2.1.0              pyhd3eb1b0_0
sortedcollections         2.1.0              pyhd3eb1b0_0
sortedcontainers          2.4.0              pyhd3eb1b0_0
soupsieve                 2.2.1              pyhd3eb1b0_0
sphinx                    4.2.0              pyhd3eb1b0_1
sphinxcontrib             1.0              py39haa95532_1
sphinxcontrib-applehelp   1.0.2              pyhd3eb1b0_0
sphinxcontrib-devhelp     1.0.2              pyhd3eb1b0_0
sphinxcontrib-htmlhelp    2.0.0              pyhd3eb1b0_0
sphinxcontrib-jsmath      1.0.1              pyhd3eb1b0_0
sphinxcontrib-qthelp      1.0.3              pyhd3eb1b0_0
sphinxcontrib-serializinghtml 1.1.5              pyhd3eb1b0_0
sphinxcontrib-websupport  1.2.4                      py_0
spyder                    5.1.5            py39haa95532_1
spyder-kernels            2.1.3            py39haa95532_0
sqlalchemy                1.4.22           py39h2bbff1b_0
sqlite                    3.36.0               h2bbff1b_0
statsmodels               0.12.2           py39h2bbff1b_0
sympy                     1.9              py39haa95532_0
tbb                       2021.4.0             h59b6b97_0
tbb4py                    2021.4.0         py39h59b6b97_0
tblib                     1.7.0              pyhd3eb1b0_0
terminado                 0.9.4            py39haa95532_0
testpath                  0.5.0              pyhd3eb1b0_0
text-unidecode            1.3                pyhd3eb1b0_0
textdistance              4.2.1              pyhd3eb1b0_0
threadpoolctl             2.2.0              pyh0d69192_0
three-merge               0.1.1              pyhd3eb1b0_0
tifffile                  2021.7.2           pyhd3eb1b0_2
tinycss                   0.4             pyhd3eb1b0_1002
tk                        8.6.11               h2bbff1b_0
toml                      0.10.2             pyhd3eb1b0_0
toolz                     0.11.1             pyhd3eb1b0_0
tornado                   6.1              py39h2bbff1b_0
tqdm                      4.62.3             pyhd3eb1b0_1
traitlets                 5.1.0              pyhd3eb1b0_0
typed-ast                 1.4.3            py39h2bbff1b_1
typing_extensions         3.10.0.2           pyh06a4308_0
tzdata                    2021e                hda174b7_0
ujson                     4.0.2            py39hd77b12b_0
unicodecsv                0.14.1           py39haa95532_0
unidecode                 1.2.0              pyhd3eb1b0_0
urllib3                   1.26.7             pyhd3eb1b0_0
vc                        14.2                 h21ff451_1
vs2015_runtime            14.27.29016          h5e58377_2
watchdog                  2.1.3            py39haa95532_0
wcwidth                   0.2.5              pyhd3eb1b0_0
webencodings              0.5.1            py39haa95532_1
werkzeug                  2.0.2              pyhd3eb1b0_0
wget                      3.2                      pypi_0    pypi
wheel                     0.37.0             pyhd3eb1b0_1
whichcraft                0.6.1              pyhd3eb1b0_0
widgetsnbextension        3.5.1            py39haa95532_0
win_inet_pton             1.1.0            py39haa95532_0
win_unicode_console       0.5              py39haa95532_0
wincertstore              0.2              py39haa95532_2
winpty                    0.4.3                         4
wrapt                     1.12.1           py39h196d8e1_1
xlrd                      2.0.1              pyhd3eb1b0_0
xlsxwriter                3.0.1              pyhd3eb1b0_0
xlwings                   0.24.9           py39haa95532_0
xlwt                      1.3.0            py39haa95532_0
xmltodict                 0.12.0             pyhd3eb1b0_0
xz                        5.2.5                h62dcd97_0
yaml                      0.2.5                he774522_0
yapf                      0.31.0             pyhd3eb1b0_0
zfp                       0.5.5                hd77b12b_6
zict                      2.0.0              pyhd3eb1b0_0
zipp                      3.6.0              pyhd3eb1b0_0
zlib                      1.2.11               h62dcd97_4
zope                      1.0              py39haa95532_1
zope.event                4.5.0            py39haa95532_0
zope.interface            5.4.0            py39h2bbff1b_0
zstd                      1.4.9                h19a0ad4_0


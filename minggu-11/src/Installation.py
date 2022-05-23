
(base) C:\Users\acer>conda create --name projects
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\acer\anaconda3\envs\projects



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate projects
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\acer>conda activate projects

(projects) C:\Users\acer>conda install flask
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\acer\anaconda3\envs\projects

  added / updated specs:
    - flask


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2022.5.18.1        |  py310haa95532_0         157 KB
    click-8.0.4                |  py310haa95532_0         157 KB
    libffi-3.4.2               |       h604cdb4_1          43 KB
    markupsafe-2.0.1           |  py310h2bbff1b_0          24 KB
    pip-21.2.4                 |  py310haa95532_0         1.9 MB
    python-3.10.4              |       hbb2ffb3_0        15.9 MB
    setuptools-61.2.0          |  py310haa95532_0         1.0 MB
    tk-8.6.11                  |       h2bbff1b_1         3.3 MB
    wincertstore-0.2           |  py310haa95532_2          15 KB
    xz-5.2.5                   |       h8cc25b3_1         246 KB
    zlib-1.2.12                |       h8cc25b3_2         116 KB
    ------------------------------------------------------------
                                           Total:        22.8 MB

The following NEW packages will be INSTALLED:

  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.4.26-haa95532_0
  certifi            pkgs/main/win-64::certifi-2022.5.18.1-py310haa95532_0
  click              pkgs/main/win-64::click-8.0.4-py310haa95532_0
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  flask              pkgs/main/noarch::flask-2.0.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jinja2             pkgs/main/noarch::jinja2-3.0.3-pyhd3eb1b0_0
  libffi             pkgs/main/win-64::libffi-3.4.2-h604cdb4_1
  markupsafe         pkgs/main/win-64::markupsafe-2.0.1-py310h2bbff1b_0
  openssl            pkgs/main/win-64::openssl-1.1.1o-h2bbff1b_0
  pip                pkgs/main/win-64::pip-21.2.4-py310haa95532_0
  python             pkgs/main/win-64::python-3.10.4-hbb2ffb3_0
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py310haa95532_0
  sqlite             pkgs/main/win-64::sqlite-3.38.3-h2bbff1b_0
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_1
  tzdata             pkgs/main/noarch::tzdata-2022a-hda174b7_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd3eb1b0_0
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py310haa95532_2
  xz                 pkgs/main/win-64::xz-5.2.5-h8cc25b3_1
  zlib               pkgs/main/win-64::zlib-1.2.12-h8cc25b3_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
zlib-1.2.12          | 116 KB    | ####################################### | 100%
setuptools-61.2.0    | 1.0 MB    | ####################################### | 100%
click-8.0.4          | 157 KB    | ####################################### | 100%
pip-21.2.4           | 1.9 MB    | ####################################### | 100%
xz-5.2.5             | 246 KB    | ####################################### | 100%
tk-8.6.11            | 3.3 MB    | ####################################### | 100%
wincertstore-0.2     | 15 KB     | ####################################### | 100%
python-3.10.4        | 15.9 MB   | ####################################### | 100%
certifi-2022.5.18.1  | 157 KB    | ####################################### | 100%
libffi-3.4.2         | 43 KB     | ####################################### | 100%
markupsafe-2.0.1     | 24 KB     | ####################################### | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done


(projects) C:\Users\acer>mkdir flask-tutorial

(projects) C:\Users\acer>cd flask-tutorial

(projects) C:\Users\acer\flask-tutorial>
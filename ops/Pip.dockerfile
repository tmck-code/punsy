FROM tmck-code/punsy:base

WORKDIR /home/punsy

RUN python -m pip install --no-cache-dir setuptools wheel twine

ADD . .

RUN ./setup.py sdist bdist_wheel && ./setup.py install

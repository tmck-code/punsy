FROM tmck-code/punsy:base

WORKDIR /home/punsy

RUN python -m pip install --upgrade pip setuptools wheel twine

ADD . .

RUN ./setup.py sdist bdist_wheel && ./setup.py install

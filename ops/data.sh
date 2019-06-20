#!/bin/bash

set -euxo pipefail

curl -O http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b
curl -O http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b.symbols
curl -O http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b.phones

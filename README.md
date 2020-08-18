# Docscan

[![Downloads](https://pepy.tech/badge/docscan)](https://pepy.tech/project/docscan)
[![Downloads](https://pepy.tech/badge/docscan/month)](https://pepy.tech/project/docscan/month)
[![Downloads](https://pepy.tech/badge/docscan/week)](https://pepy.tech/project/docscan/week)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://img.shields.io/badge/License-MIT-blue.svg)

Docscan is a document scanner. Take a photo of your documents and frame it.

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-1.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-1.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-2.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-2.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-3.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-3.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-4.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-4.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-5.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-5.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-6.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-6.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-7.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-7.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-8.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/danielgatis/docscan/master/examples/doc-8.out.png" width="100" />
</p>


### Installation

Install it from pypi

```bash
    pip install docscan
```

### Usage as a cli

Scan from a remote image
```bash
    curl -s http://input.png | docscan > output.png
```

Scan from a local file
```bash
    docscan -o path/to/output.png path/to/input.png
```

Scan from all images in a folder
```bash
    docscan -p path/to/inputs
```

### Usage as a server

Start the server
```bash
    docscan-server
```

Open your browser to
```
    http://localhost:5000?url=http://image.png
```

### Usage as a library

In `app.py`

```python
import sys
from docscan.doc import scan

sys.stdout.buffer.write(scan(sys.stdin.buffer.read()))

```

Then run
```
    cat input.png | python app.py > out.png
```

### License

Copyright (c) 2020-present [Daniel Gatis](https://github.com/danielgatis)

Licensed under [MIT License](./LICENSE.txt)

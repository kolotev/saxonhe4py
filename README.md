# saxonhe4py

A packaged Java Saxon HE for Python.

[![PyPI](https://img.shields.io/pypi/v/saxonhe4py.svg)]()

## Install

Java Saxon HE is made easy to install as a single Python package:

```bash
pip install saxonhe4py
```

## Usage

```python
>>> from saxonhe4py import SAXON_HE_JAR
>>> SAXON_HE_JAR
PosixPath('/Users/johndoe/dev/saxonhe4py/jdk4py/java-runtime')
```

### Command line

```python
>>> from subprocess import check_output, run, STDOUT
>>> from jdk4py import JAVA
>>> from saxonhe4py import SAXON_HE_JAR
>>>
>>> cmd_list = [str(JAVA), "-jar", str(SAXON_HE_JAR), "net.sf.saxon.Transform", "-t", "-?"] 
>>> print(check_output(cmd_list, stderr=subprocess.STDOUT, text=True))
SaxonJ-HE 11.4 from Saxonica
Java version 17.0.3
...
```

### With jsaxonpy & Google functions

Could be convinient if you want to execute your code as cloud function
where there is no java VM nor Saxon are avaiable in the environment
of the container.

```python
import os
import functions_framework

from jdk4py import JAVA, JAVA_HOME
from saxonhe4py import SAXON_HE_JAR
from jsaxonpy import Xslt

# following env variable must be defined, otherwise pyjnius would fail
os.environ["JAVA_HOME"] = str(JAVA_HOME)
os.environ["JDK_HOME"] = str(JAVA_HOME)

# to find the location of Saxon HE
os.environ["CLASSPATH"] = str(SAXON_HE_JAR)

# setup JVM options
os.environ["JVM_OPTIONS"] = "-Xmx64m"

# setup PATH to make java executable available for shell commands
os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + str(JAVA)

@functions_framework.http
def transform(request):
  t = Xslt()
  xml = "<root><child>text</child></root>"
  xsl = """
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
      <xsl:copy-of select="."/>
    </xsl:template>
  </xsl:stylesheet>
  """

   output = t.transform(xml, xsl)

   return output
```

If you need to pass XSL params or use catalog file for DTD resolution,
assuming code above, following snippet would help:

```python
from pathlib import Path

catalog = Path("catalog.xml") # optional catalog location
t = Xslt(catalog=catalog)

xsl_params = {"param1": "value1", "param2": "value2", ...}
print(t.transform(xml, xsl, params=xsl_params))
```

## Versioning

`saxonhe4py`'s version consist of 3 components:

- The first two are corresponding to the Java Saxon HE version.
- The third is `saxonhe4py` a release version for that version of Saxon HE.


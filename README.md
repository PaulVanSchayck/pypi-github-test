# CoverageJSON Pydantic

<p align="center">
  <a href="https://github.com/PaulVanSchayck/covjson-pydantic/actions?query=workflow%3ACI" target="_blank">
      <img src="https://github.com/PaulVanSchayck/pypi-github-test/workflows/CI/badge.svg" alt="Test">
  </a>
  <a href="https://codecov.io/gh/PaulVanSchayck/covjson-pydantic" target="_blank">
      <img src="https://codecov.io/gh/PaulVanSchayck/pypi-github-test/branch/master/graph/badge.svg" alt="Coverage">
  </a>
  <a href="https://test.pypi.org/project/covjson-pydantic" target="_blank">
      <img src="https://img.shields.io/pypi/v/covjson-pydantic?color=%2334D058&label=pypi%20package" alt="Package version">
  </a>
  <a href="https://pypistats.org/packages/covjson-pydantic" target="_blank">
      <img src="https://img.shields.io/pypi/dm/covjson-pydantic.svg" alt="Downloads">
  </a>
  <a href="https://github.com/developmentseed/covjson-pydantic/blob/main/LICENSE" target="_blank">
      <img src="https://img.shields.io/github/license/PaulVanSchayck/covjson-pydantic.svg" alt="License">
  </a>
</p>


This repository contains the coveragejson-pydantic Python package. It provides [Pydantic](https://pydantic-docs.helpmanual.io/) models for [CoverageJSON](https://covjson.org/). This can, for example, be used to develop an API using FastAPI serving or receiving CoverageJSON.

## Install
```shell
pip install covjson-pydantic
```

Or install from source:

```shell
pip install git+https://github.com/KNMI/covjson-pydantic.git
```

## Usage

```python
from covjson_pydantic import Domain
from covjson_pydantic import ValuesAxis

axis1 = ValuesAxis(values=[1.23])
d1 = Domain(
    domainType="PointSeries",
    axes={
        "x": axis1,
        "y": axis1,
        "t": {"values": [2.0]}
    }
)
print(d1.json())
```

See `example.py` for more examples.

## Contributing

Make an editable install from within the repository root

```shell
pip install -e '.[test]'
```

### Running tests

```shell
pytest tests/
```

## License

Apache License, Version 2.0

## Copyright

Koninklijk Nederlands Meteorologisch Instituut (KNMI)

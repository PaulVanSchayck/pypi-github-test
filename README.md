# CoverageJSON Pydantic

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

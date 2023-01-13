from covjson_pydantic import Domain
from covjson_pydantic import NdArray
from covjson_pydantic import ValuesAxis

axis1 = ValuesAxis(values=[1.23])
d1 = Domain(domainType="PointSeries", axes={"x": axis1, "y": axis1, "t": {"values": [2.0]}})
print(d1.json(indent=4))

d2 = Domain(
    domainType="PointSeries",
    axes={
        "x": {"values": [1.23]},
        "y": {"values": [2.0]},
        "t": {"start": 2.71, "stop": 3.14, "num": 2},
    },
)
print(d2.json())

json: str = d2.json()
print(json)
print(Domain.parse_raw(json))

r1 = NdArray(axisNames=["x", "y", "t"], shape=[1, 1, 4], values=[1.0, 2.0, 3.0, 4.0])
json_r1 = r1.json()
print(json_r1)
print(NdArray.parse_raw(json_r1))

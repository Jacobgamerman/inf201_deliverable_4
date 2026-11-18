import pytest
from src.Task1 import Temperature

def test_initialization():
    t_defaultvalue = Temperature(25)
    assert t_defaultvalue.value == 25
    assert t_defaultvalue.unit == "C"

    t_lowercase = Temperature(25, "f")
    assert t_lowercase.value == 25
    assert t_lowercase.unit == "F"

    with pytest.raises(AttributeError):
        t_lowercase.value = 30
    with pytest.raises(AttributeError):
        t_lowercase.unit = "C"

@pytest.mark.parametrize("invalid_unit", ["X", "celsius","","123", None])
def test_invalid_units(invalid_unit):
    with pytest.raises(ValueError):
        Temperature(25,invalid_unit)

@pytest.mark.parametrize(
    "value, unit",
    [
        (-273.16, "C"),
        (-459.68, "F"),
        (-0.01, "K"),
    ],
)
def test_below_absolute_zero(value, unit):
    with pytest.raises(ValueError):
        Temperature(value, unit)

# 4. Round-Trip Conversions
def test_round_trip_conversion():
    original = Temperature(25.0, "C")
    converted = original.convert_to("F").convert_to("K").convert_to("C")

    assert converted == original
    assert converted.unit == "C"
    assert converted is not original  # Ensures a new instance was returned

# 5. Cross-Unit Comparisons
def test_comparisons():
    t0_c = Temperature(0, "C")
    t32_f = Temperature(32, "F")
    t273_k = Temperature(273.15, "K")
    t100_c = Temperature(100, "C")

    # Equality and inequality across units
    assert t0_c == t32_f == t273_k
    assert t0_c != t100_c

    # Ordering across units
    assert t0_c < t100_c
    assert t32_f <= t0_c
    assert t0_c <= t100_c
    assert t100_c > t32_f
    assert t273_k >= t32_f
    assert t100_c >= t32_f

    # Comparing with non-Temperature objects
    assert (t0_c == 0) is False
    assert (t0_c != 0) is True
    with pytest.raises(TypeError):
        _ = t0_c < 100


# 6. Formatting
def test_formatting():
    t = Temperature(25, "c")
    assert repr(t) == "Temperature(25.0, 'C')"
    assert str(t) == "25.00 °C"
"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_patient_eqality():
    from inflammation.models import Patient

    name1 = 'Alice'
    name2 = 'Bob'
    p1 = Patient(name=name1)
    p2 = Patient(name=name1)
    p3 = Patient(name=name2)

    assert p1 == p2
    assert p1 != p3

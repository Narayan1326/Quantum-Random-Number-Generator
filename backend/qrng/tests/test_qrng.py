import pytest
from django.urls import reverse

from qrng.extractor import VonNeumannExtractor, HashExtractor
from qrng.qiskit_engine import QrngResult


def test_von_neumann_extractor():
    extractor = VonNeumannExtractor()
    # Test with input that has 01 and 10 pairs
    output = extractor.extract("01100011")
    assert output == "01"


def test_hash_extractor_length():
    extractor = HashExtractor()
    bits = "0101" * 64
    output = extractor.extract(bits)
    assert len(output) == extractor.digest_bits


@pytest.mark.django_db
def test_random_endpoint_success(client, monkeypatch):
    url = reverse("qrng-random")

    class DummyGenerator:
        def __init__(self, *args, **kwargs):
            pass

        def generate(self, bits):
            return QrngResult(bits="01" * (bits // 2), hex_value="0f", entropy=1.0, bias=0.0)

    monkeypatch.setattr("qrng.views.QuantumRandomGenerator", DummyGenerator)

    response = client.get(url, {"bits": 8, "mode": "simulator"})
    assert response.status_code == 200
    data = response.json()
    assert data["length"] == 8
    assert data["statistics"]["bias"] == 0.0


def test_random_endpoint_validation(client):
    url = reverse("qrng-random")
    response = client.get(url, {"bits": "invalid"})
    assert response.status_code == 400


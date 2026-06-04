from oulu_info_theory.entropy import entropy

def test_entropy():
    assert abs(entropy([0.5,0.5]) - 1.0) < 1e-6

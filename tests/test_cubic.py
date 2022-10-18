import numpy as np

from pyforfluids import Fluid


def test_pengrobinson_pv(peng_robinson_mix, peng_robinson_pv):
    composition, pr = peng_robinson_mix
    fluid = Fluid(
        model=pr, composition=composition, temperature=250, density=5
    )
    density_range = peng_robinson_pv["density"].values

    isotherm = fluid.isotherm(density_range)

    return np.allclose(
        isotherm["pressure"], peng_robinson_pv["pressure"] * 1e5
    )

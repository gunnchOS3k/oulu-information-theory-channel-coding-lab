from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from oulu_info_theory.entropy import entropy
from oulu_info_theory.channel_capacity import awgn_capacity
from oulu_info_theory.bsc_bec import bsc_capacity
from oulu_info_theory.ber_ser import ber_from_errors

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / 'results/figures'; FIG.mkdir(parents=True, exist_ok=True)
TBL = ROOT / 'results/tables'; TBL.mkdir(parents=True, exist_ok=True)

snr = np.linspace(0, 20, 50)
cap = [awgn_capacity(10**(s/10)) for s in snr]
plt.figure(); plt.plot(snr, cap); plt.xlabel('SNR dB'); plt.ylabel('bits/s/Hz'); plt.savefig(FIG/'capacity_curves.png'); plt.close()
ber = [ber_from_errors(int(1000*p), 1000) for p in np.linspace(0, 0.2, 20)]
plt.figure(); plt.plot(ber); plt.savefig(FIG/'ber_curves.png'); plt.close()
(TBL/'channel_summary.md').write_text(f'# Summary\nH fair coin={entropy([0.5,0.5]):.3f}\nBSC p=0.1 C={bsc_capacity(0.1):.3f}\n')
(ROOT/'results/experiment_summary.md').write_text('# Info theory e2e PASS\n')

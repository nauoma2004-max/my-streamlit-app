import math
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Shell & Tube HX Designer",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# PROFESSIONAL DESIGN - Purple & Cyan Theme
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --purple: #7C3AED;
    --purple-dark: #6D28D9;
    --purple-light: #A78BFA;
    --cyan: #06B6D4;
    --cyan-dark: #0891B2;
    --cyan-light: #67E8F9;
    --bg-main: #FAFBFC;
    --bg-card: #FFFFFF;
    --bg-dark: #1E1B4B;
    --text-primary: #1F2937;
    --text-secondary: #6B7280;
    --text-muted: #9CA3AF;
    --border: #E5E7EB;
    --success: #10B981;
    --warning: #F59E0B;
    --danger: #EF4444;
}

* { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

.stApp {
    background: var(--bg-main);
    color: var(--text-primary);
}

/* Hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none !important; }

/* Scroll padding for fixed nav */
html { scroll-behavior: smooth; }
section { scroll-margin-top: 70px; }

/* Navigation Bar */
.nav-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    background: linear-gradient(135deg, var(--bg-dark) 0%, #312E81 100%);
    padding: 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.nav-content {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    height: 60px;
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    color: white;
    font-size: 1.1rem;
    font-weight: 700;
}

.nav-brand-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, var(--purple) 0%, var(--cyan) 100%);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.nav-links {
    display: flex;
    gap: 4px;
}

.nav-link {
    padding: 12px 20px !important;
    color: white !important;
    text-decoration: none !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
    border: none !important;
    background: transparent !important;
}

.nav-link:hover {
    color: white !important;
    background: rgba(255,255,255,0.1) !important;
}

/* Main Content */
.main-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 100px 24px 60px;
}

/* Section */
.section { margin-bottom: 40px; }

.section-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
}

.section-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, var(--purple) 0%, var(--purple-dark) 100%);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.4rem;
    box-shadow: 0 4px 15px rgba(124,58,237,0.3);
}

.section-icon.cyan {
    background: linear-gradient(135deg, var(--cyan) 0%, var(--cyan-dark) 100%);
    box-shadow: 0 4px 15px rgba(6,182,212,0.3);
}

.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
}

/* Remove white triangle/arrow elements from section headers */
.section-header::before,
.section-header::after,
.section-icon::before,
.section-icon::after {
    display: none !important;
    content: none !important;
}

/* Hero Card */
.hero-card {
    background: linear-gradient(135deg, var(--bg-dark) 0%, #312E81 50%, var(--purple-dark) 100%);
    border-radius: 24px;
    padding: 48px;
    color: white;
    position: relative;
    overflow: hidden;
    margin-bottom: 32px;
}

.hero-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(124,58,237,0.3) 0%, transparent 70%);
    border-radius: 50%;
}

.hero-card::after {
    content: '';
    position: absolute;
    bottom: -30%;
    left: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(6,182,212,0.2) 0%, transparent 70%);
    border-radius: 50%;
}

.hero-content { position: relative; z-index: 1; }

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,255,255,0.15);
    padding: 8px 16px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 20px;
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 0 0 16px 0;
    line-height: 1.2;
}

.hero-description {
    font-size: 1.1rem;
    opacity: 0.9;
    margin: 0 0 32px 0;
    max-width: 600px;
}

.hero-tags { display: flex; flex-wrap: wrap; gap: 10px; }

.hero-tag {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 0.85rem;
    font-weight: 500;
}

/* Input Panel */
.input-panel {
    background: var(--bg-card);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
    border: 1px solid var(--border);
}

.input-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

.input-group { margin-bottom: 8px; }

.input-label {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
}

.input-label-text {
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--text-secondary);
}

.input-label-unit {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--purple);
    background: rgba(124,58,237,0.1);
    padding: 4px 10px;
    border-radius: 6px;
}

.stNumberInput > div > div > input,
.stSelectbox > div > div > div {
    border: 2px solid var(--border) !important;
    border-radius: 10px !important;
    background: var(--bg-main) !important;
    font-size: 0.9rem !important;
    padding: 12px 14px !important;
    transition: all 0.2s ease !important;
}

.stSelectbox > div { min-height: 48px !important; }
.stSelectbox > div > div { min-height: 48px !important; }
.stSelectbox > div > div > div {
    padding: 10px 14px !important;
    min-height: 48px !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    display: flex !important;
    align-items: center !important;
}

.stNumberInput > div > div > input:focus,
.stSelectbox > div > div > div:focus {
    border-color: var(--purple) !important;
    box-shadow: 0 0 0 4px rgba(124,58,237,0.1) !important;
}

/* KPI Grid */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}

@media (max-width: 1200px) { .kpi-grid { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 900px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }

.kpi-card {
    background: var(--bg-card);
    border-radius: 16px;
    padding: 24px;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--purple) 0%, var(--cyan) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(124,58,237,0.12);
    border-color: var(--purple-light);
}

.kpi-card:hover::before { opacity: 1; }

.kpi-icon {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(6,182,212,0.1) 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    margin-bottom: 16px;
}

.kpi-label {
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1;
    margin-bottom: 4px;
}

.kpi-note {
    font-size: 0.75rem;
    color: var(--text-muted);
    margin-top: 8px;
}

/* Chart Container */
.chart-container {
    background: var(--bg-card);
    border-radius: 20px;
    padding: 24px;
    border: 1px solid var(--border);
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--purple) 0%, var(--purple-dark) 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 14px 28px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(124,58,237,0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(124,58,237,0.4);
}

/* Validation Cards */
.validation-banner {
    border-radius: 16px;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
    font-weight: 700;
    font-size: 1.1rem;
}
.validation-banner.pass {
    background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(16,185,129,0.05) 100%);
    border: 2px solid #10B981;
    color: #065F46;
}
.validation-banner.fail {
    background: linear-gradient(135deg, rgba(239,68,68,0.12) 0%, rgba(239,68,68,0.05) 100%);
    border: 2px solid #EF4444;
    color: #7F1D1D;
}
.validation-banner.warn {
    background: linear-gradient(135deg, rgba(245,158,11,0.12) 0%, rgba(245,158,11,0.05) 100%);
    border: 2px solid #F59E0B;
    color: #78350F;
}
.check-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 24px;
}
@media (max-width: 1100px) { .check-grid { grid-template-columns: repeat(2, 1fr); } }
.check-card {
    background: var(--bg-card);
    border-radius: 14px;
    padding: 18px 20px;
    border: 1.5px solid var(--border);
    display: flex;
    align-items: flex-start;
    gap: 14px;
}
.check-card.pass  { border-color: #10B981; background: rgba(16,185,129,0.04); }
.check-card.fail  { border-color: #EF4444; background: rgba(239,68,68,0.04); }
.check-card.warn  { border-color: #F59E0B; background: rgba(245,158,11,0.04); }
.check-dot { font-size: 1.4rem; margin-top: 2px; }
.check-title { font-size: 0.78rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.4px; margin-bottom: 4px; }
.check-value { font-size: 1.15rem; font-weight: 800; color: var(--text-primary); }
.check-limit { font-size: 0.72rem; color: var(--text-muted); margin-top: 3px; }
.opt-box {
    background: var(--bg-card);
    border-radius: 20px;
    padding: 28px 32px;
    border: 1px solid var(--border);
    box-shadow: 0 4px 24px rgba(0,0,0,0.04);
    margin-bottom: 24px;
}
.opt-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin-top: 16px;
}
.opt-table th {
    background: linear-gradient(135deg, var(--purple) 0%, var(--cyan) 100%);
    color: white;
    padding: 10px 16px;
    text-align: left;
    font-weight: 600;
    font-size: 0.8rem;
    letter-spacing: 0.3px;
}
.opt-table th:first-child { border-radius: 8px 0 0 8px; }
.opt-table th:last-child  { border-radius: 0 8px 8px 0; }
.opt-table td {
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
    color: var(--text-primary);
}
.opt-table tr:last-child td { border-bottom: none; }
.opt-table .changed { color: var(--purple); font-weight: 700; }
.opt-table .good    { color: #10B981; font-weight: 700; }
.opt-table .bad     { color: #EF4444; font-weight: 700; }

/* Footer */
.footer {
    text-align: center;
    padding: 32px;
    color: var(--text-muted);
    font-size: 0.85rem;
}

.footer-brand {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 8px;
    font-weight: 600;
    color: var(--text-secondary);
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# ENGINEERING CONSTANTS & DEFAULTS
# ═══════════════════════════════════════════════════════════════
DEFAULTS = {
    "m_h": 60000.0, "m_c": 89142.8,
    "T_hin": 250.0, "T_hout": 150.0, "T_cin": 85.0, "T_cout": 120.0,
    "Do_in": 0.75, "Di_in": 0.62, "L_ft": 16.0, "PT_in": 1.0,
    "B_space_in": 6.975, "n_p": 4,
    "Rd_shell": 0.002, "Rd_tube": 0.002,
    "UD_est": 40.0, "DP_limit_shell": 10.0, "DP_limit_tube": 10.0,
    "Cp_shell": 0.52, "k_shell": 0.074, "mu_shell": 6.65, "sg_shell": 0.82,
    "Cp_tube": 1.00, "k_tube": 0.36, "mu_tube": 1.63, "sg_tube": 1.015,
    "Ffactor": 1.0,
    "n_tubes": 310, "Ds_in": 23.25, "k_metal": 26.0,
    # Delaware-specific inputs
    "Dotl_in": 21.81,      # Tube bundle outer tube limit diameter (in)
    "delta_tb_in": 0.0157, # Tube-to-baffle diametral clearance (in)
    "delta_sb_in": 0.0995, # Shell-to-baffle diametral clearance (in)
    "Bc_frac": 0.20,       # Baffle cut fraction (-)
    "Nss_Nc": 0.10,        # Sealing strip pairs / crossflow rows ratio (-)
    "Ncw": 18.0,           # Crossflow rows in window (-)
    "Nc": 99.0,            # Total crossflow rows (-)
    "Nb": 42.0,            # Number of baffles (-)
    "DP_nozzle": 0.20,     # Nozzle pressure drop (psi)
    "ji_factor": 0.0063,   # Ideal j-factor from Colburn chart (-)
}

UNITS = {
    "mass_flow": ["lb/h", "kg/h"],
    "temperature": ["°F", "°C"],
    "length": ["ft", "in", "mm"],
    "length_in": ["in", "mm"],
    "density": ["lb/ft³", "kg/m³"],
    "cp": ["Btu/lbm·°F", "kJ/kg·K"],
    "k": ["Btu/h·ft·°F", "W/m·K"],
    "viscosity": ["lb/ft·h", "mPa·s"],
    "fouling": ["h·ft²·°F/Btu", "m²·K/W"],
    "u": ["Btu/h·ft²·°F", "W/m²·K"],
    "dp": ["psi", "kPa"],
    "sg": ["-", "-"],
}

UNIT_MAP = {
    "m_h": "mass_flow", "m_c": "mass_flow",
    "T_hin": "temperature", "T_hout": "temperature", "T_cin": "temperature", "T_cout": "temperature",
    "Do_in": "length_in", "Di_in": "length_in", "L_ft": "length", "PT_in": "length_in", "B_space_in": "length_in", "Ds_in": "length_in",
    "sg_shell": "sg", "sg_tube": "sg",
    "Cp_shell": "cp", "Cp_tube": "cp",
    "k_shell": "k", "k_tube": "k", "k_metal": "k",
    "mu_shell": "viscosity", "mu_tube": "viscosity",
    "Rd_shell": "fouling", "Rd_tube": "fouling",
    "UD_est": "u", "DP_limit_shell": "dp", "DP_limit_tube": "dp",
    "n_tubes": "count", "n_p": "count",
    "Ffactor": "factor",
    # Delaware-specific
    "Dotl_in": "length_in",
    "delta_tb_in": "length_in",
    "delta_sb_in": "length_in",
    "Bc_frac": "factor",
    "Nss_Nc": "factor",
    "Ncw": "factor",
    "Nc": "factor",
    "Nb": "count",
    "DP_nozzle": "dp",
    "ji_factor": "factor",
}

UNITS["count"] = ["-", "-"]
UNITS["factor"] = ["-", "-"]

def init():
    for k, v in DEFAULTS.items():
        st.session_state.setdefault(f"v_{k}", v)
        g = UNIT_MAP.get(k, "mass_flow")
        st.session_state.setdefault(f"u_{k}", UNITS[g][0])

init()


def clamp(v, m=1e-9):
    try: v = float(np.real(v))
    except: return m
    return max(v if np.isfinite(v) else m, m)

def sp(b, e): return clamp(abs(b))**e

def conv_t(v, u): return v if u == "°F" else v*9/5+32
def conv_tb(v, u): return v if u == "°F" else (v-32)*5/9
def conv_m(v, u): return v if u == "lb/h" else v*2.20462
def conv_mb(v, u): return v if u == "lb/h" else v/2.20462
def conv_l(v, u): return v if u == "ft" else (v*12 if u == "in" else v*304.8)
def conv_lb(v, u): return v if u == "ft" else (v/12 if u == "in" else v/304.8)
def conv_li(v, u): return v if u == "in" else v/25.4
def conv_lib(v, u): return v if u == "in" else v*25.4
def conv_d(v, u): return v if u == "lb/ft³" else v*0.062428
def conv_db(v, u): return v if u == "lb/ft³" else v/0.062428
def conv_cp(v, u): return v if u == "Btu/lbm·°F" else v/4.1868
def conv_cpb(v, u): return v if u == "Btu/lbm·°F" else v*4.1868
def conv_k(v, u): return v if u == "Btu/h·ft·°F" else v/1.730735
def conv_kb(v, u): return v if u == "Btu/h·ft·°F" else v*1.730735
def conv_vis(v, u): return v*0.672 if u == "lb/ft·h" else v*1000
def conv_visb(v, u): return v/0.672 if u == "lb/ft·h" else v/1000
def conv_f(v, u): return v if u == "h·ft²·°F/Btu" else v*5.678263
def conv_fb(v, u): return v if u == "h·ft²·°F/Btu" else v/5.678263
def conv_u(v, u): return v if u == "Btu/h·ft²·°F" else v/5.678263
def conv_ub(v, u): return v if u == "Btu/h·ft²·°F" else v*5.678263
def conv_dp(v, u): return v if u == "psi" else v*6.89475729
def conv_dpb(v, u): return v if u == "psi" else v/6.89475729

def fval(v, d=2):
    if v is None or not np.isfinite(v): return "ERR"
    try: v = float(np.real(v))
    except: return "ERR"
    return f"{v:.{d}f}"


class FP:
    def __init__(self, name, cp, k, mu_lb_ft_h, sg):
        self.name = name
        self.Cp = clamp(cp)
        self.k = clamp(k)
        self.mu = clamp(mu_lb_ft_h)
        self.sg = clamp(sg)
        self.rho = self.sg * 62.4
        self.s = self.sg
        self.Pr = max(self.Cp * self.mu / self.k, 0.01)

def calc_F(T_hi, T_ho, T_ci, T_co):
    dTh, dTc = T_hi - T_ho, T_co - T_ci
    if dTh <= 0 or dTc <= 0: raise ValueError("T diff must be positive")
    R = dTh / clamp(dTc)
    P = dTc / clamp(T_hi - T_ci)
    try:
        S = math.sqrt(R**2 + 1)
        num = S * math.log((1-P)/clamp(1-P*R))
        a = 2/clamp(P) - 1 - R + S
        b = 2/clamp(P) - 1 - R - S
        if b <= 0: raise ValueError
        F = num / math.log(a/b)
        if not np.isfinite(F): raise ValueError
    except: F = 0.90
    return min(max(F, 0.50), 1.00)

def kern(inp, sh, tu):
    m_h, m_c = clamp(inp["m_h"]), clamp(inp["m_c"])
    T_hi, T_ho = float(inp["T_hin"]), float(inp["T_hout"])
    T_ci, T_co = float(inp["T_cin"]), float(inp["T_cout"])
    Do = clamp(inp["Do_in"]) / 12
    Di = clamp(inp["Di_in"]) / 12
    L = clamp(inp["L_ft"])
    PT = clamp(inp["PT_in"]) / 12
    np_ = max(int(round(inp["n_p"])), 1)
    Rdt = max(float(inp["Rd_tube"]), 0)
    Rds = max(float(inp["Rd_shell"]), 0)

    nt = int(inp.get("n_tubes", 310))
    Ds = float(inp.get("Ds_in", 23.25))
    kw = float(inp.get("k_metal", 26.0))
    B_in = float(inp.get("B_space_in", 6.975))

    Ffactor = float(inp.get("Ffactor", 1.0))

    if Di >= Do: raise ValueError("Tube ID must be < tube OD")
    if PT <= Do: raise ValueError("Tube pitch must be > tube OD")

    Q = m_h * sh.Cp * (T_hi - T_ho)
    dT1, dT2 = T_hi - T_co, T_ho - T_ci
    if dT1 <= 0 or dT2 <= 0: raise ValueError("Invalid T driving force")
    LMTD = dT1 if abs(dT1-dT2)<1e-9 else (dT1-dT2)/math.log(dT1/dT2)
    F = calc_F(T_hi, T_ho, T_ci, T_co)
    dT = F * LMTD

    Ds_ft = Ds / 12
    A_act = nt * math.pi * Do * L
    U_req = Q / clamp(A_act * dT)

    G_t = (m_c * np_/nt) / (math.pi * Di**2 / 4)
    Re_t = max(abs(Di * G_t / tu.mu), 1)
    hi = (tu.k/Di)*0.023*sp(Re_t,0.8)*sp(tu.Pr,1/3) * Ffactor
    hi = max(float(np.real(hi)), 5)

    B = B_in / 12
    de = 0.0792
    as_area = (Ds * (PT*12 - Do*12) * B_in) / 144
    G_s = abs(m_h / as_area)
    Re_s = max(abs(de * G_s / sh.mu), 1)

    jh = 0.5 * (1 + B/Ds_ft) * (0.08*sp(Re_s,0.6821) + 0.7*sp(Re_s,0.1772))
    ho = max(float(np.real(jh*(sh.k/de)*sp(sh.Pr,1/3))), 5) * Ffactor

    Uc = 1/( (Do/(hi*Di)) + ((Do*math.log(Do/Di))/(2*kw)) + 1/ho )
    Rd = Rdt*(Do/Di) + Rds
    UDf = 1/(1/Uc + Rd)

    ov_s = (Uc/U_req - 1)*100
    ov_d = (UDf/U_req - 1)*100

    ft = 0.4137*sp(Re_t,-0.2585)
    dp_f = (ft * np_ * L * G_t**2) / (7.50e12 * Di * tu.s)
    dp_r = 1.334e-13 * (2 * np_ - 1.5) * G_t**2 / tu.s
    DP_tube = dp_f + dp_r

    nb_plus_1 = (L * 12 / B_in)
    f1 = (0.0076 + 0.000166 * Ds) * sp(Re_s, -0.125)
    f2 = (0.0016 + 5.8e-5 * Ds) * sp(Re_s, -0.157)
    f_s = 144 * (f1 - 1.25 * (1 - B_in/Ds) * (f1 - f2))
    DP_shell = (f_s * G_s**2 * Ds_ft * nb_plus_1) / (7.50e12 * de * sh.s)

    return {
        "Q":float(Q), "LMTD":float(LMTD), "F":float(F), "dT":float(dT),
        "nt":int(nt), "Ds":float(Ds), "Uc":float(Uc), "UD":float(UDf),
        "hi":float(hi), "ho":float(ho), "Re_t":float(Re_t), "Re_s":float(Re_s),
        "DP_t":float(DP_tube), "DP_s":float(DP_shell),
        "ov_s":float(ov_s), "ov_d":float(ov_d),
        "B":float(B_in), "nb":int(nb_plus_1-1), "s_s":float(sh.s), "s_t":float(tu.s),
        "G_t":float(G_t), "G_s":float(G_s),
        "Ffactor_used":float(Ffactor),
    }

def delaware(inp, sh, nt, Ds):
    """
    Delaware Method — shell-side heat transfer & pressure drop.
    Follows the exact procedure from PHT3 / Example 6.1 (Kern-Seader).

    All geometry inputs already in inches (internal storage).
    """
    import math

    # ── Inputs ──────────────────────────────────────────────────────────────
    ws      = clamp(inp["m_h"])                          # shell-side mass flow  [lb/h]
    do      = clamp(inp["Do_in"])                        # tube OD               [in]
    pitch   = clamp(inp["PT_in"])                        # tube pitch            [in]
    b_space = max(float(inp.get("B_space_in", 6.975)), 1.0)  # baffle spacing   [in]
    bc      = float(inp.get("Bc_frac",   0.20))          # baffle cut fraction   [-]
    dotl    = float(inp.get("Dotl_in",   Ds - 1.44))     # outer tube limit diam [in]
    delta_tb = float(inp.get("delta_tb_in", 0.0157))     # tube-baffle clearance [in]
    delta_sb = float(inp.get("delta_sb_in", 0.0995))     # shell-baffle clearance[in]
    rss     = float(inp.get("Nss_Nc",    0.10))          # Nss/Nc sealing ratio  [-]
    ncw     = float(inp.get("Ncw",       18.0))          # crossflow rows window [-]
    nc      = max(float(inp.get("Nc",    99.0)), 1.0)    # total crossflow rows  [-]
    nb      = int(inp.get("Nb",          42))            # number of baffles     [-]
    dpn     = float(inp.get("DP_nozzle", 0.20))          # nozzle DP             [psi]
    ji      = float(inp.get("ji_factor", 0.0063))        # ideal j from chart    [-]
    Ffactor = float(inp.get("Ffactor",   1.0))           # F-factor correction   [-]

    # ── 1. GEOMETRY & AREAS ─────────────────────────────────────────────────
    # theta_ds: shell-baffle cut angle [rad]
    theta_ds  = 2.0 * math.acos(max(min(1.0 - 2.0*bc, 1.0), -1.0))

    # theta_ctl: tube-limit angle [rad]
    denom_ctl = max(dotl - do, 0.001)
    arg_ctl   = max(min(Ds * (1.0 - 2.0*bc) / denom_ctl, 1.0), -1.0)
    theta_ctl = 2.0 * math.acos(arg_ctl)

    # Fc: fraction of tubes in crossflow zone
    fc = 1.0 + (math.sin(theta_ctl) - theta_ctl) / math.pi
    fc = max(min(fc, 1.0), 0.0)

    # Fw: fraction of tubes in window zone
    fw = 0.5 * (1.0 - fc)

    # Sm: crossflow area [in²  → /144 → ft²]
    sm_in2 = b_space * ((Ds - dotl) + ((dotl - do) / pitch) * (pitch - do))
    sm_ft2 = max(sm_in2 / 144.0, 1e-6)

    # Sw: net window area [in² → ft²]
    sw_gross_in2 = (Ds**2 / 8.0) * (theta_ds - math.sin(theta_ds))
    sw_tubes_in2 = nt * fw * math.pi * do**2 / 4.0
    sw_ft2 = max((sw_gross_in2 - sw_tubes_in2) / 144.0, 1e-6)

    # Stb: tube-to-baffle leakage area [in² → ft²]
    stb_ft2 = (0.5 * math.pi * do * delta_tb * nt * (1.0 + fc)) / 144.0

    # Ssb: shell-to-baffle leakage area [in² → ft²]
    ssb_ft2 = (Ds * delta_sb * (math.pi - theta_ds / 2.0)) / 144.0

    # Sb: bypass area [in² → ft²]
    sb_ft2 = (b_space * (Ds - dotl)) / 144.0

    # ── 2. MASS VELOCITY & REYNOLDS ─────────────────────────────────────────
    gs    = ws / clamp(sm_ft2)                           # [lb/h·ft²]
    re_s  = max(abs((do / 12.0) * gs / clamp(sh.mu)), 1.0)  # Re_s [-]

    # ── 3. CORRECTION FACTORS ───────────────────────────────────────────────
    # Jc: baffle-cut correction
    jc = 0.55 + 0.72 * fc

    # Jl / Rl: leakage correction
    rs    = ssb_ft2 / clamp(ssb_ft2 + stb_ft2)
    rl_a  = (ssb_ft2 + stb_ft2) / clamp(sm_ft2)
    jl    = 0.44*(1.0-rs) + (1.0 - 0.44*(1.0-rs)) * math.exp(-2.2 * rl_a)
    p_lk  = 0.8 - 0.15*(1.0 + rs)
    rl    = math.exp(-1.33*(1.0+rs) * max(rl_a,1e-9)**p_lk)

    # Jb / Rb: bypass correction
    bypass_arg = max(1.0 - (2.0*rss)**(1.0/3.0), 0.0)
    jb = math.exp(-1.25 * (sb_ft2 / clamp(sm_ft2)) * bypass_arg)
    rb = math.exp(-3.7  * (sb_ft2 / clamp(sm_ft2)) * bypass_arg)

    # ── 4. HEAT TRANSFER ────────────────────────────────────────────────────
    # ho_ideal from user-supplied ji (read from Colburn chart at Re_s)
    ho_ideal = ji * sh.Cp * gs * (sh.Pr**(-2.0/3.0)) * Ffactor
    ho       = ho_ideal * jc * jl * jb

    # ── 5. PRESSURE DROP  (Eq. 6.16, Kern-Seader) ───────────────────────────
    # dPi and dPwi must be supplied by user OR estimated from Re_s
    # Here we compute them from first principles matching PHT3 approach:
    #   dPi  [psf] = ideal bundle drop per crossflow row × Nc rows
    #   dPwi [psf] = ideal window drop
    gc = 4.17e8  # [lb·ft / lbf·h²]

    # friction factor for ideal bank (Bell-Delaware correlation)
    if re_s >= 1000:
        f_ideal = 0.372 * re_s**(-0.123)
    else:
        f_ideal = 0.837 * re_s**(-0.292)

    dPi_psf  = (2.0 * f_ideal * nc * gs**2) / (gc * sh.rho)  # [lbf/ft²]
    dPwi_psf = (2.0 + 0.6*ncw) * ws**2 / (2.0 * gc * sh.rho * clamp(sm_ft2 * sw_ft2))

    term1    = ((nb - 1) * dPi_psf * rb + nb * dPwi_psf) * rl
    term2    = 2.0 * dPi_psf * (1.0 + ncw / nc) * rb
    dp_f_psi = (term1 + term2) / 144.0                        # [psi]
    dp_total = dp_f_psi + dpn                                  # [psi]

    return {
        "hi":      float(ho_ideal),
        "ho":      float(ho),
        "Re":      float(re_s),
        "Sm_ft2":  float(sm_ft2),
        "Sw_ft2":  float(sw_ft2),
        "Stb_ft2": float(stb_ft2),
        "Ssb_ft2": float(ssb_ft2),
        "Fc":      float(fc),
        "Fw":      float(fw),
        "Jc":      float(jc),
        "JL":      float(jl),
        "JB":      float(jb),
        "RL":      float(rl),
        "RB":      float(rb),
        "Jt":      float(jc*jl*jb),
        "DP_fric": float(dp_f_psi),
        "DP":      float(dp_total),
    }

def safe(inp, sh, tu):
    try: return kern(inp, sh, tu)
    except: return {"DP_s":np.nan,"DP_t":np.nan,"ho":np.nan}

def sens(base, sh, tu):
    o = {}
    x = np.linspace(20000, 120000, 36)
    o["flow"] = (x, [safe({**base,"m_h":v},sh,tu)["DP_s"] for v in x],[safe({**base,"m_h":v},sh,tu)["DP_t"] for v in x])
    x = np.linspace(0.5, 1.5, 32)
    o["do"] = (x, [safe({**base,"Do_in":v,"Di_in":min(base["Di_in"],0.82*v),"PT_in":max(base["PT_in"],v+0.1)},sh,tu)["DP_s"] for v in x],[safe({**base,"Do_in":v,"Di_in":min(base["Di_in"],0.82*v),"PT_in":max(base["PT_in"],v+0.1)},sh,tu)["DP_t"] for v in x])
    x = np.linspace(6, 30, 32)
    o["len"] = (x, [safe({**base,"L_ft":v},sh,tu)["DP_s"] for v in x],[safe({**base,"L_ft":v},sh,tu)["DP_t"] for v in x])
    x = np.linspace(3.0, 15.0, 32)
    o["baf"] = (x, [safe({**base,"B_space_in":v},sh,tu)["DP_s"] for v in x])
    x = np.linspace(0.5, 20.0, 32)
    o["vis"] = (x, [safe(base,FP(sh.name,sh.Cp,sh.k,v,sh.sg),tu)["DP_s"] for v in x])
    return o

def make_chart(base, sh, tu):
    s = sens(base, sh, tu)

    um = st.session_state.get("u_m_h", "lb/h")
    ul = st.session_state.get("u_Do_in", "in")
    udp = st.session_state.get("u_DP_limit_shell", "psi")

    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=(
            "<b>Mass Flow Rate</b>",
            "<b>Tube OD</b>",
            "<b>Tube Length</b>",
            "<b>Baffle Spacing</b>",
            "<b>Shell Viscosity</b>"
        ),
        specs=[[{"secondary_y":True},{"secondary_y":True},{"secondary_y":True}],[{"secondary_y":True},{"secondary_y":True},None]],
        vertical_spacing=0.18,
        horizontal_spacing=0.1
    )

    purple = "#7C3AED"
    cyan = "#06B6D4"

    # Mass Flow
    x, ds, dt = s["flow"]
    fig.add_trace(go.Scatter(x=x, y=ds, name="Shell ΔP", mode="lines", line=dict(color=purple, width=3), fill='tozeroy', fillcolor='rgba(124,58,237,0.1)'), row=1, col=1)
    fig.add_trace(go.Scatter(x=x, y=dt, name="Tube ΔP", mode="lines", line=dict(color=cyan, width=3, dash="dash"), fill='tozeroy', fillcolor='rgba(6,182,212,0.05)'), row=1, col=1, secondary_y=True)
    fig.update_xaxes(title_text=f"Mass Flow ({um})", row=1, col=1)
    fig.update_yaxes(title_text=f"ΔP ({udp})", row=1, col=1)
    fig.update_yaxes(title_text=f"ΔP ({udp})", secondary_y=True, row=1, col=1)

    # Tube OD
    x, ds, dt = s["do"]
    fig.add_trace(go.Scatter(x=x, y=ds, showlegend=False, mode="lines", line=dict(color=purple, width=3), fill='tozeroy', fillcolor='rgba(124,58,237,0.1)'), row=1, col=2)
    fig.add_trace(go.Scatter(x=x, y=dt, showlegend=False, mode="lines", line=dict(color=cyan, width=3, dash="dash"), fill='tozeroy', fillcolor='rgba(6,182,212,0.05)'), row=1, col=2, secondary_y=True)
    fig.update_xaxes(title_text=f"Tube OD ({ul})", row=1, col=2)
    fig.update_yaxes(title_text=f"ΔP ({udp})", row=1, col=2)
    fig.update_yaxes(title_text=f"ΔP ({udp})", secondary_y=True, row=1, col=2)

    # Tube Length
    x, ds, dt = s["len"]
    fig.add_trace(go.Scatter(x=x, y=ds, showlegend=False, mode="lines", line=dict(color=purple, width=3), fill='tozeroy', fillcolor='rgba(124,58,237,0.1)'), row=1, col=3)
    fig.add_trace(go.Scatter(x=x, y=dt, showlegend=False, mode="lines", line=dict(color=cyan, width=3, dash="dash"), fill='tozeroy', fillcolor='rgba(6,182,212,0.05)'), row=1, col=3, secondary_y=True)
    fig.update_xaxes(title_text="Tube Length (ft)", row=1, col=3)
    fig.update_yaxes(title_text=f"ΔP ({udp})", row=1, col=3)
    fig.update_yaxes(title_text=f"ΔP ({udp})", secondary_y=True, row=1, col=3)

    # Baffle Spacing
    x, ds = s["baf"]
    fig.add_trace(go.Scatter(x=x, y=ds, showlegend=False, mode="lines", line=dict(color=purple, width=3), fill='tozeroy', fillcolor='rgba(124,58,237,0.1)'), row=2, col=1)
    fig.update_xaxes(title_text="Baffle Ratio (B/Ds)", row=2, col=1)
    fig.update_yaxes(title_text=f"ΔP ({udp})", row=2, col=1)

    # Shell Viscosity
    x, ds = s["vis"]
    fig.add_trace(go.Scatter(x=x, y=ds, showlegend=False, mode="lines", line=dict(color=purple, width=3), fill='tozeroy', fillcolor='rgba(124,58,237,0.1)'), row=2, col=2)
    fig.update_xaxes(title_text="Viscosity (lb/ft·h)", row=2, col=2)
    fig.update_yaxes(title_text=f"ΔP ({udp})", row=2, col=2)

    fig.update_layout(
        height=750, margin=dict(l=50, r=50, t=60, b=60),
        paper_bgcolor="white", plot_bgcolor="#FAFAFA",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0.5, xanchor="center", bgcolor="rgba(255,255,255,0.8)", bordercolor="#E5E7EB", borderwidth=1),
        font=dict(family="Inter, sans-serif", color="#1F2937", size=12), title_font_size=16, showlegend=True
    )

    for i in range(1, 4):
        for j in range(1, 4):
            fig.update_xaxes(showgrid=True, gridcolor="#E5E7EB", gridwidth=1, title_font_size=11, tickfont_size=10, linecolor="#D1D5DB", row=j if i == 1 else None, col=i)
            fig.update_yaxes(showgrid=True, gridcolor="#E5E7EB", gridwidth=1, title_font_size=11, tickfont_size=10, linecolor="#D1D5DB", row=j if i == 1 else None, col=i)

    return fig

# ═══════════════════════════════════════════════════════════════
# NAVIGATION BAR
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="nav-container">
    <div class="nav-content">
        <div class="nav-brand">
            <div class="nav-brand-icon">⬢</div>
            <span>STHE Designer</span>
        </div>
        <div class="nav-links">
            <a class="nav-link" href="#home">Home</a>
            <a class="nav-link" href="#input">Inputs</a>
            <a class="nav-link" href="#kern">Kern Method</a>
            <a class="nav-link" href="#delaware">Delaware Method</a>
            <a class="nav-link" href="#designcheck">Design Check</a>
            <a class="nav-link" href="#sensitivity">Sensitivity Analysis</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HOME SECTION
st.markdown('<section id="home"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-card">
    <div class="hero-content">
        <div class="hero-badge">
            <span>🔬</span> CHPE4412 - Heat Exchanger Design
        </div>
        <h1 class="hero-title">Shell-and-Tube Heat Exchanger</h1>
        <p class="hero-description">
            Professional engineering tool for designing and analyzing shell-and-tube heat exchangers using Kern and Delaware methods with real-time sensitivity analysis.
        </p>
        <div class="hero-tags">
            <span class="hero-tag">Group 2</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT SECTION
st.markdown('<section id="input"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-icon">⚙️</div>
    <div>
        <h2 class="section-title">Process Inputs</h2>
    </div>
</div>
""", unsafe_allow_html=True)

def inp_row(label, key, group, min_v=None, step=None, fmt="%.3f"):
    u = st.session_state.get(f"u_{key}", UNITS[group][0])
    val = st.session_state[f"v_{key}"]
    if group == "mass_flow": dv = conv_mb(val, u); ni = lambda x: conv_m(x, u)
    elif group == "temperature": dv = conv_tb(val, u); ni = lambda x: conv_t(x, u)
    elif group == "length": dv = conv_lb(val, u); ni = lambda x: conv_l(x, u)
    elif group == "length_in": dv = conv_lib(val, u); ni = lambda x: conv_li(x, u)
    elif group == "density": dv = conv_db(val, u); ni = lambda x: conv_d(x, u)
    elif group == "cp": dv = conv_cpb(val, u); ni = lambda x: conv_cp(x, u)
    elif group == "k": dv = conv_kb(val, u); ni = lambda x: conv_k(x, u)
    elif group == "viscosity": dv = conv_visb(val, u); ni = lambda x: conv_vis(x, u)
    elif group == "fouling": dv = conv_fb(val, u); ni = lambda x: conv_f(x, u)
    elif group == "u": dv = conv_ub(val, u); ni = lambda x: conv_u(x, u)
    elif group == "dp": dv = conv_dpb(val, u); ni = lambda x: conv_dp(x, u)
    elif group == "sg": dv = val; ni = lambda x: x
    elif group == "count": dv = int(val); ni = lambda x: int(x)
    else: dv = val; ni = lambda x: x

    # Convert min_v and step from internal units to display units
    def to_display(v):
        if v is None: return None
        if group == "mass_flow": return conv_mb(v, u)
        if group == "temperature": return None  # temps have no meaningful min in display
        if group == "length": return conv_lb(v, u)
        if group == "length_in": return conv_lib(v, u)
        if group == "density": return conv_db(v, u)
        if group == "cp": return conv_cpb(v, u)
        if group == "k": return conv_kb(v, u)
        if group == "viscosity": return conv_visb(v, u)
        if group == "fouling": return conv_fb(v, u)
        if group == "u": return conv_ub(v, u)
        if group == "dp": return conv_dpb(v, u)
        return float(v)
    min_v_f = to_display(min_v)
    step_f = to_display(step) if step is not None else None

    st.markdown(f'<div class="input-label-text">{label}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([2.5, 1])
    with col1:
        st.number_input("__", value=float(dv), min_value=min_v_f, step=step_f, format=fmt, key=f"in_{key}", label_visibility="collapsed")
        st.session_state[f"v_{key}"] = ni(st.session_state[f"in_{key}"])
    with col2:
        idx = UNITS[group].index(u) if u in UNITS[group] else 0
        st.selectbox("__", UNITS[group], key=f"u_{key}", label_visibility="collapsed", index=idx)

col1, col2 = st.columns(2)
with col1:
    inp_row("Shell Mass Flow", "m_h", "mass_flow", 1.0, 1000.0, "%.2f")
    inp_row("Tube Mass Flow", "m_c", "mass_flow", 1.0, 1000.0, "%.2f")
    inp_row("Hot Inlet Temp", "T_hin", "temperature", None, 1.0, "%.2f")
    inp_row("Hot Outlet Temp", "T_hout", "temperature", None, 1.0, "%.2f")
    inp_row("Cold Inlet Temp", "T_cin", "temperature", None, 1.0, "%.2f")
    inp_row("Cold Outlet Temp", "T_cout", "temperature", None, 1.0, "%.2f")

with col2:
    inp_row("Tube OD", "Do_in", "length_in", 0.1, 0.05, "%.3f")
    inp_row("Tube ID", "Di_in", "length_in", 0.05, 0.05, "%.3f")
    st.markdown('<div class="input-label-text">Tube Length</div>', unsafe_allow_html=True)
    col_tl1, col_tl2 = st.columns([2.5, 1])
    with col_tl1:
        st.number_input("__", value=float(st.session_state["v_L_ft"]), min_value=1.0, step=1.0, format="%.2f", key="in_L_ft", label_visibility="collapsed")
        st.session_state["v_L_ft"] = st.session_state["in_L_ft"]
    with col_tl2:
        st.selectbox("__", ["ft"], key="u_L_ft", label_visibility="collapsed")
    inp_row("Tube Pitch", "PT_in", "length_in", 0.2, 0.05, "%.3f")
    inp_row("Shell Fouling", "Rd_shell", "fouling", 0.0, 0.0001, "%.5f")
    inp_row("Tube Fouling", "Rd_tube", "fouling", 0.0, 0.0001, "%.5f")
    inp_row("Estimated U", "UD_est", "u", 0.1, 1.0, "%.2f")
    inp_row("Shell ΔP Limit", "DP_limit_shell", "dp", 0.1, 0.5, "%.2f")
    inp_row("Tube ΔP Limit",  "DP_limit_tube",  "dp", 0.1, 0.5, "%.2f")

st.markdown("---")
c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="input-label-text">Tube Passes</div>', unsafe_allow_html=True)
    np_default = DEFAULTS["n_p"]
    np_options = [1,2,4,6,8]
    np_idx = np_options.index(st.session_state["v_n_p"]) if st.session_state["v_n_p"] in np_options else np_options.index(np_default)
    st.selectbox("__", np_options, index=np_idx, key="in_n_p", label_visibility="collapsed")
    st.session_state["v_n_p"] = st.session_state["in_n_p"]
    inp_row("Cp Shell", "Cp_shell", "cp", 0.001, 0.01, "%.4f")
    inp_row("k Shell", "k_shell", "k", 0.001, 0.01, "%.4f")
    inp_row("Viscosity Shell", "mu_shell", "viscosity", 0.1, 0.1, "%.3f")
    inp_row("SG Shell", "sg_shell", "sg", 0.1, 0.01, "%.3f")
with c4:
    inp_row("Cp Tube", "Cp_tube", "cp", 0.001, 0.01, "%.4f")
    inp_row("k Tube", "k_tube", "k", 0.001, 0.01, "%.4f")
    inp_row("Viscosity Tube", "mu_tube", "viscosity", 0.1, 0.1, "%.3f")
    inp_row("SG Tube", "sg_tube", "sg", 0.1, 0.01, "%.3f")
    inp_row("F Factor", "Ffactor", "factor", 0.1, 0.1, "%.2f")

st.markdown("---")
c7, c8 = st.columns(2)
with c7:
    inp_row("No. Tubes", "n_tubes", "count", 10, 10, "%.0f")
    inp_row("Shell ID", "Ds_in", "length_in", 8.0, 0.25, "%.2f")
    inp_row("Baffle Space", "B_space_in", "length_in", 1.0, 0.5, "%.3f")
with c8:
    inp_row("Metal k", "k_metal", "k", 10.0, 1.0, "%.1f")

st.markdown("---")
st.markdown("""
<div class="section-header" style="margin-top:8px;">
    <div class="section-icon cyan" style="width:36px;height:36px;font-size:1rem;">🔬</div>
    <div><h2 class="section-title" style="font-size:1.1rem;">Delaware Method — Additional Inputs</h2></div>
</div>
""", unsafe_allow_html=True)
cd1, cd2 = st.columns(2)
with cd1:
    inp_row("Tube Bundle OTL (Dotl)", "Dotl_in",     "length_in", 1.0,    0.1,   "%.3f")
    inp_row("Tube-Baffle Clearance",  "delta_tb_in", "length_in", 0.001,  0.001, "%.4f")
    inp_row("Shell-Baffle Clearance", "delta_sb_in", "length_in", 0.001,  0.001, "%.4f")
    inp_row("Baffle Cut Fraction",    "Bc_frac",     "factor",    0.05,   0.01,  "%.3f")
    inp_row("Nss/Nc (Sealing Ratio)", "Nss_Nc",      "factor",    0.0,    0.01,  "%.3f")
with cd2:
    inp_row("Ncw (Window Rows)",      "Ncw",         "factor",    1.0,    1.0,   "%.1f")
    inp_row("Nc  (Crossflow Rows)",   "Nc",          "factor",    1.0,    1.0,   "%.1f")
    inp_row("Nb  (No. of Baffles)",   "Nb",          "count",     1,      1,     "%.0f")
    inp_row("Nozzle ΔP",              "DP_nozzle",   "dp",        0.0,    0.01,  "%.3f")
    inp_row("Ideal j-factor (ji)",    "ji_factor",   "factor",    0.0001, 0.0001,"%.4f")

st.markdown('</div>', unsafe_allow_html=True)

# CALCULATIONS
inputs = {k: st.session_state[f"v_{k}"] for k in DEFAULTS}
sh = FP("Shell", st.session_state["v_Cp_shell"], st.session_state["v_k_shell"], st.session_state["v_mu_shell"], st.session_state["v_sg_shell"])
tu = FP("Tube", st.session_state["v_Cp_tube"], st.session_state["v_k_tube"], st.session_state["v_mu_tube"], st.session_state["v_sg_tube"])

try:
    kr = kern(inputs, sh, tu)
    de = delaware(inputs, sh, kr["nt"], kr["Ds"])
except Exception as e:
    st.error(str(e)); st.stop()

um, ut = st.session_state["u_m_h"], st.session_state["u_T_hin"]
ul, uu, udp = st.session_state["u_Do_in"], st.session_state["u_UD_est"], st.session_state["u_DP_limit_shell"]

# KERN METHOD SECTION
st.markdown('<section id="kern"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-icon">📊</div>
        <div>
            <h2 class="section-title">Kern Method Analysis</h2>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)

kern_data = [
    ("Q", kr["Q"], "Btu/h", "Heat Duty", "🔥"),
    ("LMTD", kr["LMTD"], ut, "Log-mean Temp", "🌡️"),
    ("F Factor", st.session_state["v_Ffactor"], "-", "User Input", "📐"),
    ("n Tubes", kr["nt"], "-", "Tube Count", "🔢"),
    ("Shell Diam", conv_lib(kr["Ds"],ul), ul, "Shell Size", "⭕"),
    ("Uc Clean", conv_ub(kr["Uc"],uu), uu, "Clean Coeff", "✨"),
    ("hᵢ Tube", conv_ub(kr["hi"],uu), uu, "Tube Coeff", "💨"),
    ("hₒ Shell", conv_ub(kr["ho"],uu), uu, "Shell Coeff", "🌊"),
]

for t, v, u_, n, icon in kern_data:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{t} {'' if u_=='-' else f'({u_})'}</div>
        <div class="kpi-value">{fval(v, 3 if t=='F Factor' else (0 if u_=='-' else 2))}</div>
        <div class="kpi-note">{n}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="kpi-grid" style="margin-top:16px;">', unsafe_allow_html=True)

kern_data2 = [
    ("Re Tube", kr["Re_t"], "-", "Reynolds", "⚡"),
    ("Re Shell", kr["Re_s"], "-", "Reynolds", "🌀"),
    ("ΔP Tube", conv_dpb(kr["DP_t"],udp), udp, "Tube Drop", "📉"),
    ("ΔP Shell", conv_dpb(kr["DP_s"],udp), udp, "Shell Drop", "📊"),
    ("Over-surface", kr["ov_s"], "%", "Clean Margin", "🎯"),
    ("UD Design", conv_ub(kr["UD"],uu), uu, "Design Coeff", "🎛️"),
    ("Baffle Spacing", conv_lib(kr["B"],ul), ul, "Baffle", "📏"),
    ("n Baffles", kr["nb"], "-", "Count", "🔱"),
]

for t, v, u_, n, icon in kern_data2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{t} {'' if u_=='-' else f'({u_})'}</div>
        <div class="kpi-value">{fval(v, 0 if u_=='-' else 2)}</div>
        <div class="kpi-note">{n}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# DELAWARE METHOD SECTION
st.markdown('<section id="delaware"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-icon cyan">🔬</div>
        <div>
            <h2 class="section-title">Delaware Method Analysis</h2>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)

# Row 1: key heat-transfer results
delaware_data = [
    ("h Ideal",      conv_ub(de["hi"],uu),    uu,  "Ideal Shell Coeff",   "⚡"),
    ("h Corrected",  conv_ub(de["ho"],uu),    uu,  "Final Shell Coeff",   "✨"),
    ("Re Delaware",  de["Re"],                "-", "Shell Reynolds",      "🌀"),
    ("Sm (ft²)",     de["Sm_ft2"],            "-", "Crossflow Area",      "📐"),
    ("Sw (ft²)",     de["Sw_ft2"],            "-", "Window Area",         "🪟"),
    ("Stb (ft²)",    de["Stb_ft2"],           "-", "Tube-Baffle Leak",    "🔩"),
    ("Ssb (ft²)",    de["Ssb_ft2"],           "-", "Shell-Baffle Leak",   "🔧"),
    ("Fc",           de["Fc"],                "-", "Crossflow Fraction",  "🔢"),
]

for t, v, u_, n, icon in delaware_data:
    dp = 4 if t in ("Sm (ft²)","Sw (ft²)","Stb (ft²)","Ssb (ft²)") else (3 if t in ("Fc",) else (0 if u_=="-" and t=="Re Delaware" else 2))
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{t} {''  if u_=='-' else f'({u_})'}</div>
        <div class="kpi-value">{fval(v, dp)}</div>
        <div class="kpi-note">{n}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Row 2: correction factors & pressure drop
st.markdown('<div class="kpi-grid" style="margin-top:16px;">', unsafe_allow_html=True)
delaware_data2 = [
    ("Jc Factor",    de["Jc"],                "-",  "Baffle-Cut Corr",   "📐"),
    ("JL Factor",    de["JL"],                "-",  "Leakage Corr",      "💧"),
    ("JB Factor",    de["JB"],                "-",  "Bypass Corr",       "🔀"),
    ("RL Factor",    de["RL"],                "-",  "Leak ΔP Corr",      "🎚️"),
    ("RB Factor",    de["RB"],                "-",  "Bypass ΔP Corr",    "🎛️"),
    ("J Total",      de["Jt"],                "-",  "Jc×JL×JB",         "🎯"),
    ("ΔP Friction",  conv_dpb(de["DP_fric"],udp), udp, "Bundle + Window Drop", "📊"),
    ("ΔP Total",     conv_dpb(de["DP"],udp),  udp,  "Incl. Nozzle Drop", "📉"),
]

for t, v, u_, n, icon in delaware_data2:
    dp = 4 if t in ("Jc Factor","JL Factor","JB Factor","RL Factor","RB Factor","J Total") else 2
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{t} {''  if u_=='-' else f'({u_})'}</div>
        <div class="kpi-value">{fval(v, dp)}</div>
        <div class="kpi-note">{n}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# DESIGN VALIDATION & OPTIMIZATION SECTION
# ═══════════════════════════════════════════════════════════════
st.markdown('<section id="designcheck"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-icon" style="background:linear-gradient(135deg,#F59E0B,#D97706);">✅</div>
    <div><h2 class="section-title">Design Validation & Optimization</h2></div>
</div>
""", unsafe_allow_html=True)

dp_lim_shell = float(inputs["DP_limit_shell"])  # shell DP limit [psi]
dp_lim_tube  = float(inputs["DP_limit_tube"])   # tube DP limit [psi]
udp_val = st.session_state["u_DP_limit_shell"]

def make_check(title, value, limit, unit, pass_cond, fmt=".2f", note=""):
    status = "pass" if pass_cond else ("warn" if abs(value - limit)/max(abs(limit),1e-9) < 0.15 else "fail")
    dot    = "🟢" if status=="pass" else ("🟡" if status=="warn" else "🔴")
    return {"title":title,"value":value,"limit":limit,"unit":unit,
            "status":status,"dot":dot,"fmt":fmt,"note":note}

# ── Build checks for both methods ────────────────────────────────────────
kern_dp_s  = conv_dpb(kr["DP_s"],  udp_val)
kern_dp_t  = conv_dpb(kr["DP_t"],  udp_val)
de_dp_tot  = conv_dpb(de["DP"],    udp_val)
dp_lim_shell_disp = conv_dpb(dp_lim_shell, udp_val)
dp_lim_tube_disp  = conv_dpb(dp_lim_tube,  udp_val)

kern_checks = [
    make_check("Kern — Shell ΔP",   kern_dp_s,    dp_lim_shell_disp, udp_val,  kern_dp_s  <= dp_lim_shell_disp),
    make_check("Kern — Tube ΔP",    kern_dp_t,    dp_lim_tube_disp,  udp_val,  kern_dp_t  <= dp_lim_tube_disp),
    make_check("Over-surface %",    kr["ov_s"],   35.0,        "%",      0 < kr["ov_s"] <= 35,    ".1f", "Ideal: 0–35 %"),
    make_check("F Factor",          kr["F"],      0.75,        "—",      kr["F"]    >= 0.75,      ".3f", "Must be ≥ 0.75"),
    make_check("Re Tube (turbulent)",kr["Re_t"],  10000,       "—",      kr["Re_t"] >= 10000,     ".0f", "Need Re > 10 000"),
    make_check("Re Shell",          kr["Re_s"],   100,         "—",      kr["Re_s"] >= 100,       ".0f", "Need Re > 100"),
    make_check("Di/Do ratio",       inputs["Di_in"]/max(inputs["Do_in"],1e-9), 0.7, "—",
               inputs["Di_in"]/max(inputs["Do_in"],1e-9) >= 0.7, ".3f", "Need Di/Do ≥ 0.70"),
    make_check("Baffle/Shell ratio",inputs["B_space_in"]/max(inputs["Ds_in"],1e-9), 0.20, "—",
               0.20 <= inputs["B_space_in"]/max(inputs["Ds_in"],1e-9) <= 1.0, ".3f", "Ideal: 0.20–1.00"),
]

de_checks = [
    make_check("Delaware — Shell ΔP", de_dp_tot,  dp_lim_shell_disp, udp_val, de_dp_tot  <= dp_lim_shell_disp),
    make_check("Jc (baffle cut)",     de["Jc"],   0.60,        "—",     de["Jc"]   >= 0.60,  ".3f", "Good: ≥ 0.60"),
    make_check("JL (leakage)",        de["JL"],   0.60,        "—",     de["JL"]   >= 0.60,  ".3f", "Good: ≥ 0.60"),
    make_check("JB (bypass)",         de["JB"],   0.60,        "—",     de["JB"]   >= 0.60,  ".3f", "Good: ≥ 0.60"),
    make_check("J Total",             de["Jt"],   0.40,        "—",     de["Jt"]   >= 0.40,  ".3f", "Good: ≥ 0.40"),
    make_check("Re Delaware",         de["Re"],   1000,        "—",     de["Re"]   >= 1000,  ".0f", "Need Re > 1000"),
]

all_checks  = kern_checks + de_checks
n_fail = sum(1 for c in all_checks if c["status"]=="fail")
n_warn = sum(1 for c in all_checks if c["status"]=="warn")

# ── Overall banner ────────────────────────────────────────────────────────
if n_fail == 0 and n_warn == 0:
    banner_cls, banner_icon, banner_msg = "pass", "✅", "Design is fully acceptable — all checks passed."
elif n_fail == 0:
    banner_cls, banner_icon, banner_msg = "warn", "⚠️", f"Design has {n_warn} marginal check(s) — review highlighted items."
else:
    banner_cls, banner_icon, banner_msg = "fail", "❌", f"Design FAILS {n_fail} check(s) — optimization recommended."

st.markdown(f'''
<div class="validation-banner {banner_cls}">
    <span style="font-size:1.6rem;">{banner_icon}</span>
    <span>{banner_msg}</span>
</div>
''', unsafe_allow_html=True)

# ── Kern checks grid ──────────────────────────────────────────────────────
st.markdown("**Kern Method Checks**")
st.markdown('<div class="check-grid">', unsafe_allow_html=True)
for c in kern_checks:
    lim_txt = (f"Limit: " + format(c['limit'], c['fmt'])) if isinstance(c['limit'],float) else f"Limit: {c['limit']}"
    st.markdown(f'''
    <div class="check-card {c['status']}">
        <div class="check-dot">{c['dot']}</div>
        <div>
            <div class="check-title">{c['title']}</div>
            <div class="check-value">{format(c['value'], c['fmt'])}{" "+c['unit'] if c['unit'] not in ("—","-") else ""}</div>
            <div class="check-limit">{c['note'] or lim_txt}</div>
        </div>
    </div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Delaware checks grid ──────────────────────────────────────────────────
st.markdown("**Delaware Method Checks**")
st.markdown('<div class="check-grid">', unsafe_allow_html=True)
for c in de_checks:
    lim_txt = (f"Limit: " + format(c['limit'], c['fmt'])) if isinstance(c['limit'],float) else f"Limit: {c['limit']}"
    st.markdown(f'''
    <div class="check-card {c['status']}">
        <div class="check-dot">{c['dot']}</div>
        <div>
            <div class="check-title">{c['title']}</div>
            <div class="check-value">{format(c['value'], c['fmt'])}{" "+c['unit'] if c['unit'] not in ("—","-") else ""}</div>
            <div class="check-limit">{c['note'] or lim_txt}</div>
        </div>
    </div>''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Optimization Panel (only if failures exist) ───────────────────────────
if n_fail > 0:
    st.markdown('<div class="opt-box">', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-header" style="margin-bottom:12px;">
        <div class="section-icon" style="width:38px;height:38px;font-size:1rem;background:linear-gradient(135deg,#7C3AED,#06B6D4);">⚙️</div>
        <div><h2 class="section-title" style="font-size:1.1rem;">Automated Optimization</h2></div>
    </div>
    """, unsafe_allow_html=True)

    opt_param = st.selectbox(
        "Parameter to optimize",
        ["Baffle Spacing (B)", "No. of Tubes (nt)", "Tube Passes (np)", "Shell ID (Ds)", "Tube Length (L)"],
        key="opt_param_sel"
    )

    oc1, oc2, oc3 = st.columns(3)
    with oc1:
        if opt_param == "Baffle Spacing (B)":
            lo = st.number_input("Min B (in)", value=2.0,  min_value=1.0, step=0.5, key="opt_lo")
            hi_v= st.number_input("Max B (in)", value=20.0, min_value=2.0, step=0.5, key="opt_hi")
        elif opt_param == "No. of Tubes (nt)":
            lo = st.number_input("Min tubes", value=100, min_value=10, step=10, key="opt_lo")
            hi_v= st.number_input("Max tubes", value=600, min_value=50, step=10, key="opt_hi")
        elif opt_param == "Tube Passes (np)":
            lo = 1; hi_v = 8
            st.info("Will sweep: 1, 2, 4, 6, 8 passes")
        elif opt_param == "Shell ID (Ds)":
            lo = st.number_input("Min Ds (in)", value=10.0, min_value=4.0,  step=1.0, key="opt_lo")
            hi_v= st.number_input("Max Ds (in)", value=48.0, min_value=10.0, step=1.0, key="opt_hi")
        else:  # Tube Length
            lo = st.number_input("Min L (ft)", value=6.0,  min_value=1.0, step=1.0, key="opt_lo")
            hi_v= st.number_input("Max L (ft)", value=30.0, min_value=2.0, step=1.0, key="opt_hi")
    with oc2:
        n_steps = st.number_input("Search steps", value=40, min_value=10, max_value=200, step=5, key="opt_steps")
    with oc3:
        st.markdown("<br>", unsafe_allow_html=True)
        run_opt = st.button("🔍  Run Optimization", use_container_width=True)

    if run_opt:
        with st.spinner("Searching for optimal design…"):
            base_inp = dict(inputs)
            if opt_param == "Tube Passes (np)":
                sweep = [1, 2, 4, 6, 8]
            else:
                sweep = list(np.linspace(lo, hi_v, int(n_steps)))

            best = None
            results_table = []

            for val in sweep:
                trial = dict(base_inp)
                if opt_param == "Baffle Spacing (B)":   trial["B_space_in"] = float(val)
                elif opt_param == "No. of Tubes (nt)":  trial["n_tubes"]    = int(val)
                elif opt_param == "Tube Passes (np)":   trial["n_p"]        = int(val)
                elif opt_param == "Shell ID (Ds)":      trial["Ds_in"]      = float(val)
                else:                                    trial["L_ft"]       = float(val)

                try:
                    kr_t = kern(trial, sh, tu)
                    de_t = delaware(trial, sh, kr_t["nt"], kr_t["Ds"])
                    dp_s = kr_t["DP_s"]; dp_t = kr_t["DP_t"]; dp_de = de_t["DP"]
                    os_  = kr_t["ov_s"]
                    ok = (dp_s <= dp_lim_shell and dp_t <= dp_lim_tube and dp_de <= dp_lim_shell
                          and 0 < os_ <= 35 and kr_t["F"] >= 0.75)
                    results_table.append({
                        "param_val": val,
                        "DP_shell_K": dp_s, "DP_tube_K": dp_t,
                        "DP_de": dp_de, "oversurface": os_,
                        "F": kr_t["F"], "passes": ok
                    })
                    if ok and best is None:
                        best = (val, kr_t, de_t, trial)
                except:
                    continue

            st.session_state["opt_results_table"] = results_table
            st.session_state["opt_best"] = best
            st.session_state["opt_param_used"] = opt_param
            st.session_state["opt_best_inp"] = best[3] if best else None

    # ── Show optimization results ─────────────────────────────────────────
    if st.session_state.get("opt_results_table"):
        rt    = st.session_state["opt_results_table"]
        best  = st.session_state.get("opt_best")
        pname = st.session_state.get("opt_param_used","")

        if best:
            bval, kr_b, de_b, best_inp = best
            st.success(f"✅ Optimal value found: **{pname.split('(')[0].strip()} = {bval:.3f}**")

            # Comparison table
            def row(label, cur, opt, unit="", fmt=".2f", lower_better=True):
                cur_v = float(cur); opt_v = float(opt)
                improved = (opt_v < cur_v) if lower_better else (opt_v > cur_v)
                cur_cls  = "bad"  if not improved else ""
                opt_cls  = "good" if improved     else ""
                return f"""<tr>
                  <td>{label}</td>
                  <td class="{cur_cls}">{cur_v:{fmt}} {unit}</td>
                  <td class="{opt_cls} changed">{opt_v:{fmt}} {unit}</td>
                  <td>{"✅ Better" if improved else "— Same/Worse"}</td>
                </tr>"""

            param_label = pname.split("(")[0].strip()
            cur_val_map = {
                "Baffle Spacing (B)":  inputs["B_space_in"],
                "No. of Tubes (nt)":   inputs["n_tubes"],
                "Tube Passes (np)":    inputs["n_p"],
                "Shell ID (Ds)":       inputs["Ds_in"],
                "Tube Length (L)":     inputs["L_ft"],
            }
            cur_pval = cur_val_map.get(pname, 0)

            table_html = f"""
<table class="opt-table">
  <thead><tr>
    <th>Metric</th><th>Current Design</th><th>Optimized</th><th>Status</th>
  </tr></thead>
  <tbody>
    <tr><td><b>{param_label}</b></td>
        <td class="changed">{cur_pval:.3f}</td>
        <td class="changed">{bval:.3f}</td><td>🔧 Modified</td></tr>
    {row("Kern — Shell ΔP (psi)", kr["DP_s"], kr_b["DP_s"], "psi")}
    {row("Kern — Tube ΔP (psi)",  kr["DP_t"], kr_b["DP_t"], "psi")}
    {row("Delaware — Shell ΔP (psi)", de["DP"],  de_b["DP"],  "psi")}
    {row("Over-surface (%)", kr["ov_s"], kr_b["ov_s"], "%", ".1f", lower_better=False)}
    {row("F Factor",         kr["F"],    kr_b["F"],    "",  ".3f", lower_better=False)}
    {row("Re Tube",          kr["Re_t"], kr_b["Re_t"], "",  ".0f", lower_better=False)}
    {row("Re Shell (Kern)",  kr["Re_s"], kr_b["Re_s"], "",  ".0f", lower_better=False)}
    {row("Uc Clean (Btu/h·ft²·°F)", kr["Uc"], kr_b["Uc"], "", ".2f", lower_better=False)}
    {row("ho Shell — Kern",  kr["ho"],   kr_b["ho"],   "", ".2f", lower_better=False)}
    {row("ho Shell — Delaware", de["ho"], de_b["ho"],  "", ".2f", lower_better=False)}
  </tbody>
</table>"""
            st.markdown(table_html, unsafe_allow_html=True)

            # Apply button
            st.markdown("<br>", unsafe_allow_html=True)
            apply_col, _ = st.columns([1, 3])
            with apply_col:
                if st.button("⚡  Apply Optimized Values", use_container_width=True, key="apply_opt"):
                    key_map = {
                        "Baffle Spacing (B)":  ("B_space_in", float(bval)),
                        "No. of Tubes (nt)":   ("n_tubes",    int(bval)),
                        "Tube Passes (np)":    ("n_p",        int(bval)),
                        "Shell ID (Ds)":       ("Ds_in",      float(bval)),
                        "Tube Length (L)":     ("L_ft",       float(bval)),
                    }
                    k, v = key_map[pname]
                    st.session_state[f"v_{k}"] = v
                    for wk in [f"in_{k}", f"u_{k}"]:
                        st.session_state.pop(wk, None)
                    st.session_state.pop("opt_results_table", None)
                    st.session_state.pop("opt_best", None)
                    st.rerun()
        else:
            st.error("❌ No design in the search range satisfies all constraints. Try widening the search range or relaxing the ΔP limit.")

        # Mini sweep chart
        if len(rt) > 2:
            pvals = [r["param_val"] for r in rt]
            dp_s_vals = [r["DP_shell_K"] for r in rt]
            dp_t_vals = [r["DP_tube_K"]  for r in rt]
            dp_d_vals = [r["DP_de"]      for r in rt]
            fig_opt = go.Figure()
            fig_opt.add_trace(go.Scatter(x=pvals, y=dp_s_vals, name="Kern Shell ΔP",    mode="lines", line=dict(color="#7C3AED", width=2)))
            fig_opt.add_trace(go.Scatter(x=pvals, y=dp_t_vals, name="Kern Tube ΔP",     mode="lines", line=dict(color="#06B6D4", width=2, dash="dash")))
            fig_opt.add_trace(go.Scatter(x=pvals, y=dp_d_vals, name="Delaware Shell ΔP",mode="lines", line=dict(color="#F59E0B", width=2, dash="dot")))
            fig_opt.add_hline(y=dp_lim_shell, line_color="#EF4444", line_dash="dash", line_width=2,
                              annotation_text=f"Shell ΔP Limit ({dp_lim_shell:.1f} psi)", annotation_position="top right")
            fig_opt.add_hline(y=dp_lim_tube, line_color="#F59E0B", line_dash="dot", line_width=2,
                              annotation_text=f"Tube ΔP Limit ({dp_lim_tube:.1f} psi)", annotation_position="bottom right")
            if best:
                fig_opt.add_vline(x=best[0], line_color="#10B981", line_dash="solid", line_width=2,
                                  annotation_text="Optimal", annotation_position="top left")
            fig_opt.update_layout(
                title=f"<b>ΔP vs {pname}</b>",
                xaxis_title=pname, yaxis_title="ΔP (psi)",
                height=380, margin=dict(l=50,r=50,t=50,b=50),
                paper_bgcolor="white", plot_bgcolor="#FAFAFA",
                font=dict(family="Inter, sans-serif", size=12),
                legend=dict(orientation="h", y=1.12, x=0.5, xanchor="center"),
            )
            st.plotly_chart(fig_opt, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# SENSITIVITY ANALYSIS SECTION
st.markdown('<section id="sensitivity"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-icon">📈</div>
        <div>
            <h2 class="section-title">Sensitivity Analysis</h2>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.plotly_chart(make_chart(inputs, sh, tu), use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Download
df = pd.DataFrame({"Metric": list(kr.keys())+[f"delaware_{k}" for k in de.keys()], "Value": list(kr.values())+list(de.values())})
st.download_button("Download Results CSV", df.to_csv(index=False).encode("utf-8"), "sthe_results.csv", "text/csv")

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-brand">
        <span>⬢</span> Shell & Tube HX Designer
    </div>
    <div>CHPE4412 • Spring 2026</div>
    <div>Naeema Al Amri (141056) • Jumana Al Maani (142225) • Rawya Al Hashimi (141334)</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

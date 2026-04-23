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
    "UD_est": 40.0, "DP_limit": 10.0,
    "Cp_shell": 0.52, "k_shell": 0.074, "mu_shell": 6.65, "sg_shell": 0.82,
    "Cp_tube": 1.00, "k_tube": 0.36, "mu_tube": 1.63, "sg_tube": 1.015,
    "Ffactor": 1.0,
    "n_tubes": 310, "Ds_in": 23.25, "k_metal": 26.0,
}

UNITS = {
    "mass_flow": ["lb/h", "kg/h"],
    "temperature": ["°F", "°C"],
    "length": ["in", "mm"],
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
    "Do_in": "length", "Di_in": "length", "L_ft": "length", "PT_in": "length", "B_space_in": "length", "Ds_in": "length",
    "sg_shell": "sg", "sg_tube": "sg",
    "Cp_shell": "cp", "Cp_tube": "cp",
    "k_shell": "k", "k_tube": "k", "k_metal": "k",
    "mu_shell": "viscosity", "mu_tube": "viscosity",
    "Rd_shell": "fouling", "Rd_tube": "fouling",
    "UD_est": "u", "DP_limit": "dp",
    "n_tubes": "count", "n_p": "count",
    "Ffactor": "factor",
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
def conv_l(v, u): return v if u == "in" else v*25.4
def conv_lb(v, u): return v if u == "in" else v/25.4
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

def reset():
    for k in DEFAULTS: st.session_state[f"v_{k}"] = DEFAULTS[k]
    st.rerun()

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
    m_h = clamp(inp["m_h"])
    Do = clamp(inp["Do_in"])
    PT = clamp(inp["PT_in"])
    Bc, rss = 0.20, 0.10
    B = max(float(inp.get("B_space_in", 6.975)), 1.0)
    L_ft = clamp(inp["L_ft"])
    nb = max(int(round(L_ft/(B/12)))-1, 1)
    dsb = max((0.8+0.002*Ds+0.75)/25.4, 0.08)
    UL = 2*B
    dtb = 0.4/25.4 if UL/12 < 3 else 0.8/25.4
    Ffactor = float(inp.get("Ffactor", 1.0))

    Ddotl = max(25+0.0135*Ds*25.4, 20)/25.4
    Dotl = Ds - Ddotl
    Dctl = max(Dotl-Do, 0.1)

    Sm = max(B*((Ds-Dotl)+(Dotl-Do)/PT*(PT-Do)), 0.01)
    t_ctl = 2*math.acos(max(min(Ds*(1-2*Bc)/max(Dctl,0.1),1),-1))
    Fc = 1+(1/math.pi)*(math.sin(t_ctl)-t_ctl)

    Stb = 0.5*math.pi*Do*dtb*nt*(1+Fc)
    t_ds = 2*math.acos(max(min(1-2*Bc,1),-1))
    Ssb = Ds*dsb*(math.pi-0.5*t_ds)
    Sb = B*(Ds-Dotl)
    Fw = 0.5*(1-Fc)
    Sw = max((1/8)*Ds**2*(t_ds-math.sin(t_ds))-(1/4)*nt*Fw*math.pi*Do**2, 1)

    Smf = Sm/144; Stbf = Stb/144; SsbF = Ssb/144; SbF = Sb/144; Swf = Sw/144
    G = m_h/clamp(Smf)
    Re = max(abs((Do/12)*G/clamp(sh.mu)), 1)

    if Re > 1000: j, f = 0.321*sp(Re,-0.388), 0.372*sp(Re,-0.123)
    else: j, f = 0.593*sp(Re,-0.477), 0.837*sp(Re,-0.292)

    hi = j*sh.Cp*G*sp(sh.Pr,-2/3)
    Jc = 0.55+0.72*Fc
    rs = SsbF/clamp(SsbF+Stbf)
    rl = (SsbF+Stbf)/clamp(Smf)
    p = 0.8-0.15*(1+rs)
    JL = 0.44*(1-rs)+(1-0.44*(1-rs))*math.exp(-2.2*rl)
    RL = math.exp(-1.33*(1+rs)*sp(rl,p))
    JB = math.exp(-1.25*(SbF/clamp(Smf))*(1-sp(2*rss,1/3)))
    RB = math.exp(-3.7*(SbF/clamp(Smf))*(1-sp(2*rss,1/3)))
    ho = hi*Jc*JL*JB * Ffactor

    Nc, Ncw = Ds*(1-2*Bc)/PT, 0.8*Bc*Ds/PT
    gc = 4.17e8
    dPi = (2*f*Nc*G**2)/(gc*sh.rho)
    dPw = (2+0.6*Ncw)*m_h**2/(2*gc*sh.rho*clamp(Smf*Swf))
    DP = (((nb-1)*dPi*RB+nb*dPw)*RL+2*dPi*(1+Ncw/max(Nc,0.01))*RB)/144

    return {"hi":float(hi),"ho":float(ho),"Re":float(Re),
            "Jc":float(Jc),"JL":float(JL),"JB":float(JB),
            "Jt":float(Jc*JL*JB),"DP":float(DP)}

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
    udp = st.session_state.get("u_DP_limit", "psi")

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
            <a class="nav-link" href="#input">Input</a>
            <a class="nav-link" href="#kern">Kern Method</a>
            <a class="nav-link" href="#delaware">Delaware</a>
            <a class="nav-link" href="#sensitivity">Sensitivity</a>
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
            <span class="hero-tag">Kern Method</span>
            <span class="hero-tag">Delaware Method</span>
            <span class="hero-tag">Sensitivity Analysis</span>
            <span class="hero-tag">Group 2</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT SECTION
st.markdown('<section id="input"></section>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
    <div class="section-header">
        <div class="section-icon">⚙️</div>
        <div>
            <h2 class="section-title">Process Inputs</h2>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="input-panel">', unsafe_allow_html=True)

def inp_row(label, key, group, min_v=None, step=None, fmt="%.3f"):
    u = st.session_state.get(f"u_{key}", UNITS[group][0])
    val = st.session_state[f"v_{key}"]
    if group == "mass_flow": dv = conv_mb(val, u); ni = lambda x: conv_m(x, u)
    elif group == "temperature": dv = conv_tb(val, u); ni = lambda x: conv_t(x, u)
    elif group == "length": dv = conv_lb(val, u); ni = lambda x: conv_l(x, u)
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

    min_v_f = float(min_v) if min_v is not None else None
    step_f = float(step) if step is not None else None

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
    inp_row("Tube OD", "Do_in", "length", 0.1, 0.05, "%.3f")
    inp_row("Tube ID", "Di_in", "length", 0.05, 0.05, "%.3f")
    st.markdown('<div class="input-label-text">Tube Length</div>', unsafe_allow_html=True)
    col_tl1, col_tl2 = st.columns([2.5, 1])
    with col_tl1:
        st.number_input("__", value=float(st.session_state["v_L_ft"]), min_value=1.0, step=1.0, format="%.2f", key="in_L_ft", label_visibility="collapsed")
        st.session_state["v_L_ft"] = st.session_state["in_L_ft"]
    with col_tl2:
        st.selectbox("__", ["ft"], key="u_L_ft", label_visibility="collapsed")
    inp_row("Tube Pitch", "PT_in", "length", 0.2, 0.05, "%.3f")
    inp_row("Shell Fouling", "Rd_shell", "fouling", 0.0, 0.0001, "%.5f")
    inp_row("Tube Fouling", "Rd_tube", "fouling", 0.0, 0.0001, "%.5f")
    inp_row("Estimated U", "UD_est", "u", 0.1, 1.0, "%.2f")
    inp_row("DP Limit", "DP_limit", "dp", 0.1, 0.5, "%.2f")

st.markdown("---")
c3, c4 = st.columns(2)
with c3:
    st.markdown('<div class="input-label-text">Tube Passes</div>', unsafe_allow_html=True)
    st.selectbox("__", [1,2,4,6,8], key="v_n_p", label_visibility="collapsed")
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
    inp_row("Shell ID", "Ds_in", "length", 8.0, 0.25, "%.2f")
    inp_row("Baffle Space", "B_space_in", "length", 1.0, 0.5, "%.3f")
with c8:
    inp_row("Metal k", "k_metal", "k", 10.0, 1.0, "%.1f")

st.markdown("---")
if st.button("Reset to Defaults", use_container_width=True): reset()
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
ul, uu, udp = st.session_state["u_Do_in"], st.session_state["u_UD_est"], st.session_state["u_DP_limit"]

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
    ("Shell Diam", conv_lb(kr["Ds"],ul), ul, "Shell Size", "⭕"),
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
    ("Baffle Spacing", conv_lb(kr["B"],ul), ul, "Baffle", "📏"),
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

delaware_data = [
    ("h Ideal", conv_ub(de["hi"],uu), uu, "Ideal Coeff", "⚡"),
    ("h Corrected", conv_ub(de["ho"],uu), uu, "Final Coeff", "✨"),
    ("Re Delaware", de["Re"], "-", "Reynolds", "🌀"),
    ("Jc Factor", de["Jc"], "-", "Crossflow", "📐"),
    ("JL Factor", de["JL"], "-", "Leakage", "💧"),
    ("JB Factor", de["JB"], "-", "Bypass", "🔀"),
    ("J Total", de["Jt"], "-", "Combined", "🎯"),
    ("ΔP Shell", conv_dpb(de["DP"],udp), udp, "Shell Drop", "📉"),
]

for t, v, u_, n, icon in delaware_data:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{t} {'' if u_=='-' else f'({u_})'}</div>
        <div class="kpi-value">{fval(v, 3 if t in ['Jc Factor','JL Factor','JB Factor','J Total'] else (0 if u_=='-' else 2))}</div>
        <div class="kpi-note">{n}</div>
    </div>
    """, unsafe_allow_html=True)

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

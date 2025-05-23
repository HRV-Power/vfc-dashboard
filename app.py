
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Função para simular dados de intervalos RR (em milissegundos)
def simulate_rr_intervals(n=1000, mean_rr=800, sdnn=50):
    np.random.seed(42)
    rr_intervals = np.random.normal(mean_rr, sdnn, n)
    return rr_intervals

# Função para calcular métricas de VFC
def calculate_hrv_metrics(rr_intervals):
    rr_diff = np.diff(rr_intervals)
    rmssd = np.sqrt(np.mean(rr_diff**2))
    sdnn = np.std(rr_intervals)
    pnn50 = np.sum(np.abs(rr_diff) > 50) / len(rr_diff) * 100
    mean_hr = 60000 / np.mean(rr_intervals)
    stress_index = 60000 / (np.mean(rr_intervals) * sdnn) * 100
    return rmssd, sdnn, pnn50, mean_hr, stress_index

# Função para plotar gráficos
def plot_rr_intervals(rr_intervals):
    fig, ax = plt.subplots()
    ax.plot(rr_intervals, label='RR Intervals')
    ax.set_xlabel('Interval')
    ax.set_ylabel('RR Interval (ms)')
    ax.legend()
    st.pyplot(fig)

# Simular dados de intervalos RR
rr_intervals = simulate_rr_intervals()

# Calcular métricas de VFC
rmssd, sdnn, pnn50, mean_hr, stress_index = calculate_hrv_metrics(rr_intervals)

# Título do dashboard
st.title('Dashboard de Análise de VFC')

# Exibir métricas calculadas
st.header('Métricas de VFC')
st.write(f'RMSSD: {rmssd:.2f} ms')
st.write(f'SDNN: {sdnn:.2f} ms')
st.write(f'pNN50: {pnn50:.2f} %')
st.write(f'Frequência Cardíaca Média: {mean_hr:.2f} bpm')
st.write(f'Índice de Estresse de Baevsky: {stress_index:.2f}')

# Plotar gráfico de intervalos RR
st.header('Gráfico de Intervalos RR')
plot_rr_intervals(rr_intervals)

# Exibir tabela de dados simulados
st.header('Dados Simulados de Intervalos RR')
st.dataframe(pd.DataFrame(rr_intervals, columns=['RR Interval (ms)']))

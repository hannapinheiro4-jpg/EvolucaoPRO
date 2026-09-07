import streamlit as st
from datetime import datetime

# ==========================================
# 1. IDENTIDADE E CONFIGURAÇÃO DE PÁGINA
# ==========================================
st.set_page_config(page_title="EvoluçãoPRO | Sistema Clínico", layout="wide")

st.markdown("""
    <style>
    .stApp::before {
        content: "";
        display: block;
        height: 20px;
        background: linear-gradient(90deg, #2C3E50, #3498DB, #2980B9);
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 999999;
    }
    
    .block-container {
        padding-top: 2.5rem;
    }

    .stApp { 
        background-color: var(--background-color); 
        color: var(--text-color);
    }
    
    [data-testid="stSidebar"] { 
        background-color: #2C3E50 !important; 
        border-right: 1px solid #2980B9; 
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
    }
    
    h1, h2, h3, h4, h5, h6, p, span, label, div { 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
    }
    
    .stButton>button { 
        background-color: #2980B9; 
        color: #FFFFFF !important; 
        border-radius: 4px; 
        border: none; 
        font-weight: 600; 
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover { 
        background-color: #3498DB; 
        color: #FFFFFF !important; 
    }
    
    hr { border-top: 1px solid #2980B9; }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>select, .stTextArea>div>textarea, .stMultiSelect>div>div {
        border: 1px solid #3498DB;
        border-radius: 4px;
    }
    
    .footer-dev {
        background-color: var(--secondary-background-color);
        padding: 12px;
        border-radius: 6px;
        border-left: 4px solid #2980B9;
        margin-top: 20px;
        font-size: 14px;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. MOTOR GRAMATICAL SEGURO E FLEXÍVEL
# ==========================================
def motor_gramatical(sexo, modulo):
    if modulo in ["Obstetrícia - Gestante", "Obstetrícia - Puérpera"]:
        sexo = "Feminino"
    elif modulo == "Recém-Nascido":
        sexo = "Masculino"

    if sexo == "Feminino":
        return {
            "art": "A", "art_min": "a", "pac": "A paciente", "adm": "admitida", 
            "luc": "lúcida", "ori": "orientada", "eup": "eupneica", "aco": "acomodada", 
            "port": "portadora", "int_str": "internada", "med": "medicada", 
            "calmo": "calma", "colab": "colaborativa", "conf": "confusa", 
            "agit": "agitada", "sonol": "sonolenta", "resp": "responsiva", 
            "desor": "desorientada", "sed": "sedada", "comat": "comatosa", 
            "extub": "extubada", "normo": "normocorada", "hidr": "hidratada", 
            "queix": "queixosa", "ans": "ansiosa", "repos": "reposicionada", "nasc": "nascida",
            "trazido": "trazida pelo serviço de urgência", "encaminhado": "encaminhada do centro cirúrgico",
            "acomp_fam": "acompanhada por familiar", "acomp_leg": "acompanhada por acompanhante legal", "desacomp": "desacompanhada",
            "pos": "posicionada", "alocado": "alocada"
        }
    else:
        return {
            "art": "O", "art_min": "o", "pac": "O paciente", "adm": "admitido", 
            "luc": "lúcido", "ori": "orientado", "eup": "eupneico", "aco": "acomodado", 
            "port": "portador", "int_str": "internado", "med": "medicado", 
            "calmo": "calmo", "colab": "colaborativo", "conf": "confuso", 
            "agit": "agitado", "sonol": "sonolento", "resp": "responsivo", 
            "desor": "desorientado", "sed": "sedado", "comat": "comatoso", 
            "extub": "extubado", "normo": "normocorado", "hidr": "hidratado", 
            "queix": "queixoso", "ans": "ansioso", "repos": "reposicionado", "nasc": "nascido",
            "trazido": "trazido pelo serviço de urgência", "encaminhado": "encaminhado do centro cirúrgico",
            "acomp_fam": "acompanhado por familiar", "acomp_leg": "acompanhado por acompanhante legal", "desacomp": "desacompanhado",
            "pos": "posicionado", "alocado": "alocado"
        }

# ==========================================
# 3. MÓDULO NANDA, NIC E NOC
# ==========================================
def renderizar_modulo_nanda_nic_noc():
    st.subheader("Processo de Enfermagem: NANDA, NIC e NOC")
    st.markdown("Selecione os elementos padronizados do julgamento clínico e prescrição.")
    
    col_n1, col_n2, col_n3 = st.columns(3)
    
    with col_n1:
        nanda_diag = st.multiselect(
            "Diagnósticos de Enfermagem (NANDA-I)",
            [
                "00047 - Risco de integridade da pele prejudicada",
                "00031 - Limpeza ineficaz das vias aéreas",
                "00004 - Risco de infecção",
                "00132 - Dor aguda",
                "00201 - Risco de perfusão tissular ineficaz",
                "00032 - Padrão respiratório ineficaz",
                "00155 - Risco de queda",
                "00046 - Deterioração da integridade cutânea"
            ],
            placeholder="Selecione os diagnósticos...",
            key="nanda_sel"
        )
        
    with col_n2:
        nic_interv = st.multiselect(
            "Intervenções de Enfermagem (NIC)",
            [
                "3540 - Prevenção de úlceras por pressão",
                "3390 - Auxílio na ventilação",
                "6540 - Controle de infecções",
                "1400 - Manejo da dor",
                "6650 - Vigilância",
                "2210 - Administração de analgésicos",
                "0400 - Manejo da eliminação intestinal",
                "1800 - Cuidados com os olhos e ouvidos"
            ],
            placeholder="Selecione as intervenções...",
            key="nic_sel"
        )
        
    with col_n3:
        noc_result = st.multiselect(
            "Resultados Esperados (NOC)",
            [
                "1101 - Integridade tissular: pele e membranas mucosas",
                "0410 - Status respiratório: permeabilidade das vias aéreas",
                "1902 - Controle do risco",
                "1605 - Controle da dor",
                "0909 - Estado neurológico",
                "0501 - Eliminação intestinal",
                "0208 - Mobilidade"
            ],
            placeholder="Selecione os resultados...",
            key="noc_sel"
        )
        
    return {
        "nanda": nanda_diag,
        "nic": nic_interv,
        "noc": noc_result
    }

# ==========================================
# 4. GERENCIAMENTO DE ESTADO
# ==========================================
if 'historico_evolucoes' not in st.session_state:
    st.session_state['historico_evolucoes'] = []

if 'texto_anterior' not in st.session_state:
    st.session_state['texto_anterior'] = ""

if 'texto_final' not in st.session_state:
    st.session_state['texto_final'] = ""

# ==========================================
# 5. CONFIGURAÇÕES E MENU LATERAL
# ==========================================
try:
    st.sidebar.image("logo_branca.png.png", use_container_width=True)
except:
    pass

col_esq, col_centro, col_dir = st.columns([1, 2, 1])
with col_centro:
    try:
        st.image("logo_evolucaopro.png.png", use_container_width=True)
    except:
        pass

st.sidebar.title("EvoluçãoPRO")
st.sidebar.markdown("Sistema de apoio à documentação")
st.sidebar.markdown("---")

st.sidebar.subheader("Configurações do Profissional")
nome_prof = st.sidebar.text_input("Nome do profissional", placeholder="Digite o nome completo...", key="prof_nome")
coren_prof = st.sidebar.text_input("COREN", placeholder="Ex: 123456-SP", key="prof_coren")
cargo_prof = st.sidebar.text_input("Cargo", placeholder="Ex: Enfermeiro(a) | Técnico(a) de Enfermagem", key="prof_cargo")
setor_prof = st.sidebar.text_input("Unidade/Setor", placeholder="Ex: Clínica Médica | UTI | Pediatria", key="prof_setor")
st.sidebar.markdown("---")
st.sidebar.subheader("Módulo Assistencial")
modulo = st.sidebar.selectbox("Selecione o setor:", [
    "Clínica Médica",
    "Clínica Ortopédica",
    "Clínica Cirúrgica",
    "Obstetrícia - Gestante",
    "Obstetrícia - Puérpera",
    "Pediatria",
    "Recém-Nascido",
    "Intercorrência / UTI"
], key="mod_assistencial")

sexo_input = st.sidebar.radio("Sexo Biológico", ["Feminino", "Masculino"], key="sexo_bio")

if modulo in ["Obstetrícia - Gestante", "Obstetrícia - Puérpera"] and sexo_input == "Masculino":
    st.sidebar.warning("Atenção: A gramática foi ajustada para o feminino devido ao módulo.")
if modulo == "Recém-Nascido" and sexo_input == "Feminino":
    st.sidebar.warning("Atenção: A gramática seguirá o termo masculino 'O recém-nascido'.")

st.sidebar.markdown("---")
st.sidebar.subheader("Configurações Avançadas")
ativar_nanda = st.sidebar.toggle("Habilitar NANDA, NIC e NOC", value=False, key="toggle_nanda")

# PAINEL LATERAL PARA O LOTE DE PACIENTES SALVOS E SELEÇÃO NA ÍNTEGRA
st.sidebar.markdown("---")
st.sidebar.subheader(f"📦 Lote do Plantão ({len(st.session_state['historico_evolucoes'])})")
if st.session_state.get('historico_evolucoes'):
    opcoes_lote = [f"#{i+1} - {e['paciente']} (Leito: {e['leito']})" for i, e in enumerate(st.session_state['historico_evolucoes'])]
    escolha_lote = st.sidebar.selectbox("Selecionar evolução para acessar:", options=opcoes_lote, key="sel_lote_box")
    
    col_l1, col_l2 = st.sidebar.columns(2)
    with col_l1:
        if st.button("📂 Carregar"):
            idx = opcoes_lote.index(escolha_lote)
            st.session_state['texto_final'] = st.session_state['historico_evolucoes'][idx]['texto']
            st.rerun()
    with col_l2:
        if st.button("🗑️ Limpar Lote"):
            st.session_state['historico_evolucoes'] = []
            st.rerun()

g = motor_gramatical(sexo_input, modulo)
sexo_efetivo = "Feminino" if (modulo in ["Obstetrícia - Gestante", "Obstetrícia - Puérpera"] or (sexo_input == "Feminino" and modulo != "Recém-Nascido")) else "Masculino"

assinatura = f"\n\n__________________________________________\n{cargo_prof} {nome_prof}\nCOREN: {coren_prof} | {setor_prof}"

# ==========================================
# 6. INTERFACE PRINCIPAL
# ==========================================
st.title("Processo de Enfermagem")
st.markdown("Selecione os achados clínicos detalhados conforme a avaliação semiológica.")

st.subheader("1. Identificação e Contexto de Alocação")
col1, col2, col3 = st.columns(3)
tipo_evo = col1.selectbox("Tipo de Evolução", ["Evolução diária", "Admissão", "Pós-procedimento", "Transferência", "Alta hospitalar"], key="in_tipo")
horario = col2.text_input("Horário da Avaliação", datetime.now().strftime("%H:%M"), key="in_horario")
nome_paciente = col3.text_input("Nome/Iniciais do Paciente", "", placeholder="Digite o nome ou iniciais...", key="in_nome")

col4, col5, col6 = st.columns(3)
idade = col4.text_input("Idade", "", placeholder="Ex: 32 anos", key="in_idade")
leito = col5.text_input("Leito / Posto", "", placeholder="Ex: Leito 1.4, Posto 4", key="in_leito")
diag = col6.text_input("Diagnóstico / Motivo", "", placeholder="Ex: Pós-op de colecistectomia", key="in_diag")

col7, col8, col9 = st.columns(3)
forma_chegada = col7.selectbox("Modo de Entrada / Chegada", [
    "Deambulando", "Em cadeira de rodas", "Em maca", "Trazido pelo serviço de urgência", "Encaminhado do centro cirúrgico"
], key="in_chegada")
posicao_leito = col8.selectbox("Posicionamento no Leito", [
    "Em decúbito dorsal", "Em decúbito lateral direito", "Em decúbito lateral esquerdo", "Posição Fowler / Semi-Fowler", "Sentado no leito"
], key="in_pos")
acompanhante_status = col9.selectbox("Acompanhamento", [
    "Acompanhado por familiar", "Acompanhado por acompanhante legal", "Desacompanhado"
], key="in_acomp")

st.subheader("2. Sinais Vitais")
cv1, cv2, cv3, cv4, cv5, cv6 = st.columns(6)
pa = cv1.text_input("PA (mmHg)", "", placeholder="Ex: 120x80", key="sv_pa")
fc = cv2.text_input("FC (bpm)", "", placeholder="Ex: 78", key="sv_fc")
fr = cv3.text_input("FR (irpm)", "", placeholder="Ex: 18", key="sv_fr")
spo2 = cv4.text_input("SpO2 (%)", "", placeholder="Ex: 98", key="sv_spo2")
temp = cv5.text_input("Temp (°C)", "", placeholder="Ex: 36.5", key="sv_temp")
dor = cv6.text_input("Dor (0-10)", "", placeholder="Ex: 0", key="sv_dor")

ssvv_str = []
if pa: ssvv_str.append(f"PA de {pa} mmHg")
if fc: ssvv_str.append(f"FC de {fc} bpm")
if fr: ssvv_str.append(f"FR de {fr} irpm")
if spo2: ssvv_str.append(f"SpO₂ de {spo2}%")
if temp: ssvv_str.append(f"temperatura de {temp}°C")
ssvv_final = "Sinais vitais aferidos: " + ", ".join(ssvv_str) + "." if ssvv_str else ""
dor_final = f"Paciente refere dor classificada em grau {dor}." if dor and dor != "0" else "Paciente nega dor no momento."

# ==========================================
# 7. EXAMES FÍSICOS DETALHADOS (SEMIOLOGIA)
# ==========================================
st.subheader("3. Exame Físico e Avaliação Semiológica")

exame_fisico_partes = []

if modulo in ["Clínica Médica", "Clínica Cirúrgica", "Clínica Ortopédica"]:
    st.markdown("**1. Neurológico / Estado Mental**")
    n1, n2 = st.columns(2)
    estado_mental = n1.selectbox("Estado de Consciência", [
        "Não avaliado" if sexo_efetivo == "Masculino" else "Não avaliada",
        "Alerta, vígil e orientado" if sexo_efetivo == "Masculino" else "Alerta, vígil e orientada",
        "Sonolento / Letárgico" if sexo_efetivo == "Masculino" else "Sonolenta / Letárgica",
        "Obnubilado" if sexo_efetivo == "Masculino" else "Obnubilada",
        "Estuporoso / Comatoso" if sexo_efetivo == "Masculino" else "Estuporosa / Comatosa"
    ], key="ef_consciencia")
    
    neuro_mult = n2.multiselect("Achados Neurológicos e Motores", [
        "desorientação temporal", "desorientação espacial", "hipoprosexia", 
        "déficit de memória recente", "déficit de memória remota",
        "afasia de expressão", "afasia de compreensão", "disartria", 
        "pupilas isocóricas e fotorreagentes", "anisocoria", "midríase", "miose", 
        "paresia", "plegia", "marcha atáxica", "marcha ceifante", "marcha parkinsoniana", "marcha escarvante", "sem alterações motoras",
        "hipestesia", "parestesia", "hiporreflexia", "hiperreflexia", "arreflexia", 
        "sinal de Babinski presente", "rigidez de nuca", "sinais de irritação meníngea"
    ], placeholder="Selecione múltiplos achados...", key="ef_neuro")

    if not estado_mental.startswith("Não avaliad"):
        exame_fisico_partes.append(f"no aspecto neurológico, apresenta-se {estado_mental.lower()}")
    if neuro_mult:
        exame_fisico_partes.append(f"com evidência de {', '.join(neuro_mult)}")

    st.markdown("**2. Cabeça e Pescoço**")
    cabeca_opcoes = [
        "normocéfalo e simétrico" if sexo_efetivo == "Masculino" else "normocéfala e simétrica", 
        "mucosas coradas e hidratadas", "mucosas hipocoradas", "mucosas anictéricas", "mucosas ictéricas", 
        "mucosas acianóticas", "mucosas cianóticas", "traqueia centrada e móvel", "desvio da traqueia", 
        "tireoide impalpável", "bócio palpável", "nódulo de tireoide palpável", "turgor jugular patológica a 45°", 
        "sopro carotídeo", "linfonodomegalias cervicais", "linfonodomegalias supraclaviculares"
    ]
    cabeca_mult = st.multiselect("Cabeça, Pescoço e Vias Aéreas", cabeca_opcoes, placeholder="Selecione os achados...", key="ef_cabeca")
    if cabeca_mult:
        exame_fisico_partes.append(f"segmento cefálico e pescoço exibindo {', '.join(cabeca_mult)}")

    st.markdown("**3. Aparelho Respiratório**")
    resp_mult = st.multiselect("Padrão e Ausculta Respiratória", [
        "tórax simétrico e expansibilidade preservada bilateralmente", "expansibilidade torácica diminuída", 
        "murmúrio vesicular distribuído bilateralmente, sem ruídos adventícios", "murmúrio vesicular diminuído", "murmúrio vesicular abolido", 
        "presença de estertores crepitantes", "presença de roncos", "presença de sibilos", "estridor laríngeo", "atrito pleural", 
        "eupneico" if sexo_efetivo == "Masculino" else "eupneica", 
        "taquipneico" if sexo_efetivo == "Masculino" else "taquipneica", 
        "bradipneico" if sexo_efetivo == "Masculino" else "bradipneica", 
        "dispneico" if sexo_efetivo == "Masculino" else "dispneica", 
        "uso de musculatura acessória", "tiragem intercostal", "tórax em tonel", "pectus excavatum", "pectus carinatum"
    ], placeholder="Selecione os achados respiratórios...", key="ef_resp")
    if resp_mult:
        exame_fisico_partes.append(f"sistema respiratório caracterizado por {', '.join(resp_mult)}")

    st.markdown("**4. Aparelho Cardiovascular**")
    cardio_mult = st.multiselect("Ritmo, Bulhas e Perfusão Cardíaca", [
        "ritmo cardíaco regular em 2 tempos, bulhas normofonéticas", "ritmo cardíaco irregular", 
        "bulhas hipofonéticas", "bulhas hiperfonéticas", "terceira bulha (B3)", "quarta bulha (B4)", 
        "sopro sistólico", "sopro diastólico", "atrito pericárdico", 
        "ictus cordis palpável no 5º espaço intercostal", "ictus cordis desviado", "ictus cordis propulsivo"
    ], placeholder="Selecione os achados cardiovasculares...", key="ef_cardio")
    if cardio_mult:
        exame_fisico_partes.append(f"aparelho cardiovascular apresentando {', '.join(cardio_mult)}")

    st.markdown("**5. Abdome e Aparelho Digestivo (TGI)**")
    abd_mult = st.multiselect("Inspeção, Palpação e Semiologia Abdominal", [
        "abdome plano", "abdome globoso", "abdome distendido", "abdome escavado", "abdome simétrico, flácido e indolor à palpação", 
        "ruídos hidroaéreos presentes e normoativos", "ruídos hidroaéreos aumentados", "ruídos hidroaéreos diminuídos", "ruídos hidroaéreos abolidos", 
        "timpanismo fisiológico", "macicez maciça", "sinal do piparote positivo", 
        "dor à palpação superficial", "dor à palpação profunda", "defesa muscular", "rigidez abdominal", 
        "sinal de Blumberg positivo", "fígado e baço impalpáveis", "hepatomegalia palpável", "esplenomegalia palpável", 
        "massa abdominal palpável", "sinal de Murphy positivo", "sinal de Giordano positivo"
    ], placeholder="Selecione os achados abdominais...", key="ef_abd")
    if abd_mult:
        exame_fisico_partes.append(f"abdome com achados de {', '.join(abd_mult)}")

    st.markdown("**6. Extremidades e Perfusão Periférica**")
    ext_mult = st.multiselect("Pulsos, Edemas e Circulação", [
        "extremidades aquecidas e bem perfundidas", "extremidades frias", "cianose periférica", 
        "tempo de enchimento capilar < 2 segundos", "tempo de enchimento capilar > 2 segundos", 
        "pulsos periféricos simétricos, cheios e ritmados", "pulsos periféricos diminuídos", "pulsos periféricos abolidos", "pulsos periféricos assimétricos", 
        "edema de membros inferiores", "sinal de Godet positivo", "panturrilhas livres", "sem sinais de TVP", 
        "panturrilhas empastadas", "sinal de Homans positivo", "baqueteamento digital"
    ], placeholder="Selecione os achados de extremidades...", key="ef_ext")
    if ext_mult:
        exame_fisico_partes.append(f"extremidades e perfusão periférica com {', '.join(ext_mult)}")

    st.markdown("**7. Pele e Tegumento**")
    pele_mult = st.multiselect("Integridade e Lesões Cutâneas", [
        "pele íntegra, com cor, elasticidade e turgor preservados", "turgor cutâneo diminuído", "sinal do pregueamento positivo", 
        "palidez cutânea", "icterícia", "cianose", "petéquias", "púrpura", "equimoses", 
        "exantema", "enantema", "rash cutâneo", "eritema", "hiperemia local", 
        "pápulas", "pústulas", "vesículas", "bolhas", "nódulos", 
        "úlcera por pressão", "escoriações", "ferida operatória", "sinais flogísticos"
    ], placeholder="Selecione os achados cutâneos...", key="ef_pele")
    if pele_mult:
        exame_fisico_partes.append(f"tegumento cutâneo apresentando {', '.join(pele_mult)}")

    st.markdown("**8. Gênito-Urinário**")
    gu_mult = st.multiselect("Eliminações e Sistema Urinário", [
        "débito urinário presente e espontâneo", "anúria", "oligúria", "poliúria", 
        "disúria", "estrangúria", "hematúria macroscópica", "hematúria microscópica", 
        "urina colúrica", "piúria", "retenção urinária", "globo vesical palpável", 
        "incontinência urinária de esforço", "incontinência urinária de urgência", 
        "em uso de sonda vesical de demora (SVD)", "em uso de sonda vesical de alívio (SVA)", "em uso de cistostomia", "em uso de urostomia", 
        "secreção uretral patológica", "secreção vaginal patológica", "dor à palpação suprapúbica", "sinal de Giordano positivo"
    ], placeholder="Selecione os achados gênito-urinários...", key="ef_gu")
    if gu_mult:
        exame_fisico_partes.append(f"sistema gênito-urinário com {', '.join(gu_mult)}")

    if modulo == "Clínica Ortopédica":
        st.markdown("**Avaliação Ortopédica Específica**")
        co1, co2 = st.columns(2)
        membro = co1.multiselect("Membro Afetado", ["sem alterações neurovasculares", "extremidade aquecida", "perfusão preservada", "pulso distal presente", "mobilidade reduzida", "dor à movimentação", "edema local", "extremidade fria"], placeholder="Selecione o estado do membro...", key="ort_membro")
        imob = co2.selectbox("Imobilização", ["Sem imobilização", "Tala", "Gesso", "Órtese", "Fixador externo", "Tração"], key="ort_imob")
        if membro: exame_fisico_partes.append(f"membro afetado exibindo {', '.join(membro)}")
        if imob != "Sem imobilização": exame_fisico_partes.append(f"encontrando-se em uso de imobilização do tipo {imob}")

    if modulo == "Clínica Cirúrgica":
        st.markdown("**Avaliação Cirúrgica**")
        cc1, cc2 = st.columns(2)
        sit = cc1.selectbox("Situação Cirúrgica", ["Não aplicável", "Pré-operatório", "Pós-operatório imediato", "Pós-operatório tardio"], key="cir_sit")
        ferida = cc2.multiselect("Ferida Operatória", ["limpa e seca", "curativo íntegro", "com pequena quantidade de secreção", "presença de hiperemia", "presença de sangramento", "deiscência"], placeholder="Condições da ferida...", key="cir_ferida")
        dreno = cc1.selectbox("Drenos", ["Sem dreno", "Dreno de Portovac", "Dreno de Penrose", "Dreno de Kehr"], key="cir_dreno")
        dieta = cc2.selectbox("Dieta", ["Não especificada", "Jejum", "Líquida", "Pastosa", "Branda", "Geral", "Boa aceitação", "Baixa aceitação"], key="cir_dieta")
        if sit != "Não aplicável": exame_fisico_partes.append(f"encontrando-se em {sit.lower()}")
        if ferida: exame_fisico_partes.append(f"ferida operatória com aspecto de {', '.join(ferida)}")
        if dreno != "Sem dreno": exame_fisico_partes.append(f"portador de {dreno.lower()}")
        if dieta != "Não especificada": exame_fisico_partes.append(f"dieta prescrita do tipo {dieta.lower()}")

elif modulo == "Obstetrícia - Gestante":
    c1, c2 = st.columns(2)
    ig = c1.text_input("Idade Gestacional", "", placeholder="Ex: 32 semanas", key="obs_ig")
    gpa = c2.text_input("G/P/A", "", placeholder="Ex: G2P1A0", key="obs_gpa")
    geral = c1.multiselect("Estado Geral", ["consciente, orientada, eupneica", "ansiosa", "queixosa de dor"], placeholder="Estado geral...", key="obs_geral")
    dinamica = c1.multiselect("Dinâmica Uterina", ["dinâmica uterina ausente", "dinâmica uterina presente", "dinâmica uterina irregular"], placeholder="Dinâmica...", key="obs_dinamica")
    fetal = c2.multiselect("Avaliação Fetal", ["BCF audíveis e rítmicos", "movimentação fetal presente", "movimentação fetal reduzida"], placeholder="Avaliação fetal...", key="obs_fetal")
    obs_geral = c2.multiselect("Outros Achados", ["perda de líquido claro", "sangramento vaginal ausente", "sangramento vaginal presente", "sem edemas em MMII", "edema maleolar leve (+/4+)"], placeholder="Outros achados...", key="obs_outros")
    
    if ig: exame_fisico_partes.append(f"gestante com idade gestacional estimada em {ig} ({gpa})")
    if geral: exame_fisico_partes.append(f"apresentando condição geral {', '.join(geral)}")
    if dinamica: exame_fisico_partes.append(f"ao exame obstétrico, {', '.join(dinamica)}")
    if fetal: exame_fisico_partes.append(f"avaliação fetal demonstrando {', '.join(fetal)}")
    if obs_geral: exame_fisico_partes.append(f"observando-se ainda {', '.join(obs_geral)}")

elif modulo == "Obstetrícia - Puérpera":
    c1, c2 = st.columns(2)
    geral = c1.multiselect("Condição Geral", ["estável", "com queixa", "ansiosa", "sonolenta"], placeholder="Condição geral...", key="puer_geral")
    mamas = c1.multiselect("Mamas", ["mamas íntegras", "mamas túrgidas", "com ingurgitamento", "presença de fissura mamilar"], placeholder="Mamas...", key="puer_mamas")
    aleit = c2.multiselect("Aleitamento", ["amamentando com boa pega", "apresentando dificuldade de pega", "necessita auxílio", "não está amamentando"], placeholder="Aleitamento...", key="puer_aleit")
    utero = c2.multiselect("Útero e Lóquios", ["útero contraído (globo de Pinard presente)", "involução uterina compatível", "lóquios rubros em quantidade fisiológica", "lóquios serosos"], placeholder="Útero e lóquios...", key="puer_utero")
    perineo = c1.multiselect("Períneo / FO", ["períneo íntegro", "episiotomia/laceração suturada sem flogose", "ferida operatória de cesárea limpa e seca"], placeholder="Períneo ou FO...", key="puer_perineo")
    
    if geral: exame_fisico_partes.append(f"puérpera com condição geral {', '.join(geral)}")
    if mamas: exame_fisico_partes.append(f"mamas avaliadas com {', '.join(mamas)}")
    if aleit: exame_fisico_partes.append(f"quanto ao aleitamento, {', '.join(aleit)}")
    if utero: exame_fisico_partes.append(f"involução uterina e lóquios com {', '.join(utero)}")
    if perineo: exame_fisico_partes.append(f"região perineal/cirúrgica apresentando {', '.join(perineo)}")

elif modulo == "Pediatria":
    c1, c2 = st.columns(2)
    termo_ativo = "ativa e responsiva" if sexo_efetivo == "Feminino" else "ativo e responsivo"
    termo_reativo = "ativa e reativa" if sexo_efetivo == "Feminino" else "ativo e reativo"
    termo_sonolenta = "sonolenta, responsiva ao estímulo" if sexo_efetivo == "Feminino" else "sonolento, responsivo ao estímulo"
    termo_irritada = "irritada" if sexo_efetivo == "Feminino" else "irritado"
    termo_eupneica = "eupneica" if sexo_efetivo == "Feminino" else "eupneico"
    termo_taquipneica = "taquipneica" if sexo_efetivo == "Feminino" else "taquipneico"
    termo_dispneica = "dispneica" if sexo_efetivo == "Feminino" else "dispneico"

    geral = c1.multiselect("Estado Geral", [termo_ativo, termo_reativo, termo_sonolenta, termo_irritada, "choro presente"], placeholder="Estado geral...", key="ped_geral")
    resp = c1.multiselect("Respiratório", [termo_eupneica, termo_taquipneica, termo_dispneica, "com tiragem", "presença de sibilos"], placeholder="Respiratório...", key="ped_resp")
    abd = c2.multiselect("Abdome", ["plano e indolor", "globoso", "flácido"], placeholder="Abdome...", key="ped_abd")
    alim = c2.multiselect("Alimentação", ["em aleitamento materno", "dieta com boa aceitação", "baixa aceitação", "recusa alimentar"], placeholder="Alimentação...", key="ped_alim")
    
    if geral: exame_fisico_partes.append(f"paciente pediátrico encontrando-se {', '.join(geral)}")
    if resp: exame_fisico_partes.append(f"padrão respiratório {', '.join(resp)}")
    if abd: exame_fisico_partes.append(f"abdome {', '.join(abd)}")
    if alim: exame_fisico_partes.append(f"quanto à alimentação, {', '.join(alim)}")

elif modulo == "Recém-Nascido":
    c1, c2 = st.columns(2)
    geral = c1.multiselect("Estado Geral", ["ativo e reativo", "hiporreativo", "sonolento", "irritável"], placeholder="Estado geral...", key="rn_geral")
    cranio = c1.multiselect("Crânio", ["normocefálico", "fontanelas normotensas", "bossa serossanguínea"], placeholder="Crânio...", key="rn_cranio")
    pele = c2.multiselect("Tegumento", ["pele rosada", "icterícia presente", "acrocianose em extremidades"], placeholder="Pele...", key="rn_pele")
    resp = c2.multiselect("Respiratório", ["respiração regular sem esforço", "taquipneia", "tiragem intercostal"], placeholder="Respiratório...", key="rn_resp")
    coto = c1.multiselect("Coto Umbilical", ["coto íntegro", "em mumificação", "sem secreção", "com sinais flogísticos"], placeholder="Coto umbilical...", key="rn_coto")
    reflexos = c2.multiselect("Reflexos", ["reflexos de Moro, preensão e sucção presentes"], placeholder="Reflexos...", key="rn_reflexos")
    
    if geral: exame_fisico_partes.append(f"recém-nascido apresentando estado geral {', '.join(geral)}")
    if cranio: exame_fisico_partes.append(f"crânio {', '.join(cranio)}")
    if pele: exame_fisico_partes.append(f"tegumento com {', '.join(pele)}")
    if resp: exame_fisico_partes.append(f"padrão respiratório {', '.join(resp)}")
    if coto: exame_fisico_partes.append(f"coto umbilical {', '.join(coto)}")
    if reflexos: exame_fisico_partes.append(f"presença de {', '.join(reflexos)}")

elif modulo == "Intercorrência / UTI":
    intercorrencia_texto = st.text_area("Descreva a situação clínica / intercorrência:", height=100, placeholder="Descreva os eventos do plantão...", key="uti_texto")
    if intercorrencia_texto: exame_fisico_partes.append(f"intercorrência registrada: {intercorrencia_texto}")

# --- NANDA / NIC / NOC ---
dados_nanda = None
if ativar_nanda:
    st.markdown("---")
    dados_nanda = renderizar_modulo_nanda_nic_noc()

# --- DISPOSITIVOS E CUIDADOS ---
st.subheader("4. Dispositivos, Segurança e Cuidados")
d1, d2, d3 = st.columns(3)
dispositivos = d1.multiselect("Dispositivos Presentes", ["AVP", "CVC", "PICC", "SVD", "SNG", "SNE", "Dreno", "Ostomia", "Oxigenoterapia", "Ventilação mecânica"], placeholder="Dispositivos...", key="disp_sel")
riscos = d2.multiselect("Riscos Identificados", ["Risco de queda", "Risco de lesão por pressão (LPP)", "Risco de alergia", "Risco de broncoaspiração", "Risco de TEV", "Protocolo de Identificação conferido"], placeholder="Riscos...", key="riscos_sel")
cuidados = d3.multiselect("Cuidados Realizados", ["Administração de medicação conforme prescrição", "Higiene", "Mudança de decúbito", "Curativo", "Controle de sinais vitais", "Controle de glicemia", "Auxílio na alimentação", "Auxílio na mobilização", "Orientações prestadas"], placeholder="Cuidados...", key="cuidados_sel")

# ==========================================
# 8. MOTOR DE GERAÇÃO COM FLUIDEZ
# ==========================================
st.markdown("---")
if st.button("GERAR EVOLUÇÃO"):
    abertura_paciente = f"{g['pac']}"
    if idade: abertura_paciente += f" de {idade} de idade"
    
    detalhes_local = []
    if leito: detalhes_local.append(f"no(a) {leito}")
    local_str = f" alocado(a) {' '.join(detalhes_local)}" if detalhes_local else ""
    
    if forma_chegada == "Trazido pelo serviço de urgência":
        chegada_str = f" deu entrada {g['trazido']}"
    elif forma_chegada == "Encaminhado do centro cirúrgico":
        chegada_str = f" deu entrada {g['encaminhado']}"
    else:
        chegada_str = f" deu entrada {forma_chegada.lower()}"

    if acompanhante_status == "Acompanhado por familiar":
        acomp_str = f", {g['acomp_fam']}"
    elif acompanhante_status == "Acompanhado por acompanhante legal":
        acomp_str = f", {g['acomp_leg']}"
    else:
        acomp_str = f", {g['desacomp']}"

    pos_str = f", encontrando-se {g['pos']} {posicao_leito.lower()}"
    diagnostico_str = f" sob cuidados com diagnóstico de {diag}" if diag else ""
    
    paragrafo_1 = f"{horario} — {tipo_evo.upper()}\n{abertura_paciente}{local_str}{chegada_str}{acomp_str}{pos_str}{diagnostico_str}. Durante a avaliação inicial, {g['pac'].lower()} demonstra-se {g['luc'].lower()} e {g['ori'].lower()}, mantendo padrão {g['eup'].lower()} em ar ambiente."
    
    paragrafo_2 = ""
    if ssvv_final or dor_final:
        paragrafo_2 = f"No controle hemodinâmico, constatou-se {ssvv_final} {dor_final}"

    paragrafo_3 = ""
    if exame_fisico_partes:
        texto_exame_unificado = "; ".join(exame_fisico_partes)
        paragrafo_3 = f"Ao exame físico sistemático, observa-se: {texto_exame_unificado}."

    paragrafo_disp = f"Atualmente em uso de {', '.join(dispositivos)}." if dispositivos else ""
    paragrafo_riscos = f"Medidas de segurança adotadas contemplam: {', '.join(riscos)}." if riscos else ""
    paragrafo_cuidados = f"No decorrer do plantão, foram executados os seguintes cuidados: {', '.join(cuidados)}." if cuidados else ""
    
    bloco_intermediario = " ".join([p for p in [paragrafo_disp, paragrafo_riscos, paragrafo_cuidados] if p])

    bloco_processo = ""
    if ativar_nanda and dados_nanda:
        p_nanda = f"Diagnósticos de Enfermagem identificados: {', '.join(dados_nanda['nanda'])}." if dados_nanda['nanda'] else ""
        p_nic = f"Intervenções prescritas (NIC): {', '.join(dados_nanda['nic'])}." if dados_nanda['nic'] else ""
        p_noc = f"Resultados esperados (NOC): {', '.join(dados_nanda['noc'])}." if dados_nanda['noc'] else ""
        if p_nanda or p_nic or p_noc:
            bloco_processo = f"\n\n[Processo de Enfermagem]\n" + " ".join([p for p in [p_nanda, p_nic, p_noc] if p])

    encerramento = "\n\nMantidos os cuidados de enfermagem pertinentes ao plano assistencial, permanecendo sob monitorização contínua."
    
    corpo_evolucao = f"{paragrafo_1}\n\n{paragrafo_2}\n\n{paragrafo_3}\n\n{bloco_intermediario}{bloco_processo}{encerramento}{assinatura}"
    
    st.session_state['texto_anterior'] = st.session_state.get('texto_final', '')
    st.session_state['texto_final'] = corpo_evolucao

# ==========================================
# 9. ÁREA DE EDIÇÃO E BOTÕES DE CONTROLE
# ==========================================
if 'texto_final' in st.session_state and st.session_state['texto_final']:
    st.subheader("5. Evolução Gerada (Editável)")
    st.markdown("Faça os ajustes manuais necessários abaixo e utilize os botões de controle:")
    
    texto_editavel = st.text_area(
        "Edição da Evolução",
        value=st.session_state['texto_final'],
        height=320,
        label_visibility="collapsed",
        key="txt_edicao_final"
    )
    st.session_state['texto_final'] = texto_editavel
    
    col_b1, col_b2, col_b3, col_b4 = st.columns(4)
    
    with col_b1:
        if st.button("💾 Salvar na Lista do Plantão"):
            if nome_paciente or leito:
                st.session_state['historico_evolucoes'].append({
                    "paciente": nome_paciente if nome_paciente else "Não identificado",
                    "leito": leito if leito else "N/A",
                    "texto": st.session_state['texto_final']
                })
                st.toast("Evolução salva com sucesso no lote do plantão!", icon="✅")
            else:
                st.warning("Informe ao menos o nome ou leito do paciente para salvar.")
                
    with col_b2:
        if st.button("↩️ Voltar ao Anterior"):
            if st.session_state.get('texto_anterior'):
                st.session_state['texto_final'] = st.session_state['texto_anterior']
                st.rerun()
            else:
                st.info("Não há estado anterior registrado.")

    with col_b3:
        if st.button("➕ Novo Paciente"):
            lote_temp = st.session_state.get('historico_evolucoes', [])
            st.session_state.clear()
            st.session_state['historico_evolucoes'] = lote_temp
            st.rerun()

    with col_b4:
        if st.button("🧹 Limpar Campos"):
            lote_temp = st.session_state.get('historico_evolucoes', [])
            st.session_state.clear()
            st.session_state['historico_evolucoes'] = lote_temp
            st.rerun()

st.markdown("---")

st.markdown("""
<div class="footer-dev">
    <strong>Sistema de apoio à documentação de enfermagem.</strong> O registro deve refletir exclusivamente dados avaliados, observados e cuidados efetivamente realizados pelo profissional.<br>
    Desenvolvido por <strong>Enfª Hanna Pinheiro Vieira Sales</strong> | COREN-BA: <strong>982842</strong>
</div>
""", unsafe_allow_html=True)
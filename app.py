import streamlit as st
from datetime import datetime

# ==========================================
# 1. IDENTIDADE E CONFIGURAÇÃO DE PÁGINA
# ==========================================
st.set_page_config(page_title="EvoluçãoPRO | Sistema Clínico", layout="wide")

st.markdown("""
    <style>
    /* Faixa de destaque de ponta a ponta no topo absoluto da tela */
    .stApp::before {
        content: "";
        display: block;
        height: 20px;
        /* Gradiente invertido ou completo de ponta a ponta */
        background: linear-gradient(90deg, #2C3E50, #3498DB, #2980B9);
        width: 100vw;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 999999;
    }
    
    /* Ajuste para afastar o conteúdo do topo */
    .block-container {
        padding-top: 2.5rem;
    }

    /* Cores Globais baseadas no tema */
    .stApp { 
        background-color: var(--background-color); 
        color: var(--text-color);
    }
    
    /* Ajustes específicos para a Barra Lateral */
    [data-testid="stSidebar"] { 
        background-color: #2C3E50 !important; 
        border-right: 1px solid #2980B9; 
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
    }
    
    /* Tipografia */
    h1, h2, h3, h4, h5, h6, p, span, label, div { 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
    }
    
    /* Botões */
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
# 2. MOTOR GRAMATICAL SEGURO (GLOBAL E RIGOROSO)
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
            "trazido": "trazida", "acompanhado": "acompanhada", "alocado": "alocada"
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
            "trazido": "trazido", "acompanhado": "acompanhado", "alocado": "alocado"
        }

# ==========================================
# 3. MÓDULO SEPARADO: NANDA, NIC E NOC (ISOLADO)
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
            placeholder="Selecione os diagnósticos..."
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
            placeholder="Selecione as intervenções..."
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
            placeholder="Selecione os resultados..."
        )
        
    return {
        "nanda": nanda_diag,
        "nic": nic_interv,
        "noc": noc_result
    }

# ==========================================
# 4. CONFIGURAÇÕES E MENU LATERAL
# ==========================================
st.sidebar.image("logo_branca.png.png", use_container_width=True)
# logo centralizada
col_esq, col_centro, col_dir = st.columns([1, 2, 1])
with col_centro:
    st.image("logo_evolucaopro.png.png", use_container_width=True)
st.sidebar.title("EvoluçãoPRO")
st.sidebar.markdown("Sistema de apoio à documentação")
st.sidebar.markdown("---")

st.sidebar.subheader("Configurações do Profissional")
nome_prof = st.sidebar.text_input("Nome do profissional", placeholder="Digite o nome completo...")
coren_prof = st.sidebar.text_input("COREN", placeholder="Ex: 123456-SP")
cargo_prof = st.sidebar.text_input("Cargo", placeholder="Ex: Enfermeiro(a) | Técnico(a) de Enfermagem")
setor_prof = st.sidebar.text_input("Unidade/Setor", placeholder="Ex: Clínica Médica | UTI | Pediatria")
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
])

sexo_input = st.sidebar.radio("Sexo Biológico", ["Feminino", "Masculino"])

if modulo in ["Obstetrícia - Gestante", "Obstetrícia - Puérpera"] and sexo_input == "Masculino":
    st.sidebar.warning("Atenção: A gramática foi ajustada para o feminino devido ao módulo.")
if modulo == "Recém-Nascido" and sexo_input == "Feminino":
    st.sidebar.warning("Atenção: A gramática seguirá o termo masculino 'O recém-nascido'.")

st.sidebar.markdown("---")
st.sidebar.subheader("Configurações Avançadas")
ativar_nanda = st.sidebar.toggle("Habilitar NANDA, NIC e NOC", value=False)

g = motor_gramatical(sexo_input, modulo)
# Define o sexo ativo real considerando as travas de módulos
sexo_efetivo = "Feminino" if (modulo in ["Obstetrícia - Gestante", "Obstetrícia - Puérpera"] or (sexo_input == "Feminino" and modulo != "Recém-Nascido")) else "Masculino"

assinatura = f"\n\n__________________________________________\n{cargo_prof} {nome_prof}\nCOREN: {coren_prof} | {setor_prof}"

# ==========================================
# 5. INTERFACE PRINCIPAL
# ==========================================
st.title("Processo de Enfermagem")
st.markdown("Selecione os achados clínicos detalhados conforme a avaliação semiológica.")

# --- DADOS DO PACIENTE E CONTEXTO ESPACIAL ---
st.subheader("1. Identificação e Contexto de Alocação")
col1, col2, col3 = st.columns(3)
tipo_evo = col1.selectbox("Tipo de Evolução", ["Evolução diária", "Admissão", "Pós-procedimento", "Transferência", "Alta hospitalar"])
horario = col2.text_input("Horário da Avaliação", datetime.now().strftime("%H:%M"))
nome_paciente = col3.text_input("Nome/Iniciais do Paciente", "", placeholder="Digite o nome ou iniciais...")

col4, col5, col6 = st.columns(3)
idade = col4.text_input("Idade", "", placeholder="Ex: 32 anos")
leito = col5.text_input("Leito / Posto", "", placeholder="Ex: Leito 1.4, Posto 4")
diag = col6.text_input("Diagnóstico / Motivo", "", placeholder="Ex: Pós-op de colecistectomia")

col7, col8, col9 = st.columns(3)
forma_chegada = col7.selectbox("Modo de Entrada / Chegada", [
    "Deambulando", "Em cadeira de rodas", "Em maca", "Trazido pelo serviço de urgência", "Encaminhado do centro cirúrgico"
])
posicao_leito = col8.selectbox("Posicionamento no Leito", [
    "Em decúbito dorsal", "Em decúbito lateral direito", "Em decúbito lateral esquerdo", "Posição Fowler / Semi-Fowler", "Sentado no leito"
])
acompanhante_status = col9.selectbox("Acompanhamento", [
    "Acompanhado por familiar", "Acompanhado por acompanhante legal", "Desacompanhado"
])

# --- SINAIS VITAIS ---
st.subheader("2. Sinais Vitais")
cv1, cv2, cv3, cv4, cv5, cv6 = st.columns(6)
pa = cv1.text_input("PA (mmHg)", "", placeholder="Ex: 120x80")
fc = cv2.text_input("FC (bpm)", "", placeholder="Ex: 78")
fr = cv3.text_input("FR (irpm)", "", placeholder="Ex: 18")
spo2 = cv4.text_input("SpO2 (%)", "", placeholder="Ex: 98")
temp = cv5.text_input("Temp (°C)", "", placeholder="Ex: 36.5")
dor = cv6.text_input("Dor (0-10)", "", placeholder="Ex: 0")

ssvv_str = []
if pa: ssvv_str.append(f"PA {pa} mmHg")
if fc: ssvv_str.append(f"FC {fc} bpm")
if fr: ssvv_str.append(f"FR {fr} irpm")
if spo2: ssvv_str.append(f"SpO₂ {spo2}%")
if temp: ssvv_str.append(f"T {temp}°C")
ssvv_final = "SSVV: " + ", ".join(ssvv_str) + "." if ssvv_str else ""
dor_final = f"Refere dor grau {dor}." if dor else ""

# ==========================================
# 6. EXAMES FÍSICOS DETALHADOS (SEMIOLOGIA SEPARADA POR GÊNERO)
# ==========================================
st.subheader("3. Exame Físico e Avaliação Semiológica")

exame_fisico_partes = []

if modulo in ["Clínica Médica", "Clínica Cirúrgica", "Clínica Ortopédica"]:
    c1, c2 = st.columns(2)
    
    st.markdown("**1. Neurológico / Estado Mental**")
    n1, n2 = st.columns(2)
    estado_mental = n1.selectbox("Estado de Consciência (Única escolha)", [
        "Não avaliado",
        "Alerta, vígil e orientado",
        "Sonolento / Letárgico",
        "Obnubilado",
        "Estuporoso / Comatoso"
    ] if sexo_efetivo == "Masculino" else [
        "Não avaliada",
        "Alerta, vígil e orientada",
        "Sonolenta / Letárgica",
        "Obnubilada",
        "Estuporosa / Comatosa"
    ])
    
    neuro_opcoes_masc = [
        "desorientação temporal", "desorientação espacial", "hipoprosexia", 
        "déficit de memória recente", "déficit de memória remota",
        "afasia de expressão", "afasia de compreensão", "disartria", 
        "pupilas isocóricas e fotorreagentes", "anisocoria", "midríase", "miose", 
        "paresia", "plegia", "marcha atáxica", "marcha ceifante", "marcha parkinsoniana", "marcha escarvante", "sem alterações motoras"
        "hipestesia", "parestesia", "hiporreflexia", "hiperreflexia", "arreflexia", 
        "sinal de Babinski presente", "rigidez de nuca", "sinais de irritação meníngea"
    ]
    neuro_mult = n2.multiselect("Achados Neurológicos e Motores", neuro_opcoes_masc, placeholder="Selecione múltiplos achados...")

    if estado_mental not in ["Não avaliado", "Não avaliada"]:
        exame_fisico_partes.append(f"Neurológico: {estado_mental}.")
    if neuro_mult:
        exame_fisico_partes.append(f"Alterações neurológicas observadas: {', '.join(neuro_mult)}.")

    st.markdown("**2. Cabeça e Pescoço**")
    cabeca_opcoes = [
        "normocéfalo e simétrico" if sexo_efetivo == "Masculino" else "normocéfala e simétrica", 
        "mucosas coradas e hidratadas", 
        "mucosas hipocoradas", 
        "mucosas anictéricas", 
        "mucosas ictéricas", 
        "mucosas acianóticas", 
        "mucosas cianóticas", 
        "traqueia centrada e móvel", 
        "desvio da traqueia", 
        "tireoide impalpável", 
        "bócio palpável", 
        "nódulo de tireoide palpável", 
        "turgor jugular patológica a 45°", 
        "sopro carotídeo", 
        "linfonodomegalias cervicais", 
        "linfonodomegalias supraclaviculares"
    ]
    cabeca_mult = st.multiselect("Cabeça, Pescoço e Vias Aéreas", cabeca_opcoes, placeholder="Selecione os achados de cabeça e pescoço...")
    if cabeca_mult:
        exame_fisico_partes.append(f"Cabeça e pescoço: {', '.join(cabeca_mult)}.")

    st.markdown("**3. Aparelho Respiratório**")
    resp_mult = st.multiselect("Padrão e Ausculta Respiratória", [
        "tórax simétrico e expansibilidade preservada bilateralmente", "expansibilidade torácica diminuída", 
        "murmúrio vesicular distribuído bilateralmente, sem ruídos adventícios", "murmúrio vesicular diminuído", "murmúrio vesicular abolido", 
        "presença de estertores crepitantes", "presença de roncos", "presença de sibilos", "estridor laríngeo", "atrito pleural", 
        "eupneico" if sexo_efetivo == "Masculino" else "eupneica", 
        "taquipneico" if sexo_efetivo == "Masculino" else "taquipneica", 
        "bradipneico" if sexo_efetivo == "Masculino" else "bradipneica", 
        "dispneico" if sexo_efetivo == "Masculino" else "dispneica", 
        "uso de musculatura acessória", "tiragem intercostal", 
        "tórax em tonel", "pectus excavatum", "pectus carinatum"
    ], placeholder="Selecione os achados respiratórios...")
    if resp_mult:
        exame_fisico_partes.append(f"Aparelho respiratório: {', '.join(resp_mult)}.")

    st.markdown("**4. Aparelho Cardiovascular**")
    cardio_mult = st.multiselect("Ritmo, Bulhas e Perfusão Cardíaca", [
        "ritmo cardíaco regular em 2 tempos, bulhas normofonéticas", "ritmo cardíaco irregular", 
        "bulhas hipofonéticas", "bulhas hiperfonéticas", "terceira bulha (B3)", "quarta bulha (B4)", 
        "sopro sistólico", "sopro diastólico", "atrito pericárdico", 
        "ictus cordis palpável no 5º espaço intercostal", "ictus cordis desviado", "ictus cordis propulsivo"
    ], placeholder="Selecione os achados cardiovasculares...")
    if cardio_mult:
        exame_fisico_partes.append(f"Cardiovascular: {', '.join(cardio_mult)}.")

    st.markdown("**5. Abdome e Aparelho Digestivo (TGI)**")
    abd_mult = st.multiselect("Inspeção, Palpação e Semiologia Abdominal", [
        "abdome plano", "abdome globoso", "abdome distendido", "abdome escavado", "abdome simétrico, flácido e indolor à palpação", 
        "ruídos hidroaéreos presentes e normoativos", "ruídos hidroaéreos aumentados", "ruídos hidroaéreos diminuídos", "ruídos hidroaéreos abolidos", 
        "timpanismo fisiológico", "macicez maciça", "sinal do piparote positivo", 
        "dor à palpação superficial", "dor à palpação profunda", "defesa muscular", "rigidez abdominal", 
        "sinal de Blumberg positivo", "fígado e baço impalpáveis", "hepatomegalia palpável", "esplenomegalia palpável", 
        "massa abdominal palpável", "sinal de Murphy positivo", "sinal de Giordano positivo"
    ], placeholder="Selecione os achados abdominais...")
    if abd_mult:
        exame_fisico_partes.append(f"Abdome: {', '.join(abd_mult)}.")

    st.markdown("**6. Extremidades e Perfusão Periférica**")
    ext_mult = st.multiselect("Pulsos, Edemas e Circulação", [
        "extremidades aquecidas e bem perfundidas", "extremidades frias", "cianose periférica", 
        "tempo de enchimento capilar < 2 segundos", "tempo de enchimento capilar > 2 segundos", 
        "pulsos periféricos simétricos, cheios e ritmados", "pulsos periféricos diminuídos", "pulsos periféricos abolidos", "pulsos periféricos assimétricos", 
        "edema de membros inferiores", "sinal de Godet positivo", "panturrilhas livres", "sem sinais de TVP", 
        "panturrilhas empastadas", "sinal de Homans positivo", "baqueteamento digital"
    ], placeholder="Selecione os achados de extremidades...")
    if ext_mult:
        exame_fisico_partes.append(f"Extremidades e perfusão: {', '.join(ext_mult)}.")

    st.markdown("**7. Pele e Tegumento**")
    pele_mult = st.multiselect("Integridade e Lesões Cutâneas", [
        "pele íntegra, com cor, elasticidade e turgor preservados", "turgor cutâneo diminuído", "sinal do pregueamento positivo", 
        "palidez cutânea", "icterícia", "cianose", "petéquias", "púrpura", "equimoses", 
        "exantema", "enantema", "rash cutâneo", "eritema", "hiperemia local", 
        "pápulas", "pústulas", "vesículas", "bolhas", "nódulos", 
        "úlcera por pressão", "escoriações", "ferida operatória", 
        "sinais flogísticos (calor, rubor, tumor, dor, secreção)"
    ], placeholder="Selecione os achados cutâneos...")
    if pele_mult:
        exame_fisico_partes.append(f"Pele e tegumento: {', '.join(pele_mult)}.")

    st.markdown("**8. Gênito-Urinário**")
    gu_mult = st.multiselect("Eliminações e Sistema Urinário", [
        "débito urinário presente e espontâneo", "anúria", "oligúria", "poliúria", 
        "disúria", "estrangúria", "hematúria macroscópica", "hematúria microscópica", 
        "urina colúrica", "piúria", "sedimentos na urina", "retenção urinária", "globo vesical palpável", 
        "incontinência urinária de esforço", "incontinência urinária de urgência", "incontinência urinária paradoxal", 
        "em uso de sonda vesical de demora (SVD)", "em uso de sonda vesical de alívio (SVA)", "em uso de cistostomia", "em uso de urostomia", 
        "secreção uretral patológica", "secreção vaginal patológica", "lesões em genitália externa", 
        "prurido em região genital ou perineal", "dor em região genital ou perineal", "dor à palpação suprapúbica", "sinal de Giordano positivo"
    ], placeholder="Selecione os achados gênito-urinários...")
    if gu_mult:
        exame_fisico_partes.append(f"Gênito-urinário: {', '.join(gu_mult)}.")

    if modulo == "Clínica Ortopédica":
        st.markdown("**Avaliação Ortopédica Específica**")
        co1, co2 = st.columns(2)
        membro = co1.multiselect("Membro Afetado", ["sem alterações neurovasculares", "extremidade aquecida", "perfusão preservada", "pulso distal presente", "mobilidade reduzida", "dor à movimentação", "edema local", "extremidade fria"], placeholder="Selecione o estado do membro...")
        imob = co2.selectbox("Imobilização", ["Sem imobilização", "Tala", "Gesso", "Órtese", "Fixador externo", "Tração"])
        if membro: exame_fisico_partes.append(f"Membro afetado com: {', '.join(membro)}.")
        if imob != "Sem imobilização": exame_fisico_partes.append(f"Em uso de imobilização tipo {imob}.")

    if modulo == "Clínica Cirúrgica":
        st.markdown("**Avaliação Cirúrgica**")
        cc1, cc2 = st.columns(2)
        sit = cc1.selectbox("Situação Cirúrgica", ["Não aplicável", "Pré-operatório", "Pós-operatório imediato", "Pós-operatório tardio"])
        ferida = cc2.multiselect("Ferida Operatória", ["limpa e seca", "curativo íntegro", "com pequena quantidade de secreção", "presença de hiperemia", "presença de sangramento", "deiscência"], placeholder="Selecione as condições da ferida...")
        dreno = cc1.selectbox("Drenos", ["Sem dreno", "Dreno de Portovac", "Dreno de Penrose", "Dreno de Kehr"])
        dieta = cc2.selectbox("Dieta", ["Não especificada", "Jejum", "Líquida", "Pastosa", "Branda", "Geral", "Boa aceitação", "Baixa aceitação"])
        if sit != "Não aplicável": exame_fisico_partes.append(f"Paciente em {sit}.")
        if ferida: exame_fisico_partes.append(f"Ferida operatória: {', '.join(ferida)}.")
        if dreno != "Sem dreno": exame_fisico_partes.append(f"Dreno presente: {dreno}.")
        if dieta != "Não especificada": exame_fisico_partes.append(f"Dieta: {dieta}.")

elif modulo == "Obstetrícia - Gestante":
    c1, c2 = st.columns(2)
    ig = c1.text_input("Idade Gestacional", "", placeholder="Ex: 32 semanas")
    gpa = c2.text_input("G/P/A", "", placeholder="Ex: G2P1A0")
    geral = c1.multiselect("Estado Geral", ["consciente, orientada, eupneica", "ansiosa", "queixosa de dor"], placeholder="Selecione o estado geral...")
    dinamica = c1.multiselect("Dinâmica Uterina", ["dinâmica uterina ausente", "dinâmica uterina presente", "dinâmica uterina irregular"], placeholder="Selecione a dinâmica...")
    fetal = c2.multiselect("Avaliação Fetal", ["BCF audíveis e rítmicos", "movimentação fetal presente", "movimentação fetal reduzida"], placeholder="Selecione a avaliação fetal...")
    obs_geral = c2.multiselect("Outros Achados", ["perda de líquido claro", "sangramento vaginal ausente", "sangramento vaginal presente", "sem edemas em MMII", "edema maleolar leve (+/4+)"], placeholder="Selecione outros achados...")
    
    if ig: exame_fisico_partes.append(f"Gestante, IG: {ig}, {gpa}.")
    if geral: exame_fisico_partes.append(f"Estado geral: {', '.join(geral)}.")
    if dinamica: exame_fisico_partes.append(f"{', '.join(dinamica)}.")
    if fetal: exame_fisico_partes.append(f"{', '.join(fetal)}.")
    if obs_geral: exame_fisico_partes.append(f"{', '.join(obs_geral)}.")

elif modulo == "Obstetrícia - Puérpera":
    c1, c2 = st.columns(2)
    geral = c1.multiselect("Condição Geral", ["estável", "com queixa", "ansiosa", "sonolenta"], placeholder="Selecione a condição geral...")
    mamas = c1.multiselect("Mamas", ["mamas íntegras", "mamas túrgidas", "com ingurgitamento", "presença de fissura mamilar"], placeholder="Selecione as condições das mamas...")
    aleit = c2.multiselect("Aleitamento", ["amamentando com boa pega", "apresentando dificuldade de pega", "necessita auxílio", "não está amamentando"], placeholder="Selecione o aleitamento...")
    utero = c2.multiselect("Útero e Lóquios", ["útero contraído (globo de Pinard presente)", "involução uterina compatível", "lóquios rubros em quantidade fisiológica", "lóquios serosos"], placeholder="Selecione útero e lóquios...")
    perineo = c1.multiselect("Períneo / FO", ["períneo íntegro", "episiotomia/laceração suturada sem flogose", "ferida operatória de cesárea limpa e seca"], placeholder="Selecione o períneo ou FO...")
    
    if geral: exame_fisico_partes.append(f"Condição geral: {', '.join(geral)}.")
    if mamas: exame_fisico_partes.append(f"Mamas: {', '.join(mamas)}.")
    if aleit: exame_fisico_partes.append(f"{', '.join(aleit)}.")
    if utero: exame_fisico_partes.append(f"Útero/lóquios: {', '.join(utero)}.")
    if perineo: exame_fisico_partes.append(f"Região perineal/cirúrgica: {', '.join(perineo)}.")

elif modulo == "Pediatria":
    c1, c2 = st.columns(2)
    geral = c1.multiselect("Estado Geral", ["ativa e responsiva" if sexo_efetivo == "Feminino" else "ativo e responsivo", "ativa e reativa" if sexo_efetivo == "Feminino" else "ativo e reativo", "sonolenta, responsiva ao estímulo" if sexo_efetivo == "Feminino" else "sonolento, responsivo ao estímulo", "irritada" if sexo_efetivo == "Feminino" else "irritado", "choro presente"], placeholder="Selecione o estado geral...")
    resp = c1.multiselect("Respiratório", ["eupneica" if sexo_efetivo == "Feminino" else "eupneico", "taquipneica" if sexo_efetivo == "Feminino" else "taquipneico", "dispneica" if sexo_efetivo == "Feminino" else "dispneico", "com tiragem", "presença de sibilos"], placeholder="Selecione o respiratório...")
    abd = c2.multiselect("Abdome", ["plano e indolor", "globoso", "flácido"], placeholder="Selecione o abdome...")
    alim = c2.multiselect("Alimentação", ["em aleitamento materno", "dieta com boa aceitação", "baixa aceitação", "recusa alimentar"], placeholder="Selecione a alimentação...")
    
    if geral: exame_fisico_partes.append(f"Estado geral: {', '.join(geral)}.")
    if resp: exame_fisico_partes.append(f"Respiratório: {', '.join(resp)}.")
    if abd: exame_fisico_partes.append(f"Abdome: {', '.join(abd)}.")
    if alim: exame_fisico_partes.append(f"Alimentação: {', '.join(alim)}.")

elif modulo == "Recém-Nascido":
    c1, c2 = st.columns(2)
    geral = c1.multiselect("Estado Geral", ["ativo e reativo", "hiporreativo", "sonolento", "irritável"], placeholder="Selecione o estado geral...")
    cranio = c1.multiselect("Crânio", ["normocefálico", "fontanelas normotensas", "bossa serossanguínea"], placeholder="Selecione o crânio...")
    pele = c2.multiselect("Tegumento", ["pele rosada", "icterícia presente", "acrocianose em extremidades"], placeholder="Selecione a pele...")
    resp = c2.multiselect("Respiratório", ["respiração regular sem esforço", "taquipneia", "tiragem intercostal"], placeholder="Selecione o respiratório...")
    coto = c1.multiselect("Coto Umbilical", ["coto íntegro", "em mumificação", "sem secreção", "com sinais flogísticos"], placeholder="Selecione o coto...")
    reflexos = c2.multiselect("Reflexos", ["reflexos de Moro, preensão e sucção presentes"], placeholder="Selecione os reflexos...")
    
    if geral: exame_fisico_partes.append(f"Estado geral: {', '.join(geral)}.")
    if cranio: exame_fisico_partes.append(f"Crânio: {', '.join(cranio)}.")
    if pele: exame_fisico_partes.append(f"Pele: {', '.join(pele)}.")
    if resp: exame_fisico_partes.append(f"Respiratório: {', '.join(resp)}.")
    if coto: exame_fisico_partes.append(f"Coto umbilical: {', '.join(coto)}.")
    if reflexos: exame_fisico_partes.append(f"{', '.join(reflexos)}.")

elif modulo == "Intercorrência / UTI":
    intercorrencia_texto = st.text_area("Descreva a situação clínica / intercorrência:", height=100, placeholder="Descreva os eventos do plantão...")
    if intercorrencia_texto: exame_fisico_partes.append(intercorrencia_texto)

# --- CHAMADA DO MÓDULO NANDA / NIC / NOC (SE HABILITADO) ---
dados_nanda = None
if ativar_nanda:
    st.markdown("---")
    dados_nanda = renderizar_modulo_nanda_nic_noc()

# --- DISPOSITIVOS, RISCOS E CUIDADOS ---
st.subheader("4. Dispositivos, Segurança e Cuidados")
d1, d2, d3 = st.columns(3)
dispositivos = d1.multiselect("Dispositivos Presentes", ["AVP", "CVC", "PICC", "SVD", "SNG", "SNE", "Dreno", "Ostomia", "Oxigenoterapia", "Ventilação mecânica"], placeholder="Selecione os dispositivos...")
riscos = d2.multiselect("Riscos Identificados", ["Risco de queda", "Risco de lesão por pressão (LPP)", "Risco de alergia", "Risco de broncoaspiração", "Risco de TEV", "Protocolo de Identificação conferido"], placeholder="Selecione os riscos...")
cuidados = d3.multiselect("Cuidados Realizados", ["Administração de medicação conforme prescrição", "Higiene", "Mudança de decúbito", "Curativo", "Controle de sinais vitais", "Controle de glicemia", "Auxílio na alimentação", "Auxílio na mobilização", "Orientações prestadas"], placeholder="Selecione os cuidados...")

# ==========================================
# 7. MOTOR DE GERAÇÃO 
# ==========================================
st.markdown("---")
if st.button("GERAR EVOLUÇÃO"):
    
    abertura_paciente = f"{g['pac']}"
    if idade: abertura_paciente += f" de {idade}"
    
    detalhes_local = []
    if leito: detalhes_local.append(f"no(a) {leito}")
    local_str = f" alocado(a) {' '.join(detalhes_local)}" if detalhes_local else ""
    
    modo_chegada_ajustado = forma_chegada.lower()
    if forma_chegada == "Trazido pelo serviço de urgência" and sexo_efetivo == "Feminino":
        modo_chegada_ajustado = "trazida pelo serviço de urgência"
    elif forma_chegada == "Encaminhado do centro cirúrgico" and sexo_efetivo == "Feminino":
        modo_chegada_ajustado = "encaminhada do centro cirúrgico"

    chegada_str = f" deu entrada {modo_chegada_ajustado}"
    
    acomp_ajustado = acompanhante_status.lower()
    if acompanhante_status == "Acompanhado por familiar" and sexo_efetivo == "Feminino":
        acomp_ajustado = "acompanhada por familiar"
    elif acompanhante_status == "Acompanhado por acompanhante legal" and sexo_efetivo == "Feminino":
        acomp_ajustado = "acompanhada por acompanhante legal"
    elif acompanhante_status == "Desacompanhado" and sexo_efetivo == "Feminino":
        acomp_ajustado = "desacompanhada"

    Acomp_str = f", {acomp_ajustado}"
    pos_str = f", encontra-se {posicao_leito.lower()}"
    
    diagnostico_str = f" com diagnóstico de {diag}" if diag else ""
    
    cabecalho = f"{horario} — {tipo_evo.upper()}\n{abertura_paciente}{local_str},{chegada_str}{Acomp_str}{pos_str}{diagnostico_str}. "
    
    ssvv_block = ""
    if ssvv_final or dor_final:
        ssvv_block = f"{ssvv_final} {dor_final}\n"
        
    texto_exame = " ".join(exame_fisico_partes)
    bloco_exame = f"Ao exame físico: {texto_exame}\n" if texto_exame else ""
    
    bloco_disp = f"Em uso de: {', '.join(dispositivos)}.\n" if dispositivos else ""
    bloco_riscos = f"Segurança do paciente: {', '.join(riscos)}.\n" if riscos else ""
    bloco_cuidados = f"Cuidados no plantão: {', '.join(cuidados)}.\n" if cuidados else ""
    
    bloco_processo = ""
    if ativar_nanda and dados_nanda:
        p_nanda = f"Diagnósticos (NANDA-I): {', '.join(dados_nanda['nanda'])}.\n" if dados_nanda['nanda'] else ""
        p_nic = f"Intervenções (NIC): {', '.join(dados_nanda['nic'])}.\n" if dados_nanda['nic'] else ""
        p_noc = f"Resultados (NOC): {', '.join(dados_nanda['noc'])}.\n" if dados_nanda['noc'] else ""
        if p_nanda or p_nic or p_noc:
            bloco_processo = f"--- PROCESSO DE ENFERMAGEM ---\n{p_nanda}{p_nic}{p_noc}"

    encerramento = "Mantidos cuidados de enfermagem conforme plano assistencial e prescrição vigente."
    
    texto_gerado = cabecalho + "\n" + ssvv_block + bloco_exame + bloco_disp + bloco_riscos + bloco_cuidados + bloco_processo + encerramento + assinatura
    
    st.session_state['texto_final'] = texto_gerado

# ==========================================
# 8. ÁREA DE EDIÇÃO E CÓPIA
# ==========================================
if 'texto_final' in st.session_state:
    st.subheader("5. Evolução Gerada (Editável)")
    texto_editado = st.text_area("Revise, edite e copie (Ctrl+C / Cmd+C) para o prontuário:", value=st.session_state['texto_final'], height=300)
    
    c_btn1, c_btn2 = st.columns([1, 5])
    if c_btn1.button("Limpar Dados"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.markdown("---")

st.markdown("""
<div class="footer-dev">
    <strong>Sistema de apoio à documentação de enfermagem.</strong> O registro deve refletir exclusivamente dados avaliados, observados e cuidados efetivamente realizados pelo profissional.<br>
    Desenvolvido por <strong>Enfª Hanna Pinheiro Vieira Sales</strong> | COREN-BA: <strong>982842</strong>
</div>
""", unsafe_allow_html=True)
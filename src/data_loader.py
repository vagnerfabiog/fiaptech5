import pandas as pd
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'

def load_data():
    # === JOBS ===
    with open(DATA_DIR / 'raw' / 'Jobs.json', encoding='utf-8') as f:
        raw_jobs = json.load(f)

    jobs_list = []
    for job_id, job_data in raw_jobs.items():
        info = job_data.get('informacoes_basicas', {})
        perfil = job_data.get('perfil_vaga', {})
        jobs_list.append({
            'job_id': job_id,
            'titulo': info.get('titulo_vaga', ''),
            'tipo_contratacao': info.get('tipo_contratacao', ''),
            'descricao_vaga': perfil.get('principais_atividades', ''),
            'requisitos': perfil.get('competencia_tecnicas_e_comportamentais', ''),
            'local_trabalho': perfil.get('local_trabalho', ''),
            'nivel_academico_vaga': perfil.get('nivel_academico', ''),
            'nivel_ingles_vaga': perfil.get('nivel_ingles', ''),
            'nivel_espanhol_vaga': perfil.get('nivel_espanhol', ''),
        })
    jobs = pd.DataFrame(jobs_list)

    # === PROSPECTS ===
    with open(DATA_DIR / 'raw' / 'Prospects.json', encoding='utf-8') as f:
        raw_prospects = json.load(f)

    prospects_list = []
    for job_id, data in raw_prospects.items():
        for p in data.get('prospects', []):
            p['job_id'] = job_id
            prospects_list.append(p)

    prospects = pd.DataFrame(prospects_list)
    prospects.rename(columns={
        'codigo': 'applicant_id',
        'situacao_candidado': 'status'
    }, inplace=True)

    # === APPLICANTS ===
    with open(DATA_DIR / 'raw' / 'Applicants.json', encoding='utf-8') as f:
        raw_applicants = json.load(f)

    applicants_list = []
    for applicant_id, data in raw_applicants.items():
        formacao = data.get('formacao_e_idiomas', {})
        resumo = data.get('cv_pt', '')
        applicants_list.append({
            'applicant_id': applicant_id,
            'nome': data.get('infos_basicas', {}).get('nome', ''),
            'nivel_academico': formacao.get('nivel_academico', ''),
            'nivel_ingles': formacao.get('nivel_ingles', ''),
            'nivel_espanhol': formacao.get('nivel_espanhol', ''),
            'resumo_candidato': resumo
        })

    applicants = pd.DataFrame(applicants_list)

    # === Forçar tipos para merge ===
    prospects['job_id'] = prospects['job_id'].astype(str)
    jobs['job_id'] = jobs['job_id'].astype(str)
    prospects['applicant_id'] = prospects['applicant_id'].astype(str)
    applicants['applicant_id'] = applicants['applicant_id'].astype(str)

    # === Criar target ===
    prospects['status'] = prospects['status'].fillna('')
    prospects['target'] = prospects['status'].str.lower().str.contains('contratado').astype(int)

    # === Merge final ===
    df = prospects.merge(jobs, on='job_id', how='left') \
                  .merge(applicants, on='applicant_id', how='left')

    # === Preencher campos textuais que podem estar ausentes ===
    df.fillna({
        'descricao_vaga': '',
        'requisitos': '',
        'resumo_candidato': '',
        'titulo': ''
    }, inplace=True)

    return df


if __name__ == '__main__':
    df = load_data()
    print(f"DataFrame final: {df.shape} linhas")
    print(df[['job_id', 'applicant_id', 'titulo', 'status', 'target']].head())

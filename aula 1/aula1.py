def mediaTurma(turma):
    mediaTurma = 0
    for aluno in turma:
        mediaTurma += aluno['media']
    return mediaTurma / len(turma)

def mediaAluno(turma, mediaTurma):
    alunoMaior = []
    alunoMenor = []
    for aluno in turma:
        if aluno['media'] >= mediaTurma:
            alunoMaior.append(aluno)
        else:
            alunoMenor.append(aluno)
    return alunoMaior, alunoMenor

def nota():
    notaAluno = input('Digite a nota do aluno: ')
    try:
        return float(notaAluno)
    except ValueError:
        print('Valor inválido')
        return nota()

turma = []
for _ in range(3):

    nome = input('Nome: ')
    g1 = nota()
    g2 = nota()
    media = (g1 + g2) / 2
    turma.append({
        'nome': nome,
        'g1': g1,
        'g2': g2,
        'media': media
    })
    print(f'Nome do aluno: {nome}\nNota 1: {g1}\nNota 2: {g2}\nMédia: {media}')

mediaTurma = mediaTurma(turma)
print(f'A media da turma é: {mediaTurma}')

(alunoMaior, alunoMenor) = mediaAluno(turma, mediaTurma)
print(f'A porcentagem de alunos com a nota maior que a média é: {((len(alunoMaior)/len(turma))*100):.2f}')
print(f'A porcentagem de alunos com a nota menor que a média é: {((len(alunoMenor)/len(turma))*100):.2f}')
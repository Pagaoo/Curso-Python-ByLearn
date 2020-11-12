def main():
    alunos = ['Amanda', 'Gabriel', 'Roger', 'Anderson']
    notas = [[10,10], [8,9], [3,5], [7,4]]

    if(len(alunos) == len(notas)):
        for i in range(len(alunos)):
            soma = 0
            for nota in notas[i]:
                soma += nota
            media = soma / len(notas[i])
            print(f'O aluno: {alunos[i]} tem a média {media}')
            if(media >= 7):
                print(f'- Foi aprovado')
            else:
                print(f'- foi reprovado')
    else:
        print('Possivel falta de nota!')
main()
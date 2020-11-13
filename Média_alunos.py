def main():
    alunos = ['Amanda', 'Gabriel', 'Roger', 'Anderson']
    notas = [[10,10], [8,9], [3,5], [7,4]]

    if(len(alunos) == len(notas)):
        for i in range(len(alunos)):
            soma = 0
            for nota in notas[i]:
                soma += nota
            media = soma / len(notas[i])
            if(media >= 7):
                print('Aluno aprovado: ')
            else:
                print('Aluno reprovado: ')
            print(f'{alunos[i]} tem a média {media}')
            
    else:
        print('Possivel falta de nota!')
main()
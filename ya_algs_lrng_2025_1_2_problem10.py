import re


def main():
    n = int(input())

    fgn_lst = {}
    for i in range(n):
        command = input()
        if len(command.split()) >= 4 and command.split()[3] == 'new':
            fgn_lst[command.split()[1]] = list(map(int, re.findall(r'\d+', command)))

        elif len(command.split('.')) >= 2 and len(command.split('.')[1]) >= 7 and command.split('.')[1][:7] == 'subList':
            frm, t = map(int, re.findall(r'\d+', command))

            if type(fgn_lst[command.split('.')[0].split()[3]][0]) == str:
                fgn_lst[command.split()[1]] = [fgn_lst[command.split('.')[0].split()[3]][0], fgn_lst[command.split('.')[0].split()[3]][1] + frm - 1, fgn_lst[command.split('.')[0].split()[3]][1] + t - frm + 1]
            else:
                fgn_lst[command.split()[1]] = [command.split('.')[0].split()[3], frm]

        elif command.split('.')[1][:3] == 'set':
            frm, t = map(int, re.findall(r'\d+', command))
            if type(fgn_lst[command.split('.')[0]][0]) == str:
                fgn_lst[fgn_lst[command.split('.')[0]][0]] [fgn_lst[command.split('.')[0]][1] + frm - 1 - 1] = t
            else:
                fgn_lst[command.split('.')[0]][frm-1] = t

        elif command.split('.')[1][:3] == 'add':
            ind = re.findall(r'\d+', command)
            fgn_lst[command.split('.')[0]].append(int(ind[0]))

        elif command.split('.')[1][:3] == 'get':
            ind = re.findall(r'\d+', command)
            if type(fgn_lst[command.split('.')[0]][0]) == str:
                print(fgn_lst[fgn_lst[command.split('.')[0]][0]] [fgn_lst[command.split('.')[0]][1] + int(ind[0]) - 1 - 1])
            else:
                print(fgn_lst[command.split('.')[0]][int(ind[0])-1])

    return

if __name__ == '__main__':
    main()

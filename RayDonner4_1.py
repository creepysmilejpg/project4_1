def main():
    import re
    import csv

    file = open('files/input.txt', 'r')
    csvfile = open('files/output.csv', 'w', newline='')
    fileout = open('output.txt', 'w')

    file.seek(0)
    csvfile.seek(0)
    fileout.seek(0)

    output = {}
    output2 = {}

    emailcount = 0
    dspamcount = 0
    dspamcount2 = 0

    for line in file:
        line = line.rstrip()
        if re.findall('^From: (\S*@\S*)', line):
            line.split()
            line.strip()
            line = line.replace('From: ', '')
            output[line] = output.get(line, 0) + 1

        if re.findall('^X-DSPAM-Confidence:', line):
            fileout.write(line + '\n')
            output2[line] = output2.get(line, 0) + 1

            l = len(line)
            middle = (l // 2)+7
            first, second = line[:middle], line[middle:]
            dspamcount += float(second)

    fileout.write('--------------------------------------------------\n')
    fileout.write(f'Total dspam confidence {dspamcount:.2f}\n')

    for key, value in output2.items():
        dspamcount2 += value

    fileout.write(f'Average dspam confidence {(dspamcount / dspamcount2):.2f}')

    csvfile.write('Email           Count\n')

    for key, value in output.items():
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([f'{key}'] + ["{:>20}".format(value)])
        #csvfile.write(f'{key}' + "{:>20}".format(value) + '\n')
        emailcount += value

    csvfile.write(f'TOTAL' + "{:>20}".format(emailcount))

    file.close()
    csvfile.close()
    fileout.close()


if __name__ == "__main__":
    main()

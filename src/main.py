import sys, getopt

from ris_conv import RISConv


class Main:

    @staticmethod
    def run(argv) -> None:
        inputfile = outputfile = None

        try:
            opts, _ = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
        except getopt.GetoptError:
            print('main.py -i <inputfile> -o <outputfile>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print('main.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ('-i', '--ifile'):
                inputfile = arg
            elif opt in ('-o', '--ofile'):
                outputfile = arg

        if all((inputfile, outputfile)):
            print(f'Input file is {inputfile}')
            reader = RISConv(inputfile)
            reader.ris_to_csv(outputfile)
            print(f'Output file is {outputfile}')
        else:
            print('main.py -i <inputfile> -o <outputfile>')


Main.run(sys.argv[1:])

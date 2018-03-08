import yaml

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile_path',help = "path of the input file")
    parser.add_argument('outfile_path',help = "path of the output file")
    parser.add_argument('yaml_path',help = "path of the yaml file")

    args = parser.parse_args()
    with (open(args.yaml_path,'r') as f:
        data_metafile = yaml.load(f)

def read_data(inputfile,yaml_data):
    try:
        with open(inputfile,'r') as f:
            data =
    except IOError:
            raise SystemExit('')

import argparse
import zipfile

def unzip_data_file(path_to_zip_data, dir_to_extract):
    with zipfile.ZipFile(path_to_zip_data, 'r') as zip_ref:
        zip_ref.extractall(dir_to_extract)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='unzip_data.py')
    parser.add_argument('--input_path', type=str, default='data/coco128.zip', help='The path to the zipped data file')
    parser.add_argument('--output_path', type=str, default='data/', help='The path to output the files')
    args = parser.parse_args()
    unzip_data_file(args.input_path,args.output_path)
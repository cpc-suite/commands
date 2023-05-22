import json
import subprocess
import click
import shutil
import os
import sys

@click.command()
@click.option('-f', '--filename', required=True, help='Input file name')
@click.option('-m', '--mode', type=click.Choice(['0', '1', '2']), default='0', help='Image Mode')
@click.option('-w', '--width',required=True, help='width file')
@click.option('-h', '--height',required=True, help='height file')
@click.option('-o', '--out', help='Folder where the artifacts are generated')

def main(filename, mode, width, height, out):

    TMP_FOLDER = out + "/f-"+os.path.basename(filename)
    ASM_FILE = os.path.basename(os.path.splitext(filename)[0])
    TMP_ASM = TMP_FOLDER + "/" + ASM_FILE+".TXT"
    ASM_FOLDER = "asm/"
    cmd = ['martine', '-in', filename, '-width', str(width),'-height',str(height),'-mode', str(mode), '-out', TMP_FOLDER, '-json','-noheader']
    
    try:
        if out:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            # print(output.decode())
            print ("[INFO] Convert Sprite: " + filename + " --> asm/" + os.path.basename(ASM_FILE.upper() + '.ASM'))
            if not os.path.exists(out):
                os.makedirs(out)
        else:
            subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f'Error executing command: {e.output.decode()}')
        sys.exit(1)

    if not os.path.exists(ASM_FOLDER):
        os.makedirs(ASM_FOLDER)

    only=0
    copy = False
    with open(TMP_ASM, 'r') as input_file:
        with open(ASM_FOLDER + ASM_FILE+".ASM", 'w') as output_file:
            if only == 0:
                output_file.write(";------ BEGIN SPRITE --------\n")
                output_file.write(ASM_FILE)
                output_file.write("\ndb " + width + " ; ancho")
                output_file.write("\ndb " + height + " ; alto\n")
                only = 1
            for line in input_file:
                if line.startswith('; width'):
                    copy = True
                    continue
                elif line.startswith('; Palette'):
                    copy = False
                    continue
                if copy:
                    output_file.write(line)
            output_file.write("\n;------ END SPRITE --------")
    # Delete temporary folder
    shutil.rmtree(TMP_FOLDER)

if __name__ == '__main__':
    main()

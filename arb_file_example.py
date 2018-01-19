#!/usr/bin/env python 
import argparse
import os,sys

def parse_commandline():
	parser = argparse.ArgumentParser(description='Example file for parsing arbitrary list of files')
        parser.add_argument('--files',nargs='+',help='list of files')
        return parser.parse_args()

def main():
        opts = parse_commandline()

        for x in opts.files:
                with open("{0}.out.log".format(x),"w") as g:
                        try:
                                f = open("testFiles/{0}".format(x),"r")
                                g.write("The File {0} has '{1}' in it\n".format(x,f.readlines()))
                        except Exception as e:
                                g.write("The file {0} had problems\n".format(x))
                        


if __name__ == "__main__":
        main()
        

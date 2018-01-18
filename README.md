# arbitrary_file_list_boutiqes_example
An example of using boutiques with an arbitrary list of files

This example consists of a simple python script that takes an arbirary numbr of arguments for input files and checks the testFiles directory for whether they exist or not, and prints their contents to an output file.

It is enabled with a file runarb.json, which is Boutiques descriptor (https://github.com/boutiques/boutiques) and also has been pushed to dockerhub for convienence.

To run, you must have Boutiques installed in your python environment.  You can edit the input.json to have appropriate command line flags, and then launch with:

bosh exec launch runarb.json input.json

The result will be an output file that has a print out of whether the files exist or not.



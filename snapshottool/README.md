# EC2 Snapshot Creation Tool

This document describes the requirements and usage of the script.


## Usage Guide
<pre>
python3 main.py --help
python3 main.py --importfile ~/file.txt
python3 main.py -i ~/file.txt
</pre>

### Requirements

* AWS CLI 2
* boto3
* Click

#### Installation

1. pip3 install git+https://github.com/DeivPod/aws.git (doesn't work)

#### Input

* <filename>.txt file to which path is define with --importfile or -i parameter
* <filename>.txt file should contain EC2 instance tag names and values separated by spaces or new lines.
* Script only creates snapshots of instances with tags provided in the file.

Example of input file
<pre>
backup yes
Name testmachine
</pre>


#### Output

snapshots EC2 snapshots created

Console output:
<pre>
Path provided: /HOME/USER/SCRIPT/FILE.TXT
Tags list read from the input file: ['backup', 'yes', 'Name', 'testmachine']
Name: backup, Value:yes 
Snapshots are being created, check EC2 console
End of script
</pre>


#### Verified on the following platforms

|Operating System|Verified|
|-----------------|:------------:|
|Ubuntu 20.04 LTS|Yes|


#### Version History
|Date|Version|Description|
|:-----------------|:------------|:------------|
2021 03 25 |1.0.0 |Initial version<br /> Created by: Deividas|

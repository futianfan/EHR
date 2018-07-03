#!/bin/bash

cd datasets/snowdata/
## input file is training_data_1.txt
sed '1d' training_data_1.txt | awk '{print $1}' | sed 's/True/1/;s/False/0/' > snow.Y
sed '1d' training_data_1.txt | awk -F "\t" '{print $3}' > tmp
n=`python findmax.py`
((n=n+1))
python generate_X_data.py $n tmp snow.X
cd -

python main.py




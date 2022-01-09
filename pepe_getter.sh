#!/bin/bash
input="pepe_links.txt"
output_dir="pepe_images/"

while IFS= read -r line
do
  wget -P "$output_dir/" "$line"
done < "$input"

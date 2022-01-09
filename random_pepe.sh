#!/bin/bash

pepe_dir="pepe_images/"

ls "$pepe_dir" |sort -R |tail -1 |while read file; do
    chafa "$pepe_dir$file"
done

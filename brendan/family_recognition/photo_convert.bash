for file in *.HEIC;
do heif-convert
do heif-convert $file ${file%.HEIC}.jpg; done; rm *.HEIC 

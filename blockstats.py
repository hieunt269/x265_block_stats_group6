# BAI TAP LON DA PHUONG TIEN NANG CAO
# Thong ke so luong frames co ma hoa kieu intra voi cac block 32x32, 16x16, 8x8, 4x4
# NHOM 6 - KSTN DTVT K59

import csv
import numpy as np

#types of frames
frame_I = 0
frame_P = 0
frame_B = 0

#numbers of encoded intra frames has block 32x32
dc32 = 0 
planar32 = 0
ang32 = 0

#numbers of encoded intra frames has block 16x16
dc16 = 0 
planar16 = 0
ang16 = 0

#numbers of encoded intra frames has block 8x8
dc8 = 0 
planar8 = 0
ang8 = 0

#numbers of encoded intra frames has block 4x4
intra4 = 0

#read data from a csv file created when encoding a video *mp4 with x265
with open('blockstat_2.csv') as f:
	csv_reader = csv.reader(f, delimiter = ',')
	for row in csv_reader:
		frame_I += ((row[1].strip() == 'I-SLICE') | (row[1].strip() == 'i-SLICE'))
		frame_P += (row[1].strip() == 'P-SLICE')
		frame_B += ((row[1].strip() == 'B-SLICE') | (row[1].strip() == 'b-SLICE'))
		dc32 += (row[13].strip() != '0.00%')
		planar32 += (row[14].strip() != '0.00%')
		ang32 += (row[15].strip() != '0.00%')
		dc16 += (row[16].strip() != '0.00%')
		planar16 += (row[17].strip() != '0.00%')
		ang16 += (row[18].strip() != '0.00%')
		dc8 += (row[19].strip() != '0.00%')
		planar8 += (row[20].strip() != '0.00%')
		ang8 += (row[21].strip() != '0.00%')
		intra4 += (row[22].strip() != '0.00%')

print('==================================================')

print('Numbers of frame I: ', frame_I)
print('Numbers of frame P: ', frame_P)
print('Numbers of frame B: ', frame_B)

print('Intra 32x32 DC: %d, Planar: %d, Ang: %d' %((dc32 - 1), (planar32 - 1), (ang32 - 1)))
print('Intra 16x16 DC: %d, Planar: %d, Ang: %d' %((dc16 - 1), (planar16 - 1), (ang16 - 1)))
print('Intra 8x8 DC: %d, Planar: %d, Ang: %d' %((dc8 - 1), (planar8 - 1), (ang8 - 1)))
print('Intra 4x4: %d' %(intra4))

print('==================================================')
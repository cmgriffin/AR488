EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Arduino USB to GPIB Interface"
Date "2021-05-29"
Rev "1.0"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Label 7000 3550 0    50   ~ 0
DIO1
Text Label 7000 3650 0    50   ~ 0
DIO2
Text Label 7000 3750 0    50   ~ 0
DIO3
Text Label 7000 3850 0    50   ~ 0
DIO4
Text Label 7900 3550 2    50   ~ 0
DIO5
Text Label 7900 3650 2    50   ~ 0
DIO6
Text Label 7900 3750 2    50   ~ 0
DIO7
Text Label 7900 3850 2    50   ~ 0
DIO8
Text Label 7000 4450 0    50   ~ 0
SRQ
Text Label 7900 3950 2    50   ~ 0
REN
Text Label 7000 4550 0    50   ~ 0
ATN
Text Label 7000 4350 0    50   ~ 0
IFC
Text Label 7000 4250 0    50   ~ 0
NDAC
Text Label 7000 4150 0    50   ~ 0
NRFD
Text Label 7000 3950 0    50   ~ 0
EOI
$Comp
L Connector_Generic:Conn_02x12_Top_Bottom J1
U 1 1 60B1AC9D
P 7400 4050
F 0 "J1" H 7450 4767 50  0000 C CNN
F 1 "Conn_02x12_Top_Bottom" H 7450 4676 50  0000 C CNN
F 2 "central_lib:PinHeader_2x12_P2.54mm_Vertical_Top_Bottom" H 7400 4050 50  0001 C CNN
F 3 "~" H 7400 4050 50  0001 C CNN
	1    7400 4050
	1    0    0    -1  
$EndComp
Text Label 7000 4050 0    50   ~ 0
DAV
Wire Wire Line
	7200 3550 7000 3550
Wire Wire Line
	7200 3650 7000 3650
Wire Wire Line
	7200 3750 7000 3750
Wire Wire Line
	7200 3850 7000 3850
Wire Wire Line
	7200 3950 7000 3950
Wire Wire Line
	7200 4050 7000 4050
Wire Wire Line
	7200 4150 7000 4150
Wire Wire Line
	7200 4250 7000 4250
Wire Wire Line
	7200 4350 7000 4350
Wire Wire Line
	7200 4450 7000 4450
Wire Wire Line
	7200 4550 7000 4550
$Comp
L power:GND #PWR03
U 1 1 60B24B94
P 7450 4900
F 0 "#PWR03" H 7450 4650 50  0001 C CNN
F 1 "GND" H 7455 4727 50  0000 C CNN
F 2 "" H 7450 4900 50  0001 C CNN
F 3 "" H 7450 4900 50  0001 C CNN
	1    7450 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7200 4650 7150 4650
Wire Wire Line
	7150 4650 7150 4850
Wire Wire Line
	7700 4550 7800 4550
Wire Wire Line
	7700 4450 7800 4450
Wire Wire Line
	7800 4450 7800 4550
Connection ~ 7800 4550
Wire Wire Line
	7700 4350 7800 4350
Wire Wire Line
	7800 4350 7800 4450
Connection ~ 7800 4450
Wire Wire Line
	7700 4250 7800 4250
Wire Wire Line
	7800 4250 7800 4350
Connection ~ 7800 4350
Wire Wire Line
	7700 4150 7800 4150
Wire Wire Line
	7800 4150 7800 4250
Connection ~ 7800 4250
Wire Wire Line
	7700 4050 7800 4050
Wire Wire Line
	7800 4050 7800 4150
Connection ~ 7800 4150
Wire Wire Line
	7800 4550 7800 4850
NoConn ~ 7700 4650
Wire Wire Line
	7900 3950 7700 3950
Wire Wire Line
	7900 3850 7700 3850
Wire Wire Line
	7900 3750 7700 3750
Wire Wire Line
	7900 3650 7700 3650
Wire Wire Line
	7900 3550 7700 3550
Wire Wire Line
	7150 4850 7450 4850
Wire Wire Line
	7450 4900 7450 4850
Connection ~ 7450 4850
Wire Wire Line
	7450 4850 7800 4850
$Comp
L power:GND #PWR02
U 1 1 60B2B9CF
P 5650 5150
F 0 "#PWR02" H 5650 4900 50  0001 C CNN
F 1 "GND" H 5655 4977 50  0000 C CNN
F 2 "" H 5650 5150 50  0001 C CNN
F 3 "" H 5650 5150 50  0001 C CNN
	1    5650 5150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 4950 5650 5050
Wire Wire Line
	5550 4950 5550 5050
Wire Wire Line
	5550 5050 5650 5050
Connection ~ 5650 5050
Wire Wire Line
	5650 5050 5650 5150
Text Label 6350 3650 2    50   ~ 0
REN
Text Label 6350 4050 2    50   ~ 0
ATN
Text Label 6350 4150 2    50   ~ 0
IFC
Text Label 6350 4250 2    50   ~ 0
NDAC
Text Label 6350 4350 2    50   ~ 0
NRFD
Text Label 6350 4450 2    50   ~ 0
DAV
Text Label 6350 4550 2    50   ~ 0
EOI
Text Label 4950 3950 0    50   ~ 0
DIO1
Text Label 4950 4050 0    50   ~ 0
DIO2
Text Label 4950 4150 0    50   ~ 0
DIO3
Text Label 4950 4250 0    50   ~ 0
DIO4
Text Label 4950 4350 0    50   ~ 0
DIO5
Text Label 4950 4450 0    50   ~ 0
DIO6
Text Label 6350 3750 2    50   ~ 0
DIO7
Text Label 6350 3850 2    50   ~ 0
DIO8
Text Label 6350 3550 2    50   ~ 0
SRQ
Wire Wire Line
	6350 3550 6150 3550
Wire Wire Line
	6350 3650 6150 3650
Wire Wire Line
	6350 3750 6150 3750
Wire Wire Line
	6350 3850 6150 3850
Wire Wire Line
	6350 4050 6150 4050
Wire Wire Line
	6350 4150 6150 4150
Wire Wire Line
	6350 4250 6150 4250
Wire Wire Line
	6350 4350 6150 4350
Wire Wire Line
	6350 4450 6150 4450
Wire Wire Line
	6350 4550 6150 4550
Wire Wire Line
	4950 4450 5150 4450
Wire Wire Line
	4950 4350 5150 4350
Wire Wire Line
	4950 4250 5150 4250
Wire Wire Line
	4950 4150 5150 4150
Wire Wire Line
	4950 4050 5150 4050
Wire Wire Line
	4950 3950 5150 3950
$Comp
L Switch:SW_SPDT SW1
U 1 1 60B40689
P 4750 3250
F 0 "SW1" H 4750 3535 50  0000 C CNN
F 1 "SW_SPDT" H 4750 3444 50  0000 C CNN
F 2 "Button_Switch_THT:SW_Slide_1P2T_CK_OS102011MS2Q" H 4750 3250 50  0001 C CNN
F 3 "~" H 4750 3250 50  0001 C CNN
	1    4750 3250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR01
U 1 1 60B424DF
P 4250 3800
F 0 "#PWR01" H 4250 3550 50  0001 C CNN
F 1 "GND" H 4255 3627 50  0000 C CNN
F 2 "" H 4250 3800 50  0001 C CNN
F 3 "" H 4250 3800 50  0001 C CNN
	1    4250 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 60B42C8D
P 4250 3550
F 0 "C1" H 4365 3596 50  0000 L CNN
F 1 "10uF" H 4365 3505 50  0000 L CNN
F 2 "Capacitor_THT:C_Radial_D10.0mm_H12.5mm_P5.00mm" H 4288 3400 50  0001 C CNN
F 3 "~" H 4250 3550 50  0001 C CNN
	1    4250 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4250 3800 4250 3700
Wire Wire Line
	4250 3400 4250 3250
Wire Wire Line
	4250 3250 4550 3250
NoConn ~ 4950 3150
Text Notes 3450 3150 0    50   ~ 0
Switch to enable serial\nDTR reset for bootloading\n
NoConn ~ 5450 2950
NoConn ~ 5550 2950
NoConn ~ 5750 2950
NoConn ~ 6150 3350
NoConn ~ 6150 3450
NoConn ~ 5150 3750
NoConn ~ 5150 4550
NoConn ~ 5150 4650
NoConn ~ 6150 4650
NoConn ~ 6150 3950
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 60B5D167
P 5550 5050
F 0 "#FLG0101" H 5550 5125 50  0001 C CNN
F 1 "PWR_FLAG" V 5550 5177 50  0000 L CNN
F 2 "" H 5550 5050 50  0001 C CNN
F 3 "~" H 5550 5050 50  0001 C CNN
	1    5550 5050
	0    -1   -1   0   
$EndComp
Connection ~ 5550 5050
Text Label 4950 3350 0    50   ~ 0
NRST
$Comp
L MCU_Module:Arduino_Nano_v3.x A1
U 1 1 60AFCD0E
P 5650 3950
F 0 "A1" H 5200 2850 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 5150 2950 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 5650 3950 50  0001 C CIN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 5650 3950 50  0001 C CNN
	1    5650 3950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4950 3350 5150 3350
NoConn ~ 5150 3450
$EndSCHEMATC

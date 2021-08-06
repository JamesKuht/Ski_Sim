####### This config file seeks to create a realistic set of sensor values
import time
import csv

### This bit allows a simple import into Ski_sim for testing purposes when running config.py simply as an import
### balanced going roughly straight
ski_area = ['leftSkiFront', 'leftSkiLeft', 'leftSkiRight', 'leftSkiRear', 'rightSkiFront', 'rightSkiLeft', 'rightSkiRight', 'rightSkiRear']
pressure = [49, 48, 52, 51, 51, 51, 49, 49]

### This is the main program, if this program is run as the main program (i.e. 'python config.py')
if __name__ == '__main__':
    # w+ mode 'truncates' the file - i.e. deletes everything inside it
    f = open('ski_sim_data.csv', 'w+')
    f.close()
    f = open('ski_sim_data.csv', 'w+')
    writer = csv.writer(f)
    writer.writerow(ski_area)
    for i in range(2):
        ### balanced going roughly straight
        pressure = [49,48,52,51,51,51,49,49]
        writer.writerow(pressure)
        time.sleep(0.5)

        ### weight back going straight (classic beginner technique
        pressure = [42,48,52,58,41,51,49,59]
        writer.writerow(pressure)
        time.sleep(0.5)

        ### perfect smooth right turn
        pressure = [50,42,58,50,50,44,56,50]
        writer.writerow(pressure)
        time.sleep(0.5)

        ### perfect hard right turn
        pressure = [50,30,70,50,50,34,66,50]
        writer.writerow(pressure)
        time.sleep(0.5)        

        ### smooth right with poor angulation of inside ski
        pressure = [50,42,58,50,50,47,53,50]
        writer.writerow(pressure)
        time.sleep(0.5)        

        ### hard right with poor angulation of inside ski
        leftSkiFront = 50
        leftSkiLeft = 30
        leftSkiRight = 70
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 42
        rightSkiRight = 58
        rightSkiRear = 50

        time.sleep(0.5)

        ### terrible (weight-back poorly balanced) right turn
        leftSkiFront = 40
        leftSkiLeft = 37
        leftSkiRight = 63
        leftSkiRear = 60
        rightSkiFront = 41
        rightSkiLeft = 47
        rightSkiRight = 53
        rightSkiRear = 59

        ############### Left turns #################

        time.sleep(0.5)

        ### perfect smooth left turn
        leftSkiFront = 50
        leftSkiLeft = 56
        leftSkiRight = 44
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 58
        rightSkiRight = 42
        rightSkiRear = 50

        time.sleep(0.5)

        ### perfect hard left turn
        leftSkiFront = 50
        leftSkiLeft = 66
        leftSkiRight = 34
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 70
        rightSkiRight = 30
        rightSkiRear = 50

        time.sleep(0.5)

        ### smooth left with poor angulation of inside ski
        leftSkiFront = 50
        leftSkiLeft = 53
        leftSkiRight = 47
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 58
        rightSkiRight = 42
        rightSkiRear = 50

        time.sleep(0.5)

        ### hard left with poor angulation of inside ski
        leftSkiFront = 50
        leftSkiLeft = 58
        leftSkiRight = 42
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 70
        rightSkiRight = 30
        rightSkiRear = 50

        time.sleep(0.5)

        ### terrible (weight-back poorly balanced) left turn
        leftSkiFront = 40
        leftSkiLeft = 53
        leftSkiRight = 47
        leftSkiRear = 60
        rightSkiFront = 41
        rightSkiLeft = 63
        rightSkiRight = 37
        rightSkiRear = 59

    f.close()

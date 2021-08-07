####### This config file seeks to create a realistic set of sensor values
import time
import csv

### This bit allows a simple import into Ski_sim for testing purposes when running config.py simply as an import
### balanced going roughly straight
ski_area = ['leftSkiFront', 'leftSkiLeft', 'leftSkiRight', 'leftSkiRear', 'rightSkiFront', 'rightSkiLeft', 'rightSkiRight', 'rightSkiRear']
pressure = [50,50,50,50,50,50,50,50]

def nice_turn(pressures):
    #left turn initiation
    for i in range(10):
        pressure[1] += 2
        pressure[2] -= 2
        pressure[5] += 2
        pressure[6] -= 2
        writer.writerow(pressure)
    #left turn finish into right turn initiation
    for i in range(20):
        pressure[1] -= 2
        pressure[2] += 2
        pressure[5] -= 2
        pressure[6] += 2
        writer.writerow(pressure)
    #right turn finish
    for i in range(10):
        pressure[1] += 2
        pressure[2] -= 2
        pressure[5] += 2
        pressure[6] -= 2
        writer.writerow(pressure)

def example_values(pressures):
    # Some example values
    for i in range(1):
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
        pressure = [50,42,58,50,50,49,51,50]
        writer.writerow(pressure)
        time.sleep(0.5)        

        ### hard right with poor angulation of inside ski
        pressure = [50,30,70,50,50,46,54,50]
        writer.writerow(pressure)
        time.sleep(0.5)   

        ### terrible (weight-back poorly balanced) right turn
        pressure = [40,37,63,60,41,47,53,59]
        writer.writerow(pressure)
        time.sleep(0.5)   

        ############### Left turns #################
        ### perfect smooth left turn
        pressure = [50,56,44,50,50,58,42,50]
        writer.writerow(pressure)
        time.sleep(0.5)   
 
         ### perfect hard left turn
        pressure = [50,66,34,50,50,70,30,50]
        writer.writerow(pressure)
        time.sleep(0.5)   

        ### smooth left with poor angulation of inside ski
        pressure = [50,51,49,50,50,58,42,50]
        writer.writerow(pressure)
        time.sleep(0.5)   

        ### hard left with poor angulation of inside ski
        pressure = [50,56,44,50,50,70,30,50]
        writer.writerow(pressure)
        time.sleep(0.5)   

        ### terrible (weight-back poorly balanced) left turn
        pressure = [40,53,47,60,41,63,37,59]
        writer.writerow(pressure)
        time.sleep(0.5)   

### This is the main program, if this program is run as the main program (i.e. 'python config.py')
if __name__ == '__main__':
    # w+ mode 'truncates' the file - i.e. deletes everything inside it
    f = open('ski_sim_data.csv', 'w+')
    f.close()
    f = open('ski_sim_data.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(ski_area)
    
    # This function populates the csv with values for perfectly balanced turns, that match the skier video
    for i in range(2):
        nice_turn(pressure)
    
    # This hashed-out function populates the csv with a range of turns, to demonstrate tutorial functionality for a poor skier
    # example_values(pressure)
    
    f.close()

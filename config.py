####### This config file seeks to create a realistic set of sensor values
import time

### balanced going roughly straight
leftSkiFront = 49
leftSkiLeft = 48
leftSkiRight = 52
leftSkiRear = 51
rightSkiFront = 51
rightSkiLeft = 51
rightSkiRight = 49
rightSkiRear = 49

print(rightSkiRear)
### this bit doesn't work yet

if __name__ == '__main__':
    for i in range(2):
        ### balanced going roughly straight
        leftSkiFront = 49
        leftSkiLeft = 48
        leftSkiRight = 52
        leftSkiRear = 51
        rightSkiFront = 51
        rightSkiLeft = 51
        rightSkiRight = 49
        rightSkiRear = 49

        time.sleep(0.5)
        print(rightSkiRear)
        ### weight back going straight (classic beginner technique
        leftSkiFront = 42
        leftSkiLeft = 48
        leftSkiRight = 52
        leftSkiRear = 58
        rightSkiFront = 41
        rightSkiLeft = 51
        rightSkiRight = 49
        rightSkiRear = 59

        time.sleep(0.5)
        print(rightSkiRear)
        ### perfect smooth right turn
        leftSkiFront = 50
        leftSkiLeft = 42
        leftSkiRight = 58
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 44
        rightSkiRight = 56
        rightSkiRear = 50

        time.sleep(0.5)

        ### perfect hard right turn
        leftSkiFront = 50
        leftSkiLeft = 30
        leftSkiRight = 70
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 34
        rightSkiRight = 66
        rightSkiRear = 50

        time.sleep(0.5)

        ### smooth right with poor angulation of inside ski
        leftSkiFront = 50
        leftSkiLeft = 42
        leftSkiRight = 58
        leftSkiRear = 50
        rightSkiFront = 50
        rightSkiLeft = 47
        rightSkiRight = 53
        rightSkiRear = 50

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

        print(rightSkiRear)
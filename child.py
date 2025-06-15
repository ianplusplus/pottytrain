import ast

class Child:
    def __init__(self, name, reminder_time, major_reward, records_list, records_current, records_max):
        self.name = name
        self.reminder_time = reminder_time
        self.major_reward = major_reward
        self.records = records_list
        self.records_current = records_current
        self.records_max = records_max

    @staticmethod
    def LoadChildFromFile(filename):
        with open(filename, "r") as file:
            line = file.readline()
            line = line.strip()
            name = line
            line = file.readline()
            line = line.strip()
            reminder_time = int(line)
            line = file.readline()
            line = line.strip()
            major_reward = int(line)
            line = file.readline()
            line = line.strip()
            records = ast.literal_eval(line)
            line = file.readline()
            line = line.strip()
            records_current = int(line)
            line = file.readline()
            line = line.strip()
            records_max = int(line)
            return Child(name, reminder_time, major_reward, records, records_current, records_max)
    
    @staticmethod
    def SaveChildToFile(filename, child):
        with open(filename, "w") as file:
            file.write(child.name + '\n')
            file.write(str(child.reminder_time) + '\n')
            file.write(str(child.major_reward) + '\n')
            file.write(str(child.records) + '\n')
            file.write(str(child.records_current))
            file.write(str(child.records_max))

    def SaveChild(self):
        with open(self.name, "w") as file:
            file.write(self.name + '\n')
            file.write(str(self.reminder_time) + '\n')
            file.write(str(self.major_reward) + '\n')
            file.write(str(self.records) + '\n')
            file.write(str(self.records_current) + '\n')
            file.write(str(self.records_max) + '\n')

    def PottyAttempt(self, outcome):
        if self.records_current >= self.records_max:
            self.records = []

            for i in range(self.records_max):
                self.records.append(False)

            self.records_current = 0

        self.records[self.records_current] = outcome
        self.records_current = self.records_current + 1

    def CheckForMajorReward(self):
        counter = 0
        for i in range(self.records_current):
            if self.records[i]:
                counter = counter + 1

        if counter % self.major_reward == 0:
            return True
        else:
            return False

def main():

    #records_list = []

    #for i in range(36):
    #    records_list.append(False)

    #child = Child('Jackson', 30, 6, records_list, 0, 36)
    child = Child.LoadChildFromFile('Jackson')
    for i in range(1):
        child.PottyAttempt(True)

    print(child.CheckForMajorReward())

    child.SaveChild()

    print(child.records)
main()
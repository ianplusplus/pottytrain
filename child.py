import ast

class Child:
    def __init__(self, name, reminder_time, major_reward, records_list, records_current):
        self.name = name
        self.reminder_time = reminder_time
        self.major_reward = major_reward
        self.records = records_list
        self.records_current = records_current

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
            return Child(name, reminder_time, major_reward, records, records_current)
    
    @staticmethod
    def SaveChildToFile(filename, child):
        with open(filename, "w") as file:
            file.write(child.name + '\n')
            file.write(str(child.reminder_time) + '\n')
            file.write(str(child.major_reward) + '\n')
            file.write(str(child.records) + '\n')
            file.write(str(child.records_current))


def main():

    records_list = []

    for i in range(36):
        records_list.append(False)

    #child = Child('Jackson', 30, 6, records_list, 0)
    #Child.SaveChildToFile('jackson.chld', child)
    child = Child.LoadChildFromFile('jackson.chld')
    print(child.name, child.reminder_time, child.major_reward, child.records, child.records_current)

main()
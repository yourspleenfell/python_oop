class Hospital(object):
    def __init__(self, location):
        self.patients = [ ]
        self.location = location
        self.capacity = 10
        self.beds_occupied = [ ]
    def admit(self, val):
        if (len(self.patients) < self.capacity):
            for x in range(len(Patient.all_patients)):
                if (val == Patient.all_patients[x].id) or val == Patient.all_patients[x].name:
                    self.patients.append(Patient.all_patients[x])
                    beds = [ ]
                    for num in range(self.capacity):
                        beds.append(num + 1)
                        Patient.all_patients[x].bed_number = "B" + str(num + 1)
                    if (x <= self.capacity):
                        bed = "B" + str(x + 1)
                        print x
                        self.beds_occupied.append(bed)
                        Patient.all_patients[x].bed_number = bed                   
                    print "Successfully addmited " + Patient.all_patients[x].name
        else:
            print "Cannot admit patient. Hospital is full."
        return self
    def discharge(self,val):
        for x in self.patients:
            if (val == x.id or val ==x.name):
                self.patients.remove(x)
                self.beds_occupied.remove(x.bed_number)
                x.bed_number = "None"
                print x.name + " was successfully discharged."
        return self

class Patient(object):
    all_patients = [ ]
    def __init__(self, name, age, allergies):
        self.name = name
        self.age = age
        self.allergies = allergies
        Patient.all_patients.append(self)
        self.bed_number = "None"
        self.get_id()
    def get_id(self):
        for val in range(len(Patient.all_patients)):
            self.id = "P" + str(val + 1)
        return self

p1 = Patient("John Doe", 35, "Peanuts")
p2 = Patient("Jayne Willicker", 26, "Shellfish")
p3 = Patient("Morty Goldstein", 14, "None known")
p4 = Patient("Rick Sanchez", 60, "None known")
p5 = Patient("Tom Cruise", 52, "Being humble")
p6 = Patient("Inigo Montoya", 32, "People who killed his father")
p7 = Patient("Mike Wazowski", 37, "Humans")
p8 = Patient("Titus Andronicus", 74, "None known")
p9 = Patient("Dana Scully", 44, "Believing in aliens")
p10 = Patient("Cloud Strife", 26, "Being happy")
p11 = Patient("Zidane Tribal", 22, "None known")
p12 = Patient("Bellatrix LaStrange", 50, "She is just crazy")


hospital = Hospital("Phoenix")

hospital.admit("P1").admit("P2")

hospital.admit("P3").admit("Tom Cruise").admit("P6").admit("P7").admit("P8").admit("P4").admit("P9").admit("P10").admit("P11")


hospital.discharge("P2")
hospital.admit("P11")

print p2.bed_number

hospital.discharge("P11")
print p11.bed_number
hospital.admit("P12")
print p12.bed_number

print hospital.beds_occupied

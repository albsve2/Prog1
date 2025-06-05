from time import sleep

class Vehicle:
    def __init__(self, destination):
        self.destination = destination
        
    def get_destination(self):
        return self.destination

class Lane:
    def __init__(self, length):
        self.length = length
        self.cars_in_lane = []
        for _ in range(length): #Loppar över längden på filen och tilldelar none till platserna
            self.cars_in_lane.append(None)

    def __str__(self): #skapar strängen
        self.str = "["
        for i in range(self.length):
            if self.cars_in_lane[i] == None:
                self.str += "."
            else:
                self.str += self.cars_in_lane[i].get_destination()
        self.str += "]"
        return self.str

    def last_free(self): #kollar om det finns plats för en ny bil
        return self.cars_in_lane[-1] == None
    
    def enter(self, vehicle): #ny bil in i filen
        if self.last_free():
            self.cars_in_lane[-1] = vehicle

    def step(self): #metod som gör tidsteg i körfältet
        for i in range(len(self.cars_in_lane)):
            if self.cars_in_lane[i] == None:
                self.cars_in_lane.pop(i) #tar bort första tomma platsen och lägger till i slutet på filen
                self.cars_in_lane.append(None)
                break #avbryter för att inte skapa fler tomma utrymmen

    def remove_first(self): #tar bort den första bilen i en fil, om ingen bil finns returneras None
        d = self.cars_in_lane.pop(0)
        self.cars_in_lane.insert(0, None)
        return d

class Light:
    def __init__(self, period, green_period): # Skapar trafikljus med period och grönperiod
        self.period = period
        self.green_period = green_period
        self.clock = 0

    def __str__(self):
        if self.is_green():
            return "(G)"
        else:
            return "(R)"

    def step(self): # steppar trafikljusets klocka
        self.clock += 1
        if self.clock >= self.period:
            self.clock = 0

    def is_green(self):
        return self.clock < self.green_period

class DestinationGenerator: # Genererar destinationer

    def __init__(self):
        """Add internal data."""
        self._arrivals = (
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1) # 0 none 1 South 2 West

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self): # steppar klockan och returnerar nästa bilens destination
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals) #ökar med 1 och "cirkulerar tillbaka" till 0 när det når längden av sekvensen
        return 'W' if ind == 1 else 'S' if ind == 2 else None

class TrafficSystem:

    def __init__(self): #startar trafiksystemet med trafikljus, 2 filer, destinationsgenerator, en tom kö och klockan på 0
        self.a_light = Light(10, 8)
        self.lane_befor = Lane(5)
        self.lane_after = Lane(5)
        self.dgen = DestinationGenerator()
        self.carpool = []
        self.time = 0

    def snapshot(self): # Printar systemets nuvarande tillstånd
        print(self.lane_after, self.a_light, self.lane_befor, self.carpool)

    def step(self): # Utför ett tidssteg för alla komponenter
        self.time += 1

        self.lane_after.remove_first()
        self.lane_after.step()

        if self.a_light.is_green():
            self.lane_after.enter(self.lane_befor.remove_first())

        d = self.dgen.step()
        if d is not None:
            self.carpool.append(d)

        self.lane_befor.step()

        if self.lane_befor.last_free() and len(self.carpool) > 0:
            self.lane_befor.enter(Vehicle(self.carpool.pop(0)))

        self.a_light.step()

def main():
    ts = TrafficSystem()
    for i in range(34):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()

main()


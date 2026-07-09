class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # one lane highway, n cars
        # position of ith car
        # speed of ith car 
        # destination at position target mile
        # return number of different car fleets that will arrive at the destination
       
        # if a.pos < b.pos but a.speed > b.speed (can become a fleet) if time a < time b
        res = 1
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        prevTime = (target-cars[0][0])/cars[0][1]
        for i in range(1, len(cars)):
            currentTime = (target-cars[i][0])/cars[i][1]
            if currentTime > prevTime:
                prevTime = currentTime
                res += 1
            print("for " + str(i) + ": " + str(res))
        return res
        
def Rec(Dx, Dy, r):
    #Define the rectangle
    points = np.array([[0 + Dx, 0 + Dy], [1 + Dx, 0 + Dy], [1 + Dx, 1/math.sqrt(2) + Dy], [0 + Dx, 1/math.sqrt(2) + Dy], [0 + Dx, 0 + Dy]])

    
    theta = np.radians(r)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))

    Recinitial = 1 * 1/math.sqrt(2)
    rotated_points = np.dot(points, R.T)

    plt.plot(rotated_points[:, 0], rotated_points[:, 1])

def cost(Dx, Dy, r):
    
    points = np.array([[0 + Dx, 0+ Dy], [1+ Dx, 0+ Dy], [1+ Dx, 1/math.sqrt(2)+ Dy], [0+ Dx, 1/math.sqrt(2) + Dy], [0+ Dx, 0+ Dy]])

    theta = np.radians(r)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c, -s), (s, c)))

    Recinitial = 1 * 1/math.sqrt(2)

    rotated_points = np.dot(points, R.T)
   
    theta = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(2 * theta)
    Xc = r * np.cos(theta)
    Yc = r * np.sin(theta)
    
    x1, y1 = rotated_points[0] 

    x2, y2 = rotated_points[1]  

    x3, y3 = rotated_points[2]

    x4, y4 = rotated_points[3]

    Bslope = (y2 - y1) / (x2 - x1)
    Rslope = (y3 - y2) / (x3 - x2)
    Tslope = (y4 - y3) / (x4 - x3)
    Lslope = (y1 - y4) / (x1 - x4)

    xrand = np.random.uniform(-1, 1, 100000)
    yrand = np.random.uniform(-1, 1, 100000)
    
    above_line_points = []

    for i in range(len(yrand)):
        if yrand[i] > Bslope * xrand[i] + (y1 - Bslope * x1):
            above_line_points.append((xrand[i], yrand[i]))

   
    side_of_line_points_R = []

    for point in above_line_points:
        expected_y = Rslope * point[0] + (y2 - Rslope * x2)
    
    #Check if the y-coordinate is above the expected y-coordinate
        if point[1] < expected_y: 
            side_of_line_points_R.append(point)
    
    right_of_line_points_L = []

    for point in side_of_line_points_R:
        expected_y = Lslope * point[0] + (y4 - Lslope * x4)
    
    
        if point[1] > expected_y:  
            right_of_line_points_L.append(point)
 
    under_line_points_T = []

    for point in right_of_line_points_L:
        expected_x = (point[1] - (y3 - Tslope * x3)) / Tslope
    
        if point[0] > expected_x:  
            under_line_points_T.append(point)

    #Separate the points into x and y lists
    xnew = [point[0] for point in under_line_points_T]
    ynew = [point[1] for point in under_line_points_T]

    satisfied_points = []

    for x, y in under_line_points_T:
        #Compute the value of the function at the given point
        value = (x**2 + y**2)**3 - 4 * x**2 * y**2
    

        if value < 0:  
            satisfied_points.append((x, y))

    xfunc = [point[0] for point in satisfied_points]
    yfunc = [point[1] for point in satisfied_points]

    #Monte Carlo integration implementation
    Funcpoints = len(yfunc)
    totalpoints = len(xnew)

    if totalpoints == 0:
        return 0

    A = Recinitial * (Funcpoints / totalpoints)

    return A

    
def simulated_annealing(Dx, Dy, r, initial_temperature, cooling_rate, num_steps):
    current_solution = [Dx, Dy, r]
    current_cost = cost(Dx, Dy, r)
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature

    for step in range(num_steps):
        #Generate a neighboring solution
        Dx_new, Dy_new, r_new = [current_solution[i] + np.random.normal(0, 0.1) for i in range(3)]
        new_solution = [Dx_new, Dy_new, r_new]
        
        new_cost = cost(Dx_new, Dy_new, r_new)

        #If the new solution is better, accept it
        if new_cost > current_cost or np.random.rand() < np.exp((new_cost - current_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost
            #update the best solution
            if new_cost > best_cost:
                best_solution = new_solution
                best_cost = new_cost
        #Update temperature
        temperature *= cooling_rate

    return best_solution

initial_solution = [-.2, -.6, 1]  #Initial position
initial_temperature = 1.0
cooling_rate = 0.95 
num_steps = 1000 

best_solution = simulated_annealing(*initial_solution, initial_temperature, cooling_rate, num_steps)
print("Best solution:", best_solution)
print("Best cost:", cost(*best_solution))

best_x, best_y, best_r = best_solution

theta = np.linspace(0, 2*np.pi, 1000)
r = np.sin(2 * theta)
Xc = r * np.cos(theta)
Yc = r * np.sin(theta)
plt.plot(Xc, Yc, color='green')
plt.grid(True)
Rec(best_x, best_y, best_r)

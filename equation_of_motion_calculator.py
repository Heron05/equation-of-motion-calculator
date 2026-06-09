print()
class EquationOfMotionCalculator:
    
    def __init__(self):
        self.u = None
        self.a = None
        self.v = None
        self.s = None
        self.t = None
        
    def main(self):
        w_t_f = input("what to find(t, v, u, a, s): ")
        try:
            match w_t_f:
                case 'v':
                    self.u = float(input("\nEnter the initial velocity (u in m/sec): "))
                    self.a = float(input("Enter the accleration(a in m/sec^2): "))
                    t_input = input("Enter the total time taken (t in sec): ")
                    s_input = input("Enter the displacement (s in m): ")
                    
                    if s_input == "":
                        self.s = None
                    else:
                        self.s = float(s_input)
                        
                    if t_input == "":
                        self.t = None
                    else:
                        self.t = float(t_input)
                    
                    if self.s is None and self.t is None:
                        print("pls put either one of the s or t...")
                        return
                        

                case 'u':
                    self.v = float(input("\nEnter the final velocity (V in m/sec): "))
                    self.a = float(input("Enter the accleration (a in m/sec^2): "))
                    t_input= input("Enter the total time taken (t in sec): ")
                    
                    s_input = input("Enter the displacement (s in m): ")
                    
                    if s_input == "":
                        self.s = None
                    else:
                        self.s = float(s_input)
                        
                    if t_input == "":
                        self.t = None
                    else:
                        self.t = float(t_input)
                    
                    if self.s is None and self.t is None:
                        print("pls put either one of the s or t...")
                        return
                        

                case 'a':
                    self.u = float(input("\nEnter the initial velocity (u in m/sec): "))
                    
                    s_input = input("Enter the displacement (s in m): ")
                    t_input = input("Enter the total time taken (t in s): ")
                    v_input = input("Enter the final velocity (v in m/sec): ") 
                    
                    
                    try:
                        if v_input != "":
                            self.v = float(v_input)
                    
                        if t_input != "":
                            self.t = float(t_input)
                                
                        if s_input != "":
                            self.s = float(s_input)
                        
                    except ValueError:
                        print("\n Error while executing the code as insuffcent information given... so pls provide more than 2 parameter there...")
                        
                    if self.v is None and self.s is None and self.t is None:
                        print("you need to enter atleast 2 of the parameters among s, t or v...")
                        return
                        
                    
                    
                case 't':
                    self.u = float(input("\nEnter the initial velocity (u in m/sec): "))
                    self.v = float(input("Enter the final velocity (v in m/sec): "))
                    self.a = float(input("Enter the accleration (a in m/sec^2): "))
                    
                    s_input = input("Enter the displacement (s in m): ")
                    
                    if s_input == "":
                        self.s = None
                    else:
                        self.s = float(s_input)
                        
                case 's':
                    self.u = float(input("\nEnter the initial velocity (u in m/s): "))
                    self.a = float(input("Enter the accleration (a in m/s^2): "))
                    
                    t_input = input("Enter the total time taken (t in s): ")
                    v_input = input("Enter the final velocity (v in m/sec): ")
                    
                    try:
                        if v_input != "":
                            self.v = float(v_input)
                    
                        if t_input != "":
                            self.t = float(t_input)
                    except ValueError:
                        print("put the value of either time or final velocity...")
                        
                case _:
                    print("Pls put input in among (s, t, v, u, a) !!!")
                    
        except ValueError:
            print("Pls enter an integer!!!")
            return
        
        self.physics_math(w_t_f)

    def physics_math(self, target):
        try:
            
            match target:
                case 'v':
                    if self.s != None:
                        for_v = ((self.u * self.u) + (2) * (self.a) * (self.s))**(0.5)
                    else:
                        for_v = self.u + (self.a * self.t)
                    print(f"the value of v is {for_v} m/s")
                        
                        
                case 'u':
                    if self.s != None:
                        for_u = (2 * (self.s) - (self.a) * (self.t)**2) / (2 * (self.t))
                    else:
                        for_u = self.v - (self.a * self.t)
                    print(f"the value of u is {for_u} m/s")
                
                case 't':
                    if self.s != None:
                        print("its in quadratic...")
                        return
                    else:
                        for_t = (self.v - self.u) / self.a
                    print(f"the value of t is {for_t} s")
                
                
                case 's':
                    if self.t == None:
                        for_s = ((self.v)**2 - (self.u)**2) / (2 * self.a)
                    
                    
                    elif self.v == None:
                        for_s = (self.u * self.t) + (0.5) * (self.a) * (self.t)**2
                    
                    else: 
                      for_s = (self.u * self.t) + (0.5) * (self.a) * (self.t)**2
                    
                    print(f"the value of s is {for_s} m.")    
                    
                    
                case 'a':
                    if self.s == None:
                        for_a = (self.v - self.u) / self.t
                    
                    elif self.t == None:
                        for_a = (((self.v)**2) - (self.u)**2)/ (2 * (self.s))
                    
                    elif self.v == None:
                        for_a = 2 * (self.s - self.u * self.t) / (self.t**2)
                    
                    print(f"the value of a is {for_a} m/sec^2")
                    
        except TypeError:
            print("\nError: Not enough information! You must provide at least 3 known variables.")        
            return
        
calculator = EquationOfMotionCalculator()

calculator.main()

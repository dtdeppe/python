import webbrowser
import time
total_iterations = 3
iteration = 0
print ("Take a break")
print ("Started up at",time.ctime())
while (iteration < total_iterations):
    time.sleep(2*60*60)
    print ("Latest iteration at ",time.ctime())
    webbrowser.open("https://youtu.be/ZEs9zmF-Fwk")
    iteration = iteration + 1
    

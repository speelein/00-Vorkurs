import datetime
import time
# import
print(datetime.datetime.now().strftime(
    "%H:%M:%S-%d.%m.%Y"))  # B,b.W,w moeglich

# gibt dann keine Zeit zurueck   B,b.W,w moeglich
print(datetime.date.today().strftime("%H:%M:%S-%d.%m.%Y"))

print(time.time())  # Zeit seit 1950 ?? die vergangen ist

# time kann Differenzen berechnen
start = time.time()
time.sleep(10)         # wartet 10 sek
end = time.time()
print(end-start)
# letzter Stand

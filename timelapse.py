from picamera import PiCamera
import os
import sys
from datetime import datetime
from time import sleep

def createDir(dirName): # Συνάρτηση δημιουργία φακέλου
    try:
        os.makedirs(dirName)
        print("Δημιουργήθηκε ο φάκελος " , dirName)
    except FileExistsError:
        print("Ο φάκελος " , dirName ,  " υπάρχει ήδη!!")

minutesRun = 240 # Χρόνος κατά τον οποίο θα γίνεται λήψη φωτογραφιών (λεπτά)
photoInterval = 15 # Χρόνος μεταξύ δύο λήψεων (δευτερόλεπτα)
fps = 30 # Πλαίσια ανά δευτερόλεπτο
numberPhotos = int((minutesRun*60)/photoInterval) # Πλήθος φωτογραφιών
print("Θα ληφθούν ", numberPhotos, " φωτογραφίες")

camera = PiCamera() # Δημιουργία αντικειμένου κάμερας
#camera.resolution = (1024, 768) # Ανάλυση φωτογραφιών
#camera.iso = 0 # Ρύθμιση του iso της κάμερας
#camera.shutter_speed = 0 # Ρύθμιση του χρόνο του κλείστρου της κάμερας
#camera.white_balance = 

dirName = os.path.join(sys.path[0],'/media/usb/' +'photos-' + datetime.now().strftime('%d%m%y-%H%M%S')) # Όνομα φακέλου που θα αποθηκευτούν οι φωτογραφίες

createDir(dirName)  # Κλήση της συνάρτησης δημιουργίας φακέλου

for i in range(numberPhotos):   # Επαναληπτική διαδικασία λήψης φωτογραφιών
    camera.capture(dirName + '/image{0:08d}.jpg'.format(i)) # Λήψη φωτογραφίας
    sleep(photoInterval)    # Χρόνος αναμονής μεταξύ δύο λήψεων
print("Ολοκληρώθηκε η λήψη των φωτογραφιών")
print("Ακολουθεί η δημιουργία του βίντεο. Η διαδικασία θα κρατήσει αρκετή ώρα!!")

os.system('ffmpeg -i ' + dirName + '/image%08d.jpg -c:v libx264 ' + dirName + '/timelapse.mp4') # Δημιουργία του βίντεο

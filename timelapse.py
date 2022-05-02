from picamera import PiCamera
import os
import sys
from datetime import datetime
from time import sleep
import yaml

camera = PiCamera()  # Δημιουργία αντικειμένου κάμερας
config = yaml.safe_load(open(os.path.join(sys.path[0], "config.yml")))  # Άνοιγμα του αρχείο ρυθμίσεων

def createDir(dirName):  # Συνάρτηση δημιουργία φακέλου
    try:
        os.makedirs(dirName)
        print("Δημιουργήθηκε ο φάκελος ", dirName)
    except FileExistsError:
        print("Ο φάκελος ", dirName,  " υπάρχει ήδη!!")

if config['resolution']:
    camera.resolution = (
    config['resolution']['width'],
    config['resolution']['height']
)

if config['iso']:
    camera.iso = config['iso']

if config['shutter_speed']:
    camera.shutter_speed = config['shutter_speed']
    sleep(1)
    camera.exposure_mode = 'off'

if config['white_balance']:
    camera.awb_mode = 'off'
    camera.awb_gains = (
        config['white_balance']['red_gain'],
        config['white_balance']['blue_gain']
    )

if config['rotation']:
    camera.rotation = config['rotation']

numberPhotos = int((config['minutesRun']*60)/config['photoInterval'])  # Πλήθος φωτογραφιών
print("Θα ληφθούν ", numberPhotos, " φωτογραφίες")

dirName = os.path.join(sys.path[0], str(config['dir_path']) + 'photos-' + datetime.now().strftime('%d%m%y-%H%M%S'))  # Όνομα φακέλου που θα αποθηκευτούν οι φωτογραφίες

createDir(dirName)  # Κλήση της συνάρτησης δημιουργίας φακέλου

for i in range(numberPhotos):   # Επαναληπτική διαδικασία λήψης φωτογραφιών
    camera.capture(dirName + '/image{0:08d}.jpg'.format(i))  # Λήψη φωτογραφίας
    sleep(config['photoInterval'])    # Χρόνος αναμονής μεταξύ δύο λήψεων
print("Ολοκληρώθηκε η λήψη των φωτογραφιών")

if config['create_gif']:   # Δημιουργία animated Gif
    print ('\nΔημιουργία animated gif.\n')
    os.system('convert -delay 10 -loop 0 ' + dirName + '/image*.jpg ' + dirName + '/animated.gif')

if config['create_video']:
    print("\nΔημιουργία βίντεο. Η διαδικασία θα κρατήσει αρκετή ώρα!!\n")
    os.system('ffmpeg -i ' + dirName + '/image%08d.jpg -c:v libx264 ' + dirName + '/video.mp4')  # Δημιουργία του βίντεο

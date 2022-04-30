# Συσκευή δημιουργίας βίντεο με χρονική καθυστέρηση (time lapse)

Με αύτην την συσκευή είναι δυνατή η δημιουργία βίντεο με χρονική καθυστέρηση (time lapse). Πιο συγκεκριμένα, γίνεται λήψη φωτογραφιών ανά τακτά χρονικά διαστήματα (π.χ. κάθε ένα λεπτό) και στη συνέχεια παράγεται ένα βίντεο από το σύνολο των εικόνων. Η συσκευή μεταξύ άλλων μπορεί να χρησιμοποιηθεί για την παρακολούθηση της ανάπτυξης φυτών, την καταγραφή του ουρανού (ανατολή, ηλιοβασίλεμα, κίνηση άστρων), την πορεία εκτύπωσης ενός μοντέλου σε 3D εκτυπωτή.

## Υλικό και λογισμικό που χρησιμοποιήθηκε

Για την δημιουργία της συσκευής χρησιμοποιήθηκαν τα παρακάτω υλικά:
1. <a href="https://www.raspberrypi.com/products/raspberry-pi-4-model-b/">Raspberry Pi 4</a>
2. <a href="https://www.raspberrypi.com/products/camera-module-v2/">Pi Camera</a>
3. USB stick

Για την καταγραφή των φωτογραφιών, χρησιμοποιήθηκε το λογισμικό <a href="https://github.com/fsphil/fswebcam">fswebcam</a>. Για την λήψη των φωτογραφιών σε τακτά χρονικά διαστήματα, χρησιμοποιήθηκε το λογισμικό cron. Για την δημιουργία του βίντεο, από το σύνολο των εικόνων, χρησιμοποιήθηκε το λογισμικό ffmpeg.


ffmpeg -i image%01d.jpg -c:v libx264 output.mp4

ffmpeg -r 60 -pattern_type glob -i '/home/pi/TimelapsePhotos/*.jpg' -c:v copy /home/pi/TimelapsePhotos/timelapse.avi

ffmpeg -r 30 -pattern_type glob -i "*.jpg" -c:v libx264 -pix_fmt yuv420p -movflags +faststart timelapse.mp4
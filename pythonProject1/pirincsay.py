import cv2

# Video yakalamayı başlat
cap = cv2.VideoCapture(0)  # 0, ilk kamerayı temsil eder. Birden fazla kamera varsa değeri değiştirilebilir.

# Pirinç görüntüsünü yükle
pirinc_img = cv2.imread('pirinc.jpg')

while True:
    # Kameradan bir kareyi al
    ret, frame = cap.read()

    if not ret:
        print("Kameradan alınamıyor.")
        break

    # Gri tonlamaya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Pirinç tanelerini tespit etmek için
    _, threshold = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)

    # Nesne tespiti için konturları bul
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Pirinç tanesi sayısı
    rice_count = len(contours)

    # Görüntü üzerine pirinç sayısını yazdır
    cv2.putText(frame, f"Pirinc sayisi: {rice_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Pirinç görüntüsünü kareye ekle
    frame[10:10 + pirinc_img.shape[0], 10:10 + pirinc_img.shape[1]] = pirinc_img

    cv2.imshow('Web Kamera', frame)

    # 'q' tuşuna basarak döngüyü kır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak
cap.release()
cv2.destroyAllWindows()


def center_window(screen_width, screen_height, window_width, window_height):
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    return f"{window_width}x{window_height}+{x}+{y}"
#Bu hesaplamalar, pencerenin ekranın ortasında olabilmesi için gerekli olan sol üst köşe koordinatını (x, y) belirler.
#Bu fonksiyon, bir Tkinter penceresini ekranın tam ortasına yerleştirmek için gerekli olan pencere koordinatlarını hesaplar
#Eğer pencere boyutları 400x300 ve ekran boyutları 1920x1080 ise, bu fonksiyon şu değeri döndürecektir: "400x300+760+390".
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        if self.path.startswith("/src/img"):
            file_path = f"{self.path[5:]}"
            print("good1")
            print(f"это file_path {file_path}")
            print(f"это self.path {self.path}")
            print(f"это os.path {os.path.exists(file_path)}")
            if file_path.endswith(".png"):
                if os.path.exists(file_path):
                    self.send_header("Content-type", "image/png")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
            elif file_path.endswith("svg"):
                if os.path.exists(file_path):
                    self.send_header("Content-type", "image/svg+xml")
                    self.end_headers()
                    with open(file_path, "rb") as file:
                        self.wfile.write(file.read())
            else:
                print("good3")
                self.send_error(404, "Image Not Found")

        if self.path == "/":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/contacts.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))
        elif self.path == "/catalog":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/catalog.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))
        elif self.path == "/category":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/category1.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))
        elif self.path == "/contacts":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/contacts.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))
        elif self.path == "/main":
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(
                "C:/Users/Nurlan/IT/Проекты/django/html/main.html",
                "r",
                encoding="utf-8",
            ) as file:
                reader = file.read()
            self.wfile.write(bytes(reader, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")

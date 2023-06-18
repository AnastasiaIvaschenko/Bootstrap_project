from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def __get_html_content(self):
        return """
        <!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    <div class="container">
        <div class="row  text-center mt-5">
            <div class="col-12">
                <div class="card-body">
                        <h5 class="card-header">Контакты</h5>
                </div>
            </div>
        </div>
        <div class="row row-cols-1 row-cols-md-2 g-2 mt-5">
            <div class="col-6">
                <div class="card">
                    <div class="card-body">
                        <div class="mb-3">
                            <label class="form-label">Имя</label>
                            <div class="input-group">
                                <input type="text" class="form-control">
                            </div>
                        </div>
                        <div class="mb-3">
                          <label for="basic-url" class="form-label">Почта</label>
                          <div class="input-group">
                            <span class="input-group-text" id="basic-addon1">@</span>
                            <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4">
                          </div>
                        </div>
                        <div class="imb-3">
                          <label class="form-label">Сообщение</label>
                          <textarea class="form-control" aria-label="With textarea"></textarea>
                        </div>
                        <div class="mb-3 mt-3">
                            <input class="btn btn-primary" type="submit" value="Отправить">
                        </div>
                    </div>
                </div>

                <div class="col-6">
                    <div class="card-body">
                        <h5 class="card-header">Наши контакты</h5>
                        Здесь идет сплошной текст описания контактов
                    </div>
                </div>
            </div>
        </div>
    </div>
  </body>
</html>
        """
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_html_content()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "application/json") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8")) # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
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
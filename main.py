from handlers.server_handler import ServerHandler
import socketserver
from constants import SERVER_PORT


# Script para lanzar la aplicacion
Handler = ServerHandler

try:
    with socketserver.TCPServer(("", SERVER_PORT), Handler) as httpd:
        print(f'Starting http://0.0.0.0:{SERVER_PORT}')
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping by Ctrl+C")
    httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
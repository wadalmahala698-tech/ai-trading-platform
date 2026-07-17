from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from users import register, login, get_balance, deposit, withdraw


class Server(BaseHTTPRequestHandler):

    def send_json(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


    def read_data(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length)
        return json.loads(data)


    def do_POST(self):

        data = self.read_data()

        if self.path == "/login":

            user = login(
                data["username"],
                data["password"]
            )

            if user:
                self.send_json({
                    "login": "success",
                    "balance": user[3]
                })
            else:
                self.send_json({
                    "login": "failed"
                })


        elif self.path == "/register":

            result = register(
                data["username"],
                data["password"]
            )

            self.send_json({
                "result": result
            })


        elif self.path == "/deposit":

            deposit(
                data["username"],
                data["amount"]
            )

            self.send_json({
                "status": "deposit complete"
            })


        elif self.path == "/withdraw":

            withdraw(
                data["username"],
                data["amount"]
            )

            self.send_json({
                "status": "withdraw complete"
            })


server = HTTPServer(("0.0.0.0", 8000), Server)

print("AI Trading Server running on port 8000")

server.serve_forever()

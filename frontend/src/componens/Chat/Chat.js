import {useEffect, useRef, useState} from "react";
import {socketService} from "../../services/socketService";
import {client} from "websocket";

const Chat = () => {
    const [room, setRoom] = useState(null)
    const [socketClient, setSocketClient] = useState(null)
    const [messages, setMessages] = useState([])
    const roomImput = useRef();

    useEffect(() => {
        if (room) {
            socketInit(room).then(client => setSocketClient(client))
        }
    }, [room]);
    const socketInit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);

        client.onopen = () => {
            console.log('Chat socket connected');
        }

        client.onmessage = ({data}) => {
            const parse = JSON.parse(data.toString());
            const {message, user} = parse;
            setMessages(prevState => [...prevState, {user, message}])
        }

        return client
    }

    const setRoomHandler = () => {
        setRoom(roomImput.current.value)
    }

    const handlePressEnter = (e)=>{
        if (e.key === 'Enter'){
            socketClient.send(JSON.stringify({
                data:e.target.value,
                action:'send_message',
                request_id:new Date().getTime()
            }))
            e.target.value = ''
        }
    }
    return (
        <div>
            {
                !room ?
                    <div>
                        <input type="text" ref={roomImput}/>
                        <button onClick={setRoomHandler}>set</button>
                    </div>
                    :
                    <div>
                        {
                            messages.map(message=><div>{message.user}: {message.message}</div>)
                        }
                        <input type="text" onKeyDown={handlePressEnter}/>
                    </div>
            }
        </div>
    );
};

export {Chat};
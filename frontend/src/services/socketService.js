import {authService} from "./authService";
import {w3cwebsocket as W3cWebsocket} from 'websocket';
import {socketBaseURL} from "../constants/urls";

const socketService = async () => {
    const {data: {token}} = await authService.getSoketToken();
    return {
        chat: (room) => new W3cWebsocket(`${socketBaseURL}/chat/${room}/?token=${token}`),
        cars: ()=>new W3cWebsocket(`${socketBaseURL}/cars/?token=${token}`)
    }
}

export {
    socketService
}
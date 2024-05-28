const baseURL = '/api'
const socketBaseURL = 'ws://localhost/api'
const auth = '/auth'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/socket`
    }
}

export {
    baseURL,
    socketBaseURL,
    urls
}
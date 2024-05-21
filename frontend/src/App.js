import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [users, setUsers] = useState([])

    useEffect(() => {
        axios.get('/api/users').then(({data}) => setUsers(data.data))
    }, []);

    return (
        <div>
            {users.map(user => <div key={user.id}>{JSON.stringify(user)}</div>)}
        </div>
    );
};

export {App};
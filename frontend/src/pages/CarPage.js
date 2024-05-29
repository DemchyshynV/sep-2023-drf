import {Chat} from "../componens/Chat/Chat";
import {CarForm} from "../componens/CarConteiner/CarForm";
import {Cars} from "../componens/CarConteiner/Cars";

const CarPage = () => {
    return (
        <div>
            <CarForm/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {CarPage};
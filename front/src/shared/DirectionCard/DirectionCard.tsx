import '../DirectionCard/DirectionCard.scss';
import {DirectionCardInterface, DirectionInterface} from "@/interfases/interfaces";

function DirectionCard({id, main_image, icon, type}: DirectionCardInterface) {


    return (

        <div className={type} >
            <img className="DirectionCard__style" src={main_image}></img>
            <div className="DirectionCard__overlay">
                <img className="DirectionCard__overlay__style" src={icon}></img>
            </div>
        </div>
    );
}

export default DirectionCard;

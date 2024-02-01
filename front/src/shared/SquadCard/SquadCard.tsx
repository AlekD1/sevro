import "./squadcard.scss";
import Link from "next/link";

interface SquadCardProps {
    id: number;
    name: string;
    main_image: string;
    description: string;
    isActive?: boolean;
    vk: string;
}

function SquadCard({id, name, description, main_image, isActive, vk}: SquadCardProps) {

    return (
        <div className={isActive ? "squad-card_active squad-card" : "squad-card"}>
            <img src={main_image} className="squad-card__img"/>
            <div className="squad-card__name">{name}</div>
            <p className="squad-card__description">{description}</p>
            <Link href={vk}>
                <button className="squad-card__button">Перейти</button>
            </Link>

        </div>
    );
}

export default SquadCard;

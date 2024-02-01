import '../PeopleCard/PeopleCard.scss';
import {PersonInterface} from "@/interfases/interfaces";
import Image from "next/image";


function PeopleCard({position, image, name, phone, email}: PersonInterface) {

    return (
        <div className="PeopleCard">
            <div className="PeopleCard__photo">
                <Image src={image} fill alt=" " />
            </div>
            <div className="PeopleCard__name">{name}</div>
            <div className="PeopleCard__position">
                {/* eslint-disable-next-line react/no-unescaped-entities */}
                <p>{position}</p>
            </div>
            <div className='PeopleCard__contact'>
                <div className="PeopleCard__contact__number">
                    {phone}
                </div>
                <div className="PeopleCard__contact__email">
                    {email}
                </div>
            </div>
        </div>
    );
}

export default PeopleCard;

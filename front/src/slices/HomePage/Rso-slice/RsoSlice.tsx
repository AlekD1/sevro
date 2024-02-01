import '../Rso-slice/rso.scss';
import RsoBlock from "@/shared/RsoBlock/RsoBlock";
import friendsIcon from "/public/img/ico-friend.png"
import loveIcon from "/public/img/ico-love.png"
import jobIcon from "/public/img/ico-job.png"
import Link from "next/link";

function RsoSlice() {
    return (

        <div className="Rso-slice">
            <div className="container Rso-slice-container">
                <div className="Rso-slice__blocks">
                    <RsoBlock img={friendsIcon} title="Друзья"/>
                    <RsoBlock img={loveIcon} title="Любовь"/>
                    <RsoBlock img={jobIcon} title="Работа"/>
                </div>
                <div className="Rso-slice__info">
                    <div className="Rso-slice__info__header">о нас</div>
                    <div className="Rso-slice__info__title"> Российские Студенческие Отряды</div>
                    <div className="Rso-slice__info__description">Молодежная общероссийская общественная организация «Российские Студенческие Отряды» (РСО) – крупнейшая молодежная организация страны, которая обеспечивает временной трудовой занятостью более 150 тысяч молодых людей из 81 субъекта РФ, а также занимается гражданским и патриотическим воспитанием, развивает творческий и спортивный потенциал молодежи.</div>
                    <div className="Rso-slice__info__button">
                        <Link href="/about">
                            <button className="Rso-slice__info__button__stylebtn">
                                Подробнее
                                <img src="./img/arrow-right.png"></img>
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default RsoSlice;

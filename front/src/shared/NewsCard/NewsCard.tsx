import "./newscard.scss"
import {NewsCardInterface} from "@/interfases/interfaces";
import Image from "next/image";


function NewsCard({id, title, image, description}: NewsCardInterface) {
	return (
			<div className="News-card">
				<div className="News-card__photo">
					<Image src={image} alt="test" fill/>
				</div>
				<div className="News-card__text">
					<h3 className="News-card__title">
						{title}
					</h3>
					<p className="News-card__description">
						{description}
					</p>
				</div>
			</div>
	);
}

export default NewsCard;

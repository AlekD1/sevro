'use client'
import "./directions.scss";
import Link from "next/link";
import DirectionCard from "../../../shared/DirectionCard/DirectionCard";
import {useEffect, useState} from "react";
import {DirectionInterface} from "@/interfases/interfaces";
import useSWR from "swr";
import {clientAPI} from "@/api/clientAPI";

async function getDirections(): Promise<DirectionInterface[]> {
	try {
		return await clientAPI.get("direction/").json();
	} catch (error) {
		return []
	}
}

 function DirectionsSlice() {

	const {data, isLoading, error} = useSWR<DirectionInterface[]>('direction/', getDirections);
	const [activeCard, setActiveCard] = useState<undefined | number>(undefined);
	const [activeDescription, setActiveDescription] = useState('');
	const [activeTitle, setActiveTitle] = useState('');


	 useEffect(() => {
		if(data && data[0]) {
			setActiveCard(data[0].id);
			setActiveDescription(data[0].description);
			setActiveTitle(data[0].name);
		}
	}, [data]);

	 useEffect(() => {
		 if (data && data[0] && activeCard) {
			 const activeData = data.find(item => item.id === activeCard);
			 if (activeData) {
				 setActiveDescription(activeData.description);
				 setActiveTitle(activeData.name);
			 }
		 }
	 }, [activeCard, data]);

	if(isLoading || !data) return null

	return (
		<div className="Directions-slice">
			<div className="container Directions-slice-container">
				<div className="Directions-slice__info">
					<div className="Directions-slice__info__header">направления</div>
					<div className="Directions-slice__info__title">{activeTitle}</div>
					<div className="Directions-slice__info__description">{activeDescription}</div>
					<div className="Directions-slice__info__button">
						<Link href={`/direction/${activeCard}`}>
							<button className="Directions-slice__info__button__stylebtn">
								Перейти
								<img src="./img/arrow-right.png" />
							</button>
						</Link>
					</div>
				</div>
				<div className="Directions-slice__icons">
					{data.map((value) => {
						return (
							<div key={value.id} onClick={() => setActiveCard(value.id)}>
								<DirectionCard id={value.id} main_image={value.main_image} icon={value.icon} type={activeCard === value.id ? "DirectionCard active" : "DirectionCard"} />
							</div>
						);
					})}
				</div>
			</div>
		</div>
	);
}

export default DirectionsSlice;

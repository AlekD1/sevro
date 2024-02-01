'use client'
import "./TeamSlice.scss";
import PeopleCard from "@/shared/PeopleCard/PeopleCard";
import {NewsCardInterface, PersonInterface} from "@/interfases/interfaces";
import {clientAPI} from "@/api/clientAPI";
import useSWR from "swr";
import React from "react";
import Loader from "@/app/loading";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";

async function getFigures(url: string): Promise<PersonInterface[]> {
	try {
		return await clientAPI.get(url).json();
	} catch (error) {
		return []
	}
}

function TeamSlice() {
	const {data, isLoading, error} = useSWR('figures/',getFigures);

	if (isLoading) return <LoaderCard/>
	if (error || !data || data.length === 0) return null
	return (
		<div className="Team-slice">
			<div className="container Team-slice-container">
				<div className="Team-slice__title"> Команда СевРО</div>
				<div className="Team-slice__PeopleCards">
					{data.map((value) => {
						return <PeopleCard key={value.id} email={value.email} id={value.id}
										   image={value.image} name={value.name} phone={value.phone} position={value.position}/>
					})}
				</div>
			</div>
		</div>
	);
}

export default TeamSlice;

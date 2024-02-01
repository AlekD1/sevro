'use client'
import "./newsslice.scss";
import Image from "next/image";
import {NewsItem} from "@/interfases/interfaces";
import {clientAPI} from "@/api/clientAPI";
import useSWR from "swr";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";
import React from "react";
import {useParams} from "next/navigation";

async function getNews(url: string): Promise<NewsItem | undefined> {
	try {
		return await clientAPI.get(url).json();
	} catch (error) {
		return undefined as NewsItem | undefined;
	}
}

function NewsSlice() {
	const params = useParams()
	const {data, isLoading, error} = useSWR(`news/${params.id}`,getNews);

	if (isLoading) return <LoaderCard/>
	if (error || !data) return null

	let date = new Date(data.created_at);
	let dateString = ('0' + date.getDate()).slice(-2) + "."
		+ ('0' + (date.getMonth() + 1)).slice(-2) + "."
		+ date.getFullYear();

	console.log(data)
	return (
		<div className="News-slice">
			<div className="container">
				<div className="News-slice__info">
					<h2 className="page-title">новости</h2>
					<div className="News-slice__background">
						<Image src={data.image} alt={data.title} fill/>
					</div>
					<div className="News-slice__header">
						<h1 className="News-slice__title">{data.title}</h1>
						<p className="News-slice__data">{dateString}</p>
						<div dangerouslySetInnerHTML={{ __html: data.content}}></div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default NewsSlice;

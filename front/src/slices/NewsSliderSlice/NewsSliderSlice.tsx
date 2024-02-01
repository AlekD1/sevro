'use client'
import "./newsslider.scss";
import NewsCard from "@/shared/NewsCard/NewsCard";
import Slider from "@/components/Slider/Slider";
import NewsSliderHeader from "@/slices/NewsSliderSlice/NewsSliderHeader";
import React from "react";
import {NewsCardInterface} from "@/interfases/interfaces";
import Link from "next/link";
import useSWR from "swr";
import {clientAPI} from "@/api/clientAPI";
import Loader from "@/app/loading";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";

async function getNews(url: string): Promise<NewsCardInterface[]> {
	try {
		return await clientAPI.get(url).json();
	} catch (error) {
		return []
	}
}

function NewsSliderSlice() {

	const {data, isLoading, error} = useSWR('news/',getNews);

	if (isLoading) return <LoaderCard/>
	if (error || !data || data.length === 0) return null

	return (
		<div className="news-slider-wrapper" id="news">
			<Slider title={"новости"} headerContent={<NewsSliderHeader/>}>
				{data.map((value) => {
					return  <swiper-slide key={value.id}>
						<Link href={`/news/${value.id}`}>
							<NewsCard title={value.title} description={value.description} image={value.image}/>
						</Link>
					</swiper-slide>
				} )
				}
			</Slider>
		</div>

	);
}

export default NewsSliderSlice;

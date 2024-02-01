'use client'
import "./document.scss";
import DocumentCard from "@/shared/DocumentCard/DocumentCard";
import useSWR from "swr";
import React from "react";
import {DocumentInterface} from "@/interfases/interfaces";
import {clientAPI} from "@/api/clientAPI";
import Loader from "@/app/loading";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";

async function getDocs(url: string): Promise<DocumentInterface[]> {
	try {
		return await clientAPI.get(url).json();
	} catch (error) {
		return []
	}
}

function DocumentSlice() {
	const {data, isLoading, error} = useSWR('document/',getDocs);

	if (isLoading) return <LoaderCard/>
	if (error || !data || data.length === 0) return null

	return (
		<div className="Document-slice">
			<div className="container">
				<div className="Document-slice__header">документы</div>
				<div className="Document-slice-container">
					{data.map((value) => {
						return <DocumentCard title={value.title} file={value.file} created_at={value.created_at} key={value.title}   />
					})}
				</div>
			</div>
		</div>
	);
}

export default DocumentSlice;

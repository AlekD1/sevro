'use client'
import {useEffect, useState} from "react";
import "./squadslice.scss";
import useSWR from "swr";
import {useParams} from "next/navigation";
import {SquadListItemInterface} from "@/interfases/interfaces";
import {clientAPI} from "@/api/clientAPI";
import SquadCard from "@/shared/SquadCard/SquadCard";


async function getSquads(url: string): Promise<SquadListItemInterface[]> {
    try {
        return await clientAPI.get(url).json();
    } catch (error) {
        return []
    }
}

function SquadSlice() {
    const [activeCard, setActiveCard] = useState(0);

    const params = useParams();
    const id = params.id;
    const {data, error, isLoading} = useSWR(`squad/?direction_id=${id}`, getSquads);

    useEffect(() => {
        console.log(data)
    }, [data]);
    if (!data) return null
    return (
        <div className="Squad-slice">
            <div className="container">
                <div className="Squad-slice__content">
                    <h2 className="Squad-slice__title">отряды</h2>
                    <div className="Squad-slice__cards-list">
                        {data.map((value) => {
                            return <div  key={value.id} onClick={() => setActiveCard(value.id)}>
                                <SquadCard  isActive={activeCard === value.id} vk={value.vk} id={value.id} main_image={value.main_image} name={value.name} description={value.description} />
                            </div>
                        })}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default SquadSlice;

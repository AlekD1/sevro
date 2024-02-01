'use client'
import '../Statistics-slice/statistics.scss';
import StatisticsBlock from "@/shared/StatisticsBlock/StatisticsBlock";
import {StatisticInterface} from "@/interfases/interfaces";
import useSWR from "swr";
import {clientAPI} from "@/api/clientAPI";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";

async function getStatistics(): Promise<StatisticInterface[]> {
    try {
        return await clientAPI.get("statistic/").json();
    } catch (error) {
        return []
    }
}

function StatisticsSlice() {

    const {data, isLoading, error} = useSWR('statistic/', getStatistics);

    if (isLoading) return <LoaderCard/>
    if (error || !data || data.length === 0) return null

    return (
        <div className="Statistics-slice">
            <div className="container Statistics-slice-container">
                {data.map((value, key) => {
                    return <StatisticsBlock key={value.title} title={value.title} value={value.value}/>
                })
                }
            </div>
        </div>
    );
}

export default StatisticsSlice;

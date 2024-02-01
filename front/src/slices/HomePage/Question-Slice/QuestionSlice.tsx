'use client'
import '../Question-Slice/question.scss';
import QuestionBlock from "@/shared/QuestionBlock/QuestionBlock";
import {QAInterface} from "@/interfases/interfaces";
import useSWR from "swr";
import React from "react";
import {clientAPI} from "@/api/clientAPI";
import Loader from "@/app/loading";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";



async function getQA(): Promise<QAInterface[]> {
    try {
        return await clientAPI.get("qa/").json();
    } catch (error) {
        return []
    }
}

function QuestionSlice() {
    const {data, isLoading, error} = useSWR('qa/', getQA);

    if (isLoading) return <LoaderCard/>
    if (error || !data || data.length === 0) return null

    return (
        <div className="Question-slice" id="question">
            <div className="container">
                <div className="Question-slice__header">
                    Вопросы и ответы
                </div>
                <div className="Question-slice__blocks">
                    {data.map((value) => {
                      return <QuestionBlock key={value.title} title={value.title} value={value.value}/>
                    })
                    }
                </div>
            </div>
        </div>
    );
}

export default QuestionSlice;

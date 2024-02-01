import PromoSlice from "@/slices/HomePage/PromoSlice/PromoSlice";
import RsoSlice from "@/slices/HomePage/Rso-slice/RsoSlice";
import StatisticsSlice from "@/slices/HomePage/Statistics-slice/StatisticsSlice";
import QuestionSlice from "@/slices/HomePage/Question-Slice/QuestionSlice";
import FormSlice from "@/slices/HomePage/Form-slice/FormSlice";
import React from "react";
import NewsSliderSlice from "@/slices/NewsSliderSlice/NewsSliderSlice";
import {Metadata} from "next";

export const metadata: Metadata = {
    title: 'Главная',
    description: 'Главная страница',
}

export default function Home() {
  return (
      <div className="HomePage">
        <PromoSlice />
        <StatisticsSlice />
        <RsoSlice />
        <QuestionSlice />
        <NewsSliderSlice/>
        <FormSlice />
      </div>
  )
}

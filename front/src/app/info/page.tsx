import DocumentSlice from "@/slices/DocumentSlice/DocumentSlice";
import NewsSliderSlice from "@/slices/NewsSliderSlice/NewsSliderSlice";
import {Metadata} from "next";

export const metadata: Metadata = {
    title: 'Информация бойцам',
    description: 'Информация бойцам',
}

function InfoPage () {
    return (
        <>
            <DocumentSlice/>
            <NewsSliderSlice/>
        </>
    );
};

export default InfoPage;

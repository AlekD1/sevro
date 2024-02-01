import DirectionsSlice from "@/slices/AboutPage/DirectionsSlice/DirectionsSlice";
import TeamSlice from "@/slices/AboutPage/TeamSlice/TeamSlice";
import {Metadata} from "next";

export const metadata: Metadata = {
    title: 'О нас',
    description: 'Описание страницы о нас',
}

function AboutPage () {
    return (
        <div>
            <DirectionsSlice/>
            <TeamSlice />
        </div>
    );
};

export default AboutPage;

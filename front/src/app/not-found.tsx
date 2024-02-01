import ErrorBlock from "@/shared/ErrorBlock/ErrorBlock";
import NewsSliderSlice from "@/slices/NewsSliderSlice/NewsSliderSlice";
import { Metadata } from "next";

export const metadata: Metadata = {
	title: "Страница не найдена",
	description: "Ошибка 404",
};

function Error() {
	return (
		<div className="ErrorPage">
			<ErrorBlock />
			<NewsSliderSlice />
		</div>
	);
}

export default Error;

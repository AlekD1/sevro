import "../StatisticsBlock/statisticsblock.scss";
import { StatisticInterface } from "@/interfases/interfaces";

function StatisticsBlock({ title, value }: StatisticInterface) {
	return (
		<div className="StatisticsBlock">
			<p className="StatisticsBlock__title">{title}</p>
			<p className="StatisticsBlock__value">{value}</p>
		</div>
	);
}

export default StatisticsBlock;

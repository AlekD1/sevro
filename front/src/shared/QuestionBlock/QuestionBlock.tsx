import '../QuestionBlock/questionblock.scss';
import {QAInterface} from "@/interfases/interfaces";


function QuestionBlock({title, value}: QAInterface) {
    return (
        <details className="QuestionBlock">
            <summary className="QuestionBlock__title" >
                <span>{title}</span>
                <div className="QuestionBlock__title__circle">
                    <img src="./img/arrow-bottom.png"></img>
                </div>
            </summary>
            <p className="QuestionBlock__text">{value}</p>
        </details>
    );
}

export default QuestionBlock;

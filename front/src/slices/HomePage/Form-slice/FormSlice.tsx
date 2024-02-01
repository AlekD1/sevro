'use client'
import '../Form-slice/form.scss';
import {useFormik} from "formik";
import {clientAPI} from "@/api/clientAPI";
import useSWRMutation from "swr/mutation";
import LoaderCard from "@/shared/LoaderCard/LoaderCard";

async function pushForm(url: string, { arg }: { arg: any }) {
    console.log(arg)
    return await clientAPI.post(url, {
        json: arg
    }).json();
}

 function FormSlice() {

    const { data, trigger, isMutating, error } = useSWRMutation<any>('feedback/', pushForm)

    const formik = useFormik({
        initialValues: {
            name: '',
            email: '',
            message: '',
        },
        onSubmit: async (values: any) => {
            try {
                const result = await trigger(values);
                console.log('Result:', result);
            } catch (error) {
                console.error('Error:', error);
            }
            formik.resetForm();
        },
    });
        return (
        < div className="Form-slice" id="form">
            <div className="container Form-slice-container">
                <div className="Form-slice__form">
                    <div className="Form-slice__form__header">Сотрудничество</div>
                    <div className="Form-slice__form__title"> Если вам нужны молодые специалисты</div>
                    <div className="Form-slice__form__description">Вы можете присылать заявки по форме</div>
                    {(() => {
                        if (isMutating) return <LoaderCard/>;
                        if (data) return <div>Спасибо</div>;
                        if (error) return <div>Ошибка</div>;
                        return <form onSubmit={formik.handleSubmit}>
                            <input id="name"
                                   name="name"
                                   type="text"
                                   onChange={formik.handleChange}
                                   value={formik.values.name}
                                   placeholder="Ваше имя" required/>

                            <input type="email"
                                   placeholder="Ваша почта"
                                   id="email"
                                   name="email"
                                   onChange={formik.handleChange}
                                   value={formik.values.email}
                                   required/>

                            <textarea placeholder="Ваше сообщение"
                                      id="message"
                                      name="message"
                                      onChange={formik.handleChange}
                                      value={formik.values.message}
                                      required/>

                            <div className="Form-slice__form__button">
                                <button className="Form-slice__form__button__stylebtn" type="submit">
                                    Отправить
                                    <img src="./img/arrow-right.png"></img>
                                </button>
                            </div>
                        </form>
                    })()}
                </div>
                <div className="Form-slice__partners">
                </div>
            </div>
        </div >
    );
}

export default FormSlice;

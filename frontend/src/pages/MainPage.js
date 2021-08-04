import React, {useEffect, useState} from "react";
import axios from "axios";


export const MainPage = () => {
    const [reports, setReports] = useState([]);
    useEffect(()=>{
        axios.get('http://0.0.0.0:8000/report').then(response=>response.data).then(responseObject=> {
            setReports(responseObject.data[0])
        })
    }, [])
    console.log(reports);
    return (
        <>
        <h1>Here is reports list:</h1>
            {reports.length >= 1?
                 reports.map(report=>{
                    return(
                        <div key={report.date}>
                            <p>Date: {report.date}</p>
                            <p>Path: {report.report_path}</p>
                            <hr/>
                        </div>
                    )
                })
            :
                <p>Fetching data...</p>
            }

        </>
    )
}

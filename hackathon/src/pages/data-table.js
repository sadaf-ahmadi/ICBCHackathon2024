import React from 'react'
import { useEffect, useState } from 'react'
import "../App.css";
import { BrowserRouter } from 'react-router-dom';
import { Link } from 'react-router-dom';


const DataTable = (props) => {
    
    return (
            <table>
                <thead>
                    <tr>
                        <th>Representative Name</th>
                        <th>Customer Name</th>
                        <th>Summary</th>
                        <th>Date</th>
                        <th>Call Length</th> 
                        <th>Flag</th>
                        <th>Details</th>
                        <th>Rviewed</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        props.records.map((record, i) => {
                            const getFlagClassName = (flags) => {
                                return flags.length === 0 ? 'non-negative-flag' : 'negative-flag';
                            };
                        
                            const getFlagText = (flags) => {
                                return flags.length === 0 ? 'Non-negative' : 'Negative';
                            };
                            return (
                            <tr key={i}>
                                <td>{record.short.representativeName}</td>
                                <td>{record.short.customerName}</td>
                                <td>{record.short.summary}</td>                                  
                                <td>{record.short.date}</td>
                                <td>{record.short.callLength + "mins"}</td>
                                <td className={getFlagClassName(record.short.flags)}>{getFlagText(record.short.flags)}</td>
                                <td><Link to='/details' state={record}>Show details</Link></td> 
                                <td>Reviewed</td>
                            </tr>)
                        })
                    }
                </tbody>
            </table>
      
    )
}

export default DataTable
import './App.css';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
import axios from 'axios';
import { useState, useEffect } from 'react';
import { AgGridReact } from 'ag-grid-react';
import "ag-grid-community/styles/ag-grid.css"; // Mandatory CSS required by the grid
import "ag-grid-community/styles/ag-theme-quartz.css"; // Optional Theme applied to the grid



function App() {

  function callDataParser() {
      axios.get('http://localhost:6969/Parserfile/table')
        .then(function (response){
          console.log(response.data)
          setRowData(response.data)
        });
  
      axios.get('http://localhost:6969/Parserfile/events')
        .then(function (response){
          setevents_from_data(response.data)
      });
  }

  function callDataSample() {
      axios.get('http://localhost:6969/Sampledata/table')
        .then(function (response){
          console.log(response.data)
          setRowData(response.data)
        });
  
      axios.get('http://localhost:6969/Sampledata/events')
        .then(function (response){
          setevents_from_data(response.data)
      });
  }

  const [events_from_data, setevents_from_data] = useState([]);
  const [colDefs, setColDefs] = useState([
    { field: "Title"},
    { field: "Calendar"},
    { field: "Watchlist"},
    { field: "Bookmarked"},
    { field: "Event Category" }
  ]);

  const [rowData, setRowData] = useState([]);
  useEffect(() => {
    axios.get('http://localhost:6969/Sampledata/table')
      .then(function (response){
        console.log(response.data)
        setRowData(response.data)
      });

    axios.get('http://localhost:6969/Sampledata/events')
      .then(function (response){
        setevents_from_data(response.data)
    });
  }, [])

  return (
    <div>
      <div>
        <button onClick={callDataParser}>Parser File</button>
        <button onClick={callDataSample}>Sample Data</button> 
      </div>
    <div className="App">
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
        events={events_from_data}
      />
    </div>
    <div style={{ height: 2000 }} className="ag-theme-quartz">
      <AgGridReact 
       columnDefs={colDefs}
       rowData={rowData}
       rowSelection="multiple"
   />
    </div>
    </div>
    
  );
}

export default App;

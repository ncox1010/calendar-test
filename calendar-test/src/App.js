import './App.css';
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid' // a plugin!
import axios from axios;


function App() {


  return (
    <div className="App">
      <FullCalendar
        plugins={[ dayGridPlugin ]}
        initialView="dayGridMonth"
      />
    </div>
    
  );
}

export default App;

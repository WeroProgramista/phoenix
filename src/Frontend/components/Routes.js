import { Route, Routes } from "react-router-dom";
import Statki from '../routes/Statki';
import Klienci from '../routes/Klienci';
import Kalendarz from '../routes/Kalendarz';
import HomePage from "../routes/HomePage";


function RouterConfig() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/statki" element={<Statki />} />
      <Route path="/klienci" element={<Klienci />} />
      <Route path="/kalendarz" element={<Kalendarz />} />
    </Routes>
  );
}

export default RouterConfig;

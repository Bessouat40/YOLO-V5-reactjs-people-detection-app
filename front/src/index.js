import { Stack } from "@mui/system";
import React from "react";
import ReactDOM from "react-dom/client";
import UploadImg from "./components/image";
import reportWebVitals from "./reportWebVitals";
import TitleComponent from "./components/titre";
import Divider from "@mui/material/Divider";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Stack spacing={5} divider={<Divider flexItem />}>
      <TitleComponent />
      <UploadImg />
    </Stack>
  </React.StrictMode>
);

reportWebVitals();

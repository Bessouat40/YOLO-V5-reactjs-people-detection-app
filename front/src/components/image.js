import React, { useState, useEffect } from "react";
import Button from "@mui/material/Button";
import FileUploadIcon from "@mui/icons-material/FileUpload";
import { Stack } from "@mui/system";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import DownloadIcon from '@mui/icons-material/Download';
import { saveAs } from 'file-saver'

import FormData from "form-data";

import DeleteIcon from "@mui/icons-material/Delete";

const UploadImg = () => {
  const [selected, setSelected] = useState();
  const [preview, setPreview] = useState();
  const [predict, setPredict] = useState();

  useEffect(() => {}, [preview]);

  const onUpload = (event) => {
    setSelected(event.target.files[0]);
    setPreview(URL.createObjectURL(event.target.files[0]));
    setPredict()
  };

  const onDownload = () => {
    saveAs(require('./res.png'), 'res.png')      
  }

  const onPredict = async () => {
    if (!selected) {
      alert("Veuillez uploader une image pour lancer la prédiction");
    } else {
      const formData = new FormData();
      formData.append("image", selected);
      const resp = await fetch("http://localhost:8000/prediction", {
        body: formData,
        method: "POST",
      });
      const data = await resp.json();
      setPredict(data);
      
    }
  };

  const onDelete = () => {
    setPredict();
    setPreview();
    setSelected();
  };

  return (
    <Stack spacing={10} alignItems="center">
      <Stack spacing={30} direction="row" alignItems="center">
        <Button
          color="primary"
          aria-label="upload-picture"
          component="label"
          endIcon={<FileUploadIcon />}
          variant="contained"
        >
          Upload image
          <input hidden type="file" onChange={onUpload} />
        </Button>

        <Stack direction="row" spacing={2}>
          <Button variant="contained" onClick={onPredict}>
            Predict
          </Button>
          <IconButton aria-label="delete" onClick={onDelete}>
            <DeleteIcon />
          </IconButton>
        </Stack>
      </Stack>
      <Stack spacing={4} direction="row">
      {selected ? (
        <img
          src={preview}
          style={{ width: 500, height: 300 }}
          alt="img to predict"
        />
      ) : (
        <Typography variant="h5">Sélectionnez une image</Typography>
      )}
      {predict ? 
      <Stack spacing={4} direction='row'>
        <IconButton aria-label="delete" onClick={onDownload}>
            <DownloadIcon />
          </IconButton>
      <img
          src={require('./res.png')}
          style={{ width: 500, height: 300 }}
          alt="img predict"
        /> </Stack>: <div></div>}
        </Stack>
    </Stack>
  );
};

export default UploadImg;

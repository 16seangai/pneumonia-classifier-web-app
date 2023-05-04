import { useState } from 'react';
import { Header } from './components/Header';
import { UploadForm } from './components/UploadForm';
import { Modal } from './components/Modal';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [confidence, setConfidence] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const handleFileSelect = async e => {
    const file = e.target.files[0]
    setSelectedFile(URL.createObjectURL(file));

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData,
      });
      const result = await response.json();
      setPrediction(result.class_name)
      setConfidence(result.confidence)
    } catch (error) {
      console.error(error)
    }
    setShowModal(true);
  }

  const handleModalClose = () => {
    setShowModal(false);
  }

  return (
    <div className="border-box flex flex-col items-center justify-center min-h-screen">
      <Header />
      <UploadForm onFileSelect={handleFileSelect} />
      {showModal && (
        <Modal onModalClose={handleModalClose} image={selectedFile} prediction={prediction} confidence={confidence} />
      )}
    </div>
  );
}

export default App;
